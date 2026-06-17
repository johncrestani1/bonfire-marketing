# Bonfire Terminal — Stats & Social Proof

*Last updated: 2026-06-17*

## Product Stats

| Metric | Value |
|---|---|
| Current version | 2.7.296 |
| Bundled toolchains | 16 (locked versions for deterministic builds) |
| Supported messaging bridges | 6 (Telegram, Discord, Slack, WhatsApp, Twilio, REST API) |
| AI providers | 5 (Local/TinyLlama, OpenAI, Claude, Gemini, Grok) |
| Installer size | ~2 GB |
| Minimum hardware | Windows 10, 2013+ machine, 4GB RAM |
| Build quality gates | 35 Bazel gates per release |
| BEP actions per build | 3,744 across 9 pipeline stages |
| Code signing | EV Code Signing (SSL.com, M3M3TIC LLC) |

## Technical Architecture

| Component | Technology |
|---|---|
| Daemon | Rust + Tokio/Axum |
| UI | Electron 28 + React + Vite |
| Build system | Bazel 8.7 with hermetic toolchains |
| AI orchestration | Direct HTTP to provider APIs (zero CLI dependency) |
| Speech-to-text | Whisper (local, bundled) |
| Media processing | FFmpeg (local, bundled) |
| Local LLM | TinyLlama 1.1B (bundled, runs on CPU) |

## Founder

| Metric | Value |
|---|---|
| Name | John Crestani |
| Background | 9-figure affiliate marketing business |
| Focus | Local-first AI, creator economy tools |
| Notable | Built one of the largest affiliate operations globally |
