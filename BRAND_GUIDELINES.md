# Bonfire Terminal — Brand Guidelines

*Audited from actual source code: variables.css, MainApp.css, global.css (2026-06-17)*

## Brand Identity

Bonfire Terminal is a local-first AI harness for content creators. The brand communicates: warmth, power, independence, transparency. The visual language is dark, sharp, and fire-lit.

## Logo

The Bonfire logo is a **red circle with a white flame cutout** (negative space). The dominant red is `#f94238`. A standalone flame variant exists for inline use (the "I" in "BONF🔥RE").

### Variants
- **Primary** (red circle + white flame) — default on dark backgrounds
- **Light** (white circle + white flame) — for dark photo overlays
- **Dark** (black circle + black flame) — for light backgrounds
- **Icon only** (circle + flame at small sizes: 16-256px)
- **Flame mark** (standalone flame, no circle) — inline decorative use

### Usage Rules
- **Minimum size**: 32px height digital, 10mm print
- **Clear space**: 50% of logo height as padding on all sides
- **Never**: stretch, rotate, add effects, recolor, place on busy backgrounds
- **Always**: sharp corners. The Bonfire brand uses `border-radius: 0` everywhere.

## Colors

Source of truth: `src/variables.css` and `src/components/main-app/MainApp.css`

### Core Brand

| Name | Hex | CSS Variable | Usage |
|---|---|---|---|
| Bonfire Orange | `#FF9000` | `--bonfire-orange`, `--bf-accent` | Primary accent, CTAs, highlights |
| Bonfire Red | `#f94238` | `--bonfire-red`, `--bf-red` | Logo color, blaze glow, error states |
| Crestani Gold | `#b29d60` | `--crestani-gold` | Onboarding headings, buttons, premium feel |
| Crestani Gold Light | `#D0B871` | `--crestani-gold-light` | Hover/highlight variant |
| Cerulean Blue | `#00C2FF` | `--bf-blue` | Revenue Command Center, Tesseract header |
| Secretary Teal | `#0A5C63` | `--bf-green` | Daemon-online, success states |
| Ember Orange | `#ff8c42` | (inline) | Warm accent in headings, terminal text |

### Backgrounds (dark-only — no light mode)

| Name | Hex | CSS Variable |
|---|---|---|
| BG Primary | `#0d0d0d` | `--bg-primary` |
| Slate Black | `#1A1A1A` | `--crimson-slate`, `--bf-bg` |
| Panel | `#141414` | `--bf-panel` |
| Panel Alt | `#222222` | `--bf-panel-alt` |
| BG Elevated | `#323237` | `--bg-elevated` |

### Text

| Name | Hex | CSS Variable |
|---|---|---|
| Text Primary | `#e8e8e8` | `--text-primary` |
| Text Secondary | `#999999` | `--text-secondary` |
| Text Muted | `#666666` | `--text-muted` |
| Text Dim | `#8888aa` | `--bf-text-dim` |

### Fire Gradient (Blaze cursor/effects)

```css
/* The signature Bonfire fire gradient */
--blaze: linear-gradient(135deg, #f94238, #ff8c42, #ffcc02);
/* Smolder: #f94238 → Burn: #ff8c42 → Blaze: #ffcc02 */
```

### Semantic

| Name | Hex | CSS Variable |
|---|---|---|
| Success | `#259F70` | `--success` |
| Warning | `#FFB700` | `--warning` |
| Error | `#E63946` | `--error` |
| Info | `#4A9EFF` | `--info` |

## Typography

Source of truth: `src/assets/fonts/`, `variables.css`, `global.css`

### Headings: Orbitron
- Variable font covering weights 100-900
- Most used: **700** (headings/titles), **900** (impact text)
- CSS: `--bf-font-heading: 'Orbitron', monospace;`
- Style: ALL-CAPS with letter-spacing 1.5-4px
- License: SIL Open Font License
- Source: bundled in `src/assets/fonts/Orbitron/`

### Body: Rajdhani
- 5 weights: 300 (Light), 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)
- CSS: `--bf-font-body: 'Rajdhani', 'Segoe UI', sans-serif;`
- Global: `font-family: 'Rajdhani', 'Segoe UI', system-ui, sans-serif;`
- License: SIL Open Font License
- Source: bundled in `src/assets/fonts/Rajdhani/`

### Monospace: Cascadia Code
- CSS: `--bf-font-mono: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;`
- Usage: terminal panes, code display, diagnostics, settings inputs

### CSS Font Stack
```css
:root {
  --bf-font-heading: 'Orbitron', monospace;
  --bf-font-body: 'Rajdhani', 'Segoe UI', sans-serif;
  --bf-font-mono: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
}
body { font-family: 'Rajdhani', 'Segoe UI', system-ui, sans-serif; }
h1, h2, h3 { font-family: 'Orbitron', monospace; text-transform: uppercase; letter-spacing: 2px; }
code, pre { font-family: 'Cascadia Code', 'Fira Code', 'Consolas', monospace; }
```

## Design Principles

1. **Dark-only**: Primary bg `#0d0d0d`. No light mode. Ever.
2. **Sharp corners**: `border-radius: 0` everywhere. No rounded buttons, no pill shapes.
3. **ALL-CAPS headings**: Orbitron at 700-900 weight with 1.5-4px letter-spacing.
4. **Fire as motion language**: The blaze gradient (`#f94238 → #ff8c42 → #ffcc02`) appears in cursor effects, loading states, and emphasis.
5. **Minimal chrome**: No decorative borders, no shadows on flat elements. Let the fire palette provide warmth against the black.

## Voice & Tone

- **Direct**: Say what you mean. No marketing fluff.
- **Technical but accessible**: Use proper terms but explain them.
- **Confident**: We build real software that ships.
- **Transparent**: Local-first, open architecture, no hidden data collection.

## Publisher

- **Company**: M3M3TIC LLC
- **Product**: Bonfire Terminal
- **Tagline**: "Private AI Terminal"
- **Copyright**: Copyright (C) 2026 M3M3TIC LLC. All rights reserved.
- **Website**: https://bonfireterminal.com
