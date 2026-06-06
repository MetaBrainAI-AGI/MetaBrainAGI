<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionCAGRAG

### CAG + RAG + Agentic-RAG, in one local layer.

**Give any coding agent or codebase a fast, local, three-mode memory — so it finds the right context before it acts, instead of burning tokens on a cold grep every time.**

<sub>VisionPRIME family · MetaBrainAGI · local-only · token-frugal · harness-agnostic</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Agents waste budget *finding* files. They re-search the whole tree on every question, re-learn the same map each session, and miss context that spans files. A cold grep on every turn is slow, expensive, and still misses the answer when it's spread across three modules.

## The solution

VisionCAGRAG is a small, dependency-light retrieval layer you drop next to any repository. It indexes your code and docs once, then answers "where does X live?" and "how does Y work end-to-end?" in milliseconds — locally, with no network calls and nothing written into your tracked source tree. It fixes the three failure modes at once by making retrieval cheap, cached, and iterative — and exposes the right tool for each shape of question behind one tiny API.

## What you get

- **Three retrieval modes, one entry point.** **CAG** (cache-augmented) pre-loads a bounded corpus into one warm context and recalls any in-session query in sub-millisecond time with no re-embedding. **RAG** runs classic vector search (FAISS hot + ChromaDB cold), returning top-K symbols as paths + line ranges. **Agentic RAG** is a multi-hop loop: retrieve, learn salient terms, expand the query, retrieve again — accumulating de-duplicated evidence until a budget or confidence threshold is met.
- **Token-frugal by design.** RAG and Agentic RAG return paths, line ranges, and symbol names — never whole files — so your agent reads exactly what it needs and nothing more.
- **Hot + cold vector stores.** FAISS keeps an in-memory cosine index for speed; ChromaDB persists to disk so the index survives restarts and rehydrates FAISS on a cold start.
- **Multi-language symbols.** Python (AST), JS/TS/JSX/TSX, Rust, and Markdown — functions, classes, methods, components, routes, and headings — grouped into configurable clusters, with cross-encoder reranking in CAG.
- **Fail-open, always.** A missing optional dependency degrades to a working subset instead of crashing — no `faiss` falls back to keyword search.
- **Repo-safe and local-only.** All artifacts live under `VISIONCAGRAG_HOME`; the only network call is a one-time model download; nothing touches your git-tracked files.

## Why trust it

- **Local-only, no telemetry** — the only network call is a one-time model download; nothing about your code leaves the machine or touches your tracked tree.
- **Offline, one-time license** — buy once, keep it; activation verifies an Ed25519-signed key against a bundled public key with no phone-home.
- **Drop-in, fail-open** — drive it from the Python API, the CLI, or any harness; a missing optional dependency degrades gracefully instead of crashing.

## Who it's for

RAG and knowledge-app builders, and any team running coding agents that should find context fast and cheap — without coupling to a cloud vector vendor.

## Pricing

**Pro — from $59 / seat / mo** · one-time license $890 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

## Request access

VisionCAGRAG is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionCAGRAG and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
