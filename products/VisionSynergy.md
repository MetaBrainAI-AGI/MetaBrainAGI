<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionSynergy

### Wire many AI engines into one mind.

**A native-Rust synergy mesh that links, clusters, bridges, propagates, and fuses every subsystem's signals into one confidence-rated decision — in microseconds.**

<sub>VisionPRIME family · MetaBrainAGI · Rust + PyO3 · rayon + dashmap · no Python on the hot path</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Real agent systems run a dozen independent minds at once — predictors, learners, memory, meta-controllers, executors, voices. Left alone, each one shouts its own answer with no shared structure: no weighting, no agreement signal, no way for a strong insight in one corner to inform the rest. You end up averaging votes by hand, or letting the loudest model win.

## The solution

VisionSynergy turns that scattered chorus into a consciousness pipeline — a compiled substrate where your engines are *connected*. Weighted links between subsystems, cross-cluster bridges, signal propagation across the graph, and confidence-weighted Bayesian fusion into one decision with a posterior confidence you can trust. One strong signal ripples to related clusters automatically; one per-task verdict fuses every contributing voice at once. It's compiled Rust exposed through PyO3, so fusing a decision across dozens of subsystems is a microsecond-scale operation you can call on every turn.

## What you get

- **Cluster routing.** Group subsystems into named clusters (`intel`, `memory`, `learning`, `meta`, `exec`, …) and route signals by cluster.
- **Weighted synergy links + cross-cluster bridges.** Connect any two subsystems with a tunable edge weight; well-connected nodes carry more influence in consensus. A signal crossing a cluster boundary is attenuated by the bridge weight, so domain crossings are deliberate.
- **Cluster consensus + signal propagation.** Collapse a cluster's signals into one connectivity-weighted score (parallel via `rayon`); fire a signal from one node and watch it ripple across the mesh, strongest-path wins, attenuating per edge and per bridge.
- **Confidence-weighted fusion.** Fuse multi-source `(value, confidence)` signals into one five-band decision (`STRONG_BUY → BUY → HOLD → REDUCE → AVOID`): agreement boosts the posterior, disagreement attenuates it.
- **Symbolic veto + ranking + telemetry.** Gate any fused decision behind a hard logical check; rank competing candidates best-first; read node/edge/bridge and per-method call counts for full observability.
- **Presence as a synergy node (with VisionPRIME).** Owner availability joins the mesh as a first-class signal, so "is the human reachable?" propagates across the graph and weighs into the fused verdict.

## Why trust it

- **Microsecond-scale, deterministic** — every aggregation (consensus, propagation, variance, ranking) runs in parallel across cores with `rayon`; concurrent reads are lock-free via `dashmap`; no Python round-trip on the hot path.
- **A real engine, fully implemented** — full Rust source with every method bodied; **12/12 Rust unit tests pass**.
- **Standalone** — drops into any project; it does not require the rest of the suite.

## Who it's for

Engineers orchestrating many specialist engines who want them to behave as one coordinated mind — the connective tissue for any agent system that currently averages votes by hand.

## Pricing

**Pro — from $39 / seat / mo** · one-time license $590 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

## Request access

VisionSynergy is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionSynergy and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
