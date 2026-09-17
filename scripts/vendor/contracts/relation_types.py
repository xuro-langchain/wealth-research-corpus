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

#: EVERY ALTERNATIVE BELOW IS A VERB OR A VERB PHRASE. Bare nouns were tried and
#: removed: `threshold`, `sublimit`, `tolerance band` and `schedule in` sat in
#: the `modifies` pattern and matched any claim that mentioned one, so an
#: effective-date sentence — "the IRS AMT threshold procedure applies to taxable
#: years beginning on or after 2026-01-01" — came back as a modification. A noun
#: identifies the SUBJECT a claim is about; only a verb describes what one
#: document does to another, which is the only thing this map is for.
#:
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
        r"|\b(?:applies|apply|remain(?:s)?|continue(?:s)?) in full\b|\bunchanged\b"
        r"|\bstill (?:applies|restricted|prohibited)\b|\bis (?:not )?disturbed\b"
        r"|\bdoes not (?:restore|extend|exempt|disturb)\b",
    ),
    (
        "supersedes",
        # `withdraw` was here as a synonym and matched review-policy prose —
        # "reviewed on re-issue or withdrawal of cited research" is a schedule,
        # not a supersession. A missing type withholds one answer; a wrong one
        # inverts it, so the looser synonym goes.
        # The bare participle is adjectival far more often than it is a
        # relation: "weights derived from superseded research" states a policy
        # ABOUT supersession and typed an allocation guide as superseding a
        # research note. Require the active verb or an explicit agent.
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


# --- who may do what to whom -----------------------------------------------
#
# The keyword map above reads a claim's PROSE and knows nothing about the two
# documents the claim connects. That is where it goes wrong, and patching the
# patterns one synonym at a time does not fix it: "weights derived from
# superseded research" and "2026-04 supersedes 2025-06" look nearly identical to
# a regex, and only the first is a policy statement rather than a relation.
#
# These constraints are orthogonal to wording. They come from the corpus brief's
# own definitions of the verbs, and they hold however a claim is phrased:
#
#   implements  "internal guidance carries out a requirement imposed by a
#               regulator" — so only guidance implements, and only a regulator's
#               document can be implemented.
#   supersedes  a later edition, or a regulatory change removing a view's basis.
#               Internal guidance has no such power over either.
#   restores    an exemption or relief restoring what a restriction removed.
#               That is a regulator's act.
#   constrains  "internal guidance or a regulatory requirement limits when or how
#               a position may be taken" — a research note constrains nothing.
#
# Anything not listed here is unconstrained: `modifies` and `preserves` are
# available to every role, because any document can leave another's provision
# intact or change a limit it set.
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
    """Can a document of `acting_role` stand in relation `kind` to `target_role`?

    Used to drop a type the wording produced but the roles forbid. Dropping to
    None is the documented preference: a missing type withholds one answer, a
    wrong one inverts it.
    """
    if kind is None:
        return True
    actors = _ACTOR_MUST_BE.get(kind)
    if actors is not None and acting_role not in actors:
        return False
    targets = _TARGET_MUST_BE.get(kind)
    return targets is None or target_role in targets
