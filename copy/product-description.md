# Bonfire Terminal — Product Description

## Elevator Pitch (3 sentences)
Bonfire Terminal is a local-first AI platform for content creators. It runs AI models, speech-to-text, and media editing directly on your machine — no cloud, no API keys, no data leaving your device. Interact through your phone's messaging app and get back AI-generated content in seconds.

## Short Description (1 paragraph)
Bonfire Terminal bridges your messaging apps to local AI. Send a voice note via Telegram, get a transcription back. Send an image via Discord, get an AI-edited version. Send a text prompt via WhatsApp, get an AI response powered by models running on your own hardware. Everything stays local. The product ships as a single installer with bundled AI models, FFmpeg, Whisper speech-to-text, and 16 other tools — zero setup, zero cloud dependency, zero monthly subscription for core features.

## Long Description (3 paragraphs)
Bonfire Terminal is a desktop application that turns your computer into a personal AI workstation. It connects to your messaging platforms — Telegram, Discord, WhatsApp, Slack, Twilio — and processes AI requests locally. When you send a message through any of these platforms, Bonfire's daemon intercepts it, runs it through local AI models, and sends the result back. Voice notes become text. Images get edited. Videos get generated. All on your hardware.

The architecture is fundamentally different from cloud AI services. There is no server between you and your AI. The Rust daemon handles message routing, the bundled TinyLlama model handles text generation, Whisper handles speech-to-text, and FFmpeg handles media processing. For users who want more powerful models, Bonfire also supports OpenAI, Claude, Gemini, and Grok through direct API connections — but even then, the orchestration happens locally.

Bonfire ships as a single 2GB Windows installer that includes everything: the AI daemon, the Electron UI, 16 locked toolchains, and pre-trained models. There is no "npm install", no Python environment to configure, no Docker to run. Install it, pick a folder, and start creating. The build system uses Bazel with 35 quality gates and 1,302 build actions to ensure every release is deterministic, tested, and signed.
