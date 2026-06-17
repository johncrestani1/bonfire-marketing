# Bonfire Terminal — Color Palette

*Source: src/variables.css, src/components/main-app/MainApp.css*

## Primary Brand

| Swatch | Name | Hex | RGB | CSS Variable | Usage |
|---|---|---|---|---|---|
| 🔴 | **Bonfire Red** | `#f94238` | `249, 66, 56` | `--bonfire-red` | **PRIMARY** — logo, blaze glow, brand identity |
| 🟠 | Bonfire Orange | `#FF9000` | `255, 144, 0` | `--bonfire-orange`, `--bf-accent` | CTAs, highlights, active states |
| 🟡 | Crestani Gold | `#b29d60` | `178, 157, 96` | `--crestani-gold` | Onboarding, premium elements, buttons |
| 🔵 | Cerulean Blue | `#00C2FF` | `0, 194, 255` | `--bf-blue` | Revenue Command Center, Tesseract |
| 🟢 | Secretary Teal | `#0A5C63` | `10, 92, 99` | `--bf-green` | Daemon-online, success indicators |
| 🟠 | Ember Orange | `#ff8c42` | `255, 140, 66` | (inline) | Warm accent, headings, terminal |

## Fire Gradient (signature Bonfire effect)

```css
/* Smolder → Burn → Blaze */
background: linear-gradient(135deg, #f94238, #ff8c42, #ffcc02);
```

## Backgrounds (dark-only)

| Name | Hex | CSS Variable |
|---|---|---|
| BG Primary | `#0d0d0d` | `--bg-primary` |
| Slate Black | `#1A1A1A` | `--crimson-slate`, `--bf-bg` |
| Panel | `#141414` | `--bf-panel` |
| Panel Alt | `#222222` | `--bf-panel-alt` |
| BG Elevated | `#323237` | `--bg-elevated` |

## Text

| Name | Hex | CSS Variable |
|---|---|---|
| Primary | `#e8e8e8` | `--text-primary` |
| Secondary | `#999999` | `--text-secondary` |
| Muted | `#666666` | `--text-muted` |
| Dim | `#8888aa` | `--bf-text-dim` |

## Semantic States

| State | Hex | CSS Variable |
|---|---|---|
| Success | `#259F70` | `--success` |
| Warning | `#FFB700` | `--warning` |
| Error | `#E63946` | `--error` |
| Info | `#4A9EFF` | `--info` |

## CSS Custom Properties

```css
:root {
  /* Brand */
  --bonfire-red: #f94238;
  --bonfire-orange: #FF9000;
  --crestani-gold: #b29d60;
  --crestani-gold-light: #D0B871;
  --bf-blue: #00C2FF;
  --bf-green: #0A5C63;

  /* Backgrounds */
  --bg-primary: #0d0d0d;
  --bf-bg: #1A1A1A;
  --bf-panel: #141414;
  --bf-panel-alt: #222222;
  --bg-elevated: #323237;

  /* Text */
  --text-primary: #e8e8e8;
  --text-secondary: #999999;
  --text-muted: #666666;

  /* Design */
  --bf-radius: 0;  /* sharp corners everywhere */
}
```
