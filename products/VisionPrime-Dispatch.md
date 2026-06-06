<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionPrime-Dispatch

### One task in. The right team out.

**Turn a free-text task into the right specialists — automatically routed, run in parallel, and consensus-gated before anything ships.**

<sub>VisionPRIME family · MetaBrainAGI · auto-route · worktree-isolated parallelism · consensus-gated</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

The default move with an agent is "fire one and hope." For anything real — hardening an auth flow, fixing a pipeline, shipping an endpoint — one agent on one opinion isn't enough. You want a *team*: the right specialists, the right skills loaded, running in parallel without clobbering each other, and a check on the work before it ships. Wiring that by hand every time is the bottleneck.

## The solution

VisionPrime-Dispatch is the multi-agent orchestration core extracted from the VisionPRIME harness. Give it a task; it decides *which* specialists should work it, *how many* agents to deploy, and *which skills* each one loads — then coordinates the run over a shared event bus and gates the outcome behind a swarm vote and a board review. It's the difference between a single agent and a coordinated team that checks its own work.

## What you get

- **Auto-skill + auto-route.** Tasks map to roles (security, frontend, data, deploy, research, Rust-port, audit, and more), roles to skills, skills to agents — selection is computed by scoring the task against each team's profile, not hand-configured.
- **Worktree-isolated parallelism.** Independent lanes run concurrently as isolated, file-mutating agents, so parallel work can't collide on shared state.
- **Consensus-gated delivery.** Nothing ships on a single opinion — an 8-voice swarm vote decides APPROVE / REJECT / NEUTRAL, and a Genius Council + VisionQuest board runs an adversarial premortem and returns one verdict with confidence and dissent attached.
- **Bus-based coordination.** Agents gossip progress, checkpoints, and conflicts over a per-project event bus, so parallel agents and sibling sessions see each other live and resolve collisions instead of clobbering.
- **Durable, inspectable reporting.** Every dispatch plan and verdict is logged as JSONL plus a human-readable markdown report — a full audit trail of who did what and why.
- **Rust-accelerated, fail-open, secret-free.** Hot-path compute runs on a native Rust kernel when present, with a transparent Python fallback; provider keys are read from the environment at runtime, never baked into the package.

## Why trust it

- **Nothing ships on one opinion** — every outcome passes a swarm vote and an adversarial board premortem, each with confidence and dissent recorded.
- **Parallel without collisions** — independent lanes run in isolated worktrees coordinated over a shared bus.
- **Fully auditable** — every routing decision, dispatch plan, and verdict is durable JSONL plus a readable markdown report.

## Who it's for

Teams doing multi-agent orchestration who want a task to become a coordinated, self-checking team automatically — security hardening, full-stack feature work, audits, and pipeline fixes that are too big for a single agent.

## Pricing

**Pro — from $69 / seat / mo** · one-time license $990 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles. Also included in the VisionPRIME flagship bundle.

## Request access

VisionPrime-Dispatch is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionPRIME and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
