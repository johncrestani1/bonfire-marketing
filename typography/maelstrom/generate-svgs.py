#!/usr/bin/env python
"""
MAELSTROM ALPHABET v6 — SVG Skeleton Generator
Reads skeleton-defs.py and generates:
  1. Individual SVG files per letter in skeletons/
  2. A master canvas SVG with all 26 letters for Graphite preview
  3. An HTML preview page with side-by-side reference comparison

Coordinate transform: skeleton defs use Y-up (0=baseline, 100=cap),
SVG uses Y-down, so we flip: svg_y = 100 - skeleton_y
"""

import os
import sys
import base64
from importlib import import_module

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = import_module("skeleton-defs")
GLYPHS = spec.GLYPHS
H = spec.H
SW = spec.SW

OUT = os.path.dirname(os.path.abspath(__file__))
SKEL_DIR = os.path.join(OUT, "skeletons")
os.makedirs(SKEL_DIR, exist_ok=True)

MARGIN = 5  # margin around each glyph in SVG


def flip_y(points):
    """Flip Y coordinates for SVG (Y-down)."""
    return [(x, H - y) for x, y in points]


def points_to_path(points):
    """Convert list of (x,y) to SVG path d attribute."""
    if not points:
        return ""
    d = f"M {points[0][0]:.1f} {points[0][1]:.1f}"
    for x, y in points[1:]:
        d += f" L {x:.1f} {y:.1f}"
    d += " Z"
    return d


def glyph_to_svg(char, gdef):
    """Generate SVG string for a single glyph."""
    w = gdef['width']
    margin = MARGIN + (SW/2 if 'center_strokes' in gdef else 0)
    vb_x = -margin
    vb_y = -margin
    vb_w = w + margin * 2
    vb_h = H + margin * 2

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb_x} {vb_y} {vb_w} {vb_h}">
  <!-- {char} — Maelstrom Alphabet v6 skeleton -->
  <!-- Coordinate system: 0-100 normalized, Y-flipped for SVG -->

  <!-- Grid lines -->
  <line x1="0" y1="0" x2="{w}" y2="0" stroke="#333" stroke-width="0.3" stroke-dasharray="2,2"/>
  <line x1="0" y1="{H}" x2="{w}" y2="{H}" stroke="#333" stroke-width="0.3" stroke-dasharray="2,2"/>
  <line x1="0" y1="{H/2}" x2="{w}" y2="{H/2}" stroke="#333" stroke-width="0.3" stroke-dasharray="1,3"/>
  <line x1="0" y1="0" x2="0" y2="{H}" stroke="#333" stroke-width="0.3"/>
  <line x1="{w}" y1="0" x2="{w}" y2="{H}" stroke="#333" stroke-width="0.3"/>

'''

    if 'center_strokes' in gdef:
        # Stroke-based rendering: uniform SW-wide brushstrokes
        for stroke in gdef['center_strokes']:
            pts = flip_y(stroke)
            d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
            for x, y in pts[1:]:
                d += f" L {x:.1f} {y:.1f}"
            svg += f'  <path d="{d}" fill="none" stroke="#e8e0d4" stroke-width="{SW}" '
            svg += f'stroke-linejoin="miter" stroke-linecap="butt" stroke-miterlimit="4"/>\n'

        # Point markers on center-line vertices
        svg += '  <!-- Center-line markers -->\n'
        for stroke in gdef['center_strokes']:
            for x, y in flip_y(stroke):
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="1.2" fill="#f94238" opacity="0.7"/>\n'
    else:
        # Filled polygon rendering
        outer = flip_y(gdef['outer'])
        holes = [flip_y(hole) for hole in gdef.get('holes', [])]

        path_d = points_to_path(outer)
        for hole in holes:
            path_d += " " + points_to_path(hole)

        svg += f'  <!-- Glyph path -->\n'
        svg += f'  <path d="{path_d}" fill="#e8e0d4" fill-rule="evenodd" stroke="none"/>\n\n'
        svg += '  <!-- Point markers -->\n'
        for i, (x, y) in enumerate(outer):
            svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="1.2" fill="#f94238" opacity="0.7"/>\n'
        for hole in holes:
            for x, y in hole:
                svg += f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="1.0" fill="#4a9ef9" opacity="0.7"/>\n'

    svg += '</svg>\n'
    return svg


def generate_master_canvas():
    """Generate a master SVG with all 26 letters arranged in a grid."""
    cols = 9
    cell_w = 120
    cell_h = 140
    label_h = 15

    letters = sorted([c for c in GLYPHS.keys() if c.isalpha()])
    rows = (len(letters) + cols - 1) // cols
    total_w = cols * cell_w
    total_h = rows * cell_h + 40  # header space

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{total_w}" height="{total_h}"
     viewBox="0 0 {total_w} {total_h}">

  <rect width="100%" height="100%" fill="#0a0a0a"/>

  <!-- Title -->
  <text x="{total_w/2}" y="25" text-anchor="middle"
        font-family="monospace" font-size="14" fill="#f94238"
        letter-spacing="4">MAELSTROM ALPHABET v6 — SKELETONS</text>

'''
    traced = set("MAELSTROBI")

    for idx, char in enumerate(letters):
        col = idx % cols
        row = idx // cols
        cx = col * cell_w + cell_w / 2
        cy = row * cell_h + 50  # offset for header

        gdef = GLYPHS[char]
        w = gdef['width']
        scale = min(80 / w, 80 / H)

        # Cell background
        fill_color = "#1a1a1a" if char in traced else "#111"
        svg += f'  <rect x="{col*cell_w+2}" y="{cy-5}" width="{cell_w-4}" height="{cell_h-4}" fill="{fill_color}" rx="2"/>\n'

        # Label
        label_color = "#f94238" if char in traced else "#b29d60"
        svg += f'  <text x="{cx}" y="{cy+8}" text-anchor="middle" font-family="monospace" font-size="9" fill="{label_color}">{char}</text>\n'

        # Glyph (scaled and centered)
        gx = cx - w * scale / 2
        gy = cy + label_h

        glyph_color = "#e8e0d4" if char in traced else "#b29d60"

        if 'center_strokes' in gdef:
            # Stroke-based glyph in master canvas
            for stroke in gdef['center_strokes']:
                pts = [(x * scale + gx, (H - y) * scale + gy) for x, y in stroke]
                d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
                for x, y in pts[1:]:
                    d += f" L {x:.1f} {y:.1f}"
                svg += f'  <path d="{d}" fill="none" stroke="{glyph_color}" stroke-width="{SW * scale:.1f}" '
                svg += f'stroke-linejoin="miter" stroke-linecap="butt" stroke-miterlimit="4"/>\n'
        else:
            outer = [(x * scale + gx, (H - y) * scale + gy) for x, y in gdef['outer']]
            holes = [[(x * scale + gx, (H - y) * scale + gy) for x, y in hole] for hole in gdef.get('holes', [])]

            path_d = points_to_path(outer)
            for hole in holes:
                path_d += " " + points_to_path(hole)

            svg += f'  <path d="{path_d}" fill="{glyph_color}" fill-rule="evenodd"/>\n'
        svg += '\n'

    svg += '</svg>\n'
    return svg


def generate_preview_html():
    """Generate HTML preview with reference comparison."""
    ref_path = os.path.join(OUT, "refs", "maelstrom-font-reference-sot.JPG")
    rune_path = os.path.join(OUT, "refs", "Armanen_Runes.JPG")

    # Read SVG files
    svg_data = {}
    for char in GLYPHS:
        if not char.isalpha():
            continue
        svg_path = os.path.join(SKEL_DIR, f"{char}.svg")
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                svg_data[char] = f.read()
        except:
            svg_data[char] = f'<svg viewBox="0 0 100 100"><text x="10" y="80" font-size="60">{char}</text></svg>'

    traced = "MAELSTROBI"
    extrapolated = sorted(set(GLYPHS.keys()) - set(traced) - set("0123456789"))

    # Generation method for each glyph
    methods = {
        'M': 'traced: MAELSTROM ref',
        'A': 'traced: MAELSTROM ref (flat-top)',
        'E': 'traced: MAELSTROM ref',
        'L': 'traced: MAELSTROM ref',
        'S': 'traced: Sig rune + ref',
        'T': 'traced: MAELSTROM ref',
        'R': 'traced: MAELSTROM ref (stroke)',
        'O': 'traced: MAELSTROM ref',
        'B': 'traced: Armanen Bar rune',
        'I': 'traced: Armanen Is rune',
    }
    # Extrapolated letters get their derivation noted
    extrap_methods = {
        'C': 'extrap: O minus right wall',
        'D': 'extrap: identical to O',
        'F': 'extrap: E minus bottom arm',
        'G': 'extrap: C + right spur',
        'H': 'extrap: two stems + crossbar',
        'J': 'extrap: reversed L + hook',
        'K': 'extrap: stem + two diagonals',
        'N': 'extrap: two stems + diagonal',
        'P': 'extrap: R minus leg',
        'Q': 'extrap: O (tail deferred)',
        'U': 'extrap: inverted C shape',
        'V': 'extrap: inverted A, no bar',
        'W': 'extrap: double-V (M inverted)',
        'X': 'extrap: two crossing diags',
        'Y': 'extrap: upper V + stem',
        'Z': 'extrap: S rotated (regular Z)',
    }
    methods.update(extrap_methods)

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MAELSTROM v6 — Skeleton Preview</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #0a0a0a; color: #e0e0e0; font-family: monospace; padding: 15px; }
h1 { color: #f94238; font-size: 16px; letter-spacing: 4px; text-align: center; margin: 10px 0; }
h2 { color: #b29d60; font-size: 11px; letter-spacing: 3px; margin: 15px 0 6px; }
.refs { display: flex; gap: 10px; justify-content: center; margin: 10px 0; flex-wrap: wrap; }
.refs img { max-height: 120px; border: 1px solid #333; }
.grid { display: grid; grid-template-columns: repeat(9, 1fr); gap: 4px; max-width: 1100px; margin: 10px auto; }
.cell { background: #111; border: 1px solid #1a1a1a; padding: 6px; text-align: center; }
.cell .lbl { color: #555; font-size: 8px; letter-spacing: 1px; margin-bottom: 4px; }
.cell .method { color: #333; font-size: 6px; margin-top: 3px; line-height: 1.2; }
.cell svg { max-width: 80px; max-height: 100px; }
.cell.ref { border-color: #f94238; }
.cell.ref svg { fill: #e8e0d4; }
.cell.ref .lbl { color: #f94238; }
.cell.ext svg { fill: #b29d60; }
.cell.ext .lbl { color: #b29d60; }
.notes { max-width: 800px; margin: 15px auto; padding: 12px; background: #111; border: 1px solid #1a1a1a; font-size: 10px; color: #555; line-height: 1.7; }
.notes strong { color: #b29d60; }
.notes em { color: #f94238; font-style: normal; }
</style>
</head>
<body>

<h1>MAELSTROM ALPHABET v6 — SKELETON PREVIEW</h1>

<h2>REFERENCE IMAGES</h2>
<div class="refs">
    <img src="refs/maelstrom-font-reference-sot.JPG" alt="Maelstrom Reference">
    <img src="refs/Armanen_Runes.JPG" alt="Armanen Runes">
    <img src="refs/S-like-sideways-z-bonfire.JPG" alt="S Reference">
</div>

<h2>TRACED GLYPHS (M A E L S T R O B I) — <em>RED BORDER</em></h2>
<div class="grid">
'''

    for ch in traced:
        svg = svg_data.get(ch, '')
        # Strip XML declaration for inline embedding
        svg_inline = svg.split('?>')[-1].strip() if '?>' in svg else svg
        method = methods.get(ch, '')
        html += f'<div class="cell ref"><div class="lbl">{ch}</div>{svg_inline}<div class="method">{method}</div></div>\n'

    html += '''</div>

<h2>EXTRAPOLATED GLYPHS — <span style="color:#b29d60;">GOLD</span></h2>
<div class="grid">
'''

    for ch in sorted(extrapolated):
        svg = svg_data.get(ch, '')
        svg_inline = svg.split('?>')[-1].strip() if '?>' in svg else svg
        method = methods.get(ch, '')
        html += f'<div class="cell ext"><div class="lbl">{ch}</div>{svg_inline}<div class="method">{method}</div></div>\n'

    html += '''</div>

<div class="notes">
    <strong>V6 PIPELINE:</strong> SVG skeleton masters (canonical source) → Graphite refinement → FontForge export (last step)<br>
    <em>Red border</em> = traced from reference (MAELSTROM + Armanen runes B,I) |
    <span style="color:#b29d60;">Gold</span> = extrapolated using strict geometric rules<br><br>
    <strong>DESIGN RULES:</strong> All straight lines, zero curves. Uniform stroke ~20%.
    Sharp mitered corners only — no chamfers, no bevels.<br>
    <strong>COORDINATE SYSTEM:</strong> 0-100 normalized viewport. Scale to any target size.<br>
    <strong>S:</strong> Backwards Z (Sig rune) — diagonal upper-left to lower-right, ~67 deg from horizontal.<br>
    <strong>O:</strong> Pure rectangle (NOT octagonal). Rectangular counter.<br>
    <strong>B:</strong> Bar rune — vertical spine + 2 angular chevron bumps pointing right.
</div>

</body>
</html>'''

    return html


# ── Main ──
if __name__ == '__main__':
    print("=== Generating v6 SVG skeletons ===")

    # 1. Individual SVGs
    for char in sorted(GLYPHS.keys()):
        if not char.isalpha():
            continue
        svg = glyph_to_svg(char, GLYPHS[char])
        path = os.path.join(SKEL_DIR, f"{char}.svg")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(svg)
        gd = GLYPHS[char]
        if 'center_strokes' in gd:
            n_strokes = len(gd['center_strokes'])
            n_pts = sum(len(s) for s in gd['center_strokes'])
            print(f"  {char}: {n_strokes} strokes, {n_pts} pts, width={gd['width']} [stroke-based]")
        else:
            pts = len(gd['outer'])
            holes = len(gd.get('holes', []))
            print(f"  {char}: {pts} pts, {holes} holes, width={gd['width']}")

    # 2. Master canvas
    master = generate_master_canvas()
    master_path = os.path.join(OUT, "master-canvas.svg")
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(master)
    print(f"\n  Master canvas: {master_path}")

    # 3. Preview HTML
    html = generate_preview_html()
    html_path = os.path.join(OUT, "skeleton-preview.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Preview HTML: {html_path}")

    letters = [c for c in GLYPHS if c.isalpha()]
    traced = [c for c in letters if c in "MAELSTROBI"]
    extrap = [c for c in letters if c not in "MAELSTROBI"]
    print(f"\n=== Done: {len(letters)} letters ({len(traced)} traced, {len(extrap)} extrapolated) ===")
    print(f"  file:///{OUT.replace(os.sep, '/')}/skeleton-preview.html")
    print(f"  file:///{OUT.replace(os.sep, '/')}/master-canvas.svg")
