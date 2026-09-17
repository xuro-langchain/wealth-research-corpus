---
type: regulatory-overlay
title: Pension Funding Relief and Long-Credit Research Overlay
description: Explains the prospective pension-funding relief in DOL Release 2026-31, the long-credit research premise it supersedes, and the restrictions it preserves. Separates future plan-year analysis from the historical research basis of record and from mandate implementation.
tags: [pension-funding, defined-benefit-plans, long-credit, discount-rates, regulatory-overlay, research-governance]
verified:
  - by: openwiki/0.5.0
    at: 2026-09-17T21:44:02.449Z
sources:
  - id: openwiki-source-28f8ac08cab10bd38b1c51d7
    resource: repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md
  - id: openwiki-source-782f1a3fffc4f6dec3274631
    resource: repo://internal_guidelines/allocation/us-taxable-fixed-income.md
  - id: openwiki-source-2ddd4f14dfe61f21d64eb273
    resource: repo://internal_guidelines/authority/discretion-matrix.md
  - id: openwiki-source-34464a9ae84e5251bb0b43e6
    resource: repo://internal_research/FI/US/IG-SPREADS/2025-09.md
  - id: openwiki-source-f2798a1b5239421401d0aab5
    resource: repo://internal_research/FI/US/PENSION-LDI/2026-03.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "openwiki/0.5.0", at: "2026-09-17T21:44:02.449Z" }
---

## Scope, authority, and effective-date boundary

DOL Release 2026-31 is synthetic demonstration material on which no reliance is possible. Within this corpus, this page treats it as a **regulatory overlay**, not portfolio guidance: it amends funding rules for single-employer defined-benefit plans. It was issued in 2026-08 and is effective for **“plan years beginning on or after 2027-01-01.”** [Release notice and P.1](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L1-L11)

The effective date is prospective. Frozen research and external sources are not revised in place, and an edition remains the basis of record for positions taken while it stood; a later review does not overwrite the historical edition with a later rule or research view. [Corpus model](repo://README.md#L39-L48)

## Provisions that constrain the LDI demand premise

**P.2 changes the liability-measurement input.** For affected plan years, it widens the corridor around the twenty-five-year average segment rates from 10% to **“twenty percent in each direction.”** The release says the wider corridor permits a higher discount rate, reduces measured liabilities, and will in most cases put a plan previously at or near full funding into measured surplus. [Release P.2](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L13-L17)

**P.3 changes the contribution incentive only for a qualifying plan.** A plan whose P.2 funded status **“exceeds one hundred and ten percent”** is not required to make a minimum contribution for that plan year; the sponsor may elect to make the excess available for P.4 purposes. [Release P.3](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L19-L21)

**P.4 permits only specified surplus uses.** For a plan meeting P.3’s threshold, excess assets may be transferred to a qualified replacement plan or applied to retiree health accounts, subject to P.6 notice. The release expressly says it **“does not permit a reversion to the sponsor outside the existing statutory framework.”** [Release P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L23-L25)

DOL Release 2026-31 P.2–P.4 **supersedes** the FI-US-PENSION-LDI 2026-03 L.2 demand premise prospectively, rather than every possible long-credit rationale. The note’s overweight is a long-end flow call based on corporate defined-benefit plans protecting surplus through contribution requirements and the liability discount-rate basis; it says that a rule allowing sponsors to release or re-risk surplus can reverse the flow and that the overweight does not survive. Its expressly named invalidators are surplus release, a changed discount-rate basis, and reduced contribution requirements. [Release P.2–P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L13-L25) [Pension LDI L.1–L.2 and L.6](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L16-L24) [Pension LDI L.6](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L42)

```mermaid
flowchart TD
    Historic["2026-03 historical research record"] --> PlanYear{"Plan year starts on or after 2027-01-01"}
    PlanYear -- "No" --> Record["Retain historical basis of record"]
    PlanYear -- "Yes" --> Corridor["P.2 wider discount-rate corridor"]
    Corridor --> Relief["P.3 conditional contribution relief"]
    Relief --> Uses["P.4 limited surplus uses"]
    Uses --> Premise["L.2 demand premise superseded"]
    Premise --> Review["L.7 research review"]
    Review --> Mandate["Check mandate and authority"]
```

This flow separates the prospective regulatory effect and research-review trigger from the historical position record and any mandate decision. [Release applicability and P.2–P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L7-L25) [Pension LDI L.2 and L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [Pension LDI L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46) [Corpus model](repo://README.md#L39-L48)

## Provisions the release preserves or does not address

**P.5 preserves** benefit-accrual and vesting rules and preserves **“in full”** the requirements for plans below 80% funded. Nothing in P.2 or P.3 relieves a below-80%-funded plan of an existing restriction. [Release P.5](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L27-L30)

**P.5 does not address** fiduciary standards governing investment of plan assets; they continue on their own terms. The release therefore creates neither an investment-manager permission nor a de-risking, purchase, sale, or allocation instruction for long credit. [Release P.5](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L29-L31)

**P.6 imposes the election procedure.** A sponsor electing P.3 relief **“shall notify participants within thirty days of the election”** in the prescribed form. P.4 makes its limited permitted uses subject to this notice requirement. [Release P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L23-L25) [Release P.6](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L33-L35)

## Historical record, related research, and mandate boundary

FI-US-PENSION-LDI 2026-03 was published on 2026-03-05 and applies to positions taken on or after 2026-04-01. It remains the historical basis of record for positions taken while it stood, despite the future regulatory overlay. Its expression is a long-end, single-A-and-better flow view; it does not contradict FI-US-IG-SPREADS 2025-09’s index-level valuation underweight. [Pension LDI publication and L.4–L.5](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L12-L14) [Pension LDI L.4–L.5](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L30-L36) [IG spreads G.1–G.3](repo://internal_research/FI/US/IG-SPREADS/2025-09.md#L16-L26)

The release triggers the note’s review condition—an announced change to pension-funding or discount-rate rules—but does not publish replacement research or rewrite the frozen recommendation. Research supplies a thesis; living internal guidance supplies binding portfolio weights. [Pension LDI L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46) [Corpus model](repo://README.md#L39-L48) [Taxable fixed-income guide purpose](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L1-L5)

Do not infer a replacement allocation. The available taxable fixed-income guide derives its stated municipal and investment-grade-corporate weights from FI-US-MUNI-CREDIT 2025-06 and FI-US-IG-SPREADS 2025-09, not FI-US-PENSION-LDI 2026-03. Consequently, its cited-note suspension process does not itself create an LDI-specific weight, suspension, or trade. [Taxable fixed-income guide A.1, A.3, A.5, and A.8](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Taxable fixed-income guide A.3](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L17-L23) [Taxable fixed-income guide A.5](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L33-L37) [Taxable fixed-income guide A.8](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L49-L51)

If a governing mandate does cite this research and that note is superseded or withdrawn, the manager must suspend the derived weight, record the superseded and replacement notes, derived weights, and affected accounts, and escalate to the committee. The manager may not carry the prior weight forward, re-derive it, or directly adopt a replacement recommendation; the committee alone adopts a binding weight. [Discretion matrix D.4](repo://internal_guidelines/authority/discretion-matrix.md#L31-L37)

### Review record

1. Select the frozen research edition by the position date; retain its thesis, load-bearing premise, and invalidation trigger as the historical basis of record. [Corpus model](repo://README.md#L39-L48) [Pension LDI publication, L.2, and L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L12-L24) [Pension LDI L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L44-L46)
2. For a current affected plan-year analysis, apply P.2 from 2027-01-01, test the P.3 threshold, P.4’s limited uses and non-reversion boundary, P.5’s preserved restrictions, and P.6 notice. [Release applicability and P.2–P.6](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L7-L35)
3. Record the prospective supersession of the L.2 premise and initiate L.7 review; do not convert that conclusion into execution or a new allocation. [Release P.2–P.4](repo://external_sources/DOL/2026-08-funding-relief-and-discount-rates.md#L13-L25) [Pension LDI L.2 and L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L20-L24) [Pension LDI L.6–L.7](repo://internal_research/FI/US/PENSION-LDI/2026-03.md#L38-L46)
4. If there is a documented mandate dependency, follow its suspension and committee-escalation control; otherwise obtain the governing mandate and authority decision rather than inventing one from the overlay. [Taxable fixed-income guide A.1](repo://internal_guidelines/allocation/us-taxable-fixed-income.md#L7-L11) [Discretion matrix D.1 and D.4](repo://internal_guidelines/authority/discretion-matrix.md#L7-L11) [Discretion matrix D.4](repo://internal_guidelines/authority/discretion-matrix.md#L31-L35)
