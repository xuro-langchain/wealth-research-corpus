---
type: Market research knowledge brief
title: Research Wiki Instructions
description: Guidance for building and maintaining a grounded market-research wiki over a wealth management corpus, for use by portfolio managers, investment committees, and the agents that assist them.
tags: [wealth-management, market-research, allocation, suitability, regulatory]
---

A market-research knowledge wiki for this wealth management corpus. The audience is a portfolio manager or an investment committee member who needs to answer a positioning question correctly and defensibly, and the agents that assist them.

## What to organize by

Organize by asset class first (fixed income, equities, multi-asset, real assets), then by subject within it, then by regulatory overlay. Give a research view and the internal guidance derived from it their own pages where the dependency is material — municipal credit and private markets eligibility both warrant dedicated pages.

Give the firm's internal guidance its own top-level area, separate from research. Internal guidance is not research and must never be presented as though it were. Where guidance depends on a research note, say so explicitly and cite both.

## Page types

Every page must declare a `type` in its front matter, chosen from exactly this list and written verbatim in lower case. Do not invent new values, do not add qualifiers, and do not describe the page in the type field.

- `market-view` — what a research note concludes, on what evidence, and under what stated assumptions. Use this for every page derived primarily from a research note.
- `allocation-guidance` — the firm's own binding portfolio weights, bands, and the conditions under which a weight is suspended.
- `suitability-guidance` — the firm's own rules about which clients may hold what, and the documentation standard that applies.
- `authority-guidance` — who may approve what, which conditions require escalation, and what may not be cleared by approval at any level.
- `regulatory-overlay` — a requirement imposed by a regulator, and the internal guidance that implements it.
- `position-assembly` — how note editions, re-issues, and regulatory overlays combine to produce the basis of record for a position held today.

The type carries the distinction between published research, internal guidance, and regulatory constraint. That distinction is the most important thing a reader needs and the only one the type field is for, so keep it clean. A page that could plausibly take two types takes the one matching the document it is primarily derived from.

Section index pages do not declare a type.

## What counts as a material proposition

Document what changes a positioning decision, an eligibility decision, or an operational expectation. Specifically: what a note recommends and what assumption the recommendation rests on; the exact conditions under which a regulatory change invalidates a view; target weights, bands, and how they interact; when a weight is suspended rather than carried forward; the edition and regulatory variations that govern a position taken at a given date; escalation triggers and authority levels; and the documentation an adviser must retain.

Do not document that a section exists, that a note has a code, or that a definition is present. Apply this test: if the proposition were false, would it change how a reader positions a portfolio, determines eligibility, or advises a client? If not, leave it out.

## Grounding rules

Every material proposition must cite the exact section of the exact document that establishes it. Prefer a narrow line range over a whole file.

Never paraphrase a recommendation or a regulatory requirement in a way that changes its meaning. Where an outcome turns on a specific phrase — "item of tax preference", "on or after", "may not be cleared by approval" — quote that phrase verbatim in the prose rather than restating it.

Take particular care with a note's stated assumptions. A recommendation that a note itself describes as resting on one assumption is not the same proposition as the recommendation standing alone, and recording only the recommendation is how a wiki outlives the thing that justified it.

When a proposition depends on more than one document, cite all of them. A position that composes a research view with the internal weight derived from it is one proposition supported by two pieces of evidence, not two propositions.

## Document relationships

Most material propositions in this corpus compose two documents: a view or a
requirement in one and a note, regulatory announcement, or internal rule that
acts on it. When a proposition composes documents this way, state the
relationship explicitly, with a direction and one of the verbs below used
verbatim.

Name the **acting** document first, with its provision, then the verb, then the
document and provision it acts on. The acting document is always the grammatical
subject. Write "IRS Revenue Procedure 2025-41 N.3 supersedes FI-US-MUNI-CREDIT
2025-06 M.2", never "FI-US-MUNI-CREDIT 2025-06 M.2 is superseded by IRS Revenue
Procedure 2025-41 N.3".

Use exactly one of these verbs, in lower case, spelled as shown:

- `supersedes` — a later edition replaces an earlier one for positions taken
  after its effective date, or a regulatory change removes the basis of a view.
- `restores` — an exemption or relief restores a permitted action that a
  restriction in another document removed. Use this only where access or
  treatment is actually restored.
- `preserves` — a document expressly leaves another document's restriction,
  treatment, or limit intact. Use this where a reader might otherwise assume it
  was swept away with the rest.
- `modifies` — changes a weight, band, threshold, or condition without restoring
  what was removed.
- `implements` — internal guidance carries out a requirement imposed by a
  regulator.
- `constrains` — internal guidance or a regulatory requirement limits when or how
  a position may be taken. A constraint never changes what a note concludes, only
  what the firm may do about it.

Where one document both removes the basis of a view and preserves a neighbouring
treatment, those are two propositions, not one. IRS Revenue Procedure 2025-41
removes the after-tax basis for the private activity overweight at N.3 and leaves
the qualified 501(c)(3) exception undisturbed at N.5; document both, because a
reader who knows only the first will wrongly conclude the whole municipal view is
dead.

A proposition that relates two documents must cite both. Cite the acting
provision and the provision acted on, not one standing for the other.

## Editions and supersession

Every positioning statement must say which edition it describes. The edition in force when a position was taken is the basis of record for that position, so a superseded edition is still live knowledge and must not be deleted or rewritten as though the current edition had always applied.

Where a file carries a `SUPERSEDED by` marker, document both editions and state plainly which positions each one is the basis of record for.

A note that has been withdrawn does not become wrong retrospectively. It becomes the record of why a position was taken, which is exactly what a reviewer needs.

## What not to do

Do not write architecture, component, or data-flow documentation. This is not a software system. There are no modules, responsibilities, interfaces, or extension points here — there are research views, assumptions, regulatory requirements, and internal rules.

Do not state a positioning view without citing the controlling text. Do not treat internal guidance as authority over a research conclusion, or a research conclusion as authority over a regulatory requirement. Do not resolve a conflict between a note and the guidance derived from it by inventing an answer; document the conflict and cite both.
