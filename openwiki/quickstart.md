---
type: position-assembly
title: Wealth Research Positioning Quickstart
description: Routing guide for wealth-positioning, eligibility, regulatory, and historical-review questions. It separates frozen research, living internal guidance, regulatory overlays, and the documented position basis of record.
tags: [wealth-management, position-assembly, research, internal-guidance, regulatory-overlay, eligibility]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T21:44:02.449Z
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
generated: { by: "openwiki/0.5.0", at: "2026-09-17T21:44:02.449Z" }
---

## Choose the authority before answering the question

Use this page to find the correct decision record, not to turn a research view into an account instruction. Research editions and external-source overlays are frozen when published; internal guidance is living material revised in place. For a historical review, use the research edition applicable when the position was taken. For an action now, apply current guidance, regulatory constraints, mandate limits, and authority controls. [Corpus model](repo://README.md#L39-L48)

| Authority | Answers | Does not do |
| --- | --- | --- |
| **Frozen research** | Thesis, expression, assumptions, risks, and review triggers | Set a binding account weight or clear an exception |
| **Living internal guidance** | Operative targets, limits, bands, approvals, and records | Waive a regulatory requirement or substitute for research |
| **Regulatory overlay** | Effective-date-specific tax or legal constraints | Choose an allocation |
| **Position basis of record** | Historical edition selection and current-decision assembly | Preserve a derived weight whose basis requires review |

## Task-routing map

| If the question is… | Start here | Then apply |
| --- | --- | --- |
| **How should US municipal credit and its IG funding be handled?** | [Municipal Credit and Investment-Grade Funding Views](/openwiki/research/fixed-income/municipal-credit-and-ig-funding.md) for the frozen 2025-06 view | [Municipal AMT Threshold Regulatory Overlay](/openwiki/regulatory/municipal-amt-thresholds.md), [US Taxable Fixed-Income Allocation Guidance](/openwiki/guidance/allocation/us-taxable-fixed-income.md), and [Assembling a Position Basis of Record](/openwiki/workflows/position-basis-of-record.md). See the unresolved conflict below. |
| **What duration and curve expression does research support?** | [US Duration and Curve Positioning](/openwiki/research/fixed-income/duration-and-curve.md) | Confirm mandate bands and authority in [Discretion, Escalation, and Non-Clearable Conditions](/openwiki/guidance/authority/discretion-and-escalation.md). |
| **How should long-credit pension demand be assessed after funding relief?** | [US Long Credit and Pension Demand](/openwiki/research/fixed-income/long-credit-and-pension-demand.md) | Apply [Pension Funding Relief and Long-Credit Research Overlay](/openwiki/regulatory/pension-funding-relief.md); identify the governing mandate rather than treating either record as a binding weight. |
| **What is the global balanced mix or private-markets pacing rule?** | [Rates-Regime Research and Strategic-Band Underwriting](/openwiki/research/multi-asset/rates-regime-and-strategic-bands.md) or [Private Markets Allocation Research](/openwiki/research/multi-asset/private-markets.md) | [Global Multi-Asset Allocation Guidance](/openwiki/guidance/allocation/global-multi-asset-bands.md); use the eligibility route before an offer or commitment. |
| **May a client be offered or newly subscribed to private markets?** | [Private Markets Eligibility and Documentation Guidance](/openwiki/guidance/suitability/private-markets-eligibility.md) | [Qualified-Client Regulatory Overlay](/openwiki/regulatory/private-markets-qualified-client.md), then research and suitability/liquidity review. Accredited-investor status is separate. |
| **How should a semiconductor-capex or AI-power view be used?** | [Semiconductor Capex Editions and the AI Power Constraint](/openwiki/research/equities/semiconductor-capex-and-power-constraint.md) | Check mandate limits and authority before implementation. |
| **Is a concentration, hedge, blackout trade, or band exception permitted?** | [Concentrated Position Suitability Guidance](/openwiki/guidance/suitability/concentrated-positions.md) | [Authority guidance](/openwiki/guidance/authority/discretion-and-escalation.md); stop for a non-clearable blackout, eligibility failure, or regulatory breach. |
| **What justified an existing position?** | Locate the frozen edition applicable on the position date | Use [Assembling a Position Basis of Record](/openwiki/workflows/position-basis-of-record.md) with current guidance and overlays. |

## Municipal credit: unresolved guide conflict

FI-US-MUNI-CREDIT 2025-06 is the only municipal research edition present in this repository. It applies to positions taken on or after 2025-07-01, remains marked current and not re-issued, and is the stated basis of record for municipal weightings in the taxable-account allocation guidance. Its top-bracket municipal overweight is an after-tax thesis: the AMT phase-out threshold is load-bearing, and the note says the recommendation does not survive a reduction that draws materially more top-bracket holders into AMT. [Municipal research status and applicability](repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md#L12-L16) [Load-bearing premise](repo://internal_research/FI/US/MUNI-CREDIT/2025-06.md#L24-L32)

The current taxable fixed-income guide implements that research as a 22% municipal target versus 18% neutral for top-bracket clients and makes the cited sector preferences binding limits. The paired 28% IG-corporate target versus 32% neutral funds the municipal overweight. [Municipal target and limits](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L17-L31) [Paired corporate funding](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L33-L37)

Revenue Procedure 2025-41 applies for taxable years beginning on or after 2026-01-01. It sets the AMT exemption phase-out thresholds at $500,000 for unmarried individuals and $1,000,000 for joint filers; specified private-activity-bond interest remains an AMT preference item, while qualified 501(c)(3) bond interest remains outside AMTI. [AMT thresholds](repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L18-L22) [Bond treatment](repo://external_sources/IRS/2025-08-rev-proc-2025-41-amt-thresholds.md#L24-L34)

This creates an unresolved conflict: the overlay changes the threshold premise that the still-current research and living guide cite, but there is no municipal re-issue in the repository. Do not invent a replacement research conclusion or mechanically change the weight. The guide and discretion matrix prescribe suspension and committee escalation only where a cited note has been superseded or withdrawn; the available municipal record does not establish that condition. Escalate the unresolved conflict for committee direction and preserve the research, overlay, guide, affected accounts, and decision basis in the position record. [Suspension trigger](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Superseded-note escalation](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37)

If suspension is directed under the guide, the municipal overweight and paired corporate underweight return to their stated neutral references; it is not an ordinary drift rebalance. [Suspension consequence](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L33-L43)

## Controls that recur across routes

**Research-to-guidance boundary.** A manager who finds a guide-cited research note superseded or withdrawn must suspend the derived weight and escalate to the committee. The manager may not carry forward the old weight or directly adopt the replacement recommendation. [Discretion matrix D.4](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37)

**Private markets.** Research supports a 10–20% strategic allocation only for eligible clients with a genuine ten-year horizon and treats eligibility as a regulatory, rather than research, determination. No strategy may be offered before eligibility is determined and documented; approval cannot clear ineligibility or another regulatory breach. [Private-markets research](repo://internal_research/MA/GL/PRIVATE-MARKETS/2025-12.md#L16-L22) [Eligibility gate](repo://internal_guidelines/suitability/private-markets-eligibility.md#L7-L10) [Non-clearable conditions](repo://internal_guidelines/authority/discretion-matrix.md#L39-L47)

For determinations on or after 2026-06-29, SEC Order IA-7104 sets Rule 205-3 tests of $1,400,000 under management or net worth above $2,700,000. A pre-effective-date determination remains only for its original contract or investment, not a new entry; the order does not adjust accredited-investor or qualified-purchaser standards. [Adjusted tests](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L14-L18) [Transition boundary](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L24-L28) [Separate standards](repo://external_sources/SEC/2026-04-order-ia-7104-qualified-client.md#L34-L36)

**Other research reviews.** Semiconductor-capex research changed from overweight to neutral for positions from 2026-03-01; grid interconnection constrains the rate of capacity addition, not eventual demand. [Semiconductor edition](repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md#L12-L18) [Power constraint](repo://internal_research/EQ/US/SEMI-CAPEX/2026-02.md#L30-L32)

DOL Release 2026-31 is effective for plan years beginning on or after 2027-01-01 and widens the pension discount-rate corridor, provides conditional contribution relief, and permits limited surplus uses. Those are the funding-rule changes that FI-US-PENSION-LDI 2026-03 names as invalidating its pension-demand premise and triggering review; research and the overlay still do not establish a binding account weight. [DOL change](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L7-L25) [Pension premise and trigger](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [Risk and review trigger](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46) [Authority model](repo://README.md#L39-L48)

**Records.** A cleared escalation needs the condition, clearing authority level, specific facts, and date. A private-markets eligibility file additionally needs the pathway, evidence, decision maker, and date. [Escalation record](repo://internal_guidelines/authority/discretion-matrix.md#L49-L51) [Eligibility record](repo://internal_guidelines/suitability/private-markets-eligibility.md#L27-L29)
