# Bonfire Terminal — Typography

## Primary: Inter

**Usage**: All UI text, headings, body copy, marketing materials.

| Weight | CSS Value | Use |
|---|---|---|
| Regular | `font-weight: 400` | Body text, descriptions |
| Medium | `font-weight: 500` | Emphasis, labels |
| Semibold | `font-weight: 600` | Subheadings, buttons |
| Bold | `font-weight: 700` | Headings, titles |

**Source**: [Google Fonts — Inter](https://fonts.google.com/specimen/Inter)
**License**: SIL Open Font License 1.1

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## Monospace: JetBrains Mono

**Usage**: Code blocks, terminal output, technical content, CLI examples.

| Weight | CSS Value | Use |
|---|---|---|
| Regular | `font-weight: 400` | Code, terminal text |
| Bold | `font-weight: 700` | Highlighted code |

**Source**: [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
**License**: SIL Open Font License 1.1

```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```

## CSS Stack

```css
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
code, pre { font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace; }
```
