"""Normalising a document relation to one of six types. Contract C11.

The corpus brief defines six verbs and a direction rule, and asking the compile
to use them is not the same as getting them. A large share of genuine relations
come back in synonyms instead — "replaces", "overrides", "changes only", the
noun "carve-out", "does not restore" — so the vocabulary constraint holds only
part of the time.

That is a tier-4 failure in the enforcement taxonomy, which is why the map lives
here rather than being trusted from the claim text. The brief raises the signal;
this produces the contract.

The verbs are the insurance set this corpus was adapted from, with one rename:
`writes-back` became `restores`, because what an exemption does to a trading
restriction is restore a permitted action, and "write-back" is a policy-forms
idiom that means nothing to an investment reader.
"""

from __future__ import annotations

import re

#: Ordered most-specific first; first match wins. Order matters: "replaces"
#: appears under both restores and supersedes, and an exemption replacing a
#: restriction is a restoration while an edition replacing an edition is a
#: supersession, so the restriction-scoped pattern must be tried first.
PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "restores",
        # `(?<!not )` because "does NOT restore" is a preserves, not a
        # restoration, and this pattern is tried first. Without the lookbehind
        # every negated restoration inverts to its opposite.
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
        r"|\bin full\b|\bunchanged\b|\bstill (?:applies|restricted|prohibited)\b"
        r"|\bdoes not (?:restore|extend|exempt|disturb)\b",
    ),
    (
        "supersedes",
        # `withdraw` was here as a synonym and matched review-policy prose —
        # "reviewed on re-issue or withdrawal of cited research" is a schedule,
        # not a supersession. A missing type withholds one answer; a wrong one
        # inverts it, so the looser synonym goes.
        r"\bsupersede[sd]?\b|\bwithdrawn by\b"
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
        r"|\boutside (?:mandate|the mandate)\b|\brequires? (?:approval|sign-off)\b|\bauthority\b",
    ),
    (
        "modifies",
        r"\bmodif(?:y|ies|ied|ying)\b|\bamend(?:s|ed)?\b|\bchanges only\b|\bsubject to\b"
        r"|\bschedule in\b|\bsub-limit\b|\bsublimit\b|\btolerance band\b|\bthreshold\b"
        r"|\breduces? the (?:target|weight|allocation)\b|\blimits? (?:to|the)\b",
    ),
)

TYPES: tuple[str, ...] = tuple(name for name, _ in PATTERNS)

_COMPILED = tuple((name, re.compile(pattern, re.I)) for name, pattern in PATTERNS)


def normalize(statement: str) -> str | None:
    """Return one of TYPES, or None.

    None rather than a guess, deliberately. `preserves` and `restores` are
    opposites — SEC 2026-14 restores the qualified-purchaser exemption at
    Rule 2.1 and expressly preserves the concentration limit at Rule 2.2 — so a
    wrong type inverts an allocation answer. A missing type only withholds one.
    """
    text = statement or ""
    for name, pattern in _COMPILED:
        if pattern.search(text):
            return name
    return None
