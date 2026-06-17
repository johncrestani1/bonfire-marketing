# Bonfire Terminal — Color Palette

## Primary

| Swatch | Name | Hex | RGB | HSL | Usage |
|---|---|---|---|---|---|
| 🟠 | Bonfire Orange | `#F59E0B` | `245, 158, 11` | `38°, 92%, 50%` | Primary brand, CTAs, active states |
| 🔵 | Bonfire Dark | `#1A1A2E` | `26, 26, 46` | `240°, 28%, 14%` | Backgrounds, dark mode, text |
| ⚪ | Bonfire White | `#FAFAFA` | `250, 250, 250` | `0°, 0%, 98%` | Light backgrounds, reversed text |

## UI States

| Swatch | Name | Hex | Usage |
|---|---|---|---|
| 🟢 | Pass Green | `#22C55E` | Gate pass, success, confirmation |
| 🔴 | Fail Red | `#EF4444` | Gate fail, error, destructive action |
| 🟡 | Amber | `#F59E0B` | Running, in-progress, warning |
| ⚫ | Muted Gray | `#6B7280` | Disabled, secondary, placeholder |

## CSS Custom Properties

```css
:root {
  --bonfire-orange: #F59E0B;
  --bonfire-dark: #1A1A2E;
  --bonfire-white: #FAFAFA;
  --bonfire-green: #22C55E;
  --bonfire-red: #EF4444;
  --bonfire-gray: #6B7280;
}
```
