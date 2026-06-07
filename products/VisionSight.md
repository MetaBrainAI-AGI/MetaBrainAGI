<div align="center">

<img src="../assets/vision-logo.svg" alt="Vision by MetaBrainAGI" width="120" height="120" />

# VisionSight

### Off-screen EYES for any AI agent.

**See the user's screen, browse any website headless (full-page render, DOM, console, network), and sense presence via the camera — then pass the pixels to a vision-LLM to understand them. Everything off-screen; nothing is ever shown on the user's display.**

<sub>VisionPRIME family · MetaBrainAGI · License-clean (mss MIT · Playwright/Chromium Apache-2.0/BSD · OpenCV Apache-2.0) · 100% local capture</sub>

</div>

---

## What it does
- **Screen eye** — capture the live display to a PNG and read it with a vision-LLM ("what's shown / what's wrong").
- **Web eye** — load any URL in headless Chromium and view the rendered result: full-page screenshot + title + visible text + **console errors** + **network failures**.
- **Presence eye** — opt-in webcam presence (local OpenCV face-count, frame discarded) + input-idle, to route authorization (owner away → out-of-band, not a dead terminal prompt).
- **Camera-vision eye** — *(double opt-in)* route one frame to a vision-LLM for a rich presence read; the frame is deleted after and never recorded.

## Why it matters
Turns a blind, text-only assistant into one that can actually **look** at a UI, a rendered page, or a visual bug and diagnose it — and that knows whether the owner is even at the terminal.

## Setup (you control the credentials)
On first run, VisionSight **prompts you for your vision-LLM credentials** (Gemini / OpenAI / OpenRouter — *your* keys, stored only in your local vault). All capture (screen, web, camera) is 100% local; only the chosen vision call leaves the machine, with your key.

## Pricing
**$39 / seat / mo** · one-time license available · included in the **Vision Suite** bundle. The combined eyes+voice product is **VisionPerceptionVoice**.
