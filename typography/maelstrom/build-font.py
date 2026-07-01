#!/usr/bin/env python3
"""
build-font.py — Generate BonfireMaelstrom-Regular.otf from skeleton-defs.py

Pipeline: skeleton-defs.py → T2CharStringPen (polygons) / pathops (strokes) → FontBuilder → OTF
Stack: fonttools 4.62 + skia-pathops 0.9.2
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from pathops import Path as PPath, LineCap, LineJoin, OpBuilder, PathOp

spec = import_module("skeleton-defs")
GLYPHS = spec.GLYPHS
SW = spec.SW
H = spec.H

# --- Constants ---
UPM = 1000
SCALE = UPM / H  # 10
FONT_FAMILY = "Bonfire Maelstrom"
FONT_STYLE = "Regular"
PS_NAME = "BonfireMaelstrom-Regular"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def expand_center_strokes(gdef):
    """Expand center_strokes into polygon contours via pathops stroke + union."""
    sw_scaled = SW * SCALE
    paths = []
    for stroke in gdef['center_strokes']:
        p = PPath()
        pts = [(x * SCALE, y * SCALE) for x, y in stroke]
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        p.stroke(sw_scaled, LineCap.BUTT_CAP, LineJoin.MITER_JOIN, 4.0)
        paths.append(p)

    if len(paths) == 1:
        return paths[0]

    builder = OpBuilder(fix_winding=True)
    for p in paths:
        builder.add(p, PathOp.UNION)
    return builder.resolve()


def draw_polygon_glyph(pen, gdef):
    """Draw outer + holes from polygon definition into T2CharStringPen."""
    # Outer contour (CCW in Y-up = filled in CFF)
    outer = [(x * SCALE, y * SCALE) for x, y in gdef['outer']]
    pen.moveTo(outer[0])
    for pt in outer[1:]:
        pen.lineTo(pt)
    pen.closePath()

    # Hole contours (reverse to CW for CFF)
    for hole in gdef.get('holes', []):
        hole_pts = [(x * SCALE, y * SCALE) for x, y in reversed(hole)]
        pen.moveTo(hole_pts[0])
        for pt in hole_pts[1:]:
            pen.lineTo(pt)
        pen.closePath()


def draw_pathops_contours(pen, pp):
    """Draw pathops Path contours into T2CharStringPen."""
    for contour in pp.contours:
        started = False
        for segment in contour:
            verb = segment[0]
            points = segment[1]
            if not started:
                pen.moveTo(points[0])
                started = True
            elif len(points) == 1:
                pen.lineTo(points[0])
            elif len(points) == 3:
                pen.curveTo(*points)
        pen.closePath()


def build_font():
    # Glyph order: .notdef, space, then A-Z, 0-9
    alpha = sorted([c for c in GLYPHS if c.isalpha()])
    digits = sorted([c for c in GLYPHS if c.isdigit()])
    glyph_names = ['.notdef', 'space'] + alpha + digits
    glyph_order = glyph_names[:]

    # Unicode character map
    cmap = {0x0020: 'space'}
    for c in alpha:
        cmap[ord(c)] = c
    for c in digits:
        cmap[ord(c)] = c

    # Build charstrings
    charstrings = {}

    # .notdef: 500-wide rectangle with counter
    pen = T2CharStringPen(500, None)
    pen.moveTo((50, 0))
    pen.lineTo((50, 800))
    pen.lineTo((450, 800))
    pen.lineTo((450, 0))
    pen.closePath()
    pen.moveTo((100, 50))
    pen.lineTo((400, 50))
    pen.lineTo((400, 750))
    pen.lineTo((100, 750))
    pen.closePath()
    charstrings['.notdef'] = pen.getCharString()

    # space: no contours
    pen = T2CharStringPen(250, None)
    charstrings['space'] = pen.getCharString()

    # All glyph characters
    for name in alpha + digits:
        gdef = GLYPHS[name]
        adv_width = int(round(gdef['width'] * SCALE))

        if 'center_strokes' in gdef:
            # Stroke-based: expand via pathops
            pp = expand_center_strokes(gdef)
            pen = T2CharStringPen(adv_width, None)
            draw_pathops_contours(pen, pp)
            charstrings[name] = pen.getCharString()
        else:
            # Polygon-based: direct drawing
            pen = T2CharStringPen(adv_width, None)
            draw_polygon_glyph(pen, gdef)
            charstrings[name] = pen.getCharString()

    # Build font
    fb = FontBuilder(UPM, isTTF=False)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)

    fb.setupCFF(
        psName=PS_NAME,
        fontInfo={
            'FullName': 'Bonfire Maelstrom Regular',
            'FamilyName': FONT_FAMILY,
            'Weight': 'Black',
            'ItalicAngle': 0,
        },
        charStringsDict=charstrings,
        privateDict={},
    )

    # Horizontal metrics: (advanceWidth, LSB)
    metrics = {'.notdef': (500, 50), 'space': (250, 0)}
    for name in alpha + digits:
        adv = int(round(GLYPHS[name]['width'] * SCALE))
        metrics[name] = (adv, 0)
    fb.setupHorizontalMetrics(metrics)

    fb.setupHorizontalHeader(ascent=UPM, descent=0)

    fb.setupNameTable({
        'familyName': FONT_FAMILY,
        'styleName': FONT_STYLE,
    })

    fb.setupOS2(
        sTypoAscender=UPM,
        sTypoDescender=0,
        sTypoLineGap=200,
        usWinAscent=1100,
        usWinDescent=0,
        sCapHeight=UPM,
        sxHeight=0,
        usWeightClass=900,
        usWidthClass=3,
        fsType=0,
        achVendID='BNFR',
    )

    fb.setupPost()
    fb.setupHead(unitsPerEm=UPM)
    fb.setupDummyDSIG()

    # Kerning
    kern_fea = """
feature kern {
    pos A V -80;  pos V A -80;
    pos A W -60;  pos W A -60;
    pos A Y -80;  pos Y A -80;
    pos A T -60;  pos T A -60;
    pos T O -40;
    pos L T -60;  pos L V -60;
    pos L W -40;  pos L Y -60;
    pos F A -40;  pos P A -40;
} kern;
"""
    fb.addOpenTypeFeatures(kern_fea)

    out_path = os.path.join(OUT_DIR, 'BonfireMaelstrom-Regular.otf')
    fb.save(out_path)
    print(f"Font saved: {out_path}")
    print(f"  Glyphs: {len(glyph_order)}")
    print(f"  UPM: {UPM}")
    print(f"  Family: {FONT_FAMILY}")

    # Validate
    from fontTools.ttLib import TTFont
    font = TTFont(out_path)
    required = ['head', 'hhea', 'maxp', 'OS/2', 'name', 'cmap', 'post', 'CFF ']
    missing = [t for t in required if t not in font]
    if missing:
        print(f"  WARNING: Missing tables: {missing}")
    else:
        print(f"  Validation: All {len(required)} required tables present")


if __name__ == '__main__':
    build_font()
