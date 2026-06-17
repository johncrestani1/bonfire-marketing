# Bonfire Terminal — Typography

*Source: src/assets/fonts/, variables.css, global.css, MainApp.css*

## Headings: Orbitron

**Usage**: ALL headings, titles, chapter numerals, buttons, section labels.
**Style**: ALWAYS uppercase with letter-spacing 1.5-4px.

| Weight | Value | Use |
|---|---|---|
| Bold | `700` | Standard headings, titles |
| Black | `900` | Impact text, slam text, hero banners |

**Variable font** bundled at `src/assets/fonts/Orbitron/Orbitron-VariableFont_wght.ttf` (100-900).

```css
h1, h2, h3 {
  font-family: 'Orbitron', monospace;
  text-transform: uppercase;
  letter-spacing: 2px;
}
```

**License**: SIL Open Font License 1.1
**Source**: [Google Fonts — Orbitron](https://fonts.google.com/specimen/Orbitron)

## Body: Rajdhani

**Usage**: ALL body text, form inputs, navigation, subtitles, descriptions.

| Weight | Value | Use |
|---|---|---|
| Light | `300` | Subtle text, captions |
| Regular | `400` | Body text |
| Medium | `500` | Emphasis, labels |
| SemiBold | `600` | Buttons, strong emphasis |
| Bold | `700` | Bold body text |

```css
body {
  font-family: 'Rajdhani', 'Segoe UI', system-ui, sans-serif;
}
```

**License**: SIL Open Font License 1.1
**Source**: [Google Fonts — Rajdhani](https://fonts.google.com/specimen/Rajdhani)

## Monospace: Cascadia Code

**Usage**: Terminal panes, code display, diagnostics bar, settings inputs.

```css
code, pre, .terminal {
  font-family: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
}
```

**Source**: [Microsoft Cascadia Code](https://github.com/microsoft/cascadia-code)

## Full CSS Stack

```css
:root {
  --bf-font-heading: 'Orbitron', monospace;
  --bf-font-body: 'Rajdhani', 'Segoe UI', sans-serif;
  --bf-font-mono: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
}
```

```html
<!-- Google Fonts import for web/marketing pages -->
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```
