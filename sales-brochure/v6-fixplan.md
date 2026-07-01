# V6 Fix Plan

## FIX 1: P15 JC McLaren Image Stretched
**Problem:** john-mclaren-cropped.jpg is 3141x2982 (~1:1 square) placed at w=2.8" h=1.3" (2.15:1) — horizontally stretched.
**Fix:** Pre-crop McLaren image to 2.15:1 aspect ratio (landscape band showing JC + car). Save as john-mclaren-p15.jpg.

## FIX 2: P17 JC Image Stretched + Wrong Photo
**Problem:** Same McLaren crop forced into w=2.6" h=1.3" (2:1). User wants the "john with student" image (F:\IMG_3934.jpg) instead.
**Fix:** Use john-student-lambo-redrock.jpg (6000x4000, landscape). Pre-crop to 2:1 aspect for the P17 dark bar. Save as john-student-p17.jpg.

## FIX 3: P7 HBFS Content Rewrite
**Problem:** Current HBFS text is generic tech specs. Should contrast local AI (Bonfire) vs cloud AI (OpenClaw):
- HARDER: Local AI has access to your software AND hardware (GPU, disk, peripherals) — cloud AI is sandboxed
- BETTER: Access to local files, context, and history — cloud AI only sees what you paste in the chat window
- FASTER: Verbalize instructions to your local machine-based AI — no upload/download, no latency
- STRONGER: Private, secure, no cloud SaaS trust issues — your data never leaves your machine

## Execution Order
1. Pre-crop both JC images to correct aspect ratios
2. Update P7 HBFS text in build script
3. Update P15 to use john-mclaren-p15.jpg
4. Update P17 to use john-student-p17.jpg
5. Rebuild, screenshot, verify
