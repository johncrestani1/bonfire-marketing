"""
BONFIRE MAELSTROM — IMMUTABLE LANDMARK GEOMETRY SPEC

These landmarks define the STRUCTURAL PROPORTIONS of each SOT glyph.
They are derived from visual analysis of the reference image, with grunge
discounted, and represent the clean underlying typeface geometry.

Coordinates: 0-100 normalized viewport, Y-up, cap height H=100, baseline=0.
All rendered dimensions assume stroke width SW=20.

The skeleton vertex coordinates in skeleton-defs.py MUST satisfy these
landmarks. NCC scores against the grunge reference are a SECONDARY check,
not a design objective.

FROZEN: Do not modify without explicit approval.
"""

SW = 20   # stroke width (uniform)
H = 100   # cap height

# ============================================================
# For each glyph:
#   width         — advance width (total horizontal extent)
#   structure     — construction method ('polygon' or 'strokes')
#   landmarks     — immutable geometric constraints
# ============================================================

LANDMARKS = {}

# ---- I ---- [Is rune]
# Simplest glyph: single vertical rectangle.
LANDMARKS['I'] = {
    'width': 20,
    'structure': 'polygon',
    'landmarks': {
        'stem': {'left': 0, 'right': SW, 'bottom': 0, 'top': H},
    },
}

# ---- L ---- [MAELSTROM ref]
# Right-angle: vertical stem + horizontal base arm.
# Base arm extends 22u past stem (1.1x SW). Condensed.
LANDMARKS['L'] = {
    'width': 42,
    'structure': 'polygon',
    'landmarks': {
        'stem': {'left': 0, 'right': SW, 'bottom': 0, 'top': H},
        'base_arm': {'left': 0, 'right': 42, 'bottom': 0, 'top': SW},
        'arm_extension': 22,   # how far arm extends past stem right edge
    },
}

# ---- E ---- [MAELSTROM ref]
# Vertical spine + 3 horizontal arms.
# Middle arm shorter than top/bottom (~64% of total width).
# Equal-height upper and lower notches.
LANDMARKS['E'] = {
    'width': 72,
    'structure': 'polygon',
    'landmarks': {
        'spine': {'left': 0, 'right': SW, 'bottom': 0, 'top': H},
        'top_arm': {'left': 0, 'right': 72, 'bottom': H - SW, 'top': H},
        'mid_arm': {'left': 0, 'right': 46, 'bottom': H/2 - SW/2, 'top': H/2 + SW/2},
        'bot_arm': {'left': 0, 'right': 72, 'bottom': 0, 'top': SW},
        'mid_arm_ratio': 0.639,    # 46/72 — proportion of mid arm to full width
        'upper_notch_height': 20,  # (H - SW) - (H/2 + SW/2) = 80 - 60 = 20
        'lower_notch_height': 20,  # (H/2 - SW/2) - SW = 40 - 20 = 20
        'notch_width': 52,         # 72 - SW = 52 (open right side)
    },
}

# ---- T ---- [MAELSTROM ref]
# Wide crossbar + centered stem.
# Crossbar overhang: 31u each side of stem (1.55x SW).
LANDMARKS['T'] = {
    'width': 82,
    'structure': 'polygon',
    'landmarks': {
        'crossbar': {'left': 0, 'right': 82, 'bottom': H - SW, 'top': H},
        'stem': {'left': 31, 'right': 51, 'bottom': 0, 'top': H - SW},
        'stem_center': 41,         # (82 - SW) / 2 + SW/2
        'crossbar_overhang': 31,   # each side beyond stem
    },
}

# ---- O ---- [MAELSTROM ref]
# Rectangular frame. 4 walls of uniform SW.
# Counter is a tall narrow rectangle.
LANDMARKS['O'] = {
    'width': 58,
    'structure': 'polygon',
    'landmarks': {
        'outer': {'left': 0, 'right': 58, 'bottom': 0, 'top': H},
        'counter': {'left': SW, 'right': 38, 'bottom': SW, 'top': H - SW},
        'counter_width': 18,       # 58 - 2*SW
        'counter_height': 60,      # H - 2*SW
        'wall_thickness': SW,
    },
}

# ---- S ---- [MAELSTROM ref, Sig rune]
# Lightning-bolt zigzag. Stroke-based (4-point centerline).
# 180-degree point symmetry about center.
# D-mid angle ~56 deg (3:2 rise:run).
LANDMARKS['S'] = {
    'width': 47,
    'structure': 'strokes',
    'landmarks': {
        'centerline_points': [
            (37, 90),   # top-right (SW/2 inset from edges)
            (10, 50),   # mid-left
            (37, 50),   # mid-right
            (10, 10),   # bottom-left
        ],
        'zigzag_angle_deg': 56,    # from horizontal
        'rise_run': (40, 27),      # 3:2 ratio
        'point_symmetry_center': (23.5, 50),
    },
}

# ---- R ---- [MAELSTROM ref]
# Spine + rectangular bowl (upper half) + diagonal leg (lower half).
# Stroke-based (centerlines expanded by SW via pathops union).
LANDMARKS['R'] = {
    'width': 82,
    'structure': 'strokes',
    'landmarks': {
        'spine': {
            'centerline_x': SW / 2,     # x=10
            'bottom': 0,
            'top': H,
        },
        'bowl': {
            'centerline_right': 62,      # outer rendered edge at 72
            'top': H,                    # y=100
            'bottom': H / 2,            # y=50
            'outer_right': 72,           # 62 + SW/2
            'inner_right': 52,           # 62 - SW/2
        },
        'counter': {
            'width': 32,                 # inner_right(52) - stem_right(20)
            'height': 20,               # approx: top_inner(90) - bottom_inner(70)
        },
        'leg': {
            'centerline_start': (10, 50),
            'centerline_end': (75, 0),
            'rise': 50,
            'run': 65,
            'angle_deg': 37.6,          # atan(50/65)
            'slope_label': '~1:1.3',    # rise:run
        },
    },
}

# ---- A ---- [MAELSTROM ref]
# Broad triangle with flat apex, low crossbar, counter hole.
# Left leg overshoots advance width by 5u (negative side bearing).
LANDMARKS['A'] = {
    'width': 95,
    'structure': 'polygon',
    'landmarks': {
        'apex_flat': {'left': 40, 'right': 55, 'y': H},    # 15u wide flat top
        'apex_width': 15,
        'left_base': -5,            # x at y=0 (overshoots left)
        'right_base': 95,           # x at y=0
        'visual_span': 100,         # right_base - left_base
        'crossbar_y': 30,           # low crossbar
        'crossbar_inner': {'left': 32, 'right': 58},
        'leg_thickness_at_base': 23,  # inner left base(18) to left base(-5) = 23
        'left_leg_slope': 2.22,     # run/rise = (40-(-5))/100 ≈ 45/100...
        # Actually: from (-5,0) to (40,100): dx=45, dy=100 → slope 0.45 (x per y)
        'counter': {
            'shape': 'triangle',
            'vertices': [(43, 42), (48, 42), (45.5, 50)],
        },
    },
}

# ---- M ---- [MAELSTROM ref]
# Two thick parallel legs with deep V-notch between them.
# Widest SOT glyph (W:H > 1.0).
LANDMARKS['M'] = {
    'width': 102,
    'structure': 'polygon',
    'landmarks': {
        'left_leg': {
            'outer_left': 0,
            'outer_right': SW,       # 20
            'bottom': 0,
            'top': H,
        },
        'right_leg': {
            'outer_left': 82,        # 102 - SW
            'outer_right': 102,
            'bottom': 0,
            'top': H,
        },
        'v_notch': {
            'floor_y': 18,           # deep V (82% from top)
            'floor_left_x': 46,
            'floor_right_x': 56,
            'floor_width': 10,
        },
        'inner_v': {
            'convergence_y': 78,     # where inner V walls would meet
            'convergence_x': 51,
        },
        'leg_spacing': 62,           # 82 - 20, between inner edges at top
        'v_depth_pct': 82,           # (H - floor_y) / H * 100
    },
}

# ---- B ---- [Bar rune chart]
# Vertical spine + 2 symmetrical rightward-pointing chevron bumps.
# Bilateral symmetry about y = H/2.
LANDMARKS['B'] = {
    'width': 55,
    'structure': 'strokes',
    'landmarks': {
        'spine': {
            'centerline_x': SW / 2,     # x=10
            'bottom': 0,
            'top': H,
        },
        'chevrons': {
            'upper_tip': (50, 75),       # rightward point of upper bump
            'lower_tip': (50, 25),       # rightward point of lower bump
            'junction_y': 50,            # where bumps meet (H/2)
            'tip_extension': 40,         # 50 - 10 (centerline x of tip - spine x)
        },
        'symmetry_axis': 50,             # y = H/2
    },
}


# ============================================================
# VALIDATION: check that skeleton-defs.py satisfies these landmarks
# ============================================================

def validate_landmarks():
    """Compare skeleton-defs.py GLYPHS against landmark constraints."""
    import importlib.util
    import os

    spec_path = os.path.join(os.path.dirname(__file__), 'skeleton-defs.py')
    spec = importlib.util.spec_from_file_location('skeleton_defs', spec_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    GLYPHS = mod.GLYPHS

    errors = []
    for ch, lm in LANDMARKS.items():
        if ch not in GLYPHS:
            errors.append(f"{ch}: MISSING from GLYPHS")
            continue

        g = GLYPHS[ch]
        # Check width
        if g['width'] != lm['width']:
            errors.append(f"{ch}: width {g['width']} != landmark {lm['width']}")

        # Check structure type
        if lm['structure'] == 'strokes' and 'center_strokes' not in g:
            errors.append(f"{ch}: landmark says strokes but GLYPHS has polygon")
        if lm['structure'] == 'polygon' and 'center_strokes' in g:
            errors.append(f"{ch}: landmark says polygon but GLYPHS has strokes")

    if errors:
        print("LANDMARK VIOLATIONS:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("ALL LANDMARKS SATISFIED")

    return len(errors) == 0


if __name__ == '__main__':
    ok = validate_landmarks()
    if ok:
        print("\nLandmark spec is consistent with skeleton-defs.py")
    else:
        print("\nFix skeleton-defs.py to match landmark spec!")
