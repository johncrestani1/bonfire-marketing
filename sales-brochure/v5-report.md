# Bonfire Terminal Brochure v5 — Audit Report & v6 Fix Plan
## Generated 2026-06-29

---

### CHAPTER TITLE AUDIT

The TOC (P3) defines three sections:
1. "The AI Revolution" — Pages 4–7
2. "The Bonfire Platform" — Pages 8–12
3. "The Bonfire Advantage" — Pages 13–18

**Current page titles (need normalization):**

| Page | Current Title | Issue |
|------|--------------|-------|
| P4 | AN INTRODUCTION TO ARTIFICIAL INTELLIGENCE | Doesn't match TOC "The AI Revolution" |
| P5 | THE COST OF WAITING | OK subtitle, but no section reference |
| P6 | AI MARKET GROWTH TRAJECTORY | OK subtitle |
| P7 | WHY OWN YOUR AI? | OK subtitle |
| P8 | WHAT BONFIRE CONNECTS | OK subtitle, belongs to Section 2 |
| P9 | THE BONFIRE PLATFORM | Matches TOC Section 2 title |
| P10 | (no main title) | Missing — needs title |
| P11 | CLOUD AI vs. OWNED AI | OK subtitle |
| P12 | THE ECONOMICS OF AI OWNERSHIP | OK subtitle |
| P13 | WHO IS BONFIRE FOR? | OK subtitle, belongs to Section 3 |
| P14 | WHAT'S UNDER THE HOOD | OK subtitle |
| P15 | CHOOSE YOUR EDITION | OK subtitle |
| P16 | WHY CHOOSE BONFIRE TERMINAL? | Doesn't match TOC "The Bonfire Advantage" |
| P17 | FREQUENTLY ASKED QUESTIONS | OK subtitle |

**Normalization plan:**
- P4 (Section 1 opener): Title → "THE AI REVOLUTION", subtitle → "An Introduction to Artificial Intelligence"
- P9 (Section 2 opener): Already correct "THE BONFIRE PLATFORM"
- P16 (Section 3 opener): Title → "THE BONFIRE ADVANTAGE", subtitle → "Why Choose Bonfire Terminal?"

---

### CRITICAL FIXES

#### FIX 1: P15 Pricing Layout Redesign
**Problem:** Current layout has $5k card as left half-column and $10k/$18k stacked on the right. User wants $5k as the BIGGEST box (full-width or dominant), with $10k and $18k as smaller boxes.
**Fix:**
- $5,000 Bonfire Terminal: Large card spanning full width or ~60% width, prominent
- $10,000 + Coaching: Half-width card (left side below main card)
- $18,000 + AIDE Certification: Half-width card (right side below main card)
- Replace circle headshot of JC with rectangular McLaren photo (same style as P17 mockup)
- Use `john-mclaren-redrock.jpg` (5712x3976, high-res)
- Photo style: rectangular, no oval frame — like the user's SL17 revised mockup

#### FIX 2: P16 "AS SEEN ON" Logo Overlap
**Problem:** 7 logos placed at h=0.4" with natural width. Several logos are very wide:
- Entrepreneur: 1.82" wide
- Inc Magazine: 1.12"
- Forbes: 1.02"
- Total width needed: ~7.4" on a 7" page = massive overlap

**Fix options:**
- Reduce to 5 logos (drop 2 widest) and use fixed width per logo (e.g., w=1.0")
- OR: Use BOTH w= AND h= to constrain all logos to uniform bounding boxes
- Best approach: Set w=Inches(0.8) for all logos, evenly spaced across 6.2" content area
- Keep: Forbes, CNBC, Bloomberg, Fox Business, Wired (5 logos, all reasonable aspect ratios)

#### FIX 3: P17 Bottom JC Section Redesign
**Problem:** Current design uses circle headshot (oval frame) with `john-student-lambo-redrock.jpg`. User wants:
- Rectangular photo (NOT circle/oval) — matching the mockup they provided
- Use the new `john-mclaren-redrock.jpg` (green McLaren, solo, high-res)
- Layout: Photo fills left ~40% of the dark bar, text on right ~60%
- Title: "A NOTE FROM JOHN CRESTANI" (gold, Orbitron)
- Body: Same personal statement text (gold italic, Inter)

**Fix:** Replace oval/circle placement with rectangular `pic()` call. Crop the McLaren image to show JC from chest up with car visible.

#### FIX 4: FAQ Content — ChatGPT → OpenClaw
**Problem:** FAQ #7 says "How is this different from ChatGPT?" — should address OpenClaw instead.
**Fix:** Replace with:
- Q: "How is Bonfire different from OpenClaw?"
- A: "Bonfire does all processing locally and can function completely offline using TinyLlama AI. It's built specifically for non-technical marketers, agency owners, and content creators — not developers."

#### FIX 5: Chapter Title Normalization
**Already described above.** Section openers must match their TOC entry:
- P4: "THE AI REVOLUTION"
- P9: "THE BONFIRE PLATFORM" (already correct)
- P16: "THE BONFIRE ADVANTAGE"

---

### SECONDARY ISSUES

| Page | Issue | Severity |
|------|-------|----------|
| P2 | Newton headshot face doesn't fill circle well (too zoomed out) | Minor |
| P3 | TOC page has excessive white space below entries | Minor |
| P5 | Agent Smith Matrix image — potential copyright concern | Medium |
| P8 | Deep Blue hero image is dark/industrial, OK but not inspiring | Minor |
| P10 | Missing main page title — needs "THE BONFIRE PLATFORM (cont.)" or similar | Medium |
| P10 | Cyberpunk Johnny Silverhand hero — very dark, hard to see detail | Minor |
| P14 | UNIVAC hero — some logos in bottom rows are very small/invisible | Minor |
| P15 | JC photo currently in circle oval at bottom-right — needs complete restyle | Critical |
| P18 | Back cover looks good, no changes needed | — |

---

### V6 BUILD PLAN (Priority Order)

1. **P15**: Redesign pricing — $5k big card, $10k/$18k half-cards, rectangular JC McLaren photo
2. **P16**: Fix "AS SEEN ON" logos — use w= constraint, reduce to 5 logos
3. **P16**: Change section title to "THE BONFIRE ADVANTAGE"
4. **P17**: Redesign bottom JC section — rectangular McLaren photo, no oval
5. **P17**: Update FAQ #7 — ChatGPT → OpenClaw differentiation
6. **P4**: Change title to "THE AI REVOLUTION" with subtitle
7. **P10**: Add page title
8. All title normalization across pages
