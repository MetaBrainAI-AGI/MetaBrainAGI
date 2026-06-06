<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionPerceptionVoice

### Eyes, voice, and presence for your agent.

**Give your AI assistant eyes, ears, a voice, and presence on the machine it runs on — locally, privately, license-clean.**

<sub>VisionPRIME family · MetaBrainAGI · local-first · on-device STT/VAD/TTS · safety-gated</sub>

[Pricing](../PRICING.md) · [All products](../PRODUCTS.md) · [Request access](#request-access)

</div>

---

## The problem

A coding agent is blind, deaf, and mute on the machine it runs on. It can't see the screen to tell you what's wrong, can't take a spoken instruction, can't speak back, and — worst of all — freezes on an approval prompt for hours when you step away. Cloud perception services exist, but they want your screen and your audio sent off-box.

## The solution

VisionPerceptionVoice ships three production skills together — **sight, voice, and presence** — that run on-device. STT, VAD, TTS, and screen/camera capture all run locally; the camera is presence-only (a face *count*, frame discarded) and off by default; voiceprints are stored as embeddings, never raw audio. Every side-effectful path goes through an explicit ALLOW / CONFIRM / BLOCK gate, and observed page or file content is treated as data, never as commands — so it's prompt-injection safe by construction.

## What you get

- **vision-sight.** See the screen; browse any site headless (screenshots, DOM, console, network) understood by a vision LLM; sense presence (camera + input-idle) for presence-aware authorization — all off-screen.
- **vision-voice.** A two-way local voice loop with wake word and a dual-EoU fast path; speaker LOCK + a multi-user roster with roles (IAM); voice dictation into your terminal ("enter" submits); a voice command/skill/filesystem router; and local Kokoro TTS.
- **vision-presence (always-on runtime app).** Knows when you've stepped away (keyboard/mouse idle; 3 minutes ⇒ AWAY) so the agent never idles on a human gate. Its primary escalation path convenes the Genius Board to clear soft, reversible gates (APPROVE / REFINE ⇒ auto-execute); for the immutable hard-gate floor it asks you (present) or queues + tags + surfaces-on-return — and reaches you out-of-band by email / SMS / voice call / push with a one-tap approve/deny, then ingests your reply with no public webhook.
- **Never waits on an absent you.** It uses credentials you already hold (SendGrid or free Gmail SMTP for email; Twilio for SMS + calls; harness push) — no new accounts, no public server — and a Stop hook enforces it in code, not just policy.
- **License-clean dependencies.** mss (MIT), Playwright + Chromium (Apache-2.0 / BSD), OpenCV (Apache-2.0), faster-whisper (MIT), webrtcvad (BSD), Kokoro-ONNX (Apache-2.0) — used as-is.

## Why trust it

- **Local-first and private** — capture and STT/VAD/TTS run on-device; the camera is presence-only and off by default; voiceprints are embeddings, never raw audio.
- **Safety-gated by construction** — every side-effectful path (dictation submit, voice commands, machine control) passes an explicit ALLOW / CONFIRM / BLOCK gate; destructive actions are drafted or refused, never auto-run.
- **Prompt-injection safe** — observed page and file content is treated as data, never as instructions.

## Who it's for

Builders of voice and desktop agents who want perception on the local machine — see-the-screen debugging, hands-free dictation, and a presence-aware assistant that keeps working instead of stalling when you walk away.

## Pricing

**Pro — from $49 / seat / mo** · one-time license $690 · Enterprise custom. See **[PRICING.md](../PRICING.md)** for the full table and bundles.

> **Requirements:** Python 3.11+ (3.13 recommended); a microphone for voice/dictation, a webcam only if you opt into camera presence; Windows is first-class (voice dictation via the Win32 SendInput API), with Linux/macOS supported for the eyes and the voice loop. A vision-LLM key is optional, only for "look at this and tell me what's wrong."

## Request access

VisionPerceptionVoice is in private launch. Source is private; access is granted with a license.

**[hello@metabrain.ai](mailto:hello@metabrain.ai)**

<div align="center"><sub>© MetaBrainAGI. Commercial software. VisionPRIME and the Vision mark are marks of the publisher. Not affiliated with Anthropic.</sub></div>
