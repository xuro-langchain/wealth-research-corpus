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
distinction the type field carries. `research/` is published research,
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

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "openwiki"

#: Longest prefix wins, so a more specific area can override its parent.
RULES: tuple[tuple[str, str], ...] = (
    ("guidance/allocation/", "allocation-guidance"),
    ("guidance/suitability/", "suitability-guidance"),
    ("guidance/authority/", "authority-guidance"),
    ("position-assembly/", "position-assembly"),
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


def main(check_only: bool) -> int:
    if not WIKI.is_dir():
        print("no openwiki/ — nothing to normalise")
        return 0

    changed: list[str] = []
    unmapped: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        rel = str(path.relative_to(WIKI))
        if path.name in SKIP_NAMES or is_index(rel):
            continue
        want = expected_type(rel)
        if want is None:
            unmapped.append(rel)
            continue

        text = path.read_text()
        m = FRONTMATTER.match(text)
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

    for line in changed:
        print(f"  {line}")
    if unmapped:
        print("\nNOT MAPPED — add a rule in RULES or these pages carry no type:")
        for rel in unmapped:
            print(f"  {rel}")

    if check_only and (changed or unmapped):
        print(f"\n{len(changed)} page(s) would change, {len(unmapped)} unmapped")
        return 1
    print(f"\n{len(changed)} page(s) normalised, {len(unmapped)} unmapped")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv[1:]))
