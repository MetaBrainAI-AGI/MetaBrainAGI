<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionOpenSOC

### The open, local AI Security Operations Center.

**Detect → Alert → Harden → Report — running where your code does, with nothing shipped off your machine.**

<sub>VisionPRIME family · MetaBrainAGI · open core, Apache-2.0 · local-first · free forever</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Most security tooling is either a noisy scanner that buries you in findings, or a SaaS that wants your logs. Neither runs *where your code lives*, neither remediates the safe fixes for you, and neither keeps a running posture you can hand to a release or a compliance review.

## The solution

VisionOpenSOC is a **local SOC loop**. It inventories your attack surface, continuously detects dependency CVEs, secret leaks, weak config, and control drift, raises deduplicated, severity-ranked alerts out-of-band, auto-remediates the safe and reversible fixes (and drafts the risky ones for approval), and keeps a running posture score plus an audit trail. It runs where your code does — nothing is shipped off your machine. And it's open core, Apache-2.0: read it, fork it, trust it.

## What you get

- **Detect.** Dependency CVEs, secret and key leaks, weak config (CORS / CSP / debug / permissions / insecure defaults), and control drift — continuously.
- **Alert.** Severity-ranked, deduplicated, out-of-band — never just another line in a log nobody reads.
- **Harden.** Auto-fixes the safe and reversible findings; drafts the rest for approval. It never weakens posture to "fix" a finding.
- **Report.** A posture score, a full audit trail, and a diff-able security report you can hand to a release gate or a compliance reviewer.
- **The open core, in the open.** Ships the `vision-opensoc` SOC-orchestration skill, the `vision-secops` audit + harden engine it composes, local installers, and the VisionSynergy / VisionFusion wiring — all Apache-2.0.
- **No cloud key required.** The scanners need no provider key; bring your own only if you want LLM-assisted triage.

## Why trust it

- **Open core, Apache-2.0** — the security loop is auditable source you can read and fork.
- **Local-first** — it runs where your code does; nothing about your code leaves the box.
- **Posture-safe** — it never weakens your security to clear a finding, and it drafts (never auto-applies) the risky fixes.

## Who it's for

Every team — solo devs, agent builders, and platform teams who want a continuous, local security loop over their repos and infra without sending logs to a vendor.

## Pricing

**Free — Apache-2.0, free forever.** When you need a *fleet* — continuous runtime attestation, multi-repo posture, secure cross-team skill sharing, and gated auto-response playbooks — upgrade to [**VisionOpenSOC-Pro**](VisionOpenSOC-Pro.md). See **[PRICING.md](../PRICING.md)**.

## Request access

**[hello@metabrain.ai](mailto:hello@metabrain.ai)** — or open a private issue. Source for the open core is available under Apache-2.0.

<div align="center"><sub>© MetaBrainAGI. Open core licensed under Apache-2.0. VisionOpenSOC, VisionPRIME, and the Vision mark are marks of the publisher. Not affiliated with Anthropic.</sub></div>
