---
type: position-assembly
title: Wealth Research Positioning Guide
description: Decision-first routing for wealth positioning questions. Select the applicable research view, binding firm guidance, regulatory overlay, or dated position basis of record without substituting one authority for another.
tags: [wealth-management, positioning, research, regulatory-overlay, escalation]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T14:28:14.346Z
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
  - id: openwiki-source-f6f11dc2c2c5325137161d1d
    resource: repo://research/FI/US/MUNI-CREDIT/2025-06.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T14:28:14.346Z" }
---

# Wealth Research Positioning Guide

> **Corpus boundary:** This is a routing guide for the synthetic corpus, not investment, tax, or legal advice. Regulatory-voice bulletins and their figures are synthetic; statutory citations are the corpus’s stated exception. [Corpus disclaimer](repo://README.md#L7-L19)

## Select the authority before answering

A market-view note records a desk conclusion and its assumptions. Internal guidance supplies the firm’s binding weights, limits, eligibility process, and approvals. A regulatory overlay states the bounded external condition that constrains implementation. For a dated review, position assembly retains the research edition that applied when the position was taken, identifies the separate current control, and tests the relevant overlay; a later edition does not rewrite the historical record. [Frozen and living authority](repo://README.md#L41-L48) [Position-assembly procedure](repo://openwiki/position-assembly/supersession-and-escalation.md#L11-L19)

| Decision needed | Start here | Then route to |
| --- | --- | --- |
| **Market stance or stated assumption** | The relevant research page below. | Use mandate guidance before implementing a weight; research does not itself create one. [Rates Regime R.4](repo://research/MA/GL/RATES-REGIME/2026-02.md#L28-L30) |
| **Binding account weight, band, limit, or mandate rule** | [Taxable Fixed Income Guidance](/openwiki/guidance/allocation/taxable-fixed-income.md) or [Global Multi-Asset Bands](/openwiki/guidance/allocation/global-multi-asset-bands.md). | Apply the applicable overlay and obtain approval where the guide requires it. [Taxable-guide standing](repo://guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Global-bands standing](repo://guidelines/allocation/gl-multi-asset-bands.md#L7-L11) |
| **Regulatory status, tax treatment, threshold, or effective date** | The relevant overlay below. | Do not use an approval or research view as a substitute for the requirement; a regulatory breach cannot be cleared by approval. [Discretion Matrix D.5](repo://guidelines/authority/discretion-matrix.md#L39-L47) |
| **Historical position, changed premise, supersession, or exception** | [Position Assembly](/openwiki/position-assembly/supersession-and-escalation.md). | Identify the date, edition, guide-derived control, and applicable overlay before applying the documented escalation path. [Position-assembly procedure](repo://openwiki/position-assembly/supersession-and-escalation.md#L13-L19) |

## Decision paths

### Fixed income

- **Municipal credit view:** Start with [US Municipal Credit](/openwiki/research/fixed-income/municipal-credit.md). The 2025-06 note’s two-to-four-point municipal increase is funded from investment-grade corporate credit and depends on its after-tax AMT-threshold premise; fundamentals alone support only neutral to modest overweight. [Municipal Credit M.1–M.3](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L16-L36)
- **Municipal tax condition:** Then use the [IRS Private-Activity-Bond AMT Overlay](/openwiki/regulatory/irs-private-activity-bond-amt.md). **IRS Revenue Procedure 2025-41 N.3 supersedes FI-US-MUNI-CREDIT 2025-06 M.2** for the threshold-dependent premise for affected taxpayers in taxable years beginning on or after 2026-01-01; N.5 **preserves** the qualified-501(c)(3) exception. The procedure does not choose a replacement allocation. [Revenue Procedure N.3 and N.5](repo://bulletins/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L18-L34) [Municipal Credit M.2 and M.5](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L22-L30) [Municipal Credit M.5](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L44-L50)
- **Actual taxable-sleeve controls:** Use [Taxable Fixed Income Guidance](/openwiki/guidance/allocation/taxable-fixed-income.md), not the research note, for the 22% top-bracket municipal target, 18% neutral comparison, PAB concentration, and paired 28% investment-grade corporate target. [Allocation Guide A.3 and A.5](repo://guidelines/allocation/us-taxable-fixed-income.md#L17-L23) [Allocation Guide A.5](repo://guidelines/allocation/us-taxable-fixed-income.md#L33-L37)
- **Corporate-credit view:** Use [Investment Grade Spreads](/openwiki/research/fixed-income/investment-grade-spreads.md) for the valuation-led corporate underweight and its roughly four-point sleeve expression. [IG Spreads G.1–G.5](repo://research/FI/US/IG-SPREADS/2025-09.md#L16-L34)
- **Duration and curve:** Use [US Duration and Curve](/openwiki/research/fixed-income/duration-and-curve.md), then the [Federal Reserve Policy-Path Overlay](/openwiki/regulatory/fed-policy-path.md). The research expresses +0.4 years in the five-to-ten-year sector and makes a desk scenario assumption; the statement describes a rate decision, not a committed future path. [Duration Path D.1–D.2](repo://research/FI/US/DURATION-PATH/2026-10.md#L16-L24) [FED Statement F.1 and F.5](repo://bulletins/FED/2026-09-fomc-statement.md#L10-L12) [FED Statement F.5](repo://bulletins/FED/2026-09-fomc-statement.md#L26-L30)

### Equities

- Use [Semiconductor Capex](/openwiki/research/equities/semiconductor-capex.md) for the dated US semiconductor view. Edition 2026-02 **supersedes** edition 2025-06 for positions taken on or after 2026-03-01; the 2025-06 edition remains the basis of record for positions taken while it stood. [2025-06 supersession marker](repo://research/EQ/US/SEMI-CAPEX/2025-06.md#L1-L5) [2026-02 applicability and view](repo://research/EQ/US/SEMI-CAPEX/2026-02.md#L12-L18)
- Use [AI Infrastructure Power](/openwiki/research/equities/ai-infrastructure-power.md) for the global utilities and electrical-equipment research view. **AI Infrastructure Power 2026-01 P.4 modifies Semiconductor Capex 2026-02 S.4** by limiting the rate of capacity addition rather than eventual demand; it is not a semiconductor allocation instruction. [AI Infrastructure P.1 and P.4](repo://research/EQ/GL/AI-INFRA-POWER/2026-01.md#L16-L18) [AI Infrastructure P.4](repo://research/EQ/GL/AI-INFRA-POWER/2026-01.md#L30-L32) [Semiconductor 2026-02 S.4–S.5](repo://research/EQ/US/SEMI-CAPEX/2026-02.md#L30-L36)

### Multi-asset and private markets

- Use [Global Rates Regime](/openwiki/research/multi-asset/rates-regime.md) for the higher-real-rate and diversification assumptions, and [Global Multi-Asset Bands](/openwiki/guidance/allocation/global-multi-asset-bands.md) for strategic weights and bands. The research requests a review; it does not set bands. [Rates Regime R.1–R.4](repo://research/MA/GL/RATES-REGIME/2026-02.md#L16-L30) [Global Bands B.1–B.5](repo://guidelines/allocation/gl-multi-asset-bands.md#L7-L29)
- Use [Private Markets](/openwiki/research/multi-asset/private-markets.md) only for the eligible-client research view. The firm’s 10% global-balanced sleeve, pro-rata liquid reallocation for ineligible clients, and commitment-pacing rules belong to [Global Multi-Asset Bands](/openwiki/guidance/allocation/global-multi-asset-bands.md). [Private Markets V.1–V.2](repo://research/MA/GL/PRIVATE-MARKETS/2025-12.md#L16-L22) [Global Bands B.2 and B.6](repo://guidelines/allocation/gl-multi-asset-bands.md#L13-L15) [Global Bands B.6](repo://guidelines/allocation/gl-multi-asset-bands.md#L31-L35)
- For an offer or commitment, start with [Private Markets Eligibility and Suitability](/openwiki/guidance/suitability/private-markets-eligibility.md), then [SEC Qualified Client Thresholds](/openwiki/regulatory/sec-qualified-purchaser.md). Eligibility must be determined and documented before an offer; suitability, liquidity, and approval remain separate gates. A pre-effective-date determination is preserved for its existing relationship but cannot support new business on or after 2026-06-29. [Eligibility Guide P.1 and P.6](repo://guidelines/suitability/private-markets-eligibility.md#L7-L9) [Eligibility Guide P.6](repo://guidelines/suitability/private-markets-eligibility.md#L31-L35) [SEC Order Q.4](repo://bulletins/SEC/2026-04-order-ia-7104-qualified-client.md#L24-L28)

## When a research-dependent control changes

When a mandate guide cites research that has been superseded or withdrawn, suspend the derived control and escalate to the Committee. Do not carry it forward, re-derive it, mechanically rebalance a suspension, or directly adopt replacement research; the escalation record identifies the prior and replacement note, dependent weights, and affected accounts. [Allocation Guide A.1 and A.6](repo://guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Allocation Guide A.6](repo://guidelines/allocation/us-taxable-fixed-income.md#L39-L43) [Discretion Matrix D.4](repo://guidelines/authority/discretion-matrix.md#L31-L37)

This trigger is distinct from a regulatory change to a research premise: the municipal note calls for immediate review and re-issue if its M.2 tax treatment changes, while the available controls do not establish an automatic suspension or successor weight solely from Revenue Procedure 2025-41. [Municipal Credit M.8](repo://research/FI/US/MUNI-CREDIT/2025-06.md#L68-L70) [Allocation Guide A.1](repo://guidelines/allocation/us-taxable-fixed-income.md#L7-L11)

For authority tiers, non-clearable conditions, and audit records, use [Portfolio Manager Discretion and Escalation](/openwiki/guidance/authority/discretion-and-escalation.md). Every cleared escalation needs the condition, authority level, facts relied upon, and date; absent that record, audit treats it as unapproved. [Discretion Matrix D.6](repo://guidelines/authority/discretion-matrix.md#L49-L51)

## Non-substitution check

Before closing a file, keep the historical research edition, current binding guide, and external constraint separately identifiable. A research recommendation is not a binding weight; guidance does not rewrite research; and neither guidance nor approval creates an exception to a regulatory requirement. [Position-assembly guardrails](repo://openwiki/position-assembly/supersession-and-escalation.md#L71-L75)
