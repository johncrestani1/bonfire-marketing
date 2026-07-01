"""
MAELSTROM ALPHABET v6.9 — REF-FAITHFUL MASTER VECTORS
Coordinate system: 0-100 viewport (normalized)
  Origin (0,0) at bottom-left, Y points UP
  Cap height H = 100, baseline = 0
  Stroke width SW = 28 (28% of cap height, uniform)

v6.8 changes from v6.7:
  - SW: 20 → 28 (matches reference stem measurements ~29u)
  - M: Added leg separation gap (y=0–55 triangular void)
  - A: Tightened base gap (54u→30u), shrunk counter, denser form
  - E: Width 54 → 62 (arm extensions preserved with wider spine)
  - O: Width 58 → 68 (visible counter at SW=28)
  - B: Width 55 → 65 (chevron expansion room)
  - I: Width 20 → 28 (= SW)
  - All derived glyphs updated for SW=28

Design philosophy:
  1. FOUNDATION FIRST — block shapes before detail
  2. BRUSH THINKING — one thick flat-brush stroke per section (SW=28)
  3. BUILD BY NEGATIVE SPACE — carve counters from solid blocks

FROZEN: Do not modify SOT glyph vertices without explicit approval.
"""

SW = 28  # stroke width — thick flat brush
H = 100  # cap height

GLYPHS = {}

# ================================================================
# SOURCE-OF-TRUTH GLYPHS — FROZEN MASTER VECTORS
# ================================================================

# --- M ---  [TRACED from MAELSTROM reference]
# v6.9: V-notch raised to y=91 (ref V-floor). Leg gap LEFT-OF-CENTER
# at x≈0.32 (ref asymmetric). Gap narrower: 8u top → 18u bottom.
# Three-gap system: V-notch / solid mid / leg separation.
GLYPHS['M'] = {
    'width': 90,
    'outer': [
        (0, 0),            # left foot outer-left
        (0, H),            # top-left horn outer
        (SW, H),           # left horn inner-top → V wall starts
        (43, 91),          # V-floor left (ref V-floor at y=91)
        (47, 91),          # V-floor right (4u floor)
        (90 - SW, H),      # right horn inner-top
        (90, H),           # top-right horn outer
        (90, 0),           # right foot outer-right
    ],
    'holes': [
        # Leg separation: LEFT-OF-CENTER per ref (pos=0.32)
        # Ref gap: cols 40-75 of 182px span → x≈19-37 in font coords
        # Top (y=55): 8u wide centered at x≈28
        # Bottom (y=0): 18u wide centered at x≈28
        [(24, 55), (32, 55), (37, 0), (19, 0)],
    ],
}

# --- A ---  [TRACED from MAELSTROM reference]
# v6.9: Apex narrowed to 8u (ref is pointed at 6.3% of width).
# Single continuous counter from near-apex to base with crossbar pinch
# at y=30 (ref pinch = ~1px, we use 2u). Ref counter spans 99.2% of height.
a_w = 90
GLYPHS['A'] = {
    'width': a_w,
    'outer': [
        (0, 0),            # bottom-left
        (41, H),           # apex left (8u flat top)
        (49, H),           # apex right
        (a_w, 0),          # bottom-right
    ],
    'holes': [
        # Single continuous counter (hourglass shape with crossbar pinch)
        # Top: 2u near apex → widens → pinches to 2u at crossbar → widens to base
        [
            (44, 82),      # counter top left (near apex)
            (46, 82),      # counter top right
            (50, 50),      # above crossbar, widening right
            (46, 30),      # crossbar pinch right (2u gap)
            (60, 0),       # base right
            (30, 0),       # base left
            (44, 30),      # crossbar pinch left
            (40, 50),      # above crossbar, widening left
        ],
    ],
}

# --- E ---  [TRACED from MAELSTROM reference]
# v6.8: Width 54 → 62. Spine widened to SW=28.
# Arm extensions preserved: top=10u, mid=18u, bot=34u past spine.
# Progressive arms: top=38 (61%), mid=46 (74%), bot=62 (100%).
GLYPHS['E'] = {
    'width': 62,
    'outer': [
        (0, 0),
        (0, H),
        (38, H),              # top arm right (SW+10 = 38)
        (38, H - SW),         # top arm inner-right
        (SW, H - SW),         # spine inner top
        (SW, H/2 + SW/2),    # above mid arm
        (46, H/2 + SW/2),    # mid arm right (SW+18 = 46)
        (46, H/2 - SW/2),    # mid arm inner-right
        (SW, H/2 - SW/2),    # spine below mid arm
        (SW, SW),             # spine inner bottom
        (62, SW),             # bottom arm inner-right (100%)
        (62, 0),              # bottom-right
    ],
    'holes': [],
}

# --- L ---  [TRACED from MAELSTROM reference]
# v6.8: SW=28. Stem 28u wide (67% of 42u width). Chunky.
GLYPHS['L'] = {
    'width': 42,
    'outer': [
        (0, 0),
        (0, H),
        (SW, H),
        (SW, SW),
        (42, SW),
        (42, 0),
    ],
    'holes': [],
}

# --- S ---  [TRACED from MAELSTROM reference + S-ref photo]
# v6.8: SW=28, stroke-based. Auto-thickens via pathops expansion.
# Sig rune / lightning bolt. D-mid angle ~56deg.
s_w = 47
GLYPHS['S'] = {
    'width': s_w,
    'center_strokes': [
        [(s_w - SW/2, H - SW/2), (SW/2, H/2), (s_w - SW/2, H/2), (SW/2, SW/2)],
    ],
}

# --- T ---  [TRACED from MAELSTROM reference]
# v6.8: SW=28. Stem 28u centered. Crossbar 28u thick.
t_w = 82
_stem_l = (t_w - SW) / 2   # 27
_stem_r = _stem_l + SW      # 55
GLYPHS['T'] = {
    'width': t_w,
    'outer': [
        (0, H),
        (t_w, H),
        (t_w, H - SW),
        (_stem_r, H - SW),
        (_stem_r, 0),
        (_stem_l, 0),
        (_stem_l, H - SW),
        (0, H - SW),
    ],
    'holes': [],
}

# --- R ---  [TRACED from MAELSTROM reference]
# v6.9: Converted to polygon for precise counter control.
# Ref counter = 19% of bowl outer width. Leg-stem gap = 4-5px per ref.
# Bowl counter: 17u × 20u rectangular void. Leg-stem gap: 5u triangular void.
r_w = 60
GLYPHS['R'] = {
    'width': r_w,
    'outer': [
        (0, 0),            # stem base left
        (0, H),            # stem top left
        (r_w, H),          # bowl top right
        (r_w, H/2),        # bowl bottom right / leg junction
        (43, 0),           # leg bottom right (3:2 rise:run)
    ],
    'holes': [
        # Bowl counter (rectangular, 17u × 20u)
        [(SW, H/2 + 15), (r_w - 15, H/2 + 15), (r_w - 15, H - 15), (SW, H - 15)],
        # Leg-stem separation (5u gap at junction, tapers toward baseline)
        [(SW, H/2 - 5), (SW + 5, H/2 - 5), (SW, 5)],
    ],
}

# --- O ---  [TRACED from MAELSTROM reference]
# v6.8: Width 58 → 68 for visible counter at SW=28.
# Counter: 12u × 44u rectangle.
o_w = 68
GLYPHS['O'] = {
    'width': o_w,
    'outer': [
        (0, 0),
        (0, H),
        (o_w, H),
        (o_w, 0),
    ],
    'holes': [
        [(SW, SW), (SW, H - SW), (o_w - SW, H - SW), (o_w - SW, SW)],
    ],
}

# --- B ---  [TRACED from Armanen Bar rune chart]
# v6.9: Converted to polygon. Phase-corrected chevron positions per ref.
# Ref: upper tip y=48, lower tip y=3, waist y=28. Tips extend to x=70.
# Two triangular counters at concave vertices (12u depth).
b_w = 72
GLYPHS['B'] = {
    'width': b_w,
    'outer': [
        (0, 0),            # bottom-left
        (0, H),            # top-left
        (SW, H),           # spine inner top
        (70, 48),          # upper chevron tip
        (SW, 28),          # waist (concave vertex)
        (70, 3),           # lower chevron tip
        (SW, 0),           # spine inner bottom
    ],
    'holes': [
        # Upper counter (triangular void at concave vertex)
        [(SW + 1, 76), (SW + 12, 48), (SW + 1, 36)],
        # Lower counter (triangular void at concave vertex)
        [(SW + 1, 22), (SW + 12, 3), (SW + 1, 1)],
    ],
}

# --- I ---  [TRACED from Armanen Is rune chart]
# v6.8: Width = SW = 28.
GLYPHS['I'] = {
    'width': SW,
    'outer': [
        (0, 0),
        (0, H),
        (SW, H),
        (SW, 0),
    ],
    'holes': [],
}


# ================================================================
# EXTRAPOLATED GLYPHS — derived from SOT rules
# All updated for SW=28. May be revised freely.
# ================================================================

# --- C ---  (O without right wall)
c_w = 48
GLYPHS['C'] = {
    'width': c_w,
    'outer': [
        (0, 0), (0, H), (c_w, H), (c_w, H - SW),
        (SW, H - SW), (SW, SW), (c_w, SW), (c_w, 0),
    ],
    'holes': [],
}

# --- D ---  (rectangular frame = O shape)
d_w = 68
GLYPHS['D'] = {
    'width': d_w,
    'outer': [(0, 0), (0, H), (d_w, H), (d_w, 0)],
    'holes': [[(SW, SW), (SW, H - SW), (d_w - SW, H - SW), (d_w - SW, SW)]],
}

# --- F ---  (E without bottom arm — follows E v6.8 arms)
# Top arm=38, mid arm=46 (matching E progressive style).
f_w = 46
GLYPHS['F'] = {
    'width': f_w,
    'outer': [
        (0, 0), (0, H),
        (38, H), (38, H - SW),
        (SW, H - SW), (SW, H/2 + SW/2),
        (46, H/2 + SW/2), (46, H/2 - SW/2),
        (SW, H/2 - SW/2), (SW, 0),
    ],
    'holes': [],
}

# --- G ---  (C with inward spur at mid-right)
g_w = 56
_spur = 16
GLYPHS['G'] = {
    'width': g_w,
    'outer': [
        (0, 0), (0, H), (g_w, H), (g_w, H - SW),
        (SW, H - SW), (SW, SW), (g_w, SW),
        (g_w, H/2 - SW/2), (g_w - _spur, H/2 - SW/2),
        (g_w - _spur, H/2 + SW/2), (g_w, H/2 + SW/2),
        (g_w, 0),
    ],
    'holes': [],
}

# --- H ---  (two stems + crossbar)
h_w = 62
GLYPHS['H'] = {
    'width': h_w,
    'outer': [
        (0, 0), (0, H), (SW, H), (SW, H/2 + SW/2),
        (h_w - SW, H/2 + SW/2), (h_w - SW, H), (h_w, H),
        (h_w, 0), (h_w - SW, 0), (h_w - SW, H/2 - SW/2),
        (SW, H/2 - SW/2), (SW, 0),
    ],
    'holes': [],
}

# --- J ---  (descending stem with bottom-left hook)
j_w = 38
GLYPHS['J'] = {
    'width': j_w,
    'outer': [
        (0, SW), (0, 0), (j_w, 0), (j_w, H),
        (j_w - SW, H), (j_w - SW, SW), (SW, SW),
    ],
    'holes': [],
}

# --- K ---  (spine + two diagonal arms at mid-height)
k_w = 60
GLYPHS['K'] = {
    'width': k_w,
    'outer': [
        (0, 0), (0, H), (SW, H),
        (SW, H/2 + SW), (k_w - SW, H), (k_w, H),
        (SW + SW, H/2 + SW/2),
        (k_w, 0), (k_w - SW, 0),
        (SW, H/2 - SW), (SW, 0),
    ],
    'holes': [],
}

# --- N ---  (two stems + diagonal)
n_w = 58
GLYPHS['N'] = {
    'width': n_w,
    'outer': [
        (0, 0), (0, H), (SW, H),
        (n_w, SW), (n_w, 0), (n_w - SW, 0),
        (0, H - SW),
    ],
    'holes': [],
}

# --- P ---  (spine + closed rectangular bowl, no leg)
# Bowl matches R proportions. Counter ~9u × 6u at SW=28.
p_w = 65
GLYPHS['P'] = {
    'width': p_w,
    'outer': [
        (0, 0), (0, H), (p_w, H), (p_w, H/2),
        (SW, H/2), (SW, 0),
    ],
    'holes': [
        [(SW, H - SW), (p_w - SW, H - SW), (p_w - SW, H/2 + SW), (SW, H/2 + SW)],
    ],
}

# --- Q ---  (O frame, same as D)
GLYPHS['Q'] = {
    'width': 68,
    'outer': [(0, 0), (0, H), (68, H), (68, 0)],
    'holes': [[(SW, SW), (SW, H - SW), (68 - SW, H - SW), (68 - SW, SW)]],
}

# --- U ---  (two stems + bottom bar, open top)
u_w = 62
GLYPHS['U'] = {
    'width': u_w,
    'outer': [
        (0, 0), (0, H), (SW, H), (SW, SW),
        (u_w - SW, SW), (u_w - SW, H), (u_w, H), (u_w, 0),
    ],
    'holes': [],
}

# --- V ---  (inverted A, no crossbar)
v_w = 64
GLYPHS['V'] = {
    'width': v_w,
    'outer': [
        (0, H), (v_w/2, 0), (v_w, H),
        (v_w - SW, H), (v_w/2, SW * 2.5), (SW, H),
    ],
    'holes': [],
}

# --- W ---  (double V)
w_w = 82
GLYPHS['W'] = {
    'width': w_w,
    'outer': [
        (0, H), (w_w * 0.25, 0), (w_w * 0.5, H * 0.6),
        (w_w * 0.75, 0), (w_w, H),
        (w_w - SW/2, H), (w_w * 0.75, SW * 2),
        (w_w * 0.5, H * 0.6 - SW), (w_w * 0.25, SW * 2),
        (SW/2, H),
    ],
    'holes': [],
}

# --- X ---  (two crossing diagonals)
x_w = 66
GLYPHS['X'] = {
    'width': x_w,
    'outer': [
        (0, 0), (x_w/2 - SW/2, H/2 - SW/2), (0, H),
        (SW, H), (x_w/2, H/2 + SW/2),
        (x_w - SW, H), (x_w, H),
        (x_w/2 + SW/2, H/2 + SW/2), (x_w, 0),
        (x_w - SW, 0), (x_w/2, H/2 - SW/2), (SW, 0),
    ],
    'holes': [],
}

# --- Y ---  (upper V + vertical stem)
y_w = 60
GLYPHS['Y'] = {
    'width': y_w,
    'outer': [
        (0, H), (y_w/2 - SW/2, H/2), (y_w/2 - SW/2, 0),
        (y_w/2 + SW/2, 0), (y_w/2 + SW/2, H/2),
        (y_w, H), (y_w - SW, H),
        (y_w/2 + SW/2, H/2 + SW), (y_w/2 - SW/2, H/2 + SW),
        (SW, H),
    ],
    'holes': [],
}

# --- Z ---  (horizontal bars + diagonal)
z_w = 48
GLYPHS['Z'] = {
    'width': z_w,
    'outer': [
        (0, H), (z_w, H), (z_w, H - SW),
        (SW, SW), (z_w, SW), (z_w, 0),
        (0, 0), (0, SW), (z_w - SW, H - SW), (0, H - SW),
    ],
    'holes': [],
}


# ================================================================
# NUMERALS (placeholder — condensed)
# ================================================================
import copy
for digit in '0123456789':
    if digit == '0':
        GLYPHS['0'] = copy.deepcopy(GLYPHS['O'])
    elif digit == '1':
        GLYPHS['1'] = copy.deepcopy(GLYPHS['I'])
    else:
        GLYPHS[digit] = {
            'width': 48,
            'outer': [(0, 0), (0, H), (48, H), (48, 0)],
            'holes': [[(SW, SW), (SW, H-SW), (48-SW, H-SW), (48-SW, SW)]],
        }
