"""Corpus integrity manifest — enforces C7 of 00-contracts.md.

The problem this closes. `execute` gives the agent a shell on the sandbox. It
can `chmod +w` the corpus and edit a form, and neither the read-only middleware
(which only guards write_file / edit_file / delete) nor the SHA marker (which
records which commit was fetched, not what the files contain) would notice. The
agent would then cite text no filed form ever contained — the exact
fabricated-grounding failure the whole design exists to prevent, arriving by a
side door.

Two design choices make this a real boundary rather than a speed bump.

1. THE MANIFEST IS AUTHORITATIVE, NOT SELF-REFERENTIAL.

   It is not computed from the files we downloaded. It is fetched from GitHub's
   git tree API at the pinned SHA, so it is an independent statement of what the
   corpus contains. That catches a tampered file, a truncated download, and a
   corrupted extraction with one mechanism.

2. THE MANIFEST LIVES IN THE APP PROCESS, NOT ON THE SANDBOX.

   Middleware and tools run in the deployed LangGraph app. `execute` runs
   commands on the sandbox, which is a separate machine reached through the
   backend. So shell access cannot reach the manifest: there is no file to
   rewrite and no path to it. Storing it on the sandbox filesystem would have
   made it exactly as tamperable as the thing it verifies.

Identifiers are git blob SHAs — sha1 of `blob <bytelen>\\0<content>` — so they
are directly comparable to what the tree API returns, with no separate hashing
scheme to keep in sync. Verified against this corpus: git reports
78c39dfc765e0a4982801c7d084e71f7337cc68c for internal_research/FI/US/MUNI-CREDIT/2025-06.md, and
`git_blob_sha` below reproduces it exactly.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field


class CorpusIntegrityError(RuntimeError):
    """A corpus file does not match the manifest for its pinned commit.

    Never caught. A run that cannot trust its corpus must produce no answer: a
    positioning answer citing mutated text is indistinguishable from a good one,
    which is worse than no answer at all.
    """


class CorpusUnavailableError(CorpusIntegrityError):
    """The pinned commit could not be FETCHED — nothing was verified either way.

    Distinct from an integrity failure because the right response differs: a
    mismatch is final, an unreachable tarball is transient (GitHub propagating
    a seconds-old commit). The guard lets this one end the run so the caller
    retries, instead of handing the model a corpus it cannot see and getting a
    fluent "could not verify / missing_document" report back.
    """


def git_blob_sha(content: bytes) -> str:
    """Return the git blob SHA of `content`, matching `git rev-parse <sha>:<path>`."""
    header = b"blob %d\0" % len(content)
    return hashlib.sha1(header + content).hexdigest()  # noqa: S324 - git's format, not a security hash


@dataclass
class CorpusManifest:
    """What the corpus contains at one commit, per GitHub rather than per disk."""

    corpus_sha: str
    blobs: dict[str, str] = field(default_factory=dict)   # repo-relative path -> blob sha
    truncated: bool = False

    def verify(self, path: str, content: bytes) -> bytes:
        """Return `content` if it matches the manifest, else raise.

        Called by every read tool before content reaches the model. An unknown
        path is a failure, not a pass: a file present in the sandbox but absent
        from the tree at this commit was created locally, and nothing created
        locally is corpus knowledge.
        """
        expected = self.blobs.get(path)
        if expected is None:
            if self.truncated:
                raise CorpusIntegrityError(
                    f"{path} is not in the manifest, and the manifest is truncated "
                    f"so absence proves nothing. Refusing to serve unverifiable content."
                )
            raise CorpusIntegrityError(
                f"{path} does not exist in the corpus at {self.corpus_sha[:12]}. "
                f"It was created inside the sandbox and is not corpus knowledge."
            )
        actual = git_blob_sha(content)
        if actual != expected:
            raise CorpusIntegrityError(
                f"{path} does not match the corpus at {self.corpus_sha[:12]}: "
                f"expected blob {expected[:12]}, got {actual[:12]}. The sandbox copy "
                f"has been modified. Refusing to serve it — citing it would produce "
                f"quotes no filed document contains."
            )
        return content


async def fetch_manifest(
    owner: str, repo: str, sha: str, token: str | None = None
) -> CorpusManifest:
    """Build the manifest from GitHub's git tree at `sha`.

    One extra API call per populate, which is why this is affordable: the
    populate step already runs once per thread per SHA.

    `token` is optional because the corpus repo is public. Supplying one only
    raises the rate limit from 60 requests/hour to 5000. This call runs in the
    app process, so a token given here never reaches the sandbox.

    The tree API sets `truncated: true` for very large trees rather than
    paginating. This corpus has 77 tracked files, so truncation is not expected
    — but it is recorded rather than ignored, because a silently partial
    manifest would turn `verify` into a no-op for every path it omitted, which
    is worse than having no manifest at all.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{sha}?recursive=1"
    payload = await _get_json(url, token)   # raises on any non-200
    blobs = {
        entry["path"]: entry["sha"]
        for entry in payload.get("tree", ())
        if entry.get("type") == "blob"
    }
    if not blobs:
        raise CorpusIntegrityError(f"git tree at {sha} returned no blobs")
    return CorpusManifest(
        corpus_sha=sha,
        blobs=blobs,
        truncated=bool(payload.get("truncated")),
    )


async def _get_json(url: str, token: str | None) -> dict:
    """GET `url` and return parsed JSON, raising on anything but success.

    Runs in the app process, so the token — when one is supplied at all — never
    reaches the sandbox. The corpus repo is public, so `token` is optional and
    only raises the API rate limit from 60/hour to 5000/hour.
    """
    import httpx

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # A commit pushed seconds ago can 404 on the API for a few seconds while it
    # propagates. The ingest run is dispatched right after the push, so this is
    # the normal case, not a corner: retry briefly before calling it missing.
    import asyncio

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        for delay in (0, 2, 4, 8):
            if delay:
                await asyncio.sleep(delay)
            response = await client.get(url, headers=headers)
            if response.status_code != 404:
                break

    if response.status_code == 404:
        raise CorpusIntegrityError(
            f"git tree not found at {url}. Either the commit does not exist or "
            f"the repository is no longer public — the anonymous fetch path "
            f"depends on it staying public (gate G3)."
        )
    if response.status_code == 403 and "rate limit" in response.text.lower():
        raise CorpusIntegrityError(
            "GitHub API rate limit exceeded. The unauthenticated limit is 60 "
            "requests/hour; set GITHUB_TOKEN to raise it to 5000. The token is "
            "read in this process and never reaches the sandbox."
        )
    if response.status_code != 200:
        raise CorpusIntegrityError(
            f"git tree fetch failed: HTTP {response.status_code} from {url}"
        )
    return response.json()
