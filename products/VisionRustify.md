<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionRustify

### The universal Python → Rust porter.

**Auto-port any Python repo to native Rust — strategy-classified per file, kernel scaffolded ~80% written, parity-gated before a single `.py` is deleted.**

<sub>VisionPRIME family · MetaBrainAGI · deterministic · no LLM per file · harness-agnostic</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

"We should rewrite this in Rust someday" is where most performance work goes to die. Deciding the right strategy for every file — rewrite the whole thing, keep a shim, extract just the hot kernel, or leave it alone — is slow, subjective, and easy to get wrong. Rewrite too aggressively and you break a live caller; rewrite too timidly and the hot path stays in Python.

## The solution

VisionRustify is the deterministic engine that turns "someday" into a concrete, file-by-file plan you can execute today. Point it at any repository, directory, or single file. In one parallel pass — **no LLM call per file** — it decides *how* each `.py` should become Rust, generates the PyO3 scaffold so the hard part is already typed out, and audits your installed environment for Rust-only drop-ins. The default posture is aggressive (full native rewrite + delete the `.py`) but only when it's provably safe: a module something else imports is never deleted out from under you — it gets a parity-gated shim instead.

## What you get

- **Per-file strategy classification.** Every `.py` is statically classified into one of five strategies: `FULL_NATIVE` (rewrite + delete), `DEEP_SHIM` (Rust core + parity-gated Python shim), `RUST_KERNEL` (extract the hot compute, keep the I/O facade), `ONNX` (the default for ML inference — export the fitted model, run it native via `ort`/`tract-onnx`), or `EXEMPT` (genuinely stays Python — online-training libs, async glue, audio buffers).
- **ONNX migration, first-class and decision-guided.** For ML code the default target is ONNX. VisionRustify auto-picks the runtime and exporter, detects training-vs-inference, and emits a full migration plan (`--onnx-plan <file.py>`) with every decision point spelled out — keep the trainer in Python, parity-check before deleting.
- **Deterministic, token-free.** Pure AST static analysis → a feature vector → a decision tree with a confidence score and human-readable reasons. Same input, same answer, every time — auditable and free of LLM cost.
- **Parity-safe deletes.** Reference analysis maps which modules are imported by hooks, mixins, and boot code. A referenced file can never be marked deletable — it's downgraded to a shim automatically, so a port never breaks a live caller.
- **PyO3 kernel scaffolding.** For each file it emits a Rust `#[pyclass]` / `#[pymethods]` skeleton with your real module, class, and function names and matching arity, plus the `rayon` import for parallel-by-default hot loops. The port starts roughly 80% written.
- **Installed-environment audit.** Beyond your source, it maps your installed packages to Rust-only equivalents — `json`→`orjson`, `pandas`→`polars`, `black`/`flake8`/`isort`→`ruff`, `numpy`→`ndarray`, `xgboost`→ONNX/`ort` — installing the safe drop-ins and flagging the rest.

## Why trust it

- **Deterministic and auditable** — pure AST analysis, no LLM call per file, same answer every run, with human-readable reasons for every verdict.
- **Safe by construction** — reference-gated deletes mean a port can never orphan a live caller; the audit changes nothing without `--apply`.
- **Zero install weight** — the classifier is stdlib-only Python; ONNX exporters install on demand only when you actually port ML.

## Who it's for

Performance and infrastructure engineers who want to move a real codebase toward Rust on a plan, not a vibe — and platform teams who want a token-free, reproducible answer to "what should this file become?"

## Pricing

**Pro — from $49 / seat / mo** · one-time license $690 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

## Request access

VisionRustify is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionRustify and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
