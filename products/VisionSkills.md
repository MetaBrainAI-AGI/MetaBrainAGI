<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionSkills

### The skill library that powers the family.

**Senior-grade engineering judgment, packaged as machine-loadable, harness-agnostic Claude/agent skills.**

<sub>VisionPRIME family · MetaBrainAGI · canonical skill source · harness- & OS-agnostic · bundled free</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Operational judgment — how to optimize a slow query, when to extract a hot kernel, how to triage a CVE — usually lives in senior engineers' heads and walks out the door with them. There's no clean way to package that expertise so an AI agent loads it on demand, on any machine, in any harness.

## The solution

VisionSkills is the canonical source of truth for every skill the MetaBrainAGI / VisionPRIME family ships. Each skill is a self-contained `SKILL.md` (with the YAML frontmatter the harness loads) plus any helper scripts. Skills are **harness- and OS-agnostic**: on activation a skill *discovers* the target system (reads the local config, probes the environment) and *researches* anything it needs via parallel-LLM / LLM-consensus before acting. Install once and your agent gains a library of senior-grade playbooks.

## What you get

- **A curated, sellable skill library.** Standalone skills with strong marketing names plus sellable packs — the Optimization Pack (full-optimization orchestrator, speed, DB, API, bundle, prompt, cost, memory, build, concurrency, cache, algorithmic, and benchmark optimizers, plus VisionRustify and VisionConsensus), with more packs to follow.
- **Harness- and OS-agnostic.** Every skill discovers its target and researches before acting, so the same skill works across machines and harnesses without rewiring.
- **One-command install.** `install.sh` / `install.ps1` syncs skills into the harness skills directory (`~/.claude/skills`); override the destination with `VISION_SKILLS_DEST`.
- **A clean registry.** `manifest.json` records every skill — its pack, brand, version, and harness-agnostic flag — so the catalog is inspectable and reproducible.
- **Brand-consistent.** Every skill carries the MetaBrainAGI vendor tag and the Vision skill mark in its frontmatter; sellable packs are extracted as clean product repos with no secrets and no third-party skills.

## Why trust it

- **The same library the family runs on** — this is the canonical source the VisionPRIME products are built from, not a marketing subset.
- **Inspectable and reproducible** — a manifest registry plus self-contained `SKILL.md` files; install changes only your skills directory.
- **Secret-free distribution** — sellable packs are extracted clean, with no secrets and no third-party skills bundled.

## Who it's for

Everyone running an agent harness who wants a library of senior-grade, loadable engineering skills — and teams who want optimization and infra judgment available on every machine without onboarding a person.

## Pricing

**Free — bundled with the family.** The curated packs ship with VisionPRIME and compose with the rest of the suite. See **[PRICING.md](../PRICING.md)**.

## Request access

**[hello@metabrain.ai](mailto:hello@metabrain.ai)** — or open a private issue.

<div align="center"><sub>© MetaBrainAGI. Commercial software; sellable packs distributed as clean product repos. VisionPRIME and the Vision mark are marks of the publisher. Not affiliated with Anthropic.</sub></div>
