<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionFusion

### Native multi-signal Bayesian fusion.

**Turn many model and engine outputs into one trustworthy decision — with a confidence you can act on.**

<sub>VisionPRIME family · MetaBrainAGI · Rust + PyO3 · rayon-parallel · deterministic</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Modern systems ask many models the same question — an ensemble of predictors, a panel of agents, a board of voices. The problem is never getting answers; it's **reconciling** them. Averaging the numbers hides disagreement: a loud, uncertain source drowns out a quiet, confident one, and you ship a single mean with no signal that the sources actually conflicted.

## The solution

VisionFusion is the reconciliation layer. It merges any number of model, agent, or signal outputs into a single ranked decision — weighting each source by its own confidence, measuring how much the sources actually agree, and folding both into one posterior confidence and a clear direction band. When your sources disagree, VisionFusion tells you and discounts the call accordingly, instead of hiding the conflict behind an averaged number. It's a real compiled engine, not a wrapper: written in Rust, parallelized over sources with `rayon`, and deterministic — the same answer every time.

## What you get

- **Weighted-consensus fusion.** Each input is `(source, value, confidence)`. VisionFusion computes a confidence-weighted posterior — a discrete Bayesian update where every source's confidence is its evidence weight — so a loud but uncertain source can't outvote a confident one.
- **Agreement scoring.** It measures dispersion across your sources as an `agreement` score in `[0, 1]`: tight consensus boosts the posterior, scattered opinions attenuate it — so the confidence reflects reality, not just the mean.
- **Direction banding.** The fused value maps to a clear five-level band (`STRONG_BUY → BUY → HOLD → REDUCE → AVOID`) — a categorical call, not a bare float to interpret.
- **Veto attenuation.** A symbolic or safety check can veto a result: when the guard fails, `fuse_with_veto` halves the posterior confidence and caps the decision at `HOLD` — a circuit breaker for "the numbers look good but the rules say no."
- **Ranking built in.** `rank(candidates)` orders a field of options best-first, blending value and confidence so a high-confidence mediocre option never outranks a strong, confident one.
- **Presence-aware (with VisionPRIME).** Owner availability is a first-class signal: `vision-presence` emits `("presence", availability, confidence)`, so a decision can weigh *whether the human is even reachable* alongside perception and the predictive voices.

## Why trust it

- **One call, one explainable decision** — `fuse(signals)` returns the decision, posterior confidence, fused value, agreement, mean confidence, and source count: everything you need to act *and* to explain the call.
- **Native speed, deterministic results** — Rust + PyO3, rayon-parallel, release-built with LTO; no service to run, no network hop, and the same answer every time.
- **Drop-in** — ships as a PyO3 extension (`from visionfusion import FusionEngineNative`); the engine wheel has no Python runtime deps.

## Who it's for

Anyone reconciling many noisy signals into one decision: decision and sensor fusion, model ensembles, agent panels, risk verdicts, and any place you currently average votes by hand and lose the disagreement signal.

## Pricing

**Pro — from $39 / seat / mo** · one-time license $590 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

## Request access

VisionFusion is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionFusion and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
