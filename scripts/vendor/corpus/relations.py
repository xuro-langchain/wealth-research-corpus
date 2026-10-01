"""Normalising a document relation to one of six verbs."""

from __future__ import annotations

import re

#: Verbs only (a noun names a subject, not a relation). Most specific first; first match wins.
PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "restores",
        # `(?<!not )`: "does not restore" means preserves.
        r"(?<!not )\brestor(?:e|es|ing)\b"
        r"|\bcarves? out\b|\bcarve-out\b|\bexempt(?:s|ed|ion)?\b"
        r"|\bsafe harbou?r\b|\bno-action relief\b|\brelief from\b"
        # `[\s\S]` not `[^.]`: provision references contain dots ("Rule 2.1"),
        # so a dot-excluding gap never reaches the word "restriction".
        r"|\boverrid(?:e|es)\b|\breplaces?\b[\s\S]{0,40}\b(?:restriction|prohibition)\b"
        r"|\bnotwithstanding\b|\bexcept as provided\b",
    ),
    (
        "preserves",
        r"\bpreserv(?:e|es)\b|\bcontinues? to apply\b|\bremains? in (?:full )?(?:force|effect)\b"
        r"|\b(?:applies|apply|remain(?:s)?|continue(?:s)?) in full\b|\bunchanged\b"
        r"|\bstill (?:applies|restricted|prohibited)\b|\bis (?:not )?disturbed\b"
        r"|\bdoes not (?:restore|extend|exempt|disturb)\b",
    ),
    (
        "supersedes",
        # The active verb or an explicit agent: "superseded research" alone is an adjective.
        r"\bsupersedes?\b(?! or )|\bsuperseded by\b|\bwithdrawn by\b"
        r"|\bremains the basis of record for positions\b"
        r"|\bedition in force\b|\bprior edition\b|\bgoverning (?:note|edition)\b",
    ),
    (
        "implements",
        r"\bimplement(?:s|ed|ing)?\b|\bas required by\b|\bpursuant to\b|\bcarries out\b"
        r"|\bin response to\b",
    ),
    (
        "constrains",
        r"\bconstrain(?:s|ed|ing)?\b"
        r"|\bmay not\b|\bmust not\b|\bprohibit(?:s|ed)?\b|\brequires? (?:referral|escalation)\b"
        r"|\boutside (?:mandate|the mandate)\b|\brequires? (?:approval|sign-off|referral|escalation)\b"
        r"|\bcannot be cleared\b|\bmay not be (?:cleared|approved|granted)\b",
    ),
    (
        "modifies",
        r"\bmodif(?:y|ies|ied|ying)\b|\bamend(?:s|ed)?\b|\bchanges only\b"
        r"|\breduces? the (?:target|weight|allocation|limit|band)\b"
        r"|\braises? the (?:target|weight|allocation|limit|band|threshold)\b"
        r"|\bwidens? the\b|\bnarrows? the\b|\bre-?sets? the\b"
        r"|\blimits? (?:to|the)\b|\bsubject to\b",
    ),
)

TYPES: tuple[str, ...] = tuple(name for name, _ in PATTERNS)

_COMPILED = tuple((name, re.compile(pattern, re.I)) for name, pattern in PATTERNS)


def normalize(statement: str) -> str | None:
    """Return one of TYPES, or None."""
    text = statement or ""
    for name, pattern in _COMPILED:
        if pattern.search(text):
            return name
    return None


# Which roles may stand in each relation, whatever the wording says:
#   implements  guidance implements a regulator's document
#   supersedes  a later edition, or a regulatory change removing a view's basis
#   restores    a regulator's exemption undoing a restriction
#   constrains  guidance or a requirement limiting a position
# modifies and preserves are open to any document.
_ACTOR_MUST_BE: dict[str, frozenset[str]] = {
    "implements": frozenset({"guideline"}),
    "supersedes": frozenset({"bulletin", "cross-asset-note", "asset-note"}),
    "restores": frozenset({"bulletin"}),
    "constrains": frozenset({"guideline", "bulletin"}),
}
_TARGET_MUST_BE: dict[str, frozenset[str]] = {
    "implements": frozenset({"bulletin"}),
}


def is_legal(kind: str | None, acting_role: str, target_role: str) -> bool:
    """Can a document of `acting_role` stand in relation `kind` to `target_role`?"""
    if kind is None:
        return True
    actors = _ACTOR_MUST_BE.get(kind)
    if actors is not None and acting_role not in actors:
        return False
    targets = _TARGET_MUST_BE.get(kind)
    return targets is None or target_role in targets
