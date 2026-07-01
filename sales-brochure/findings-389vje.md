# Logo & Integration Findings — 389vje (Updated with SOT analysis)

## Logo Sources Found

### Bonfire Source Code (C:\Bonfire)
**Primary curated collection:** `C:\Bonfire\marketing-brand\logos\integrations\`
- `ai-providers/` — openai, anthropic, google-gemini, xai-grok, meta-llama, huggingface (PNG+SVG)
- `messaging-bridges/` — telegram, discord, slack, whatsapp, twilio, zapier (PNG+SVG)
- `social-platforms/` — youtube, instagram, tiktok, twitter, linkedin, facebook, pinterest, reddit, snapchat, threads (PNG+SVG)
- `marketing-platforms/` — shopify, stripe, meta-ads, google-ads, canva, hubspot, sendgrid, mailchimp, convertkit, clickfunnels, wordpress, wix, squarespace, webflow (PNG+SVG)
- `affiliate-business/` — clickbank, shareasale, cj, impact, paypal, wise, revolut, mercury, plaid, quickbooks (PNG+SVG)
- `creator-tools/` — figma, adobe, notion, airtable, asana, trello, zoom, loom, calendly, typeform (PNG+SVG)
- `cloud-infra/` — aws, google-cloud, cloudflare, vercel, netlify, digitalocean, heroku, railway, supabase, azure (PNG+SVG)
- `bundled-tools/` — ffmpeg, rust, nodejs, python, golang, electron, bazel, docker, github, git (PNG+SVG)
- `misc-tech/` — grafana, prometheus, loki, ubuntu, apple, samsung, nvidia, amd, intel, microsoft (PNG+SVG)

**Onboarding logos:** `C:\Bonfire\src-code\src\assets\onboarding-logos\`
- openai, anthropic, google, grok, telegram, discord, slack, whatsapp, twilio, zapier, homepod, sonos

**Marketing extras:** `C:\Bonfire\marketing\logos\` — 70+ additional logos (press, affiliates, CRMs, etc.)

### Brochure Images (D:\marketing\18pg-sales-brochure\images)
Already has 450+ logos across multiple directories:
- `tech-logos/` + `tech-logos-png/` — 100+ SVG+PNG (claude-color, openai, gemini-color, xai-grok, meta-llama, etc.)
- `logo-badges/` — 80+ branded badge-style logos
- `logo-dev/` — 80+ dev-ecosystem logos
- `devicon-logos/` — 80+ developer icon collection (includes deepseek, grok, claude_code, copilot)
- `wikimedia-logos/` — 35+ wikimedia-sourced logos
- `as-seen-on/` — bloomberg, cnbc, entrepreneur, forbes, fox-business, inc-magazine, wired, etc.
- `certification/` — clickbank/clickfunnels/digistore24 awards, G2 badges

## Current Brochure Logo Usage

### S8 (P8 - What Bonfire Connects)
- **Connectivity row 1:** zapier, slack, discord, mailchimp, wordpress
- **Connectivity row 2:** google-ads, shopify, stripe, meta-color, youtube
- **Content row 1:** openai, claude-color, gemini-color, xai-grok, dalle
- **Content row 2:** midjourney, elevenlabs, ffmpeg, stability-ai, whisper-openai

### S9 (P9 - The Bonfire Platform)
- **AI Providers:** claude-color, openai, gemini-color, xai-grok, meta-llama (5 logos)
- **Affiliate Networks:** clickbank, digistore24, impact, cj-affiliate, awin, rakuten, jvzoo, walmart (8 logos)

## Source of Truth: Bonfire Application Logos

### Onboarding Logos (C:\Bonfire\src-code\src\assets\onboarding-logos\)
All 128x128 PNG. These are the SOT logos used/prepared for the actual app:
- **AI Providers:** anthropic.png, openai.png, google.png, grok.png
- **Bridges (active in SettingsPane.tsx):** telegram.png, discord.png, slack.png, whatsapp.png, twilio.png, zapier.png
- **Audio:** homepod.png, sonos.png
- **Missing:** meta-llama (no Llama logo in SOT set)

### Base64 Plugin Logos (plugin-logos.ts — 90 logos)
Embedded in C:\Bonfire\src-code\src\components\main-app\plugin-logos.ts
- 55 PNG + 35 SVG logos, all decodable
- Covers: affiliate networks (clickbank, digistore24, impact, cj, awin, jvzoo, rakuten, warriorplus)
- Enterprise: salesforce, hubspot, quickbooks, bloomberg, nasdaq, morningstar
- Media plugins: ffmpeg, blender, canva, premiere, remotion, kdenlive
- NO AI provider logos in base64 — they use standalone PNGs only

### Bonfire Brand Logo
- bonfire-logo-base64.ts: High-res PNG, 25KB base64 string
- Also: bonfire-white.png, bonfire-batman-black.png, bonfire-logo-128/256.png

## Gaps & Opportunities

1. **Missing from S9 AI Providers:** groq, mistral, deepseek, huggingface, ollama, cohere — all have logos available
2. **No Bridge/Messaging section in S9:** telegram, discord, slack, whatsapp logos exist but aren't showcased on the platform page
3. **No Social Platforms section:** youtube, instagram, tiktok, twitter, linkedin logos all available
4. **No Creator Tools shown:** figma, adobe, notion, canva logos available
5. **Marketing-brand collection is the highest quality** — curated with both PNG and SVG, organized by category
6. **S8 has 20 logos but S9 only has 13** — opportunity to expand S9's integration showcase
7. **Bonfire source has plugin logos** for sonos, remotion, canva, adobe-premiere, blender, ffmpeg, kdenlive — none shown in brochure
