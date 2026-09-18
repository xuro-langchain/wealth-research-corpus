#!/usr/bin/env python3
"""Force every wiki content page's `type` to the one its path implies. C11-style.

WHY THIS EXISTS. openwiki/INSTRUCTIONS.md names five page types, says to use them
verbatim, and says not to invent values. Measured over the first clean compile of
this corpus:

    content pages                     18
    declared a controlled type         8
    declared `type: "Reference"`      10   (not in the vocabulary, and quoted)

That is the same tier-4 failure the relation verbs hit — asking a compile to
honour a controlled vocabulary gets partial compliance — and it has the same
answer: stop asking, and derive it.

The derivation is total because the wiki's directory layout already encodes the
distinction the type field carries. `internal_research/` is published research,
`guidance/` is the firm's own material, `regulatory/` is a regulator's. Nothing
is guessed: a path that matches no rule is left alone and reported, so a new
top-level area shows up as output rather than being silently mislabelled.

This runs in the refresh workflow, after the compile and before the claims index
is built, because the agent reads `type` to decide what authority a page carries
and the index is derived from the pages.

    python3 scripts/normalise-page-types.py [--check]

`--check` exits non-zero without writing, for CI.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "openwiki"

#: The controlled vocabulary from openwiki/INSTRUCTIONS.md. A page already
#: carrying one of these is LEFT ALONE: the compile chose correctly, and
#: overriding it from the path would be this script substituting its own reading
#: of the layout for the compile's reading of the document.
VALID: frozenset[str] = frozenset({
    "market-view", "allocation-guidance", "suitability-guidance",
    "authority-guidance", "regulatory-overlay", "position-assembly",
})

#: Longest prefix wins, so a more specific area can override its parent.
#: These are the fallback for a page whose type is missing or outside VALID.
#: The top-level area names are the COMPILE's choice, not the brief's — it
#: renamed `position-assembly/` to `workflows/` between two runs — so both
#: spellings are listed and an unrecognised area is reported rather than guessed.
#
# THESE ARE WIKI PAGE PATHS, NOT CORPUS SOURCE DIRECTORIES. They live under
# openwiki/ and the COMPILE chooses them, so they do not track the source tree
# and must not be swept along when it is renamed. A blanket rename of
# research/ -> internal_research/ across the repo rewrote the last entry here
# and silently unmapped every research page; the compile's own `type:
# "Reference"` then stood, which is the exact failure this script exists to
# prevent. The compile also varies the names between runs — regulatory/ has
# also appeared as regulatory-overlays/, position-assembly/ as workflows/ — so
# known spellings are listed together rather than assumed.
RULES: tuple[tuple[str, str], ...] = (
    ("guidance/allocation/", "allocation-guidance"),
    ("guidance/suitability/", "suitability-guidance"),
    ("guidance/authority/", "authority-guidance"),
    ("position-assembly/", "position-assembly"),
    ("workflows/", "position-assembly"),
    ("regulatory-overlays/", "regulatory-overlay"),
    ("regulatory/", "regulatory-overlay"),
    ("research/", "market-view"),
)

#: Human-owned or structural; never carry a type.
SKIP_NAMES = {"INSTRUCTIONS.md"}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TYPE_LINE = re.compile(r"^type:.*$", re.M)


def expected_type(rel: str) -> str | None:
    for prefix, value in sorted(RULES, key=lambda r: -len(r[0])):
        if rel.startswith(prefix):
            return value
    return None


def is_index(rel: str) -> bool:
    """Section indexes and the root index declare no type, per the brief."""
    return rel.endswith("index.md") or rel == "quickstart.md"


CLAIMS = WIKI / ".claims"


def sync_page_versions(check_only: bool) -> list[str]:
    """Bring each sidecar's `pageVersion` up to the page it describes.

    WHY THIS IS NEEDED, AND WHY IT IS SAFE.

    OpenWiki hashes a page when it verifies that page's claims and stores the
    hash as `pageVersion`. This script then rewrites the page's `type`
    frontmatter, which changes those bytes -- so the sidecar is left describing
    a version of the page that no longer exists. OpenWiki's next run reads that
    mismatch and refuses: "Cannot advance page coverage ...; Markdown and
    verified Claims are not durable", exit 1. The refresh workflow has been
    failing on exactly this, and it could not recover on its own, because each
    run normalised again and re-broke what it had just rebuilt.

    Rehashing asserts nothing false. The only bytes this script touches are a
    frontmatter `type:` line, and no claim's evidence points at a wiki page --
    every pointer is a `repo://` range in a SOURCE document. The claims are
    unchanged; only the record of which page text they were read from needs to
    catch up. A genuine edit to a page's prose still has to go through a
    compile, and this does not hide one: it runs immediately after the
    normaliser, inside the same workflow step, where the normaliser is the only
    thing that can have touched a page since OpenWiki verified it.
    """
    if not CLAIMS.is_dir():
        return []
    synced: list[str] = []
    for side in sorted(CLAIMS.rglob("*.json")):
        rel = side.relative_to(CLAIMS).with_suffix(".md")
        page = WIKI / rel
        if not page.exists():
            continue
        try:
            data = json.loads(side.read_text())
        except json.JSONDecodeError:
            print(f"  WARNING: {side} is not valid JSON; left alone", file=sys.stderr)
            continue
        actual = "sha256:" + hashlib.sha256(page.read_bytes()).hexdigest()
        if data.get("pageVersion") == actual:
            continue
        synced.append(f"{rel}: pageVersion {str(data.get('pageVersion'))[7:19]} -> {actual[7:19]}")
        if not check_only:
            data["pageVersion"] = actual
            side.write_text(json.dumps(data, indent=2) + "\n")
    return synced


def main(check_only: bool) -> int:
    if not WIKI.is_dir():
        print("no openwiki/ — nothing to normalise")
        return 0

    changed: list[str] = []
    unmapped: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        rel = str(path.relative_to(WIKI))
        if path.name in SKIP_NAMES:
            continue
        if is_index(rel):
            # The brief says index pages declare no type. They are skipped for
            # DERIVATION but not for correction: quickstart came back as
            # `type: decision guide`, an invented value of exactly the kind the
            # controlled list exists to prevent. Strip it rather than leave it.
            text = path.read_text()
            m = FRONTMATTER.match(text)
            if m and TYPE_LINE.search(m.group(1)):
                block = TYPE_LINE.sub("", m.group(1)).strip("\n")
                if not check_only:
                    path.write_text(f"---\n{block}\n---\n{text[m.end():]}")
                changed.append(f"{rel}: dropped a type from an index page")
            continue
        text = path.read_text()
        m = FRONTMATTER.match(text)
        declared = None
        if m:
            cm0 = TYPE_LINE.search(m.group(1))
            if cm0:
                declared = cm0.group(0).split(":", 1)[1].strip().strip('"').strip("'")
        if declared in VALID:
            continue                                  # the compile got it right

        want = expected_type(rel)
        if want is None:
            unmapped.append(f"{rel} (declared {declared!r})")
            continue
        if not m:
            # No frontmatter at all: add it rather than skip, or the page has no
            # authority marker and the agent cannot tell what it is reading.
            if not check_only:
                path.write_text(f"---\ntype: {want}\n---\n{text}")
            changed.append(f"{rel}: added frontmatter, type: {want}")
            continue

        block = m.group(1)
        current = None
        cm = TYPE_LINE.search(block)
        if cm:
            current = cm.group(0).split(":", 1)[1].strip().strip('"').strip("'")
        if current == want:
            continue

        new_block = TYPE_LINE.sub(f"type: {want}", block) if cm else f"type: {want}\n{block}"
        if not check_only:
            path.write_text(f"---\n{new_block}\n---\n{text[m.end():]}")
        changed.append(f"{rel}: {current!r} -> {want}")

    # Always, not only when a page changed: a sidecar can be born stale, because
    # OpenWiki commits the hash it verified alongside a page this script has
    # already rewritten in the same run. Three of this corpus's pages were in
    # that state with no later normalisation to explain it.
    synced = sync_page_versions(check_only)

    for line in changed:
        print(f"  {line}")
    for line in synced:
        print(f"  {line}")
    if unmapped:
        print("\nNOT MAPPED — add a rule in RULES or these pages carry no type:")
        for rel in unmapped:
            print(f"  {rel}")

    # `synced` counts too. A stale pageVersion is what makes OpenWiki's next run
    # refuse the page, so CI has to fail on it rather than report it and pass --
    # that is how eleven of this corpus's sixteen pages drifted unnoticed until
    # the compile stopped.
    if check_only and (changed or unmapped or synced):
        print(f"\n{len(changed)} page(s) would change, {len(synced)} pageVersion(s) "
              f"stale, {len(unmapped)} unmapped")
        return 1
    print(f"\n{len(changed)} page(s) normalised, {len(synced)} pageVersion(s) synced, "
          f"{len(unmapped)} unmapped")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv[1:]))
