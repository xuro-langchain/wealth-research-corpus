---
type: market-view
title: "Credit and duration views"
openwiki_generated: true
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T23:01:11.527Z
sources:
  - id: openwiki-source-28f8ac08cab10bd38b1c51d7
    resource: repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md
  - id: openwiki-source-0bbe82e6c73600a3c9b5b5b5
    resource: repo://external_sources/FED/2026-09-fomc-statement.md
  - id: openwiki-source-9bea220ba58ad168dc3accea
    resource: repo://external_sources/FED/2026-09-rates-on-reserve-balances-and-primary-credit.md
  - id: openwiki-source-782f1a3fffc4f6dec3274631
    resource: repo://internal_guidelines/allocation/us-taxable-fixed-income.md
  - id: openwiki-source-af626860d2d1b7985491621b
    resource: repo://internal_research/FI/US/DURATION-PATH/2026-10.md
  - id: openwiki-source-34464a9ae84e5251bb0b43e6
    resource: repo://internal_research/FI/US/IG-SPREADS/2025-09.md
  - id: openwiki-source-f2798a1b5239421401d0aab5
    resource: repo://internal_research/FI/US/PENSION-LDI/2026-03.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T23:01:11.527Z" }
---


## Scope: three views, not one aggregate credit call

This is a research synthesis, not allocation guidance or investment advice. It retains three distinct US Fixed Income Research editions and their scopes:

| Edition | Position | Expression | Governing premise |
| --- | --- | --- | --- |
| `FI-US-IG-SPREADS 2025-09` | Underweight US IG corporate credit | Approximately four percentage points within a taxable fixed-income sleeve; deploy proceeds to a higher-conviction sleeve position rather than cash | Index spreads offer too little compensation for cyclical risk. |
| `FI-US-PENSION-LDI 2026-03` | Overweight long-dated IG credit | Long-end, Single-A-and-better credit | Corporate defined-benefit plans persistently buy long corporate paper while surplus plans de-risk. |
| `FI-US-DURATION-PATH 2026-10` | Long duration by +0.4 years versus benchmark | 5–10 years with a steepening bias; avoid the long end | The desk expects one further increase over 12 months, versus 1.5 priced by the market. |

The IG and pension-LDI calls are deliberately compatible rather than offsetting duplicates. The former is an index-level **valuation** view; the latter is a maturity-bucket **flow** view. The pension note explicitly says this distinction means the long-credit overweight can sit alongside the broader IG underweight. The duration note is a rates/curve call, not an instruction to add long credit. [IG spreads G.1–G.5](repo://internal_research/FI/US/IG-SPREADS/2025-09.md#L16-L34) [Pension LDI L.1–L.5](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L16-L36) [Duration path D.1–D.4](repo://internal_research/FI/US/DURATION-PATH/2026-10.md#L16-L32)

## 1. Broad IG corporate credit: valuation-driven underweight

`FI-US-IG-SPREADS 2025-09`, published 2025-09-18 and applicable to positions taken on or after 2025-10-01, moved from neutral to underweight. Its case is that spreads were inside the tenth percentile of their 20-year range and that the compensation for cyclical risk was limited. Even after adjustment for the index's improved average rating and shorter duration, the note finds the index rich. [IG spreads G.1–G.2](repo://internal_research/FI/US/IG-SPREADS/2025-09.md#L14-L22)

This is not a forecast of imminent credit deterioration: leverage is stable and interest coverage is comfortable at index level. The key implementation consequence is to avoid turning an index valuation judgment into a quality-down trade; the note's concern is price, not fundamentals. Its principal counterargument is six quarters of liability-driven-investor demand, and the listed risks are that this technical persists, growth validates spreads, or carry drag accumulates in a range-bound market. [IG spreads G.3–G.6](repo://internal_research/FI/US/IG-SPREADS/2025-09.md#L24-L38)

The research note describes an approximate four-percentage-point sleeve underweight and makes its proceeds available for a higher-conviction position elsewhere, but that is not itself a binding sleeve weight. The allocation guide, rather than this research page, supplies binding targets and pairs its corporate underweight with the municipal overweight; it also specifies suspension and escalation when supporting research is no longer usable. [IG spreads G.5](repo://internal_research/FI/US/IG-SPREADS/2025-09.md#L32-L34) [allocation guide A.1, A.5–A.6](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [allocation guide A.5–A.6](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L33-L43)

## 2. Long credit: a pension-demand call with a broken live premise

`FI-US-PENSION-LDI 2026-03`, published 2026-03-05 and applicable from 2026-04-01, upgraded long-dated IG credit from neutral to overweight. It expects corporate defined-benefit plans to remain buyers through 2028, with demand large relative to net long-end issuance. The mechanism is surplus-plan de-risking: plans extend duration and rotate return-seeking assets into long credit to protect surplus. The note restricts credit quality to Single-A and better because the expected payment is for the flow rather than incremental credit risk. [Pension LDI L.1–L.4](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L14-L32)

The view was explicitly conditional. The note says that a rule change allowing sponsors to release or re-risk surplus can reverse the flow, and names a change permitting surplus release, altering the discount-rate basis, or cutting contribution requirements as the event that takes out both its demand premise and recommendation. It calls for review at 12 months or sooner upon an announced change to pension funding or discount-rate rules. [Pension LDI L.2, L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [Pension LDI L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46)

**DOL Release 2026-31 P.2 and P.3 supersedes FI-US-PENSION-LDI 2026-03 L.2's funding-rule premise for plan years beginning on or after 2027-01-01.** The release widens the discount-rate corridor from 10% to 20%, which can permit a higher measurement discount rate and lower measured liabilities. For a plan exceeding 110% funded on that measurement, it conditionally removes the minimum required contribution and permits an election to make the excess available for specified uses. That combination is the kind of discount-rate, contribution, and surplus-use change the note identifies as invalidating its demand mechanism. [DOL release P.2–P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L13-L25) [Pension LDI L.2, L.6](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [Pension LDI L.6](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L42)

The result is a premise-level issue, not a reissue of the research edition and not evidence for a new long-credit allocation. Relief requires the above-110% result and sponsor election; participant notice follows an election. **DOL Release 2026-31 P.5 preserves** the requirements for plans below 80% funded, but that narrow preservation does not restore the surplus-plan premise. Retain the 2026-03 edition as the historical basis of record where it applied. [DOL release P.3, P.5–P.6](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L19-L35) [Pension LDI L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46)

## 3. Duration path: modest 5–10-year long duration, not long-end duration

`FI-US-DURATION-PATH 2026-10`, published 2026-10-06 and applicable from 2026-11-01, recommends +0.4 years versus benchmark, expressed in 5–10 years. It avoids long-end duration because the desk sees term premium as fair to cheap, continued heavy long-end supply, and no catalyst for compression within 12 months. The preferred curve expression has a 2s–10s steepening bias rather than a parallel extension. [Duration path D.1, D.3–D.4](repo://internal_research/FI/US/DURATION-PATH/2026-10.md#L14-L18) [Duration path D.3–D.4](repo://internal_research/FI/US/DURATION-PATH/2026-10.md#L26-L32)

The policy premise is narrow: after the September increase, the desk expects one further increase in the next 12 months versus 1.5 implied by markets. The September FOMC statement raised the target range to 3.75%–4.00% in response to elevated inflation, but expressly does not commit to a future sequence and says subsequent adjustments depend on incoming data and the evolving outlook. Thus the +0.4-year position is a modest divergence from priced policy, not a claim that the hiking cycle is complete. [Duration path D.2](repo://internal_research/FI/US/DURATION-PATH/2026-10.md#L20-L24) [FOMC statement F.1–F.2, F.5](repo://external_sources/FED/2026-09-fomc-statement.md#L10-L16) [FOMC statement F.5](repo://external_sources/FED/2026-09-fomc-statement.md#L26-L30)

**FED Implementation Note 2026-09-16 I.1–I.4 implements FED Statement 2026-09-16 F.1.** It mechanically set interest on reserve balances at 3.90% and the primary-credit rate at 4.0%, effective 2026-09-17; it does not modify or extend the FOMC statement and provides no path guidance beyond F.5. Use the FOMC statement for the policy decision and its conditional path framing, and the implementation note only for the administered-rate settings that carry out that decision. [Fed implementation note I.1–I.4](repo://external_sources/FED/2026-09-rates-on-reserve-balances-and-primary-credit.md#L8-L30) [FOMC statement F.1, F.5](repo://external_sources/FED/2026-09-fomc-statement.md#L10-L12) [FOMC statement F.5](repo://external_sources/FED/2026-09-fomc-statement.md#L26-L30)

The duration risks are a run of inflation prints that changes the assumed single increase into a sequence, additional long-end supply after a fiscal event, and disorderly term-premium repricing. The July meeting's three hawkish dissents make the first tail risk concrete, but do not turn the September statement into a promised rate path. [Duration path D.5](repo://internal_research/FI/US/DURATION-PATH/2026-10.md#L34-L36) [FOMC statement F.6](repo://external_sources/FED/2026-09-fomc-statement.md#L32-L36)

## Operating distinctions

- Do not net the broad IG underweight against the long-credit overweight without retaining their separate valuation and pension-flow premises, maturity scopes, and failure conditions.
- Do not express the duration view by adding long-end duration: its stated expression is 5–10 years with a steepening bias, and the long end is specifically avoided.
- Do not treat a research recommendation—or a regulatory overlay that defeats a premise—as a binding target. Binding weights and any suspension/escalation mechanics belong to allocation guidance and authorized decision-makers.
- For review of a pre-2027 pension-LDI position, preserve the applicable 2026-03 research edition as its decision record; for live action at the DOL effective boundary, record the premise failure and election-dependent facts without resolving the replacement allocation locally.
