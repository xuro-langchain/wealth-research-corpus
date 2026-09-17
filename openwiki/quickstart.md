---
type: position-assembly
title: Wealth Research Positioning Quickstart
description: Entry point for defensible wealth positioning and eligibility questions. Routes readers to research conclusions, binding internal guidance, regulatory overlays, and the position basis-of-record workflow without conflating their authority.
tags: [wealth-management, positioning, research, allocation-guidance, regulatory-overlay, eligibility]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T14:58:26.570Z
sources:
  - id: openwiki-source-d4d55878a53be93639d11eff
    resource: repo://bulletins/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md
  - id: openwiki-source-4a3ba03e04222e6bc5743057
    resource: repo://bulletins/SEC/2026-04-order-ia-7104-qualified-client.md
  - id: openwiki-source-0325e37b3340c7a33cd38137
    resource: repo://guidelines/allocation/us-taxable-fixed-income.md
  - id: openwiki-source-d23120db2fa553b5cde8ad5b
    resource: repo://guidelines/authority/discretion-matrix.md
  - id: openwiki-source-8454ea8f656b7e0eb040b7c7
    resource: repo://guidelines/suitability/private-markets-eligibility.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
  - id: openwiki-source-f77a3c74be717f3eaf29eed6
    resource: repo://research/EQ/GL/AI-INFRA-POWER/2026-01.md
  - id: openwiki-source-630c5331663a211371954f06
    resource: repo://research/EQ/US/SEMI-CAPEX/2026-02.md
  - id: openwiki-source-f6f11dc2c2c5325137161d1d
    resource: repo://research/FI/US/MUNI-CREDIT/2025-06.md
  - id: openwiki-source-dd22da8524a95465d7a7469c
    resource: repo://research/MA/GL/PRIVATE-MARKETS/2025-12.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T14:58:26.570Z" }
---

## Start with the question, then keep the authorities separate

Use this page to route a proposed trade, an allocation change, an eligibility decision, or a historical review. The answer is assembled from distinct layers:

| Layer | What it answers | What it cannot do |
| --- | --- | --- |
| **Research conclusion** | What the relevant desk concluded in a named, frozen edition; its thesis, expression, assumptions, risks, and review trigger | Set a binding account weight, clear an exception, or determine regulatory eligibility |
| **Binding internal guidance** | The committee or Compliance rule that governs targets, bands, limits, pacing, suitability, authority, and documentation | Replace a research conclusion or waive a regulatory requirement |
| **Regulatory overlay** | The effective-date-specific legal test or tax treatment that constrains the action | Choose a portfolio allocation or be cured by discretionary approval |
| **Basis-of-record workflow** | Which frozen edition explains a historical position and how current overlays and living guidance govern action today | Automatically carry a superseded view into a new binding weight |

Research and regulatory bulletins are frozen authorities, while internal guidance is revised in place. Preserve the edition that applied when a position was taken; apply current regulatory and living-guidance constraints before an action now. [Corpus model](repo://README.md#L39-L48) [Basis-of-record workflow](/openwiki/workflows/position-basis-of-record.md)

## Task-routing map

| If the question is… | Read the research conclusion | Then read binding guidance | Then test the overlay and workflow |
| --- | --- | --- | --- |
| **How should US municipal credit and investment-grade funding be positioned?** | [Municipal credit and IG funding](/openwiki/research/fixed-income/municipal-credit-and-ig-funding.md) | [US Taxable Fixed Income Allocation Guidance](/openwiki/guidance/allocation/us-taxable-fixed-income.md) | [Municipal AMT Threshold Regulatory Overlay](/openwiki/regulatory/municipal-amt-thresholds.md), then [basis of record](/openwiki/workflows/position-basis-of-record.md) |
| **What duration and curve expression does the current US fixed-income research support?** | [US Duration and Curve Positioning](/openwiki/research/fixed-income/duration-and-curve.md) | Confirm the governing mandate's applicable bands and authority with [Discretion, Escalation, and Non-Clearable Conditions](/openwiki/guidance/authority/discretion-and-escalation.md) | Treat the FOMC statement as evidence for the stated policy decision, not a commitment to a future path; preserve the position-date edition. [Duration research D.2](repo://research/FI/US/DURATION-PATH/2026-10.md#L20-L24) [FOMC statement F.5](repo://bulletins/FED/2026-09-fomc-statement.md#L26-L30) |
| **What is the global balanced mandate’s strategic mix, duration underwriting, or private-markets pacing rule?** | [Rates Regime Research and Strategic-Band Underwriting](/openwiki/research/multi-asset/rates-regime-and-strategic-bands.md) and, for private markets, [Private Markets Allocation Research](/openwiki/research/multi-asset/private-markets.md) | [Global Multi-Asset Allocation Guidance](/openwiki/guidance/allocation/global-multi-asset-bands.md) | For a private-markets offer or commitment, also follow the qualified-client overlay and workflow below. |
| **May this client be offered or newly subscribed to a private-markets strategy?** | [Private Markets Allocation Research](/openwiki/research/multi-asset/private-markets.md) for mix, horizon, and liquidity—not eligibility | [Private Markets Eligibility and Documentation Guidance](/openwiki/guidance/suitability/private-markets-eligibility.md) and [Discretion, Escalation, and Non-Clearable Conditions](/openwiki/guidance/authority/discretion-and-escalation.md) | [Qualified-Client Regulatory Overlay](/openwiki/regulatory/private-markets-qualified-client.md); determine accredited-investor status separately and retain the required record. |
| **How should a semiconductor-capex or AI-power view be used?** | [Semiconductor Capex Editions and the AI Power Constraint](/openwiki/research/equities/semiconductor-capex-and-power-constraint.md) | Check mandate-specific limits and [authority/escalation](/openwiki/guidance/authority/discretion-and-escalation.md) before implementation | Use the position date to distinguish the superseded 2025-06 overweight from the 2026-02 neutral edition; the power view modifies capacity-addition timing rather than semiconductor end-demand. [Semiconductor 2026-02 S.1, S.4](repo://research/EQ/US/SEMI-CAPEX/2026-02.md#L16-L32) [Power research P.4](repo://research/EQ/GL/AI-INFRA-POWER/2026-01.md#L30-L32) |
| **Is a concentration, hedge, blackout trade, or band exception permitted?** | Use research only for the investment rationale | [Concentrated Position Suitability Guidance](/openwiki/guidance/suitability/concentrated-positions.md) and [authority/escalation](/openwiki/guidance/authority/discretion-and-escalation.md) | Stop for a non-clearable blackout, eligibility, or stated regulatory breach; do not seek approval as a substitute. [Discretion matrix D.5](repo://guidelines/authority/discretion-matrix.md#L39-L47) |
| **What justified an existing position or what happens after re-issue/withdrawal?** | Locate the frozen edition effective on the position date | Locate the current guide that implemented the cited research | Follow [Assembling a Position Basis of Record](/openwiki/workflows/position-basis-of-record.md). |

## Minimum control sequence

1. **Classify the task.** Is it a research question, a mandate implementation question, a regulatory eligibility question, or a historical-review question? Use the corresponding row above; do not answer one layer with another.
2. **Identify date, mandate, account facts, and source edition.** A research edition is the historical basis for positions taken while it applied. A later edition does not rewrite that record. [Corpus conventions](repo://README.md#L41-L48) [Basis-of-record workflow](/openwiki/workflows/position-basis-of-record.md)
3. **Read the research with its conditions.** Record the recommendation, stated assumption, implementation expression, risks, and review trigger. For example, the municipal overweight is explicitly threshold-dependent, while private-markets research applies only to eligible clients with a genuine ten-year horizon. [Municipal research M.1–M.2](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L16-L30) [Private-markets research V.1–V.2](repo://research/MA/GL/PRIVATE-MARKETS/2025-12.md#L16-L22)
4. **Apply binding guidance.** The mandate guide sets the operative target, band, sector limit, pacing rule, or required approval. A research preference may be made binding only where the guide says so. [Taxable fixed-income guide A.1, A.4](repo://guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Taxable fixed-income guide A.4](repo://guidelines/allocation/us-taxable-fixed-income.md#L25-L31)
5. **Test current regulatory constraints and non-clearable conditions.** Private-markets eligibility must be determined and documented before an offer; an approval cannot clear an ineligible client or a stated regulatory breach. [Eligibility guide P.1](repo://guidelines/suitability/private-markets-eligibility.md#L7-L10) [Discretion matrix D.5](repo://guidelines/authority/discretion-matrix.md#L39-L47)
6. **Use the correct exception path.** A cited research note that is superseded or withdrawn suspends the derived weight. Escalate to the committee with the affected notes, weights, and accounts; neither retain the old weight nor directly adopt replacement research. [Discretion matrix D.4](repo://guidelines/authority/discretion-matrix.md#L31-L37)
7. **Retain the record.** Cleared escalations need the condition, clearing authority, facts, and date. Eligibility determinations need their pathway, evidence, decision maker, and date; absent recorded basis is treated as absent in audit. [Discretion matrix D.6](repo://guidelines/authority/discretion-matrix.md#L49-L51) [Eligibility guide P.5](repo://guidelines/suitability/private-markets-eligibility.md#L27-L29)

## Two high-risk forks

### Municipal AMT change: research premise is not a replacement allocation

Revenue Procedure 2025-41 N.3 **supersedes** the threshold premise in FI-US-MUNI-CREDIT 2025-06 M.2 for covered tax years: the municipal note identifies that premise as load-bearing and says its recommendation does not survive a reduction that materially expands top-bracket AMT exposure. N.4 **preserves** the specified-private-activity-bond preference treatment, and N.5 **preserves** the qualified 501(c)(3) exception. Route the resulting action through the municipal overlay, taxable fixed-income guidance, and the basis-of-record workflow rather than treating the bulletin as a new portfolio instruction. [Revenue Procedure N.3–N.5](repo://bulletins/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L18-L34) [Municipal research M.2](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L22-L30)

### Private markets: eligibility is necessary, not sufficient

For a determination on or after 2026-06-29, SEC Order IA-7104 Q.2 sets the adjusted Rule 205-3 paths; a pre-effective-date determination is preserved only for its original contract or investment and cannot support a new entry on or after that date. The order adjusts neither accredited-investor standards nor the qualified-purchaser definition. The internal eligibility guide **implements** the order, while separate suitability, liquidity, and commitment-approval controls still apply. [SEC Order Q.2, Q.4, Q.6](repo://bulletins/SEC/2026-04-order-ia-7104-qualified-client.md#L14-L18) [SEC Order Q.4](repo://bulletins/SEC/2026-04-order-ia-7104-qualified-client.md#L24-L28) [SEC Order Q.6](repo://bulletins/SEC/2026-04-order-ia-7104-qualified-client.md#L34-L36) [Eligibility guide P.2–P.6](repo://guidelines/suitability/private-markets-eligibility.md#L11-L33)

## When the answer is not clear

Do not infer a binding weight from research, waive an overlay through discretionary approval, or resolve a supersession by carrying forward a prior weight. Escalate under the authority guidance and assemble the documented basis of record. This preserves the distinction that makes a positioning or eligibility answer defensible.
