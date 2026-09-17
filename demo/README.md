# Staged demo documents

Documents held out of the corpus so they can be ingested live during a demo. `.openwikiignore`
excludes this directory, so nothing here is visible to OpenWiki until it is deliberately committed
into `research/` or `bulletins/` by the ingest API.

Do not move these into place by hand. The point of the demo is that the ingest API infers the
destination from the document's content, shows the inference on a confirm screen, and commits it —
including the supersession marker on the edition being replaced.

| File | Ingests as | What it demonstrates |
| --- | --- | --- |
| `FED-2026-09-16-implementation-note.md` | `bulletins/FED/2026-09-…` | A net-new regulatory document. Small compile, and an honest blast radius of zero — nothing cites it yet. It `implements` the FOMC statement at `F.1` and `preserves` the balance-sheet policy at `F.4`, so it exercises typed relations without invalidating anything. |
| `MUNI-CREDIT/2026-04.md` | `research/FI/US/MUNI-CREDIT/2026-04.md` | The heavier run. A re-issued research note that **supersedes** `2025-06`, which the taxable fixed income allocation guide derives its municipal overweight from. The impact analysis reports internal guidance resting on a withdrawn note. |

## The supersession beat

`MUNI-CREDIT/2026-04.md` is the one worth rehearsing. Every document in the chain is synthetic, but
the *mechanism* is real law — the statutory citations are accurate, which is what makes the chain
hold together under questioning:

1. `FI-US-MUNI-CREDIT 2025-06` recommends a municipal overweight at `M.1` and states at `M.2` that
   it rests on the AMT phase-out thresholds then in force — naming, at `M.7`, a reduction in that
   threshold as the change that would invalidate it.
2. `IRS Revenue Procedure 2025-41` does exactly that at `N.3`: the phase-out threshold for taxable
   years beginning on or after 2026-01-01 is set at $500,000 / $1,000,000, well below the level at
   which the exemption previously reached zero, and it is expressly not indexed before 2030. It is
   already in the corpus.
3. `guidelines/allocation/us-taxable-fixed-income.md` derives a binding 22% municipal weight at
   `A.3` from that note, and pairs an IG corporate underweight to it at `A.5`.
4. Ingesting `2026-04` marks `2025-06` superseded. Every claim citing `2025-06` is now a claim
   resting on a withdrawn note — including the ones the allocation guide depends on.
5. `guidelines/authority/discretion-matrix.md` at `D.4` says what a portfolio manager must then do,
   and says explicitly that carrying the prior weight forward is not the conservative choice.

The nuance that makes it a good demo rather than a dramatic one: §57(a)(5)(C)(ii) excepts qualified
501(c)(3) bonds from the preference treatment altogether, and the revenue procedure leaves that
exception undisturbed at `N.5`. Two of the three preferred sectors at `M.5` — non-profit hospital
systems and private higher education — are predominantly 501(c)(3) issuers.

A report that says the whole municipal view is dead has over-read it. A correct report separates
what the threshold reached from what the statute never exposed.
