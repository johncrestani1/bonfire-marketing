# Fix Plan 39RJ — v6.7 JC Sections

## FIX 1: S2 "Meet John Crestani" — Head Cut Off
**Problem:** book-cover-p2.jpg (2550x1275, cropped from Book-Cover-Photo.png) cuts off John's head at top.
**Fix:** Re-crop from F:\Book-Cover-Photo.png with more headroom — shift crop window UP to include full head. Keep 2:1 aspect ratio (container is 2.8"x1.4" = 2:1). Save as book-cover-p2.jpg.

## FIX 2: S2 — Too Much Whitespace
**Problem:** 1.17" gap between author bio bottom (Y=5.38") and quote start (Y=6.30"). Dark box is 3.6" tall but content doesn't fill it.
**Fix:** Tighten layout:
- Move quote text closer to bio (reduce jc_note_y+1.55 to ~jc_note_y+1.2)
- Reduce dark box height from 3.6" to ~3.1"
- OR make book cover image taller and shift all text up

## FIX 3: S2 — Copy Text Should Be White
**Problem:** Origin story text uses LGOLD (#D0B871) — hard to read on dark background.
**Fix:** Change all body text in the dark "Meet John Crestani" section from LGOLD to WHITE (RGBColor(0xFF,0xFF,0xFF)). Keep "MEET JOHN CRESTANI" heading in GOLD.

## FIX 4: S2 — Add White Signature
**Problem:** No signature on S2 currently.
**Fix:** Create jc-signature-white.png (recolor signature to white with transparent BG). Place below the origin story text, right-aligned.

## FIX 5: S15 JC Section — White Copy + White Signature
**Problem:** "Schedule a call today" section uses GOLD/LGOLD text, no signature.
**Fix:**
- Change body text to WHITE (keep heading in GOLD or also WHITE per user preference)
- Add white signature below the "No recurring fees" text

## FIX 6: S17 "A Note From John Crestani" — White Copy + White Signature
**Problem:** Personal statement uses LGOLD text, signature is gold PNG.
**Fix:**
- Change body text from LGOLD to WHITE
- Replace jc-signature-gold.png with jc-signature-white.png
- Keep "A NOTE FROM JOHN CRESTANI" heading in GOLD

## Execution Order
1. Re-crop book-cover-p2.jpg (more headroom)
2. Create jc-signature-white.png from source signature
3. Update S2: white text, tighter layout, add white signature
4. Update S15: white text, add white signature
5. Update S17: white text, white signature
6. Rebuild, PDF, verify
