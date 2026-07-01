# Font Fix Plan — 3 Issues Found, Each Needs Fix (3IFEN)

## Executive Summary

Visual feedback + quantitative analysis of M, A, R reveal three systemic problems:

| Issue | Root Cause | Measured Delta |
|-------|-----------|----------------|
| **1. Strokes too thin** | SW=20 vs reference ~28-30 | Ref stems = 29u (M), 33u (A) |
| **2. M wrong silhouette** | Missing leg separation gap | Ref void from legs = 48.7%, ours = 2.1% |
| **3. A too hollow** | Base gap 57% of width; counter too large | Ref density 67%, ours 47% |

The user's 3-principle feedback maps directly:
1. **Foundation First** → Fix structural geometry (M legs, A counter)
2. **Brush Thinking** → Increase SW from 20 to 28 (one thick brush stroke)
3. **Build by Negative Space** → Carve small counters from solid blocks, don't assemble thin strokes

---

## Issue 1: Global Stroke Width Too Thin (SW=20 → 28)

### Evidence
| Glyph | Feature | Ref Width (font units) | Current SW | Delta |
|-------|---------|----------------------|------------|-------|
| M | Vertical stem | 29u (49.7% of H) | 20 | +9 |
| A | Diagonal stroke | 33u (34.6% of W) | ~23 (vertex-defined) | +10 |
| T | Stem (visual est.) | ~29u | 20 | +9 |
| L | Stem (visual est.) | ~28u | 20 | +8 |
| E | Spine (visual est.) | ~28u | 20 | +8 |

**Median reference stroke: ~29 units. Recommended SW = 28.**

### Impact on Each Glyph Type

**Stroke-based (S, R, B)** — automatic improvement, strokes expand from 20u to 28u wide.

**Polygon-based** — requires vertex coordinate updates:

| Glyph | SW-dependent vertices | Changes needed |
|-------|----------------------|----------------|
| M | Horn edges (SW, H), (90-SW, H) | Horns become 28u wide |
| E | Spine edge x=SW, arm junctions | Arms need extending |
| L | Spine inner x=SW, base top y=SW | Minor shift |
| T | Stem edges (_stem_l, _stem_r) | Auto-recalculates |
| O | Counter insets all use SW | Walls thicken, counter shrinks |
| All derived | Most reference SW | Cascade update |

### E Arm Length Issue at SW=28
With spine at x=28 (was x=20), current arm right edges:
- Top arm right = 30 → only 2u past spine! (was 10u past)
- Mid arm right = 38 → only 10u past spine (was 18u past)
- Bottom arm right = 54 → 26u past spine (was 34u past)

**Fix**: Scale arm extensions proportionally. The arm EXTENSION (past spine) matters, not absolute position:
- Top arm: 28 + 10 = 38 (was 30, ext=10)
- Mid arm: 28 + 18 = 46 (was 38, ext=18)
- Bottom arm: 28 + 34 = 62 (was 54, ext=34) → but E width is only 54!

**E width must increase** from 54 to ~62, OR arm proportions must compress.

Option A: Increase E width to 62 (keeps arm extensions identical)
Option B: Keep E width at 54, compress arms: top=36, mid=44, bot=54

---

## Issue 2: M Missing Leg Separation (Solid Block → 3-Gap System)

### Evidence
The reference M has THREE distinct negative-space regions:

| Gap | Font Y Range | Void % | Current Model |
|-----|-------------|--------|---------------|
| V-notch (between peaks) | y=91-97 | 8.7% | MODELED (y=88, 4u floor) |
| Solid midsection | y=58-90 | 0% (solid) | MODELED (solid block) |
| **Leg separation** | **y=17-56** | **48.7%** | **MISSING** |

Our current M is a solid block below the V-notch. The reference M has splayed inner legs creating a large triangular gap in the lower half.

### Proposed Fix
Add inner diagonal strokes that diverge from center below the solid midsection:

```
Current M silhouette:          Fixed M silhouette:
┌──┐  ┌──┐                    ┌──┐  ┌──┐
│  └──┘  │  ← V-notch         │  └──┘  │  ← V-notch (same)
│        │  ← solid block      │        │  ← solid midsection
│        │                     │\      /│  ← legs begin to split
│        │                     │ \    / │  ← gap widens
│        │                     │  \  /  │  ← gap continues
└────────┘                     └──┘└──┘    ← separate feet
```

Key geometry for the leg separation:
- Separation starts at approximately y=55 (center begins to open)
- Gap widens linearly toward baseline
- At baseline: two feet, each ~28u wide (with SW=28), gap ~34u between them
- M total width = 90, so: left foot 0-28, gap 28-62, right foot 62-90
- Inner diagonal from (28, 55) → (28, 0) on left, (62, 55) → (62, 0) on right
  - Actually, the inner diagonals should converge at the top of the separation zone
  - Left inner: from (~38, 55) → (28, 0)
  - Right inner: from (~52, 55) → (62, 0)

### Revised M Vertices (SW=28)
```python
GLYPHS['M'] = {
    'width': 90,
    'outer': [
        (0, 0),            # left foot outer-left
        (0, H),            # top-left horn outer
        (SW, H),           # left horn inner → V wall starts
        (43, 88),          # V-floor left
        (47, 88),          # V-floor right
        (90-SW, H),        # right horn inner
        (90, H),           # right horn outer
        (90, 0),           # right foot outer-right
        (90-SW, 0),        # right foot inner-right
        (90-SW, 55),       # right leg separation start (inner)
        (SW, 55),          # left leg separation start (inner)
        (SW, 0),           # left foot inner-right
    ],
    'holes': [
        # Leg separation gap (triangular void in lower half)
        [(38, 55), (52, 55), (62, 0), (28, 0)],
    ],
}
```

This creates:
- Two 28u-wide horns at top with V-notch between
- Solid midsection from y=88 down to y=55
- Two 28u-wide legs from y=55 down to baseline
- Triangular gap between legs from y=55 to y=0

---

## Issue 3: A Too Hollow (47% → 67% Ink Density)

### Evidence
| Metric | Reference | Current | Target |
|--------|-----------|---------|--------|
| Ink density | 67.0% | 47.3% | 65-70% |
| Base gap (inner) | ~26% of width | 57% of width | ~28% |
| Crossbar thickness | 64.5% of H | ~12u (12%) | ~40u (40%) |
| Counter (triangle hole) | 5.1% of void | large triangle | tiny nick |
| Right stroke fill | 86.0% | 38.2% | ~80% |

The reference A is nearly a solid triangle with:
- Very thick legs (~33u each at mid-height)
- A massive crossbar zone that fills most of the lower interior
- A tiny counter (triangle hole) near the apex, only 5% of the negative space

### Current A Problems
1. **Base too wide**: Inner edges at (18,0) and (72,0) create 54u gap = 57% of 95u width
2. **Crossbar too thin/low**: At y=30 with only ~12u vertical extent
3. **Counter too large**: Triangle hole dominates the interior
4. **Legs diverge too much**: The splay angle is too steep

### Proposed Fix
Fundamentally redesign A as a SOLID TRIANGLE with a tiny carved-out counter:

```python
# A — solid triangular block with tiny counter carved out
a_w = 90  # slightly narrower (was 95)
GLYPHS['A'] = {
    'width': a_w,
    'outer': [
        (0, 0),                # bottom-left
        (35, H),               # flat top left
        (55, H),               # flat top right (20u flat apex)
        (a_w, 0),              # bottom-right
        (62, 0),               # inner-right at base (tighter)
        (55, 30),              # inner-right at crossbar
        (35, 30),              # inner-left at crossbar
        (28, 0),               # inner-left at base (tighter)
    ],
    'holes': [
        [(40, 45), (50, 45), (45, 55)],  # tiny counter (10u wide, 10u tall)
    ],
}
```

Key changes:
- Base gap: 62-28 = 34u (was 54u) → 38% of width (closer to ref 26%)
- Crossbar at y=30 (keeping low per user spec)
- Counter: tiny 10×10u triangle
- Legs are ~28u thick at base (matching SW)
- Ink density should be ~65%

### Alternative: Even more aggressive (solid trapezoid)
If the counter should be even smaller, we could make it just a 5u nick:
```python
'holes': [[(43, 42), (47, 42), (45, 47)]],  # 4u wide, 5u tall nick
```

---

## Cascade Updates Required

### Derived Glyphs (SW=28)
All glyphs that reference SW in their vertex definitions need updating:

| Glyph | Derivation | Key Change |
|-------|-----------|------------|
| C | O without right wall | Wall thickness 20→28 |
| D | Same as O | Wall thickness 20→28 |
| F | E without bottom arm | Spine 20→28, arm extensions |
| G | C with spur | Wall thickness + spur position |
| H | Two stems + crossbar | Stem 20→28 |
| J | Hook | Thickness 20→28 |
| K | Spine + diagonals | Spine 20→28, diagonal adjust |
| L | Stem + base | Stem 20→28 |
| N | Two stems + diagonal | Stem 20→28 |
| P | From R bowl | Bowl proportions at SW=28 |
| Q | Same as O | Wall thickness 20→28 |
| T | Crossbar + stem | Stem 20→28 (auto-calc) |
| U | Two stems + bottom | Stem 20→28 |
| V | Inverted A | Similar adjustments to A |
| W | Double V | Similar adjustments |
| X | Crossing diagonals | Diagonal thickness 20→28 |
| Y | Upper V + stem | Stem 20→28 |
| Z | Bars + diagonal | Bar 20→28 |

### Stroke-Based Glyphs (auto-thickened)
| Glyph | Effect of SW=28 |
|-------|----------------|
| S | Zigzag strokes widen from 20→28u. Fill increases ~40%. Good. |
| R | Stem 28u, bowl walls thicken, counter shrinks to ~7u. Good. |
| B | Spine 28u, chevron strokes widen. Good. |

---

## Summary of Changes

| Priority | Glyph | Change | Type |
|----------|-------|--------|------|
| **P0** | Global | SW: 20 → 28 | Constant |
| **P0** | M | Add leg separation hole (y=0-55) | Structural |
| **P0** | A | Tighten base gap, shrink counter, thicken legs | Structural |
| **P1** | E | Extend arms to compensate for wider spine | Proportional |
| **P1** | F | Update arms (derived from E) | Proportional |
| **P1** | All derived | Update for SW=28 | Mechanical |
| **P2** | R | Verify proportions at SW=28 | Validation |
| **P2** | S, B | Verify appearance at SW=28 | Validation |

---

## User Decisions (Resolved)

1. **SW value**: **28** (recommended) -- APPROVED
2. **M leg separation**: **Full separation** (gap y=55 to baseline, 34u at base) -- APPROVED
3. **A counter**: **Tiny nick** (6u wide, 8u tall) -- APPROVED
4. **E width**: **62** (preserve arm extensions) -- APPROVED

---

## Implementation Results (v6.8)

All changes applied to `skeleton-defs.py` and rebuilt.

### NCC Score Comparison (sigma=20)

| Glyph | v6.7 | v6.8 | Delta | Status |
|-------|------|------|-------|--------|
| E | 94.3 | **97.7** | +3.4 | FAIL -> PASS |
| S | 94.7 | **96.4** | +1.7 | FAIL -> PASS |
| O | 94.0 | **97.0** | +3.0 | FAIL -> PASS |
| L | 97.7 | **98.6** | +0.9 | PASS |
| I | 100.0 | **99.2** | -0.8 | PASS |
| T | 93.0 | 94.6 | +1.6 | FAIL (close) |
| B | 92.9 | 93.2 | +0.3 | FAIL |
| A | 92.0 | 92.4 | +0.4 | FAIL |
| M | 87.0 | 86.7 | -0.3 | FAIL |
| R | 85.1 | 84.3 | -0.8 | FAIL |

**Result: 2/10 -> 5/10 passing.** Thicker strokes improved E, S, O to passing.

### Width Changes Summary

| Glyph | v6.7 | v6.8 | Reason |
|-------|------|------|--------|
| A | 95 | 90 | Tightened base |
| E | 54 | 62 | Wider for arm extensions |
| O | 58 | 68 | Visible counter at SW=28 |
| B | 55 | 65 | Chevron expansion room |
| I | 20 | 28 | = SW |
| F | 38 | 46 | From E |
| P | 55 | 65 | Bowl counter room |
| D | 58 | 68 | Match O |
| G | 52 | 56 | Inner opening |
| H | 52 | 62 | Counter between stems |
| K | 52 | 60 | Diagonal clearance |
| N | 52 | 58 | Proportions |
| U | 52 | 62 | Match H |
| V | 58 | 64 | Inner gap |
| X | 52 | 66 | Junction clearance |
| Y | 52 | 60 | Arm room |
