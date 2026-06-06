<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionOmniCollab

### Cross-host + LAN agent federation.

**Let agent instances on different machines discover each other, see who's working on what, and hand off cleanly — signed, sealed, and automatic.**

<sub>VisionPRIME family · MetaBrainAGI · Ed25519 + X25519/AES-GCM · GitHub control plane · LAN data plane</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

Run more than one agent — a second machine, a teammate's session, a background worker — and they immediately start stepping on each other. Two sessions edit the same lane; a resumed session has no idea what the last one was doing; coordinating them means a shared chat window and good manners. There's no secure, automatic way for independent instances to know each other exists and divide the work.

## The solution

VisionOmniCollab is the federation layer for VisionPRIME instances. Instances pointed at the **same GitHub repo auto-discover each other**, see who is working on what, and exchange **sealed** coordination keys + tools-config — and when they're on the **same private network, they talk DIRECT over private LAN IPs** for signed, encrypted comms and media transfer. GitHub is the control plane; the LAN is the fast data plane. It auto-joins on session start, so the user never has to ask — and if there's no remote, no crypto, or a rate limit, it degrades to local-only and never blocks the session.

## What you get

- **Auto-join, zero user action.** A SessionStart daemon joins the mesh on the shared `origin` — discovery, presence, and group membership happen automatically.
- **Signed + sealed by construction.** Ed25519-signed presence cards that peers verify before trusting; X25519 multi-recipient + AES-256-GCM sealed coordination secrets, decryptable only by the addressed agents' local vault keys. A usable secret never touches git or the working tree.
- **LAN data plane.** Same-subnet detection by a salted hash (no IP leaked in git); an authenticated, anti-replay HTTP listener (`/vp/comm`, `/vp/media`) where the raw private IP is sealed to live peers only. Fails closed to the control plane when peers aren't co-located.
- **The handover protocol.** A fresh session discovers live peers and their lanes, claims an unclaimed lane so no one double-works it, reads peers' handoff records, and hands off cleanly before it ends — so the next session or host resumes where the last one stopped.
- **No-push-race design.** Per-host files (each instance owns its own card); the roster is a computed view, never a written object. The mesh lives on a dedicated branch — never `main` — operated from an isolated worktree.
- **GitHub Actions federation.** Dispatch + scaffold workflows across the fleet from the same control plane.

## Why trust it

- **Secrets never hit git** — coordination keys and the raw LAN IP are X25519/AES-sealed to live peers; the federation token is read from your vault per git command and never written to config, the remote URL, or logs.
- **Fail-open** — no remote, no crypto, or a rate limit degrades cleanly to local-only; the mesh never blocks a session.
- **Scope-limited by design** — the mesh carries coordination keys + tools-config only, never PII, household KEKs, or payment secrets.

## Who it's for

Teams running multi-machine agent fleets — distributed CI workers, several developers each with their own agent on the same repo, or a home/office network of VisionPRIME instances that should behave like one coordinated team.

## Pricing

**Pro — from $59 / seat / mo** · one-time license $890 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

> **Honest status:** crypto identity, signed presence cards, the git mesh, the LAN listener, and the auto-join daemon are built and self-tested (loopback). A hardening backlog (CA-roster key-pinning, cheap revocation, anti-rollback epoch, signed commits + branch protection) must land before the mesh carries real secrets; until then, secret-sharing is gated to coordination/test config only. A cross-host live exercise needs two machines on one LAN.

## Request access

VisionOmniCollab is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrain AI — MetaBrainAGI. VisionOmniCollab and the Vision mark are trademarks of MetaBrain AI. Not affiliated with Anthropic.</sub></div>
