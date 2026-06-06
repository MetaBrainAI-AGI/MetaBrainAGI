<div align="center">
<img src="assets/vision-logo.svg" alt="Vision" width="96" height="96" />

# MetaBrainAGI — Pricing
</div>

> **Status: PROPOSED — pending owner confirmation.** No prior concrete price sheet existed on disk, so these are a professional starting structure for a Rust-native AI-infrastructure family. Adjust any number before launch. Checkout is wired to **Stripe** once the live keys are provided (see *Payments* below).

## Tiers

| | **Free** | **Pro** | **Enterprise** |
|---|---|---|---|
| **Who** | Solo devs, evaluation, open-core | Teams shipping to production | Fleets, regulated, mission-critical |
| **Support** | Community | Email, 2-biz-day | Private channel + SLA |
| **License** | Apache-2.0 / community | Per-seat commercial | Site / fleet + source escrow |
| **Updates** | Public releases | All releases | Early access + roadmap input |
| **Security** | — | Signed releases | Runtime attestation, SOC2/ISO/HIPAA change-control |

## Per-product price (proposed)

| Product | Free | Pro (per seat / mo) | One-time license | Enterprise |
|---|---|---|---|---|
| **VisionPRIME** (flagship) | trial | **$99** | $1,490 | Custom |
| **VP-SIA** | — | **$79** | $1,190 | Custom |
| **VisionRustify** | trial | **$49** | $690 | Custom |
| **VisionOmniCollab** | — | **$59** | $890 | Custom |
| **VisionFusion** | — | **$39** | $590 | Custom |
| **VisionSynergy** | — | **$39** | $590 | Custom |
| **VisionCAGRAG** | trial | **$59** | $890 | Custom |
| **VisionPerceptionVoice** | trial | **$49** | $690 | Custom |
| **VisionPrime-Dispatch** | — | **$69** | $990 | Custom |
| **VisionInfraTools** | — | **$39** | $590 | Custom |
| **VisionOpenSOC** | **Free** (Apache-2.0) | — | — | — |
| **VisionOpenSOC-Pro** | — | **$129** | — | Custom |
| **VisionSkills** | **Free** | bundled | bundled | bundled |

### Bundles
- **Vision Suite (all Pro)** — ~40% off the sum: **$349 / seat / mo** *(proposed)*.
- **Founder / lifetime** — one-time **$4,900** for the full suite, all updates *(proposed, limited).*

## Payments (Stripe)

The storefront is checkout-ready as **code**: each product maps to a Stripe **Product + Price**, and a payment link is generated per tier. To go live I need **one** of:
- a Stripe **restricted API key** (`Products: write`, `Prices: write`, `Payment Links: write`), or
- the price/link IDs if you create them in the Stripe dashboard.

> I do **not** enter or store live financial keys myself (policy). Provide the restricted key in the vault or create the Products/Prices in Stripe and paste the Price IDs — I wire `assets/stripe-catalog.json` and the checkout links the moment they exist.

<div align="center"><sub>Prices in USD. Proposed structure — confirm before public launch. © MetaBrain AI.</sub></div>
