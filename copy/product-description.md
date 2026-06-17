# Bonfire Terminal — Product Description

## Elevator Pitch (3 sentences)
Bonfire Terminal enables one person to do what used to require a 13-person outsourced marketing operation — video editing, social media management, email copywriting, project coordination, ad creation, and more — all powered by local AI on your own hardware. No cloud, no data leaving your device, no monthly subscriptions draining your business. One $5,000 investment replaces $200/month in AI subscriptions and $10,000+/month in outsourced labor.

## Short Description (1 paragraph)
Bonfire Terminal bridges your messaging apps to local AI. Send a voice note via Telegram, get a transcription back. Send an image via Discord, get an AI-edited version. Send a text prompt via WhatsApp, get an AI response powered by models running on your own hardware. Everything stays local. The product ships as a single installer with bundled AI models, FFmpeg, Whisper speech-to-text, and 16 other tools — zero setup, zero cloud dependency. Built for professionals who take data privacy and cost control seriously.

## Long Description (3 paragraphs)
Bonfire Terminal is a desktop application that turns your computer into a personal AI workstation. It connects to your messaging platforms — Telegram, Discord, WhatsApp, Slack, Twilio — and processes AI requests locally. When you send a message through any of these platforms, Bonfire's daemon intercepts it, runs it through local AI models, and sends the result back. Voice notes become text. Images get edited. Videos get generated. All on your hardware.

The architecture is fundamentally different from cloud AI services. There is no server between you and your AI. The Rust daemon handles message routing, the bundled TinyLlama model handles text generation, Whisper handles speech-to-text, and FFmpeg handles media processing. For users who want more powerful models, Bonfire also supports OpenAI, Claude, Gemini, and Grok through direct API connections — but even then, the orchestration happens locally.

Bonfire ships as a single 2GB Windows installer that includes everything: the AI daemon, the Electron UI, 16 locked toolchains, and pre-trained models. There is no "npm install", no Python environment to configure, no Docker to run. Install it, pick a folder, and start creating. The build system uses Bazel with 35 quality gates and 1,302 build actions to ensure every release is deterministic, tested, and signed.

## Pricing
Bonfire Terminal is a **$5,000 one-time investment**. No subscription. No recurring fees. No hidden costs.

| | Cloud AI Subscriptions | Bonfire Terminal |
|---|---|---|
| Year 1 | $2,400 | $5,000 |
| Year 2 | $4,800 | $5,000 |
| Year 3 (breakeven at month 25) | $7,200 | $5,000 |
| Year 5 | $12,000 | $5,000 |
| **5-year savings** | | **$7,000+** |

The average marketer, content creator, or coach spends $200/month ($2,400/year) on AI subscriptions — ChatGPT, Claude, transcription services, image tools, and API costs. Bonfire replaces that stack with a single local installation. It pays for itself in 25 months, then saves $2,400/year for life.

## The 13-Person Team You No Longer Need

Before Bonfire Terminal, running a content operation required outsourcing to:

| Role | Typical Cost | Bonfire Replaces |
|---|---|---|
| Video editor | $2,000-5,000/mo | FFmpeg + AI editing pipeline |
| Social media manager | $1,500-3,000/mo | Bridge architecture + scheduled posts |
| Email copywriter | $1,000-3,000/mo | AI-assisted copy through messaging |
| Graphic designer | $1,500-3,000/mo | Image editing + overlay tools |
| Transcriptionist | $500-1,500/mo | Whisper speech-to-text (local) |
| Project coordinator | $2,000-4,000/mo | Plugin orchestration + command pipeline |
| Facebook ads specialist | $1,500-3,000/mo | Meta Ads CLI integration |
| Google ads specialist | $1,500-3,000/mo | Ad copy generation pipeline |
| SEO content writer | $1,000-2,500/mo | AI content with local models |
| Podcast editor | $500-1,500/mo | FFmpeg audio processing |
| Virtual assistant | $500-1,500/mo | AI task execution via messaging |
| Data analyst | $2,000-4,000/mo | AI-powered analytics summaries |
| Tech support / IT | $1,000-2,000/mo | Self-contained, no infrastructure |
| **TOTAL** | **$16,500-37,000/mo** | **$5,000 one-time** |

Bonfire Terminal doesn't make you a 13-person team. It makes 13 people unnecessary.

## Why Not OpenClaw?

Competitors like OpenClaw offer stripped-down "local AI" wrappers that look similar on the surface. Here's what they're missing:

| Capability | Bonfire Terminal | OpenClaw |
|---|---|---|
| Bridge architecture (Telegram, Discord, WhatsApp, Slack) | 6 native bridges | No messaging integration |
| Bundled toolchains (locked, versioned) | 16 tools, hermetic | BYO dependencies |
| Speech-to-text | Whisper bundled, runs locally | Not included |
| Media processing | FFmpeg bundled, image + video | Not included |
| Build quality | 35 Bazel gates, 1,302 actions, EV code-signed | No build system |
| Plugin architecture | 9 plugins (FFmpeg, Meta Ads, Shopify, Stripe, etc.) | No plugins |
| Offline operation | Full capability with local models | Requires internet for most features |
| Code signing | EV certificate (M3M3TIC LLC, SSL.com) | Unsigned |
| Installer | Single 2GB, zero dependencies | Manual setup required |

OpenClaw gives you a text box that talks to an API. Bonfire gives you a complete AI operations center that runs on your hardware, connects to your messaging apps, and replaces an entire outsourced team.

## Target Audience
- **Marketers** handling client campaigns, brand voice documents, and proprietary strategy
- **Content creators** producing videos, podcasts, written content, and social media at scale
- **Coaches** managing client data, session recordings, course material, and confidential communications

This is professional-grade software for serious operators who are currently spending $10,000-37,000/month on outsourced teams. Bonfire Terminal is the $5,000 replacement.
