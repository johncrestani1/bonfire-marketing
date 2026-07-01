#!/usr/bin/env python3
"""
v66-score.py — Honest scoring at sigma=20 for Bonfire Maelstrom v6.6

Methodology:
  - ref_threshold=55%, gen_threshold=25%
  - Denoise ref: Gaussian sigma=3 + re-threshold at 40%
  - Trim to content, scale to height 200 preserving aspect ratio
  - Centroid-align on shared canvas
  - Structural Gaussian blur sigma=20
  - NCC >= 95% to pass
  - B crop fixed to exclude chart cell border
"""

import os, subprocess, json, numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(ROOT)
IM = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
REF_IMG = os.path.join(PROJECT, "refs", "maelstrom-font-reference-sot.JPG")
RUNES_IMG = os.path.join(PROJECT, "refs", "Armanen_Runes.JPG")
SVG_DIR = os.path.join(PROJECT, "skeletons")
OUT_DIR = os.path.join(ROOT, "v66")

TARGET_H = 200
REF_THR = 55
GEN_THR = 25
DENOISE_SIGMA = 3
NCC_SIGMA = 20
PASS_THR = 95

REF_CROPS = {
    'M': (33, 15, 185, 195), 'A': (215, 15, 130, 195),
    'E': (342, 15, 95, 195), 'L': (428, 20, 75, 190),
    'S': (500, 15, 100, 195), 'T': (595, 15, 100, 195),
    'R': (698, 20, 105, 190), 'O': (798, 20, 115, 190),
}
RUNE_CROPS = {
    'B': (508, 8, 88, 72),   # v6.6: width 100→88 to exclude chart cell border
    'I': (275, 258, 70, 68),
}
SOT = ['M', 'A', 'E', 'L', 'S', 'T', 'R', 'O', 'B', 'I']


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if r.returncode != 0:
        print(f"  WARN: {r.stderr.strip()[:120]}")
    return r.stdout.strip()


def place(c, a, ox, oy):
    h, w = a.shape
    y0, x0 = max(0, oy), max(0, ox)
    y1, x1 = min(c.shape[0], oy+h), min(c.shape[1], ox+w)
    ay0, ax0 = max(0, -oy), max(0, -ox)
    if y1 > y0 and x1 > x0:
        c[y0:y1, x0:x1] = a[ay0:ay0+(y1-y0), ax0:ax0+(x1-x0)]


def crop_all():
    os.makedirs(OUT_DIR, exist_ok=True)
    for ch, (x, y, w, h) in REF_CROPS.items():
        out = os.path.join(OUT_DIR, f"ref-{ch}.png")
        run(f'"{IM}" "{REF_IMG}" -crop {w}x{h}+{x}+{y} +repage '
            f'-colorspace Gray -threshold {REF_THR}% -resize x{TARGET_H} "{out}"')
    for ch, (x, y, w, h) in RUNE_CROPS.items():
        out = os.path.join(OUT_DIR, f"ref-{ch}.png")
        run(f'"{IM}" "{RUNES_IMG}" -crop {w}x{h}+{x}+{y} +repage '
            f'-colorspace Gray -threshold {REF_THR}% -negate -resize x{TARGET_H} "{out}"')
    for ch in SOT:
        svg = os.path.join(SVG_DIR, f"{ch}.svg")
        out = os.path.join(OUT_DIR, f"gen-{ch}.png")
        if os.path.exists(svg):
            run(f'"{IM}" -background black -density 300 "{svg}" '
                f'-flatten -colorspace Gray -threshold {GEN_THR}% -resize x{TARGET_H} "{out}"')


def score(ch):
    rp = os.path.join(OUT_DIR, f"ref-{ch}.png")
    gp = os.path.join(OUT_DIR, f"gen-{ch}.png")
    if not os.path.exists(rp) or not os.path.exists(gp):
        return 0, {}

    ref = np.array(Image.open(rp).convert('L'), dtype=float) / 255.0
    gen = np.array(Image.open(gp).convert('L'), dtype=float) / 255.0

    ref_d = (gaussian_filter(ref, sigma=DENOISE_SIGMA) > 0.4).astype(float)
    gen_b = (gen > 0.5).astype(float)

    def trim(a):
        ys, xs = np.where(a > 0.5)
        if len(ys) == 0: return a, a.shape
        c = a[ys.min():ys.max()+1, xs.min():xs.max()+1]
        return c, c.shape

    rt, (rh, rw) = trim(ref_d)
    gt, (gh, gw) = trim(gen_b)

    th = TARGET_H
    rnw, gnw = max(1, round(rw*th/rh)), max(1, round(gw*th/gh))

    rr = np.array(Image.fromarray((rt*255).astype(np.uint8)).resize((rnw, th), Image.LANCZOS), dtype=float)/255.0
    gr = np.array(Image.fromarray((gt*255).astype(np.uint8)).resize((gnw, th), Image.LANCZOS), dtype=float)/255.0

    ry, rx = np.where(rr > 0.5)
    gy, gx = np.where(gr > 0.5)
    if len(ry) == 0 or len(gy) == 0: return 0, {}

    pad = 60
    cw = max(rnw, gnw) + pad*2
    ch_ = th + pad*2
    rc, gc = np.zeros((ch_, cw)), np.zeros((ch_, cw))
    cx, cy = cw/2, ch_/2

    place(rc, rr, int(cx-rx.mean()), int(cy-ry.mean()))
    place(gc, gr, int(cx-gx.mean()), int(cy-gy.mean()))

    # Save registered images
    Image.fromarray((rc*255).astype(np.uint8)).save(os.path.join(OUT_DIR, f"reg-ref-{ch}.png"))
    Image.fromarray((gc*255).astype(np.uint8)).save(os.path.join(OUT_DIR, f"reg-gen-{ch}.png"))

    rb = gaussian_filter(rc, sigma=NCC_SIGMA)
    gb = gaussian_filter(gc, sigma=NCC_SIGMA)

    # Save blur images
    for arr, tag in [(rb, 'ref'), (gb, 'gen')]:
        vis = (arr / max(arr.max(), 1e-10) * 255).astype(np.uint8)
        Image.fromarray(vis).save(os.path.join(OUT_DIR, f"blur-{tag}-{ch}.png"))

    rn, gn = rb - rb.mean(), gb - gb.mean()
    d = np.sqrt(np.sum(rn**2)) * np.sqrt(np.sum(gn**2))
    ncc = np.sum(rn*gn) / d if d > 1e-10 else 0

    return round(ncc*100, 1), {
        'ref_ar': round(rw/rh, 3), 'gen_ar': round(gw/gh, 3),
        'ref_reg': f"{rnw}x{th}", 'gen_reg': f"{gnw}x{th}",
    }


def main():
    print("=" * 60)
    print("BONFIRE MAELSTROM v6.6 — HONEST AUDIT (sigma=20)")
    print("=" * 60)

    print("\n[1] Cropping and rendering...")
    crop_all()

    print("\n[2] Scoring...")
    results = {}
    passing = 0
    for ch in SOT:
        pct, info = score(ch)
        ok = pct >= PASS_THR
        if ok: passing += 1
        status = 'PASS' if ok else 'FAIL'
        print(f"  {ch}: {pct:5.1f}% {status}  "
              f"ref_ar={info.get('ref_ar',0):.2f}  gen_ar={info.get('gen_ar',0):.2f}  "
              f"ref={info.get('ref_reg','')}  gen={info.get('gen_reg','')}")
        results[ch] = {'ncc': pct, 'pass': ok, **info}

    print(f"\n  RESULT: {passing}/10 at sigma={NCC_SIGMA}")
    if passing == 10:
        print("  ALL 10 SOT GLYPHS PASS")
    else:
        fails = [f"{ch}:{results[ch]['ncc']}%" for ch in SOT if not results[ch]['pass']]
        print(f"  FAILS: {', '.join(fails)}")

    with open(os.path.join(OUT_DIR, 'v66-scores.json'), 'w') as f:
        json.dump({'sigma': NCC_SIGMA, 'results': results, 'passing': passing}, f, indent=2)


if __name__ == '__main__':
    main()
