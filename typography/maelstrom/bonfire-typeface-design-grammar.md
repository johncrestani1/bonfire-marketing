# BONFIRE MAELSTROM TYPEFACE — DESIGN GRAMMAR v1

Reverse-engineered from the MAELSTROM logo reference (8 glyphs: M A E L S T R O)
and Armanen rune reference (2 glyphs: B I). Distressed/grunge texture ignored;
this document describes the underlying geometric construction only.

---

## 1. Metrics

| Parameter       | Value   | Notes                                      |
|-----------------|---------|---------------------------------------------|
| Cap height (H)  | 100     | Normalized. All caps, no lowercase.         |
| Baseline        | y = 0   | Bottom of all glyphs.                       |
| x-height        | N/A     | All-caps face, no lowercase forms.          |
| Overshoot       | 0       | No optical compensation. A has flat cap at H (no miter overshoot). |
| Descenders      | None    | All glyphs sit fully within [0, H].         |
| Unit system     | 0–100   | Y-up in definitions. Scale to any target.   |

---

## 2. Stroke Weight

| Parameter               | Value             |
|--------------------------|-------------------|
| Stroke width (SW)        | 20 units (20% H)  |
| Weight model             | Uniform           |
| Optical compensation     | None              |

All plates have the same perpendicular thickness: SW = 20.
No contrast (no thick/thin variation). No tapering.
Horizontal bars, vertical bars, and diagonal plates all share identical
perpendicular width. This is a **monoline** weight model at display scale.

---

## 3. Angular Grid

All plate edges must align to one of these angles (measured from horizontal):

| Slot   | Angle        | Rise : Run | Usage                                    |
|--------|-------------|------------|-------------------------------------------|
| H      | 0°          | 0 : 1      | Crossbars, arms, top/bottom edges         |
| V      | 90°         | 1 : 0      | Spines, stems, vertical edges             |
| D-steep| **~68°**    | **5 : 2**  | A legs, M valley walls                    |
| D-mid  | **~56°**    | **3 : 2**  | S zigzag diagonals, R leg                 |
| D-shallow | **~27°** | **1 : 2**  | B chevron arms, R bowl armature           |

Mirror images (negative slopes) are used freely. The three diagonal slots
plus the two orthogonal slots yield **5 allowed edge directions** (10 with mirrors).

### Angle rationale

Steep and shallow are complementary: 68° + 22° ≈ 90°.
The mid diagonal (~55°) bridges between them for the S zigzag and R leg,
which need a less extreme slope to fit their proportions.

### NOT allowed

- Arbitrary angles outside these 5 slots
- Curves or arcs of any kind
- Tangent-continuous transitions between plates

---

## 4. Construction Primitives (Plates)

Each glyph is assembled from **3–8 rigid polygonal plates**.
Every plate is one of these types:

| Plate type         | Shape          | Edges                          | Typical use            |
|--------------------|----------------|--------------------------------|------------------------|
| **V-bar**          | Rectangle      | 2 V + 2 H edges               | Spines, stems          |
| **H-bar**          | Rectangle      | 2 H + 2 V edges               | Crossbars, arms        |
| **Steep slab**     | Parallelogram  | 2 D-steep + 2 perpendicular    | A legs, M valley walls |
| **Mid slab**       | Parallelogram  | 2 D-mid + 2 perpendicular      | S segments, R leg      |
| **Shallow slab**   | Parallelogram  | 2 D-shallow + 2 perpendicular  | B chevrons             |
| **Apex cap**       | Trapezoid      | Mix of H + diagonal            | A top, M valley floor  |
| **Junction fill**  | Triangle/quad  | Fills miter zone at plate join | Where plates meet      |

All plates are convex polygons (no concavities).
Perpendicular width of every slab/bar = SW = 20.

### Plate-level rules

1. Every plate edge aligns to one of the 5 angular-grid slots.
2. Where two plates meet, the joint is a **sharp miter** — extend both
   plate edges until they intersect. No rounding, no chamfer, no gap.
3. A plate may be trimmed (clipped) by the baseline (y = 0) or cap line
   (y = H) to produce a clean horizontal terminal.
4. Overlapping plates of the same color merge visually (union).
5. Maximum **8 plates** per glyph. Typical is 2–5.

---

## 5. Terminal Geometry

| Terminal type      | Description                                    | Where used             |
|--------------------|------------------------------------------------|------------------------|
| **Flat baseline**  | Plate bottom edge clipped at y = 0 (horizontal)| All glyphs             |
| **Flat cap**       | Plate top edge clipped at y = H (horizontal)   | M, E, T, O, B, I      |
| **Miter apex**     | Two diagonal plates meet at a miter point      | A top                  |
| **Open butt**      | Plate ends at its natural perpendicular cut     | S segment terminals    |

No serifs. No ink traps. No swashes. No rounded terminals.

For **A**: the apex is a flat-topped trapezoid cap at y = H. Two steep-diagonal
plates meet a narrow horizontal plate at the top. The flat top is ~8 units wide.
No overshoot — the A aligns exactly to cap height like all other glyphs.

---

## 6. Corner Treatment

All corners are **sharp miters**, no exceptions.

| Joint type             | Treatment                                      |
|------------------------|-------------------------------------------------|
| Plate meets plate      | Extend edges to intersection (miter)            |
| Plate meets baseline   | Clip horizontally at y = 0                      |
| Plate meets cap line   | Clip horizontally at y = H                      |
| Plate meets counter    | Counter boundary follows plate inner edge        |

Miter limit: effectively unlimited — even very acute miters are preserved.
This produces aggressive, spiky joints (see A apex, S zigzag corners,
B chevron tips). This is a defining visual characteristic of the typeface.

---

## 7. Counter Rules

Counters are the enclosed negative spaces within a glyph.

| Rule                          | Value / Description                          |
|-------------------------------|----------------------------------------------|
| Counter shape                 | Rectangular or triangular (follows plate geometry) |
| Minimum counter dimension     | ~0.3 SW (6 units) in narrowest axis          |
| Counter wall thickness        | Always SW (20 units) perpendicular           |
| Preferred counter proportions | Width : Height ≈ 1:1 to 1:3 (tall/narrow OK)|

### Per-glyph counter inventory

| Glyph | Counter count | Counter shape     | Notes                                |
|-------|--------------|-------------------|---------------------------------------|
| M     | 0            | N/A (open valley) | Valley is open at bottom, not enclosed|
| A     | 1            | Triangle          | Small, above crossbar. Apex points up.|
| E     | 2            | Rectangle         | Between arms. Equal height preferred. |
| L     | 0            | N/A (open)        | No enclosed space.                    |
| S     | 0            | N/A (open)        | All negative space is exterior.       |
| T     | 0            | N/A (open)        | Open below crossbar.                  |
| R     | 1            | Triangle          | Inside angular bowl.                  |
| O     | 1            | Rectangle         | Central rectangle. Nearly square.     |
| B     | 2            | Triangle          | Between chevron arms and spine.       |
| I     | 0            | N/A               | Solid bar.                            |

---

## 8. Symmetry Rules

| Glyph | Symmetry type           | Axis/center                |
|-------|-------------------------|----------------------------|
| M     | Bilateral vertical      | x = width/2                |
| A     | Bilateral vertical      | x = width/2                |
| E     | None                    | —                          |
| L     | None                    | —                          |
| S     | 180° rotational (point) | Center of bounding box     |
| T     | Bilateral vertical      | x = width/2                |
| R     | None                    | —                          |
| O     | Bilateral both axes     | x = width/2, y = H/2       |
| B     | Bilateral horizontal    | y = H/2 (top/bottom mirror)|
| I     | Bilateral both axes     | x = width/2, y = H/2       |

Symmetric glyphs must be **exactly** symmetric, not approximately.
The S must have **exact** 180° point symmetry.

---

## 9. Width Classes

| Class        | Width range     | Glyphs                      |
|--------------|-----------------|------------------------------|
| Narrow       | SW–0.25H (20–25)| I                            |
| Compact      | 0.45–0.65H      | E (65), L (60), S (47)      |
| Medium       | 0.65–0.80H      | R (65), B (70), T (75), O (80) |
| Wide         | 0.85–0.90H      | A (88)                       |
| Extra-wide   | 0.90–1.00H      | M (95)                      |

Width = total advance width of the glyph bounding box (not including
inter-letter spacing). These values are initial estimates and may be
refined during glyph construction.

---

## 10. Per-Glyph Plate Assembly (SOT Glyphs)

Each glyph below is described as an ordered list of plates.
Plates are listed bottom-to-top, left-to-right. Overlap is expected
at joints; plates are unioned into a single filled outline.

### M — 4 plates

```
[1] V-bar (left leg):   x = [0, SW],  y = [0, H]
[2] V-bar (right leg):  x = [W-SW, W], y = [0, H]
[3] Steep slab (left valley wall):  from leg[1] inner-top to valley floor center-left
[4] Steep slab (right valley wall): from leg[2] inner-top to valley floor center-right
```
Valley floor: narrow horizontal gap (~14 units) at y ≈ 0.42H.
Plates 3-4 overlap plates 1-2 at the top; miter at valley floor creates
the V-point. Open at bottom (valley is not enclosed).

### A — 4 plates

```
[1] Steep slab (left leg):  from (0, 0) toward apex, clipped at baseline
[2] Steep slab (right leg): from (W, 0) toward apex, clipped at baseline
[3] Apex cap:  trapezoid or miter junction at top where legs meet
[4] H-bar (crossbar):  at y ≈ 0.33H, spanning between inner leg edges
```
Flat apex cap at y = H (~8 units wide). No miter overshoot.
The crossbar creates the single triangular counter above it.
Legs are exactly 5:2 rise:run (68°). Counter is small but visible.

### E — 4 plates

```
[1] V-bar (spine):      x = [0, SW], y = [0, H]
[2] H-bar (top arm):    y = [H-SW, H], x = [0, arm_len]
[3] H-bar (middle arm): y = [H/2 - SW/2, H/2 + SW/2], x = [0, mid_arm]
[4] H-bar (bottom arm): y = [0, SW], x = [0, arm_len]
```
Top and bottom arms equal length (~65). Middle arm shorter (~58% of full).
All meet spine at left. Two rectangular counters between arms.

### L — 2 plates

```
[1] V-bar (spine):       x = [0, SW], y = [0, H]
[2] H-bar (base arm):    y = [0, SW], x = [0, arm_len]
```
Simplest glyph. Clean right-angle joint at bottom-left.

### S — 3 plates (Sig rune / lightning bolt)

```
[1] Mid slab (upper diagonal):  from upper-right to center-left, ~55° slope
[2] H-bar (middle bridge):      horizontal segment connecting the two diagonals
[3] Mid slab (lower diagonal):  from center-right to lower-left, ~55° slope
```
180° point symmetry. The three plates form a Z-shape (backwards).
Diagonal plates use D-mid angle. Plates overlap at the two zigzag corners.
No enclosed counters — all negative space is exterior.

### T — 2 plates

```
[1] H-bar (crossbar):    y = [H-SW, H], x = [0, W]
[2] V-bar (stem):        x = [W/2 - SW/2, W/2 + SW/2], y = [0, H-SW]
```
Crossbar spans full width. Stem is centered. Clean T-joint where
stem meets underside of crossbar.

### R — 4 plates

```
[1] V-bar (spine):           x = [0, SW], y = [0, H]
[2] Shallow slab (bowl upper arm): from spine top toward bowl tip, ~27° slope
[3] Shallow slab (bowl lower arm): from bowl tip back to spine at mid-height, ~27° slope
[4] Mid slab (diagonal leg):       from spine mid-height to bottom-right, ~50° slope
```
The bowl is a **right-pointing chevron** (two shallow slabs meeting at a
tip to the right). Triangular counter inside the bowl. Leg departs from
the bowl junction and angles to the bottom-right.

### O — 4 plates

```
[1] V-bar (left wall):    x = [0, SW], y = [0, H]
[2] V-bar (right wall):   x = [W-SW, W], y = [0, H]
[3] H-bar (top wall):     y = [H-SW, H], x = [0, W]
[4] H-bar (bottom wall):  y = [0, SW], x = [0, W]
```
Pure rectangular frame. One rectangular counter.
Width should be ~0.80H for a nearly-square outer frame.
Counter aspect ratio ~(W-2SW) : (H-2SW). Target: close to 1:1.5.

### B — 5 plates (Bar rune)

```
[1] V-bar (spine):                x = [0, SW], y = [0, H]
[2] Shallow slab (upper chevron, upper arm): from spine top to tip at right
[3] Shallow slab (upper chevron, lower arm): from tip back to spine at H/2
[4] Shallow slab (lower chevron, upper arm): from spine at H/2 to tip at right
[5] Shallow slab (lower chevron, lower arm): from tip back to spine bottom
```
Two right-pointing chevrons stacked vertically, sharing the midpoint.
Upper chevron tip at y ≈ 0.75H. Lower chevron tip at y ≈ 0.25H.
Both tips at same x-coordinate. Two triangular counters inside chevrons.
Bilateral horizontal symmetry (top half mirrors bottom half about y = H/2).

### I — 1 plate

```
[1] V-bar:  x = [0, SW], y = [0, H]
```
Single vertical rectangle. Width = SW = 20.

---

## 11. Constraints Summary

| Constraint                        | Value     |
|-----------------------------------|-----------|
| Plates per glyph                  | 1–8       |
| Max polygon vertices per glyph    | 25        |
| Curves / Bezier nodes             | 0         |
| Allowed edge angles               | 5 (+ mirrors) |
| Stroke width                      | SW = 20 (uniform) |
| Min counter dimension             | 6 units   |
| Corner treatment                  | Sharp miter only |
| Terminal treatment                | Flat clip or miter |

---

## 12. Visual Character (Qualitative)

- **Heavy, aggressive, angular** — reads as industrial/military stencil
- **Runic influence** — S is the Sig rune (lightning bolt), B is the Bar rune
- **No curves anywhere** — every edge is a straight segment
- **Condensed proportions** — most glyphs narrower than tall
- **Massive stroke weight** — 20% of cap height creates dense, heavy forms
- **Minimal counters** — thick walls compress internal space; counters are
  small relative to the letter body. This produces visual tension and mass.
- **Sharp miter joints** — spiky corners at plate junctions give an
  aggressive, angular feel. No softening.

---

## Status

**APPROVED.** Grammar is authoritative. Glyph vertices recomputed to match.

---

## 13. Font Metrics

| Metric              | Value                         |
|---------------------|-------------------------------|
| UPM                 | 1000                          |
| Scale factor        | x10 (source 0-100 to 0-1000) |
| Cap height          | 1000                          |
| Ascender            | 1000                          |
| Descender           | 0                             |
| Line gap            | 200 (20% of UPM)             |
| Left side bearing   | 0 (all glyphs)               |
| Right side bearing  | 0 (all glyphs)               |
| Advance width       | glyph width x 10             |
| Weight class        | 900 (Black)                   |
| Width class         | 3 (Condensed)                 |
| Family name         | Bonfire Maelstrom             |
| Style name          | Regular                       |
| PostScript name     | BonfireMaelstrom-Regular      |
| Unicode mapping     | A-Z: U+0041-U+005A, 0-9: U+0030-U+0039 |
| Space advance       | 250 (25% UPM)                |

## 14. Kerning (15 basic pairs)

All values in font units (1000 UPM). Negative = tighter.

```
AV -80  VA -80  AW -60  WA -60  AY -80  YA -80
AT -60  TA -60  TO -40  LT -60  LV -60  LW -40
LY -60  FA -40  PA -40
```

## 15. Export Pipeline

```
skeleton-defs.py -> build-font.py -> BonfireMaelstrom-Regular.otf
                 -> generate-svgs.py -> skeletons/*.svg + skeleton-preview.html
```

Stack: Python 3.12 + fonttools 4.62 + skia-pathops 0.9.2.
Stroke-based glyphs (B, S, R) expanded via pathops at build time.
