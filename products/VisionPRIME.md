<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionPRIME

### The AGI harness-management layer.

**Make any coding agent reliable, autonomous, memory-persistent, self-correcting, and Rust-fast — without changing the model you already use.**

<sub>VisionPRIME family · MetaBrainAGI · Rust-native · 100% local · patent-backed</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

You already have a capable model. What you don't have is the system *around* it. Out of the box, an agent forgets everything between sessions and repeats the same mistakes, acts before it reasons about the consequences, claims "done" without evidence, and runs every consequential decision on a single inline opinion. Bolting on more prompts doesn't fix it — the discipline has to live *outside* the model, enforced on every step.

## The solution

VisionPRIME is *not another model* and *not another IDE*. It is the operating layer that wraps the harness you already run — Claude Code, Cursor, a CLI agent, a chat loop — and inserts a decision-and-memory layer between your agent and every consequential action. Before the agent runs a command, edits a file, or claims a task is done, VisionPRIME **recalls** what it already knows, **forecasts** the outcome, **scores** the decision, and either auto-executes on a high-confidence path or pauses on a genuine gate. After the action, it **remembers** the result so the next run is sharper. The whole loop is enforced by session hooks, so it can't silently switch off.

> **One line:** the operating system for agentic engineering — local, fast, honest.

## What you get

- **Consciousness pipeline.** Every non-trivial action flows through ANSR symbolic constraint checking, a Phantasm Monte-Carlo premortem, mission-alignment scoring, a somatic urgency gate, online learning, and an 8-voice consult that returns one `success_likelihood`. Auto-executes at ≥ 0.70; otherwise pauses and names the exact gate.
- **GC-VQ Genius Board.** For wide or high-stakes calls, VisionPRIME convenes a board — GeniusCouncil (parallel adversarial consensus) plus VisionQuest (parallel Monte-Carlo forward projection) — reconciled into a single sentinel verdict. A board of directors for your agent, on demand.
- **Unified memory mesh.** Cross-session, cross-machine recall over episodic memory, a warm cache index (CAG), vector recall (RAG), a lesson registry, and a portable identity tier. The agent carries context forward instead of starting cold.
- **Native Rust kernels.** Hot-path compute — consensus tallies, premortem ranking, hallucination verdicts, harness mapping, ONNX inference — runs in the `metabrain_core` PyO3 crate: rayon-parallel, LTO-optimized, with a pure-Python fallback so nothing breaks if the wheel isn't built.
- **Anti-hallucination discipline.** Layered gates (cite-or-skip, completion-claim evidence, live-data-first, exhaustion) plus a falsifiable 7-criteria self-score that auto-remediates when it drops. Honesty is measured, never asserted.
- **Auto-rustifier + swarm.** Audits your installed Python packages and swaps in Rust-only drop-ins on request, and fans out multi-agent work under a shared consciousness contract with a rate-limit-resilient multi-provider router.

## Why trust it

- **Rust-first compute** — the hot path is native `metabrain_core` (PyO3 / rayon / LTO), with a pure-Python fallback so it runs on any host.
- **100% local** — bring your own provider keys; nothing about your work leaves your machine. With zero keys it still runs, with the harness model as the primary voice.
- **Fail-open by construction** — the session hooks degrade gracefully; a missing dependency never blocks your session.
- **Patent-backed** — core methods are covered by filed IP, so you license proven, defensible technology.

## Who it's for

Teams running agents in production who need the agent to be reliable, auditable, and memory-persistent — not just clever for one prompt. If you ship real work with Claude Code, Cursor, or a custom agent loop and you're tired of cold starts, silent overreach, and unverifiable "done," VisionPRIME is the layer you're missing.

## Pricing

**Pro — from $99 / seat / mo** · one-time license $1,490 · Enterprise custom. The bundle includes the consciousness pipeline, the GC-VQ Genius Board, the memory mesh, the native Rust kernels, the auto-rustifier, the full Vision skill library, and VP-SIA. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

## Request access

VisionPRIME is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionPRIME and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
