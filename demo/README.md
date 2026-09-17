# Staged demo documents

Documents held out of the corpus so they can be ingested live during a demo. `.openwikiignore`
excludes this directory, so nothing here is visible to OpenWiki until it is deliberately committed
into `research/` or `bulletins/` by the ingest API.

Do not move these into place by hand. The point of the demo is that the ingest API infers the
destination from the document's content, shows the inference on a confirm screen, and commits it —
including the supersession marker on the edition being replaced.

| File | Ingests as | What it demonstrates |
| --- | --- | --- |
| `SEC-2026-14.md` | `bulletins/SEC/2026-05-qualified-purchaser-exemption-relief-for-registered-advisers.md` | A net-new regulatory document. Small compile, and an honest blast radius of zero — nothing cites it yet. It `restores` access that `SEC Release 2025-08 Q.2` removed and `preserves` the family company threshold at `E.4`. |
| `MUNI-CREDIT/2026-04.md` | `research/FI/US/MUNI-CREDIT/2026-04.md` | The heavier run. A re-issued research note that **supersedes** `2025-11`, which the taxable fixed income allocation guide derives its municipal overweight from. The impact analysis reports internal guidance resting on a withdrawn note. |

## The supersession beat

`MUNI-CREDIT/2026-04.md` is the one worth rehearsing. The chain the agent has to walk:

1. `FI-US-MUNI-CREDIT 2025-11` recommends a municipal overweight at `M.1` and states at `M.2` that
   the recommendation rests on an AMT assumption — naming, at `M.7`, the change that would
   invalidate it.
2. `IRS Notice 2026-18` makes exactly that change at `N.2` and `N.3`. It is already in the corpus.
3. `guidelines/allocation/us-taxable-fixed-income.md` derives a binding 22% municipal weight at
   `A.3` from that note, and pairs an IG corporate underweight to it at `A.5`.
4. Ingesting `2026-04` marks `2025-11` superseded. Every claim citing `2025-11` is now a claim
   resting on a withdrawn note — including the ones the allocation guide depends on.
5. `guidelines/authority/discretion-matrix.md` at `D.4` says what a portfolio manager must then do,
   and says explicitly that carrying the prior weight forward is not the conservative choice.

The nuance that makes it a good demo rather than a dramatic one: `IRS Notice 2026-18 N.4`
**preserves** the treatment of qualified 501(c)(3) interest, and two of the three preferred sectors
at `M.5` are 501(c)(3) issuers. A report that says the whole municipal view is dead has over-read
the notice. A correct report separates what was removed from what survived.
