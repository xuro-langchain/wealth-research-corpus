# OpenWiki Wealth Research Corpus

A small synthetic wealth management research corpus, used as the primary source layer for the
OpenWiki wealth research POC. The proposal that motivates it lives in the sibling
`wealth-research` repo under `docs/poc-proposal.md`.

Nothing here is a real firm's research, a real regulator's release, or investment advice. Note
codes, release numbers and section numbering deliberately resemble industry conventions so the
corpus reads realistically, but all operative language is invented. The figures are illustrative
and were written for this demo; they are not forecasts and not drawn from any real publication.

Every document in `bulletins/` carries a **SYNTHETIC DOCUMENT** banner under its title, because
those are the ones written in a regulator's voice and therefore the ones a reader could otherwise
mistake for the real thing. The issuing bodies, release numbers, dates and dollar amounts are
invented. **Statutory citations, by contrast, are to real provisions and are used accurately** —
section 57(a)(5)(A) really does make specified private activity bond interest an item of tax
preference, and section 57(a)(5)(C)(ii) really does except qualified 501(c)(3) bonds from it. That
is deliberate: the invented facts sit on a real legal mechanism, which is what lets the corpus
survive questions from someone who knows the area.

## Layout

```
research/{asset}/{region}/{note}/{edition}.md   frozen authority — never edited in place
bulletins/{regulator}/{id}.md                   frozen authority — regulator-issued
guidelines/{area}/{name}.md                     living guidance — edited in place, continuously
openwiki/INSTRUCTIONS.md                        the brief OpenWiki reads; never rewritten by a run
demo/                                           staged changes, ignored by OpenWiki
```

`{asset}` is a two-letter desk code — `FI` fixed income, `EQ` equities, `MA` multi-asset.
`{region}` is a two-letter market code, or `GL` for a note that takes a global view rather than
being scoped to one market.

The path is load-bearing. OpenWiki claims carry no domain attributes — the sidecar schema is
strict — so the evidence path is the only channel through which asset class, region, note and
edition reach the retrieval layer.

## The two halves

**Frozen authority** (`research/`, `bulletins/`) is never edited once published. A revision is a
*new file* at a new edition. The prior edition stays exactly as it was, because it remains the
basis of record for every position taken while it stood — a position taken in 2025 is reviewed
against the 2025 note in 2027, not against whatever replaced it.

**Living guidance** (`guidelines/`) is the firm's own internal material. It is revised in place,
section by section, and changes far more often than research does. This is the only half where
OpenWiki's relocation anchors ever fire.

## Conventions

**One paragraph per line. Never hard-wrap.** OpenWiki hashes evidence per line and uses three
lines of surrounding context to relocate a citation when text moves. Hard-wrapped prose produces
many short, near-identical lines, which defeats that and yields false "unresolved" flags. Long
lines are correct here even though they look wrong in a narrow editor.

**Number every section, and keep numbering stable within an edition.** Claims cite sections by
name in their statement and by line range in their evidence; stable numbering is what makes a
citation legible to a human reviewer.

**Mark supersession explicitly.** When a new edition is published, append a `> SUPERSEDED by ...`
block directly under the superseded file's title. OpenWiki detects byte changes, not semantic
supersession — this marker is what turns "a newer authority exists" into a signal it can act on.
Add only the marker; never alter operative text in a superseded file.

**State the load-bearing assumption in the note itself.** A recommendation whose justification
lives only in the analyst's head cannot be invalidated by a regulatory change, because nothing
records what would invalidate it. Notes here name the assumption and name what would break it.

**Keep the worktree clean.** Any untracked file makes OpenWiki's no-op check bail to a full model
run. Commit or ignore everything before running `--update`.

## Running OpenWiki

```sh
openwiki --init      # first build; writes openwiki/ and openwiki/.claims/
openwiki --update    # incremental; a clean run is a proven no-op with zero model calls
openwiki visualize   # interactive graph over the generated wiki
```

## Current contents

| Path | What it is |
| --- | --- |
| `research/FI/US/MUNI-CREDIT/2025-06.md` | municipal overweight; states its AMT threshold assumption as load-bearing at M.2 and names what would break it at M.7. **Never re-issued** — the premise is gone and the note still stands |
| `research/FI/US/PENSION-LDI/2026-03.md` | long credit overweight on pension demand; L.2 states the premise, L.6 names what ends it. **Never re-issued** |
| `research/FI/US/DURATION-PATH/2026-10.md` | duration and curve positioning; reads the Fed statement narrowly per F.5 |
| `research/FI/US/IG-SPREADS/2025-09.md` | investment grade underweight; funds the municipal overweight |
| `research/EQ/US/SEMI-CAPEX/2025-06.md` | semiconductor capex overweight, superseded by 2026-02, marker in place |
| `research/EQ/US/SEMI-CAPEX/2026-02.md` | semiconductor capex, current; cut to neutral on cycle position |
| `research/EQ/GL/AI-INFRA-POWER/2026-01.md` | power as the binding constraint; modifies the semi capex view at S.4 |
| `research/MA/GL/RATES-REGIME/2026-02.md` | rates regime; drives the duration underwriting in the bands guide |
| `research/MA/GL/PRIVATE-MARKETS/2025-12.md` | private markets framework; defers eligibility to the rule 205-3 thresholds |
| `bulletins/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md` | AMT amounts; resets the phase-out threshold at N.3, preserves the 501(c)(3) exception at N.5 |
| `bulletins/DOL/2026-08-funding-relief-and-discount-rates.md` | widens the discount rate corridor at P.2 and relieves surplus plans at P.3 — removing the pension-demand premise; P.5 preserves the under-80% restrictions |
| `bulletins/FED/2026-09-fomc-statement.md` | target range raised; F.5 says it is a decision and not a path |
| `bulletins/SEC/2026-04-order-ia-7104-qualified-client.md` | rule 205-3 dollar tests adjusted at Q.2; Q.4 preserves prior determinations, Q.6 leaves other standards alone |
| `guidelines/allocation/us-taxable-fixed-income.md` | taxable sleeve weights; derives the municipal overweight from M.1/M.2 |
| `guidelines/allocation/gl-multi-asset-bands.md` | strategic bands; underwrites duration per R.3 |
| `guidelines/suitability/private-markets-eligibility.md` | implements the rule 205-3 thresholds at Q.2 |
| `guidelines/suitability/concentrated-positions.md` | concentrated position standard and unwind planning |
| `guidelines/authority/discretion-matrix.md` | discretion tiers; D.4 governs a superseded note |

The documents are deliberately cross-wired, and the central pairing is a **conflict that nobody has
resolved**: the taxable fixed income guide derives its municipal weight from
`FI-US-MUNI-CREDIT 2025-06 M.1` and its rationale from `M.2`; `Rev. Proc. 2025-41 N.3` removes that
rationale, `N.5` preserves the qualified 501(c)(3) exception that two of the three preferred sectors
rely on — and **the note has never been re-issued**, so the firm is still carrying a weight whose
stated basis is gone. `FI-US-PENSION-LDI 2026-03` and `DOL Release 2026-31` are the same shape on
long credit. the discretion matrix at `D.4` says what a portfolio manager must
do when a cited note is superseded; and the IG spreads underweight at `A.5` is explicitly paired to
the municipal overweight, so suspending one suspends the other. That web is what makes a
positioning question resolve across several documents, and what a chunk-based retriever cannot
follow.
