# Ebook Format Research: Maximum Distribution Reach

**Book:** "The Untold Story of Computers" by John Crestani
**Source:** PPTX-based book, 87 pages, custom fonts (Inter), full-bleed images, drop cap layouts, precise text formatting
**Current PDF:** 2.1 MB
**Date:** 2026-06-29

---

## Table of Contents

1. [Format Comparison Matrix](#format-comparison-matrix)
2. [Detailed Format Analysis](#detailed-format-analysis)
3. [Conversion Workflow Recommendations](#conversion-workflow-recommendations)
4. [Affiliate Distribution Kit](#affiliate-distribution-kit)
5. [Priority Ranking](#priority-ranking)
6. [Sources](#sources)

---

## Format Comparison Matrix

| Format | Extension | Primary Platforms | Conversion Difficulty | Free Tools Available | Est. File Size | Affiliate Value |
|--------|-----------|-------------------|----------------------|---------------------|---------------|----------------|
| EPUB 3 (Reflowable) | `.epub` | Apple Books, Google Play, Kobo, B&N, Tolino, libraries | HARD | Calibre, Pandoc, Sigil | 1.5-3 MB | HIGH |
| EPUB 3 (Fixed Layout) | `.epub` | Apple Books, Kobo, Google Play | HARD | InDesign (paid), Sigil (manual) | 2-4 MB | HIGH |
| MOBI | `.mobi` | Legacy Kindle devices (sideloading only) | MEDIUM | Calibre | 2-3 MB | NONE |
| AZW3 / KF8 | `.azw3` | Kindle devices (sideloading) | MEDIUM | Calibre | 2-3 MB | LOW |
| KPF | `.kpf` | Amazon KDP only | MEDIUM | Kindle Create (free) | 3-5 MB | MEDIUM |
| FB2 | `.fb2` | LitRes, Russian/CIS readers | MEDIUM | Calibre, FictionBook Editor | 1.5-3 MB | LOW |
| DJVU | `.djvu` | Academic archives, niche readers | LOW VALUE | DjVuLibre, pdf2djvu | 0.5-1.5 MB | NONE |
| HTML (Web Reader) | `.html` | Any browser, SEO, web embedding | MEDIUM | Pandoc, custom scripts | 2-5 MB | HIGH |
| Flipbook / HTML5 | hosted | Web browsers, embeddable | EASY | FlipHTML5, PubHTML5 (free tiers) | hosted / 5-15 MB | VERY HIGH |
| Print-Ready PDF | `.pdf` | Print-on-demand (KDP Print, IngramSpark, Lulu) | MEDIUM | Ghostscript, LibreOffice | 5-15 MB | MEDIUM |
| Standard PDF | `.pdf` | Universal (current format) | DONE | N/A | 2.1 MB | HIGH |
| Word DOCX | `.docx` | Affiliates for customization | MEDIUM | LibreOffice, manual rebuild | 3-8 MB | HIGH |
| Audiobook M4B | `.m4b` | Apple Books, Audiobookshelf, players | MEDIUM | epub2tts, Balabolka, Edge TTS | 80-200 MB | MEDIUM |
| Audiobook MP3 | `.mp3` | Universal audio players | MEDIUM | Same as M4B + FFmpeg | 120-300 MB | MEDIUM |

---

## Detailed Format Analysis

### 1. EPUB 3 (Reflowable)

**Extension:** `.epub`

**Platforms that require/prefer it:**
- Apple Books (required for submission)
- Google Play Books (required)
- Kobo (required)
- Barnes & Noble / Nook (required)
- Tolino (European readers)
- OverDrive / Libby (library lending)
- Draft2Digital, Smashwords, PublishDrive (aggregators)
- EPUB 3.3 is a W3C Recommendation as of 2025

**Conversion difficulty from PPTX/PDF: HARD**

This is the hardest conversion for this specific book. The PPTX source uses fixed positioning, full-bleed images, drop caps, and precise text-image relationships. Reflowable EPUB fundamentally reflows content to fit any screen size, which destroys fixed layouts. The content must be restructured into semantic HTML5 with CSS styling, not just "converted." Direct PDF-to-EPUB conversion via Calibre produces poor results for image-heavy, layout-dependent books -- broken lines, misplaced images, and lost formatting are common.

**Best workflow:** Extract text manually from PPTX, restructure into Markdown or HTML chapters, use Pandoc or Sigil to build the EPUB. Images must be re-inserted with proper alt text and CSS sizing. Drop caps can be preserved via CSS `::first-letter` pseudo-element styling.

**Free conversion tools:**
- **Calibre** (desktop, all platforms) -- full ebook library manager with conversion engine; handles EPUB input/output but PDF-to-EPUB results are poor for layout-heavy books
- **Sigil** (desktop, all platforms) -- dedicated EPUB editor, full control over HTML/CSS
- **Pandoc** (command-line) -- converts Markdown/HTML/DOCX to EPUB; cannot read PPTX layouts meaningfully
- **Reedsy Book Editor** (online, free) -- web-based, outputs EPUB

**What is preserved vs lost:**
- PRESERVED: Text content, images (re-embedded), chapter structure, basic styling, drop caps (via CSS)
- LOST: Exact page layout, full-bleed image positioning, precise font rendering, slide-based pagination, Inter font appearance (unless embedded and licensed for EPUB)

**File size expectation:** 1.5-3 MB (images compressed, text is lightweight HTML)

**Affiliate value:** HIGH. This is the universal ebook format. Every major non-Amazon retailer requires it. Affiliates who want to list on Apple Books, Google Play, Kobo, or library systems need EPUB.

---

### 2. EPUB 3 (Fixed Layout)

**Extension:** `.epub` (with fixed-layout metadata)

**Platforms that require/prefer it:**
- Apple Books (supported, preferred for illustrated books)
- Kobo (supported)
- Google Play Books (supported)
- B&N Nook (limited support)

**Conversion difficulty from PPTX/PDF: HARD**

Fixed-layout EPUB preserves exact positioning -- each page is an HTML document with absolute CSS coordinates for every element. This is closer to the PPTX source in spirit, but building it requires either InDesign (paid, $22.99/mo) or manual HTML/CSS coding in Sigil. There is no reliable automated tool that converts a PPTX or PDF to a high-quality fixed-layout EPUB for free.

**Free conversion tools:**
- **Sigil** -- manual HTML/CSS editing, full control but labor-intensive
- No free automated tool produces quality fixed-layout EPUB from PDF

**What is preserved vs lost:**
- PRESERVED: Exact page layout, image positioning, drop caps, text-image relationships, full-bleed appearance
- LOST: Reflowability (text cannot resize), accessibility features are limited, some e-readers do not support fixed layout well on small screens

**File size expectation:** 2-4 MB (similar to PDF since layout is preserved)

**Affiliate value:** HIGH for illustrated/visual books specifically. Less useful for text-heavy novels, but ideal for this book given its visual design.

---

### 3. MOBI (Mobipocket)

**Extension:** `.mobi`

**Platforms:**
- Legacy Kindle devices (sideloading via USB only)
- Older Kindle apps

**Conversion difficulty from PPTX/PDF: MEDIUM** (convert EPUB first, then EPUB-to-MOBI via Calibre)

**CRITICAL NOTE:** Amazon stopped accepting MOBI uploads to KDP in June 2021. Send-to-Kindle stopped delivering MOBI files in August 2022. As of March 2025, MOBI is fully deprecated. Do NOT produce this format unless targeting very old Kindle hardware that cannot be updated.

**Free conversion tools:**
- **Calibre** -- EPUB-to-MOBI in one click

**What is preserved vs lost:**
- PRESERVED: Text, basic images, chapter navigation
- LOST: Advanced CSS, drop caps, complex layouts, many EPUB 3 features

**File size expectation:** 2-3 MB

**Affiliate value:** NONE. Dead format. Do not include in distribution kit.

---

### 4. AZW3 / KF8 (Kindle Format 8)

**Extension:** `.azw3`

**Platforms:**
- Kindle devices (sideloading via USB or Send-to-Kindle)
- Kindle desktop/mobile apps

**Conversion difficulty from PPTX/PDF: MEDIUM** (EPUB-to-AZW3 via Calibre)

AZW3 supports HTML5 and CSS3, including nested tables, sidebars, and basic fixed layouts. It is a significant improvement over MOBI. However, Amazon does not accept AZW3 uploads to KDP -- they want EPUB or KPF and convert internally. AZW3 is only useful for direct sideloading to Kindle devices.

**Free conversion tools:**
- **Calibre** -- EPUB-to-AZW3 conversion

**What is preserved vs lost:**
- PRESERVED: Most CSS3 styling, images, basic drop caps, chapter structure
- LOST: Some advanced EPUB 3 features, exact layout fidelity

**File size expectation:** 2-3 MB

**Affiliate value:** LOW. Niche use case (direct sideloading). Most readers get Kindle books through the store, not sideloading.

---

### 5. KPF (Kindle Package Format)

**Extension:** `.kpf`

**Platforms:**
- Amazon KDP exclusively

**Conversion difficulty from PPTX/PDF: MEDIUM**

Kindle Create (free desktop app from Amazon) imports PDF or DOCX files and packages them as KPF. For this book, importing the PDF into Kindle Create in "print replica" or "fixed layout" mode would preserve the visual design. Kindle Create adds interactive features like text pop-ups and image zoom. KPF is then uploaded directly to KDP, which converts it to KFX for delivery to readers.

**Free conversion tools:**
- **Kindle Create** (free, Windows/Mac) -- imports PDF, DOCX, or images; outputs KPF
- This is Amazon's official and recommended tool

**What is preserved vs lost:**
- PRESERVED: Visual layout (in fixed-layout/print-replica mode), images, fonts (embedded), page design
- LOST: Reflowability, text resizing on small screens

**File size expectation:** 3-5 MB

**Affiliate value:** MEDIUM. Only useful for Amazon KDP publishing. Affiliates selling through Amazon need this workflow, but they could also just upload the EPUB to KDP.

---

### 6. FB2 (FictionBook 2)

**Extension:** `.fb2`

**Platforms:**
- LitRes (56% of Russian ebook market; 30% of sales are in FB2)
- Russian/CIS ebook stores and apps
- FBReader, CoolReader, Moon+ Reader
- Popular across Russia, Ukraine, Belarus, and Eastern European markets

**Conversion difficulty from PPTX/PDF: MEDIUM** (EPUB-to-FB2 via Calibre)

FB2 is an XML-based format with strong bibliographic metadata support (author, series, genre). It handles text and inline images but has limited layout capabilities -- no fixed positioning, no complex CSS. Drop caps and full-bleed images will not survive. The format is purely semantic/structural.

**Free conversion tools:**
- **Calibre** -- EPUB-to-FB2 conversion
- **Convertio** (online) -- EPUB/DOCX to FB2
- **FictionBook Editor** -- manual FB2 creation and editing

**What is preserved vs lost:**
- PRESERVED: Text content, inline images, chapter structure, rich metadata
- LOST: All visual layout, drop caps, full-bleed images, custom fonts, precise formatting

**File size expectation:** 1.5-3 MB

**Affiliate value:** LOW for English-language distribution. Only relevant if targeting Russian-speaking audiences. If the book were translated to Russian, FB2 would be essential for the Russian market.

---

### 7. DJVU

**Extension:** `.djvu`

**Platforms:**
- Academic/technical document archives
- Internet Archive
- DjVu browser plugins (limited)
- WinDjView, Evince (Linux)

**Conversion difficulty from PPTX/PDF: EASY** (automated tools exist)

DJVU was designed for scanned documents and achieves superior compression for image-heavy pages. However, it has very limited software support, no major ebook store accepts it, and it is not a consumer distribution format. It is primarily used for archival of scanned academic texts.

**Free conversion tools:**
- **DjVuLibre** -- includes `pdf2djvu` command-line converter
- **Any2DjVu** (online converter)

**What is preserved vs lost:**
- PRESERVED: Visual appearance (as rasterized pages), compression is excellent
- LOST: Text selectability (unless OCR layer added), reflowability, all interactivity

**File size expectation:** 0.5-1.5 MB (excellent compression, potentially smaller than PDF)

**Affiliate value:** NONE. Not a consumer format. No ebook stores accept it. Readers would need specialized software. Skip this format entirely.

---

### 8. HTML (Web-Based Reading)

**Extension:** `.html` (single file or multi-page site)

**Platforms:**
- Any web browser on any device
- Can be hosted on any web server or CDN
- Embeddable in landing pages, blogs, WordPress sites

**Conversion difficulty from PPTX/PDF: MEDIUM**

Two approaches: (a) a single self-contained HTML file with embedded images (base64) and CSS, or (b) a multi-page website with navigation. Pandoc can convert Markdown/DOCX to HTML. For maximum fidelity, the PPTX content would need manual restructuring into responsive HTML with CSS grid/flexbox for layout preservation.

**Free conversion tools:**
- **Pandoc** -- Markdown/DOCX to HTML
- **Readk.it** -- creates single-file HTML ebooks that work offline
- **Custom scripts** -- extract PPTX content, build HTML pages
- **pdf2htmlEX** -- converts PDF to HTML preserving layout (open source)

**What is preserved vs lost:**
- PRESERVED: Text, images, can recreate drop caps via CSS, responsive design possible, custom fonts via @font-face
- LOST: Exact PPTX pagination (unless using fixed-width approach)

**File size expectation:** 2-5 MB (single file with embedded images); much less if images are external

**Affiliate value:** HIGH. Massive SEO benefit -- HTML content is fully indexable by Google, driving organic traffic. Can serve as a lead magnet on landing pages. Can be gated behind email opt-in. Each chapter could be a separate page for maximum SEO surface area. Affiliates can embed chapters on their own sites.

---

### 9. Flipbook / Interactive HTML5

**Extension:** Hosted URL (or self-hosted HTML/JS/CSS bundle)

**Platforms:**
- Any modern web browser (desktop and mobile)
- Embeddable via iframe on any website
- Social media sharing via link

**Conversion difficulty from PPTX/PDF: EASY**

This is the easiest high-impact conversion. Upload the existing PDF to a flipbook platform and get an interactive page-turning experience instantly. FlipHTML5 accepts PDF, PPT, and PPTX directly and converts in seconds. The visual design, full-bleed images, and drop caps are fully preserved because the flipbook renders page images.

**Free conversion tools:**
- **FlipHTML5** (free tier: up to 500 pages, unlimited publications, basic analytics)
- **PubHTML5** (free tier available)
- **AnyFlip** (free tier: convert in 1 minute)
- **Heyzine** (free tier with watermark)
- **FlipBuilder / Flip PDF** (free version with limitations)

**What is preserved vs lost:**
- PRESERVED: Everything -- exact visual design, full-bleed images, drop caps, fonts, colors, page layout
- LOST: Text searchability (depending on platform), text selectability, accessibility, offline reading (on free tiers)

**File size expectation:** Hosted by the platform (no file download); self-hosted bundles are 5-15 MB

**Affiliate value:** VERY HIGH. This is arguably the highest-value format for affiliate distribution:
- Instant "wow factor" with page-turn animation
- Embeddable on affiliate websites and landing pages
- Shareable via link (no download required, zero friction)
- Analytics: track who reads, how far, which pages get attention
- According to Content Marketing Institute 2025 data, interactive content like flipbooks generates 2x more engagement than static formats
- Can include clickable affiliate links within pages
- Lead capture forms can be embedded before/during reading

---

### 10. Print-Ready PDF (with Crop Marks, Bleed, CMYK)

**Extension:** `.pdf`

**Platforms:**
- Amazon KDP Print
- IngramSpark (widest print distribution: 40,000+ retailers and libraries)
- Lulu
- Barnes & Noble Press
- Local print shops
- BookBaby

**Conversion difficulty from PPTX/PDF: MEDIUM**

The existing 2.1 MB PDF is an RGB screen-optimized file. Print-ready PDF requires: CMYK color space conversion, 3mm (0.125") bleed on all sides, crop/trim marks, embedded fonts, minimum 300 DPI images, and proper trim size (typically 6x9" or 5.5x8.5" for a book this size). The source PPTX would need to be re-exported at higher resolution with bleed, or the existing PDF would need post-processing.

**Free conversion tools:**
- **Ghostscript** (command-line, free) -- RGB-to-CMYK conversion via `-sProcessColorModel=DeviceCMYK`, add bleed box via `-dUseBleedBox`, prepress quality via `-dPDFSETTINGS=/prepress`
- **LibreOffice Draw** -- can open PPTX and export PDF with some print settings
- **Scribus** (free, open-source desktop publishing) -- full CMYK, bleed, and crop mark support
- **PressPDF.com** (online) -- adds bleed and crop marks to existing PDFs

**What is preserved vs lost:**
- PRESERVED: Everything from the original design (this is the same format, just production-grade)
- CONSIDERATION: Colors may shift during RGB-to-CMYK conversion; dark blues and bright greens are most affected

**File size expectation:** 5-15 MB (higher resolution images, embedded fonts, CMYK color space)

**Affiliate value:** MEDIUM. Enables print-on-demand sales through Amazon, bookstores, and libraries. Physical books have perceived higher value. However, affiliates typically prefer digital formats for instant delivery and zero inventory.

---

### 11. Word DOCX (Editable Source)

**Extension:** `.docx`

**Platforms:**
- Microsoft Word, Google Docs, LibreOffice
- Any affiliate who wants to customize/rebrand

**Conversion difficulty from PPTX/PDF: MEDIUM**

The PPTX content needs to be restructured into a DOCX document format. PPTX slides do not map cleanly to DOCX pages -- text boxes, positioned images, and slide layouts must be manually reformatted into a document flow with styles, headers, and embedded images. This is essentially a manual rebuild, though AI tools could assist with text extraction.

**Free conversion tools:**
- **LibreOffice** -- can attempt PPTX-to-DOCX conversion but results will be rough
- **Google Docs** -- import PPTX, restructure manually, export as DOCX
- **Pandoc** -- PPTX-to-DOCX conversion (extracts text and images, loses layout)

**What is preserved vs lost:**
- PRESERVED: Text content, images (re-embedded), basic structure
- LOST: Exact layout, full-bleed design, slide-based formatting, drop caps (must be recreated as Word drop caps)

**File size expectation:** 3-8 MB (embedded images inflate DOCX size)

**Affiliate value:** HIGH for a PLR/white-label strategy. If affiliates are given DOCX with private-label rights, they can:
- Add their own branding, logo, and author bio
- Insert their own affiliate links throughout the text
- Customize the call-to-action sections
- Translate into other languages
- This is the standard PLR ebook format -- PDF + DOCX is the expected deliverable in the PLR industry

---

### 12. Audiobook -- M4B (MPEG-4 Audiobook)

**Extension:** `.m4b`

**Platforms:**
- Apple Books / iTunes
- Audiobookshelf (self-hosted)
- VLC, foobar2000, and most media players
- Supports chapter markers, cover art, bookmarks

**Conversion difficulty from PPTX/PDF: MEDIUM**

Requires: (1) extract text from PPTX/PDF, (2) run through TTS engine, (3) combine audio with chapter markers into M4B container. Modern TTS voices (Microsoft Edge TTS, OpenAI TTS, ElevenLabs) produce natural-sounding narration. The 87-page book would likely be 3-5 hours of audio at standard narration speed (assuming ~250 words/page, ~150 words/minute).

**Free conversion tools:**
- **epub2tts** (open-source Python, GitHub) -- EPUB/PDF to audiobook via Edge TTS (free, cloud-based), Coqui AI TTS, or OpenAI TTS
- **epub_to_audiobook** (open-source, GitHub) -- optimized for Audiobookshelf
- **Balabolka** (Windows, free) -- text-to-speech with M4B export
- **Audiobook Maker** (online, free tier) -- PDF/EPUB to M4B/MP3, 400+ neural voices via Microsoft Edge TTS
- **TTS-Story** (GitHub) -- multi-voice TTS with M4B export, chapter markers, cover art, ACX compliance

**What is preserved vs lost:**
- PRESERVED: Text content as spoken audio, chapter structure (as M4B chapters), cover art
- LOST: All visual elements -- images, layout, drop caps, fonts, visual design

**File size expectation:**
- At 64 kbps AAC (standard for speech): ~29 MB/hour, so 3-5 hours = **85-145 MB**
- At 128 kbps AAC (higher quality): ~58 MB/hour, so 3-5 hours = **170-290 MB**

**Affiliate value:** MEDIUM. Audiobooks expand audience to commuters, gym-goers, and accessibility-focused listeners. TTS quality in 2026 is good enough for informational content. However, TTS audiobooks are perceived as lower quality than human narration. Good for lead generation and content repurposing, less suitable as a premium product.

---

### 13. Audiobook -- MP3 (Chaptered)

**Extension:** `.mp3` (one file per chapter, or single file)

**Platforms:**
- Universal -- every device and player supports MP3
- Podcast apps (if distributed as podcast episodes)
- Gumroad, SendOwl, Payhip (direct download sales)

**Conversion difficulty from PPTX/PDF: MEDIUM** (same as M4B, different output container)

Same workflow as M4B but output as MP3 instead. MP3 does not natively support chapter markers (requires ID3v2 CHAP frames, which few players honor). Better to split into one MP3 per chapter.

**Free conversion tools:**
- Same as M4B tools above
- **FFmpeg** -- convert M4B to chaptered MP3s, or concatenate TTS output

**What is preserved vs lost:**
- Same as M4B

**File size expectation:**
- At 64 kbps: ~29 MB/hour, 3-5 hours = **85-145 MB**
- At 128 kbps: ~58 MB/hour, 3-5 hours = **170-290 MB**
- MP3 files are typically 30-40% larger than equivalent M4B (AAC) at same quality

**Affiliate value:** MEDIUM. More universally compatible than M4B but less feature-rich. Good as a bonus in a distribution kit.

---

## Conversion Workflow Recommendations

### The Core Problem

The PPTX source format is the worst possible starting point for ebook conversion. PPTX stores content as positioned text boxes on slides -- there is no document flow, no paragraph structure, and no semantic markup. Every conversion requires significant manual restructuring.

### Recommended Conversion Order

```
PPTX (source)
  |
  +--> PDF (DONE - 2.1 MB, screen quality)
  |
  +--> Restructured Markdown/HTML (MANUAL WORK - this is the critical step)
  |      |
  |      +--> EPUB 3 Reflowable (Pandoc/Sigil)
  |      |      |
  |      |      +--> AZW3 (Calibre)
  |      |      +--> FB2 (Calibre)
  |      |      +--> M4B Audiobook (epub2tts)
  |      |      +--> MP3 Audiobook (epub2tts + FFmpeg)
  |      |
  |      +--> DOCX (Pandoc)
  |      +--> HTML Web Reader (Pandoc)
  |
  +--> PDF --> Flipbook (FlipHTML5, upload existing PDF)
  +--> PDF --> KPF (Kindle Create, import PDF as fixed layout)
  +--> PDF --> Print-Ready PDF (Ghostscript for CMYK + bleed)
```

### The Critical Bottleneck

The single most important step is creating a clean, structured Markdown or HTML intermediate from the PPTX content. Once that exists, Pandoc and Calibre can generate every downstream format automatically. Without it, each format requires its own manual work.

**Estimated effort for the Markdown/HTML intermediate:** 4-8 hours for 87 pages, including:
- Extracting all text from PPTX slides (can be partially automated with `python-pptx`)
- Structuring into chapters with proper headings
- Marking up drop caps, pull quotes, and special formatting
- Re-linking all images with proper sizing and alt text
- Writing CSS for drop caps, layout, and typography

---

## Affiliate Distribution Kit

### Should You Provide One?

**Yes, absolutely.** A multi-format distribution kit dramatically increases affiliate adoption and reduces their friction. In the PLR/affiliate ebook space, the standard deliverable is a ZIP containing PDF + DOCX at minimum. Going beyond that signals professionalism and makes affiliates more effective.

### Recommended Kit Contents

#### Tier 1: Essential Kit (for all affiliates)

| File | Purpose | Size |
|------|---------|------|
| `TheUntoldStoryOfComputers.pdf` | Standard reading PDF | 2.1 MB |
| `TheUntoldStoryOfComputers.epub` | Apple Books, Kobo, Google Play, B&N, libraries | ~2 MB |
| `TheUntoldStoryOfComputers.docx` | Customization and rebranding (if PLR rights granted) | ~5 MB |
| `cover-art-high-res.png` | Marketing materials, store listings | ~1 MB |
| `cover-art-3d-mockup.png` | Landing pages, social media | ~500 KB |
| `affiliate-guide.pdf` | How to use each format, where to upload, tips | ~200 KB |
| **Total ZIP** | | **~11 MB** |

#### Tier 2: Extended Kit (for serious affiliates)

Everything in Tier 1, plus:

| File | Purpose | Size |
|------|---------|------|
| `TheUntoldStoryOfComputers-kindle.kpf` | Amazon KDP upload-ready | ~4 MB |
| `TheUntoldStoryOfComputers-print.pdf` | Print-ready with CMYK, bleed, crop marks | ~10 MB |
| `TheUntoldStoryOfComputers-audiobook.m4b` | Audiobook with chapters | ~100 MB |
| `flipbook-embed-code.txt` | HTML iframe code for embedding flipbook on websites | 1 KB |
| `social-media-assets/` | Banner images, quote cards, carousel posts | ~5 MB |
| **Total ZIP** | | **~130 MB** |

#### Tier 3: Full White-Label Kit (PLR partners only)

Everything in Tier 2, plus:

| File | Purpose | Size |
|------|---------|------|
| `TheUntoldStoryOfComputers.pptx` | Original source for full customization | ~50 MB |
| `fonts/Inter-*.ttf` | Custom fonts used in the book | ~2 MB |
| `brand-guidelines.pdf` | Color codes, typography rules, logo usage | ~500 KB |
| `email-swipe-copy.docx` | Pre-written promotional emails | ~100 KB |
| `landing-page-template.html` | Ready-to-deploy landing page | ~500 KB |

### Distribution Platform for the Kit

| Platform | Cost | Affiliate Features | Recommendation |
|----------|------|-------------------|----------------|
| **Gumroad** | 10% + $0.50/sale | Built-in affiliate system, analytics, landing pages | Best for paid kit |
| **Payhip** | Free plan (5% fee) | Affiliate program built-in, coupons | Best free option |
| **SendOwl** | From $9/mo | Advanced affiliate tools, drip delivery, cart recovery | Best for scale |
| **Google Drive / Dropbox** | Free | No affiliate features, just file hosting | Best for free kit |
| **GitHub Releases** | Free | Version control, no affiliate features | Best for open distribution |

---

## Priority Ranking

### Must-Have Formats (produce these first)

| Priority | Format | Reason |
|----------|--------|--------|
| 1 | **PDF** (standard) | Already done. Universal baseline. |
| 2 | **EPUB 3** (reflowable) | Required by every non-Amazon ebook store. Opens Apple Books, Google Play, Kobo, B&N, and library markets. |
| 3 | **Flipbook** (HTML5) | Easiest conversion (upload PDF), highest engagement for web/affiliate use, embeddable, shareable, trackable. |
| 4 | **HTML** (web reader) | SEO value is massive. Each chapter as a web page drives organic traffic. Can serve as the free "sample" that drives downloads. |

### Should-Have Formats (produce after must-haves)

| Priority | Format | Reason |
|----------|--------|--------|
| 5 | **KPF** (via Kindle Create) | Amazon is the largest ebook market. Free tool, straightforward PDF import. |
| 6 | **DOCX** (editable) | Enables affiliate customization and PLR distribution. Standard in the affiliate/PLR industry. |
| 7 | **Print-Ready PDF** | Enables print-on-demand via KDP Print and IngramSpark. Physical books have higher perceived value. |
| 8 | **M4B Audiobook** | Expands to audio audience. TTS quality in 2026 is adequate for informational content. |

### Nice-to-Have Formats (only if targeting specific markets)

| Priority | Format | Reason |
|----------|--------|--------|
| 9 | **AZW3** | Only for direct Kindle sideloading. Niche use case. |
| 10 | **FB2** | Only if targeting Russian-speaking market. |
| 11 | **MP3 Audiobook** | Only if M4B compatibility is an issue for some users. |

### Skip Entirely

| Format | Reason |
|--------|--------|
| **MOBI** | Dead format. Amazon deprecated it fully as of March 2025. |
| **DJVU** | Academic archival format with no consumer distribution value. No ebook store accepts it. |

---

## Key Takeaways

1. **Flipbook is the lowest-effort, highest-impact format to add.** Upload the existing PDF to FlipHTML5 (free), get an embeddable, shareable, trackable reading experience in minutes. Every affiliate can embed it on their site immediately.

2. **EPUB is the most important format to produce** but also the hardest from a PPTX source. The structured Markdown/HTML intermediate is the critical bottleneck. Once that exists, EPUB, DOCX, HTML, and audiobook all flow from it.

3. **Do not waste time on MOBI or DJVU.** MOBI is dead. DJVU has zero consumer distribution value.

4. **The distribution kit approach is standard practice** in affiliate/PLR ebook marketing. Providing PDF + EPUB + DOCX + cover art in a ZIP file removes friction for affiliates and increases adoption.

5. **HTML web reader format has underappreciated SEO value.** Publishing chapters as web pages creates indexable content that drives organic search traffic to the book's landing page. This is a long-term traffic source that PDF and EPUB cannot provide.

6. **For this specific book (visual, image-heavy, precise layout), fixed-layout EPUB or KPF preserves the design better than reflowable EPUB.** However, reflowable EPUB reaches more platforms. Ideally, produce both: fixed-layout for visual fidelity, reflowable for maximum device compatibility.

7. **TTS audiobook quality in 2026 is good enough** for informational/historical content. Microsoft Edge TTS (free) and OpenAI TTS produce natural narration. The 87-page book would yield a 3-5 hour audiobook at approximately 85-145 MB (M4B, 64 kbps AAC).

---

## Sources

- [Best Way to Format Your eBook for all Platforms in 2026](https://www.isbnservices.com/format-your-ebook-for-all-platforms/)
- [EPUB 3.3 W3C Recommendation](https://www.w3.org/TR/epub-33/)
- [Updated W3C Recommendation: EPUB 3.3 (2025)](https://www.w3.org/news/2025/updated-w3c-recommendation-epub-3-3/)
- [eBook Distribution in 2026: A Complete Guide (Kitaboo)](https://kitaboo.com/ebook-distribution-guide/)
- [Mandatory Ebook Distribution Requirements (Lulu)](https://help.lulu.com/en/support/solutions/articles/64000255463-mandatory-ebook-distribution-requirements)
- [Ebook Formatting Requirements (ScribeCount)](https://scribecount.com/author-resource/publishing-a-book/Ebook-Formatting-Requirements-for-Self-Published-Authors)
- [MOBI, AZW, and KFX: Amazon's Kindle Format Timeline](https://changethisfile.com/blog/mobi-azw-kindle)
- [Kindle Ebook File Types: EPUB, MOBI, KFX (Vappingo)](https://www.vappingo.com/word-blog/kindle-ebook-file-types/)
- [Kindle File Formats & DRM: Complete 2026 Guide (Imelfin)](https://www.imelfin.com/kindle-file-formats-kindle-drm-explained-the-complete-2026-guide-azw3-kfx-epub.html)
- [What Happens to Your EPUB When Amazon Converts It to Kindle?](https://www.ebookpbook.com/2026/04/11/epub-to-kindle-conversion/)
- [EPUB vs Kindle AZW3: Best eBook Format in 2025 (BookQuill)](https://bookquill.com/blog/epub-vs-azw3/)
- [Kindle Create for Fixed Layout Books (Apex Authors)](https://apexauthors.com/kindle-create-features/)
- [KDP Formatting: Complete Guide 2026 (Authorio)](https://www.authorio.com/blog/kdp-formatting)
- [Complete Guide to KDP Book Formatting 2026 (iLayoutBooks)](https://ilayoutbooks.com/the-complete-guide-to-kdp-book-formatting-2026-edition/)
- [FB2 Format Guide (KaijuConverter)](https://kaijuconverter.com/guides/fb2-fictionbook-ebook-format-guide)
- [Russian Retailer LitRes Announces New .fb3 Ebook Format (Publishing Perspectives)](https://publishingperspectives.com/2017/04/russia-litres-ebook-format-fb3/)
- [E-book Conversion (Calibre Documentation)](https://manual.calibre-ebook.com/conversion.html)
- [18 Best Ebook Converter Apps in 2026](https://howtoconvert.co/blog/best-ebook-converter-apps)
- [Creating an Ebook with Pandoc](https://pandoc.org/epub.html)
- [Top FlipBook Maker: FlipHTML5](https://fliphtml5.com/)
- [Free HTML5 Flip Book Maker: PubHTML5](https://pubhtml5.com/free-flip-book-maker)
- [Top Free Flipbook Software for 2026](https://www.fingerlakes1.com/2025/12/12/top-free-flipbook-software-for-2026-no-cost-tools-compared-and-tested/)
- [Free EPUB/PDF to MP3 & M4B Audiobook (Audiobook Maker)](https://audiobook-maker.com/en/)
- [M4B Format Guide (Audiobook Maker)](https://audiobook-maker.com/guide/m4b-format/)
- [epub2tts (GitHub)](https://github.com/aedocw/epub2tts)
- [epub_to_audiobook (GitHub)](https://github.com/p0n1/epub_to_audiobook)
- [TTS-Story (GitHub)](https://github.com/Xerophayze/TTS-Story)
- [Best TTS for Audiobooks 2026 (VoiceKeep)](https://voicekeep.io/guides/best-tts-for-audiobooks)
- [Print-Ready PDFs: RGB to CMYK with Ghostscript](https://www.filipnet.de/ghostscript-pdf-rgb2cmyk/)
- [Ghostscript: Optimizing PDFs](https://ghostscript.com/blog/optimizing-pdfs.html)
- [PressPDF.com: Add Bleed and Crop Marks](https://www.presspdf.com/)
- [Choose the Best Layout: Fixed vs Reflowable EPUB (Kitaboo)](https://kitaboo.com/reflowable-or-fixed-layout-epub-which-is-better/)
- [Reflowable vs Fixed Layout EPubs (Kobo Writing Life)](https://www.kobo.com/kobo-writing-life/blog/tech-101-reflowable-epubs-vs-fixed-layout-epubs)
- [HTML vs PDF SEO (Revenue Architects)](https://revenuearchitects.com/blog/considering-html-vs-pdf-seo-user-experience/)
- [PDFs Aren't Ideal for SEO (MarketMuse)](https://blog.marketmuse.com/why-pdfs-are-not-ideal-for-seo/)
- [Readk.it: Digital Reading Simplified](https://readk.it/)
- [PLR Content: 18,866+ Products (PLR.me)](https://www.plr.me/content)
- [What is PLR Content? 2026 (Alex Tucker)](https://alextucker.ca/what-is-plr/)
- [12 Best Gumroad Alternatives in 2026 (Payhip)](https://payhip.com/blog/gumroad-alternatives/)
- [Best Platforms to Sell Digital Products 2026 (Payhip)](https://payhip.com/blog/best-platforms-to-sell-digital-products/)
- [Ebook Formats Explained (Kindlepreneur)](https://kindlepreneur.com/book-formatting-file-types-explained/)
- [EPUB vs PDF for eBooks (EditionGuard)](https://www.editionguard.com/learn/e-book-formats-why-choose-one-or-the-other/)
- [Drop Caps in EPUB (Adobe Community)](https://community.adobe.com/t5/indesign-discussions/drop-caps-in-epub/td-p/10198675)
- [Using Drop Caps in Your eBook (Book Cave)](https://mybookcave.com/authorpost/using-drop-caps-in-your-ebook/)
