"""The app-process copy of the corpus.

Authored tools cannot reach the sandbox: `@tool` puts a `ToolRuntime` parameter
into args_schema, so a tool declaring one fails every call with "Field required:
runtime". So the app process fetches its own copy for hashing and indexing while
the model uses the sandbox copy. Both are verified against the same manifest.
"""

from __future__ import annotations

import asyncio
import io
import logging
import os
import pathlib
import tarfile

from dataclasses import dataclass, field

from contracts.corpus_manifest import CorpusIntegrityError, CorpusUnavailableError, git_blob_sha  # noqa: F401

logger = logging.getLogger(__name__)

OWNER = os.environ.get("CORPUS_OWNER", "eugeneliu-86")
REPO = os.environ.get("CORPUS_REPO", "wealth-research-corpus")

#: TMPDIR read directly rather than through tempfile.gettempdir(), which walks a
#: candidate list and calls os.getcwd() on the way. That is a blocking syscall,
#: and this module is imported lazily on any build where tools/claims.py is not
#: in the tool list -- so the call lands inside an async tool call and
#: blockbuster refuses it. On the default build the claims tools import this at
#: startup, outside the event loop, and it resolves once; the grep-only branch
#: drops them, and every tool call then raised BlockingError, returned an empty
#: answer in six seconds, and scored as though the build were merely worse.
#: Import order is not a guarantee, so the syscall goes rather than the ordering
#: being relied on.
CACHE_ROOT = pathlib.Path(os.environ.get("TMPDIR") or "/tmp") / "research-agent-corpus"

#: Text extensions worth preloading. Everything the tools read is text; the
#: whole corpus is 1.2 MB, so holding it in memory costs nothing and removes an
#: entire class of bug — see the note on BlockingError below.
TEXT_SUFFIXES = frozenset({".md", ".json", ".yml", ".yaml", ".txt"})


@dataclass
class LocalCorpus:
    """The corpus at one commit, fully in memory.

    Preloaded rather than read on demand because the dev server runs
    `blockbuster`, which raises on synchronous I/O in the event loop -- and it
    catches `rglob`, not just reads. One thread hop per commit, and every
    consumer downstream is pure CPU over this dict, so no refactor can
    reintroduce a blocking call from a tool.
    """

    corpus_sha: str
    root: pathlib.Path
    files: dict[str, list[str]] = field(default_factory=dict)
    verified_count: int = 0

    def lines(self, path: str) -> list[str]:
        try:
            return self.files[path]
        except KeyError:
            raise FileNotFoundError(path) from None

    def paths(self, prefix: str = "", suffix: str = "") -> list[str]:
        return sorted(
            p for p in self.files
            if p.startswith(prefix) and p.endswith(suffix)
        )


_locks: dict[str, asyncio.Lock] = {}
_CORPORA: dict[str, LocalCorpus] = {}


def _lock(sha: str) -> asyncio.Lock:
    """One lock per SHA, so concurrent tool calls extract once rather than race."""
    if sha not in _locks:
        _locks[sha] = asyncio.Lock()
    return _locks[sha]


async def _download(sha: str) -> bytes:
    import httpx

    # codeload first (no rate limit), then its `legacy.tar.gz` path (a different
    # edge cache key — the plain path kept serving a 404 for a fresh commit
    # after the tree API had it), then the API tarball endpoint (anonymous
    # 60/hour, so last). Same order as the sandbox fetch in corpus_guard.
    urls = [
        f"https://codeload.github.com/{OWNER}/{REPO}/tar.gz/{sha}",
        f"https://codeload.github.com/{OWNER}/{REPO}/legacy.tar.gz/{sha}",
        f"https://api.github.com/repos/{OWNER}/{REPO}/tarball/{sha}",
    ]
    async with httpx.AsyncClient(timeout=60.0, follow_redirects=True) as client:
        response = None
        for delay in (0, 3, 6, 10):
            if delay:
                await asyncio.sleep(delay)
            for url in urls:
                response = await client.get(url)
                if response.status_code == 200:
                    break
            if response is not None and response.status_code == 200:
                break
    if response is None or response.status_code != 200:
        raise CorpusUnavailableError(
            f"could not fetch the corpus tarball for {sha[:12]}: "
            f"HTTP {response.status_code}. The anonymous path depends on the "
            f"repository staying public (gate G3)."
        )
    return response.content


def _extract(payload: bytes, dest: pathlib.Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            # GitHub tarballs carry a single top-level dir; strip it.
            parts = pathlib.PurePosixPath(member.name).parts[1:]
            if not parts:
                continue
            target = dest.joinpath(*parts)
            # Refuse anything that escapes dest, however it was spelled.
            if not target.resolve().is_relative_to(dest.resolve()):
                raise CorpusIntegrityError(f"tar member escapes the cache: {member.name!r}")
            target.parent.mkdir(parents=True, exist_ok=True)
            extracted = archive.extractfile(member)
            if extracted is not None:
                target.write_bytes(extracted.read())


def _verify(root: pathlib.Path, blobs: dict[str, str]) -> int:
    """Assert every manifest path is present and hashes correctly."""
    mismatched: list[str] = []
    missing: list[str] = []
    for path, expected in blobs.items():
        candidate = root / path
        if not candidate.is_file():
            missing.append(path)
            continue
        if git_blob_sha(candidate.read_bytes()) != expected:
            mismatched.append(path)
    if mismatched or missing:
        raise CorpusIntegrityError(
            f"the app-process corpus copy is not this commit: "
            f"{len(mismatched)} differ, {len(missing)} missing. "
            f"First differing: {mismatched[:3]}. First missing: {missing[:3]}."
        )
    return len(blobs)


def _load(dest: pathlib.Path, sha: str, blobs: dict[str, str] | None) -> LocalCorpus:
    """All blocking work, called once per commit inside a thread."""
    if blobs:
        count = _verify(dest, blobs)
        (dest / ".verified").write_text(str(count))
    else:
        count = 0
    files: dict[str, list[str]] = {}
    for path in dest.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(dest))
        if rel.startswith(".verified"):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        # Split on LF only: the anchor formula joins with LF, so splitlines()
        # would disagree on any file containing a lone CR or a form feed.
        files[rel] = path.read_text(encoding="utf-8").split("\n")
    return LocalCorpus(corpus_sha=sha, root=dest, files=files, verified_count=count)


async def ensure_local_corpus(sha: str, blobs: dict[str, str] | None = None) -> LocalCorpus:
    """Return the corpus at `sha`, verified and fully loaded.

    `blobs` is the git-tree manifest the guard already fetched. When supplied,
    the extracted copy is verified against it — an unverified copy is exactly
    what the manifest exists to prevent.
    """
    cached = _CORPORA.get(sha)
    if cached is not None:
        return cached

    async with _lock(sha):
        cached = _CORPORA.get(sha)
        if cached is not None:
            return cached

        dest = CACHE_ROOT / sha

        def needs_download() -> bool:
            return not dest.is_dir() or not any(dest.iterdir())

        if await asyncio.to_thread(needs_download):
            payload = await _download(sha)
            await asyncio.to_thread(_extract, payload, dest)

        corpus = await asyncio.to_thread(_load, dest, sha, blobs)
        logger.info(
            "app-process corpus loaded at %s: %d files verified, %d text files held",
            sha[:12], corpus.verified_count, len(corpus.files),
        )
        _CORPORA[sha] = corpus
        return corpus
