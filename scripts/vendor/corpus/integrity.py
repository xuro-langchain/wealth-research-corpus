"""Corpus integrity: files are verified against GitHub, not against themselves."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field


class CorpusIntegrityError(RuntimeError):
    """A corpus file does not match the manifest for its pinned commit."""


class CorpusUnavailableError(CorpusIntegrityError):
    """The pinned commit could not be FETCHED — nothing was verified either way."""


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
        """Return `content` if it matches the manifest, else raise."""
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
    """Build the manifest from GitHub's git tree at `sha`."""
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
    """GET `url` and return parsed JSON, raising on anything but success."""
    import httpx

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # A just-pushed commit can 404 while it propagates; the ingest run hits that routinely.
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
