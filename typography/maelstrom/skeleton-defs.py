"""
MAELSTROM ALPHABET v6.8 — BRUSH-WEIGHT MASTER VECTORS
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
# v6.8: SW=28. Horns 28u wide. Shallow V-notch at y=88 (4u floor).
# Solid midsection y=88→55. Leg separation gap y=55→0 (triangular void).
# Three-gap system: V-notch / solid mid / leg separation.
GLYPHS['M'] = {
    'width': 90,
    'outer': [
        (0, 0),            # left foot outer-left
        (0, H),            # top-left horn outer
        (SW, H),           # left horn inner-top → V wall starts
        (43, 88),          # V-floor left (shallow notch)
        (47, 88),          # V-floor right (4u floor)
        (90 - SW, H),      # right horn inner-top
        (90, H),           # top-right horn outer
        (90, 0),           # right foot outer-right
    ],
    'holes': [
        # Leg separation: triangular gap between the two feet
        # Converges at y=55 (top of separation), widens to baseline
        [(40, 55), (50, 55), (90 - SW, 0), (SW, 0)],
    ],
}

# --- A ---  [TRACED from MAELSTROM reference]
# v6.8: Tightened base gap from 54u to 30u. Tiny counter (6u×8u).
# Solid triangle form — thick brush-stroke legs, massive crossbar zone.
# Crossbar at y=30. Ink density target ~65% (ref=67%).
a_w = 90
GLYPHS['A'] = {
    'width': a_w,
    'outer': [
        (0, 0),            # bottom-left
        (35, H),           # flat top left
        (55, H),           # flat top right (20u flat apex)
        (a_w, 0),          # bottom-right
        (60, 0),           # inner-right at base (tight gap)
        (52, 30),          # inner-right at crossbar
        (38, 30),          # inner-left at crossbar
        (30, 0),           # inner-left at base (tight gap)
    ],
    'holes': [
        [(42, 42), (48, 42), (45, 50)],  # tiny counter nick above crossbar
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
# v6.8: SW=28, stroke-based. At SW=28: stem 0-28, bowl wall thick,
# counter ~3u (tiny carved notch). Leg 28u wide. Very solid.
r_w = 60
GLYPHS['R'] = {
    'width': r_w,
    'center_strokes': [
        [(SW/2, 0), (SW/2, H)],                                      # spine
        [(SW/2, H), (45, H), (45, H/2), (SW/2, H/2)],               # bowl
        [(SW/2, H/2), (43, 0)],                                      # steep leg (3:2)
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
# v6.8: Width 55 → 65. SW=28 expands chevrons to ~x=64.
# Spine 28u. Chunky chevron zigzag.
b_w = 65
GLYPHS['B'] = {
    'width': b_w,
    'center_strokes': [
        [(SW/2, 0), (SW/2, H)],                                              # spine
        [(SW/2, H), (50, 75), (SW/2, 50), (50, 25), (SW/2, 0)],             # chevron zigzag
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
