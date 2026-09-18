---
title: Wealth Research Decision Guide
description: Route a wealth-management positioning, eligibility, regulatory-change, or escalation question to the research, internal guidance, regulatory overlay, and position-assembly record that governs it. Use this map to keep research conclusions, binding internal controls, and regulatory constraints distinct.
tags:
  - wealth-management
  - decision-routing
  - research
  - guidance
  - regulatory
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T23:01:11.527Z
sources:
  - id: openwiki-source-28f8ac08cab10bd38b1c51d7
    resource: repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md
  - id: openwiki-source-28793825e738ee3b286c0cbe
    resource: repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md
  - id: openwiki-source-ca8616022bc9a5e2668c0bee
    resource: repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md
  - id: openwiki-source-923e8a4660b350ffa68a69b7
    resource: repo://internal_guidelines/allocation/gl-multi-asset-bands.md
  - id: openwiki-source-782f1a3fffc4f6dec3274631
    resource: repo://internal_guidelines/allocation/us-taxable-fixed-income.md
  - id: openwiki-source-2ddd4f14dfe61f21d64eb273
    resource: repo://internal_guidelines/authority/discretion-matrix.md
  - id: openwiki-source-a3829d4e9c678bcdeb1949dc
    resource: repo://internal_guidelines/suitability/concentrated-positions.md
  - id: openwiki-source-fb21b102a1ad2b7795bf786c
    resource: repo://internal_guidelines/suitability/private-markets-eligibility.md
  - id: openwiki-source-3a77c67ca55a9fd04c605e57
    resource: repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md
  - id: openwiki-source-68f8f24fcd732cd566401775
    resource: repo://internal_research/MA/GL/RATES-REGIME/2026-02.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T23:01:11.527Z" }

openwiki_generated: true
---

# Wealth Research Decision Guide

Use this page to find the right decision record; it does not set an allocation, determine eligibility, or approve an action. This corpus is synthetic: its research, regulator-voiced documents, releases, dates, and figures are invented for the demonstration, while statutory citations are used accurately. Treat the material as corpus evidence, not real-world investment, legal, tax, or regulatory advice. [Corpus scope](repo://README.md#L1-L19)

## Start with the authority boundary

The sources have different jobs and must not be collapsed into a single “current view.” Frozen **internal research** records the desk’s view and the edition that supported a position; a new edition is a new file, while the old one remains the basis of record for positions taken during its applicability. **Internal guidance** is the firm’s living, operative material: it turns supported views into binding weights, limits, suitability files, and approval controls. A **regulatory overlay** constrains what may be done; it does not authorize a manager to create a replacement allocation. [Corpus layout and lifecycle](repo://README.md#L21-L48) [Position-assembly procedure](/openwiki/position-assembly/basis-of-record-and-suspended-weights.md)

In particular, documents under `external_sources/` are synthetic documents written in a regulator’s voice and say that no reliance is possible. Their role here is to test the stated premise of a research view and to route the internal response, not to supply real regulatory advice. [Synthetic external-source convention](repo://README.md#L12-L19) [SEC Order IA-7104 banner](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L1-L8)

## Choose the task

| If the question is… | Read first | Then apply / route to |
| --- | --- | --- |
| **What is the current fixed-income positioning view?** | [US Fixed Income: Credit Buckets and Duration Path](/openwiki/research/fixed-income/credit-and-duration-views.md) for IG credit, long credit, and 5–10-year duration; [US Municipal Credit](/openwiki/research/fixed-income/municipal-credit.md) for the municipal view and its AMT premise. | For a US taxable account’s binding targets, sector limits, duration band, paired municipal/IG weights, and drift treatment, use [Internal Guidance: US Taxable Fixed Income Allocation](/openwiki/guidance/allocation/us-taxable-fixed-income.md). Research is not itself a binding portfolio weight. [Guide standing](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L11) |
| **Which research edition supports a semiconductor or AI-infrastructure position?** | [US Semiconductor Capex: Edition History and Power Constraint](/openwiki/research/equities/semiconductor-capex.md) for the 2025-06/2026-02 edition boundary; [Global AI Infrastructure: Power as the Binding Constraint](/openwiki/research/equities/ai-infrastructure-power.md) for utilities/electrical equipment and the constraint’s limited effect on semiconductor capacity. | For a historical versus new action, select the applicable edition by position date; the 2026-02 semiconductor edition applies to positions from 2026-03-01 and supersedes 2025-06. [2026-02 applicability](repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md#L12-L18) [Assembly procedure](/openwiki/position-assembly/basis-of-record-and-suspended-weights.md) |
| **How should global balanced strategic bands or duration diversification be handled?** | [Global Rates Regime and Strategic-Band Underwriting](/openwiki/research/multi-asset/rates-regime.md). It is a framework recommendation to review bands, not a committee-set band. | [Internal Guidance: Global Multi-Asset Bands](/openwiki/guidance/allocation/global-multi-asset-bands.md) supplies the strategic weights, tolerance bands, reduced duration underwriting, and review state. A band outside its limit requires the applicable approval path. [Bands standing and review](repo://internal_guidelines/allocation/gl-multi-asset-bands.md#L7-L11) [Research/committee boundary](repo://internal_research/MA/GL/RATES-REGIME/2026-02.md#L28-L30) |
| **Can a client be offered or committed to private markets?** | Begin with [Internal Guidance: Private Markets Eligibility and File Standard](/openwiki/guidance/suitability/private-markets-eligibility.md), then [Private Markets Framework](/openwiki/research/multi-asset/private-markets.md) for the eligible-client view, horizon, and liquidity underwriting. | Check the [Qualified-Client Thresholds and Transition overlay](/openwiki/regulatory-overlays/qualified-client-thresholds.md), separate accredited-investor and suitability work, the binding liquidity limit/pacing treatment in [Global Multi-Asset Bands](/openwiki/guidance/allocation/global-multi-asset-bands.md), and approval in [Discretion, Escalation, and Non-Approvals](/openwiki/guidance/authority/discretion-and-escalation.md). Eligibility must be determined and documented before an offer and is outside portfolio-manager discretion. [Eligibility standing](repo://internal_guidelines/suitability/private-markets-eligibility.md#L7-L10) |
| **Has an AMT or pension-funding change undermined a live fixed-income rationale?** | Use [Regulatory Overlay: AMT Threshold Change and Municipal Treatment](/openwiki/regulatory-overlays/municipal-amt-thresholds.md) with [US Municipal Credit](/openwiki/research/fixed-income/municipal-credit.md), or [Regulatory Overlay: Pension Funding Relief and Long-Credit Premise](/openwiki/regulatory-overlays/pension-funding-relief.md) with the long-credit section of [US Fixed Income](/openwiki/research/fixed-income/credit-and-duration-views.md). | Follow [Position Assembly: Editions, Regulatory Changes, and Suspended Guidance](/openwiki/position-assembly/basis-of-record-and-suspended-weights.md). Test the overlay against the note’s explicit premise and break condition, separately record preserved treatment, map every derived guide consequence, and escalate rather than calculate a replacement weight. The AMT procedure applies from 2026-01-01; the pension release applies for plan years from 2027-01-01. [IRS effective date](repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L18-L22) [DOL effective rule](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L13-L21) |
| **Is a position concentrated, hedged, or subject to an employer-security blackout?** | [Internal Guidance: Concentrated Position Suitability and Unwind Controls](/openwiki/guidance/suitability/concentrated-positions.md). | Use [Discretion, Escalation, and Non-Approvals](/openwiki/guidance/authority/discretion-and-escalation.md) for authority tier and approval. A blackout-period employer-security trade is prohibited and cannot be cured by approval. [Prohibition](repo://internal_guidelines/suitability/concentrated-positions.md#L25-L29) |
| **Does an action need approval, a Committee decision, or an audit record?** | [Internal Guidance: Discretion, Escalation, and Non-Approvals](/openwiki/guidance/authority/discretion-and-escalation.md). | Apply the mandate-specific guide as the tighter control. For a cited note that is superseded or withdrawn, suspend the derived weight, identify the replacement if any, all affected weights/accounts, and escalate to Committee; a manager may not carry the old weight or directly adopt a replacement view. [Superseded-note control](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37) |

## Operating sequence for a live decision

1. **Classify the question.** Separate historical review, proposed new action, position change, eligibility determination, and approval/escalation; one client matter can require more than one route.
2. **Read research for the premise and edition.** Use the edition applicable to the original position for historical review, and the current applicable edition for a new action. Do not rewrite the original rationale with a later edition. [Frozen-edition rule](repo://README.md#L41-L48)
3. **Apply operative internal guidance.** Locate the mandate target/band, suitability file, liquidity constraint, and authority limit. Guidance can constrain implementation, but it may not manufacture a research conclusion.
4. **Test overlays separately.** If a regulatory change affects the stated premise, preserve any express exception or unaffected neighbouring treatment; it is not by itself a new allocation instruction.
5. **Use the assembly and escalation route on failure.** A premise-removing overlay without replacement research is a suspended-guidance case, not ordinary rebalancing. The Committee—not the portfolio manager—makes the binding resolution, and the cleared record needs the condition, authority, facts, and date. [Suspension and record requirements](repo://openwiki/position-assembly/basis-of-record-and-suspended-weights.md#L60-L80)

## Common routing failures

- Do not use a research range or recommendation as a client eligibility determination, approval, or binding mandate weight. Private-markets eligibility, suitability, and liquidity are distinct gates. [Private-markets separation](/openwiki/research/multi-asset/private-markets.md)
- Do not treat a preserved exception as restoration of an invalidated overall thesis. The municipal overlay preserves qualified-501(c)(3) treatment while the AMT-threshold premise requires separate handling. [Municipal treatment](/openwiki/research/fixed-income/municipal-credit.md)
- Do not treat a suspension-caused breach as routine drift or mechanically rebalance it. [US taxable fixed-income suspension rule](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L39-L43)
- Do not seek approval as a substitute for a regulatory requirement or an absolute prohibition. [Non-approvals](repo://internal_guidelines/authority/discretion-matrix.md#L39-L47)
