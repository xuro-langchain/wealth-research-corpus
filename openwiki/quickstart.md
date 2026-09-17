---
type: position-assembly
title: Wealth Research Positioning Quickstart
description: Task-routing map for selecting frozen research, living internal guidance, regulatory overlays, and the position basis of record before acting. Highlights the unresolved municipal and prospective pension-demand premise conflicts without inferring replacement weights.
tags: [wealth-management, position-assembly, research-governance, internal-guidance, regulatory-overlay, eligibility]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T22:51:12.387Z
sources:
  - id: openwiki-source-28f8ac08cab10bd38b1c51d7
    resource: repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md
  - id: openwiki-source-28793825e738ee3b286c0cbe
    resource: repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md
  - id: openwiki-source-ca8616022bc9a5e2668c0bee
    resource: repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md
  - id: openwiki-source-782f1a3fffc4f6dec3274631
    resource: repo://internal_guidelines/allocation/us-taxable-fixed-income.md
  - id: openwiki-source-2ddd4f14dfe61f21d64eb273
    resource: repo://internal_guidelines/authority/discretion-matrix.md
  - id: openwiki-source-fb21b102a1ad2b7795bf786c
    resource: repo://internal_guidelines/suitability/private-markets-eligibility.md
  - id: openwiki-source-3a77c67ca55a9fd04c605e57
    resource: repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md
  - id: openwiki-source-04ccfa0b608194f7a35603a3
    resource: repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md
  - id: openwiki-source-f2798a1b5239421401d0aab5
    resource: repo://internal_research/FI/US/PENSION-LDI/2026-03.md
  - id: openwiki-source-b9de417e95295033973fc7c2
    resource: repo://internal_research/MA/GL/PRIVATE-MARKETS/2025-12.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T22:51:12.387Z" }
---

## Start with the authority and the date

This page routes a positioning question; it does not create an account instruction. Research editions and external-source overlays are frozen when published, whereas internal guidance is revised in place. Preserve the edition that applied when a position was taken as its historical basis of record; for an action now, use the current governing guidance, applicable overlay, mandate limits, and authority process. [Corpus authority model](repo://README.md#L39-L48)

| Authority | Use it to answer | Do not use it to answer |
| --- | --- | --- |
| **Frozen research** | Thesis, expression, assumptions, risks, and review trigger for its edition | Binding account weight, eligibility determination, or exception approval |
| **Living internal guidance** | Current targets, limits, bands, approval path, and required records | A regulatory waiver or replacement research conclusion |
| **Regulatory overlay** | Effective-date-specific tax or legal facts and constraints | An allocation or trade selection |
| **Position basis of record** | Which dated evidence and current controls supported a decision | A way to rewrite historical evidence or derive an unresolved outcome |

## Task-routing map

| Question | Start here | Before acting, also use |
| --- | --- | --- |
| Municipal-credit thesis, sector exposure, or IG funding rationale | [Municipal Credit and Investment-Grade Funding Views](/openwiki/research/fixed-income/municipal-credit-and-ig-funding.md) | [Municipal AMT Threshold Regulatory Overlay](/openwiki/regulatory/municipal-amt-thresholds.md), [US Taxable Fixed-Income Allocation Guidance](/openwiki/guidance/allocation/us-taxable-fixed-income.md), and [position basis of record](/openwiki/workflows/position-basis-of-record.md) |
| Long-credit demand after pension funding relief | [US Long Credit and Pension Demand](/openwiki/research/fixed-income/long-credit-and-pension-demand.md) | [Pension Funding Relief and Long-Credit Research Overlay](/openwiki/regulatory/pension-funding-relief.md), then the governing mandate and authority process |
| Private-markets thesis, sleeve mix, horizon, or liquidity | [Private Markets Allocation Research](/openwiki/research/multi-asset/private-markets.md) | Global multi-asset guidance, eligibility/suitability review, and commitment approval; research is not an offer decision |
| Whether a client may be offered or newly subscribed to private markets | Private-markets eligibility guidance and the applicable qualified-client overlay | Separate accredited-investor status, suitability, liquidity, and approval; eligibility must be determined and documented before an offer and cannot be cleared by investment discretion. [Eligibility standing](repo://internal_guidelines/suitability/private-markets-eligibility.md#L7-L9) [Non-clearable conditions](repo://internal_guidelines/authority/discretion-matrix.md#L39-L47) |
| What justified an existing municipal position | [Assembling a Position Basis of Record](/openwiki/workflows/position-basis-of-record.md) | Position date, applicable research edition, tax-year overlay, current guide, and approval record |
| Whether a research-derived weight must be suspended | The governing guide and [authority process](/openwiki/guidance/authority/discretion-and-escalation.md) | Apply the suspension path only when the guide-cited note is actually superseded or withdrawn—not merely because an overlay constrains a premise. [D.4 condition](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37) |
| Semiconductor-capex or AI-power research | [Semiconductor Capex Editions and the AI Power Constraint](/openwiki/research/equities/semiconductor-capex-and-power-constraint.md) | Select the applicable edition and check mandate limits before implementation. The 2026-02 edition is neutral from 2026-03-01 and treats grid interconnection as constraining the rate of capacity addition, not eventual demand. [Edition and applicability](repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md#L12-L18) [Power constraint](repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md#L30-L32) |

## Cross-domain conflict summary

### Municipal AMT: material premise conflict, not an inferred allocation result

FI-US-MUNI-CREDIT 2025-06 is marked current and not re-issued, applies to positions from 2025-07-01, and is the stated research basis for taxable-account municipal weightings. Its after-tax municipal overweight depends on the AMT phase-out threshold: the note says that lowering the threshold enough to draw materially more top-bracket holders into AMT takes out the recommendation. [Research status and applicability](repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md#L12-L16) [Load-bearing premise](repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md#L24-L32)

For taxable years beginning on or after 2026-01-01, Revenue Procedure 2025-41 sets phase-out thresholds of $500,000 for an unmarried individual and $1,000,000 for a joint return. It preserves specified-private-activity-bond interest as an AMT preference item, but preserves qualified section 145 501(c)(3) bond interest outside AMTI; do not treat all private-activity exposure as identical. [Threshold and effect](repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L18-L22) [Bond-treatment distinction](repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L24-L34)

The overlay therefore constrains the historical note’s load-bearing premise and activates its immediate review-and-re-issue lifecycle, but the repository provides neither a re-issue nor a replacement target. The current guide implements a 22% municipal target for top-bracket accounts and makes the cited sector preferences binding limits; its D.4 suspension control applies only if a cited note is superseded or withdrawn. If that condition occurs, the linked municipal overweight and investment-grade-corporate underweight return to their neutral references and the suspension-caused condition is not ordinary drift. Do not mechanically change, suspend, or re-derive a weight from this unresolved conflict. [Research review trigger](repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md#L70-L72) [Guide condition and municipal target](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L23) [Sector limits](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L25-L31) [Paired corporate suspension and drift boundary](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L33-L43)

### Pension funding relief: prospective premise change and research review

DOL Release 2026-31 applies to plan years beginning on or after 2027-01-01. It widens the discount-rate corridor, grants contribution relief only for plans whose measured funded status exceeds 110%, and permits limited surplus uses subject to notice; it does not authorize sponsor reversion outside the existing framework. [Effective date and corridor](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L7-L17) [Qualifying relief and uses](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L19-L25) [Notice](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L33-L35)

Those are the rule changes FI-US-PENSION-LDI 2026-03 identifies as invalidating its pension-demand premise for the long-credit overweight, and they meet its announced-rule review trigger. They do not rewrite the historical research record or establish a binding portfolio weight; binding weights, where applicable, belong to living internal guidance. [LDI premise and invalidators](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [LDI review trigger](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46) [Corpus authority model](repo://README.md#L39-L48)

The release also preserves restrictions for plans below 80% funded and does not address investment fiduciary standards. Treat that as a boundary on the overlay, not an investment-manager permission or instruction. [Preserved restrictions and fiduciary boundary](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L27-L31)

### Private markets: research condition versus client gate

MA-GL-PRIVATE-MARKETS 2025-12 presents its 10–20% strategic view only for eligible clients with a genuine ten-year horizon, and explicitly leaves qualified-client and accredited-investor eligibility to regulatory determination. Its liquidity condition is spending-based: unfunded commitments should not exceed two years of liquid portfolio spending. [Research condition and eligibility boundary](repo://internal_research/MA/GL/PRIVATE-MARKETS/2025-12.md#L16-L22) [Liquidity condition](repo://internal_research/MA/GL/PRIVATE-MARKETS/2025-12.md#L36-L38)

For determinations on or after 2026-06-29, SEC Order IA-7104 provides the adjusted Rule 205-3 tests; a pre-effective-date determination remains limited to its original contract or investment, and the order does not adjust accredited-investor or qualified-purchaser standards. Route new entries through the eligibility record rather than carrying an old determination forward. [Adjusted tests](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L14-L18) [Transition boundary](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L24-L28) [Separate standards](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L34-L36)

## Record and escalation minimums

When a guide-cited note is actually superseded or withdrawn, suspend the research-derived weight and escalate to the committee. A manager may not retain the prior weight, re-derive it, or adopt replacement research directly. [Supersession control](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37)

Retain the dated research, applicable overlay, current guidance, mandate facts, affected holdings, and decision rationale in the position record. A cleared escalation must state the condition, authority level, specific facts, and date. A private-markets eligibility determination must also state its pathway, evidence, decision maker, and date. [Escalation documentation](repo://internal_guidelines/authority/discretion-matrix.md#L49-L51) [Eligibility documentation](repo://internal_guidelines/suitability/private-markets-eligibility.md#L27-L29)
