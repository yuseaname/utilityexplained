# Style Bible + Asset Inventory — Utility Explained

**Date:** 2026-08-28  
**Source:** Mason seat, SQ-050 visual-content recon  
**Method:** Read-file audit of IMAGE_AUDIT_REPORT.md, static/images/ tree, assets/css/site-overrides.css, SVGs, rendered article frontmatter, and per-directory file inventories  

---

## 1. OVERALL VISUAL DOCTRINE

> "The Independent Bill Auditor" — flat ledger surfaces, mono as the voice of numbers, amber reserved for the one line that matters.

(Source: `assets/css/site-overrides.css`, line 16-18)

**Aesthetic:** Engineering-blueprint meets utility-ledger. Flat vector, no gradients, no glassmorphism, no card lifts. Images are flat illustrations (gpt-image-2), annotated bill diagrams, process flow charts, and timeline graphics. Charts are data-driven tables rendered in markdown, not image-based.

---

## 2. COLOR PALETTE (from CSS vars + SVGs)

| Role | Hex | CSS Variable | Where Used |
|------|-----|-------------|------------|
| Deep ink (primary text) | `#0e201c` | `--color-primary-900` | Body text, popular-item background |
| Ink 80% | `#16302b` | `--color-primary-800` | Dark card backgrounds |
| Ink 5% | `#f2f6f5` | `--color-primary-50` | Cross-desk strip background |
| Warm cream (paper) | `#fffcfa` | — | Quick-answer bg, popular-item bg, hub-cross-link bg |
| Amber accent | `#e8a33d` | `--color-accent-500` | Primary accent (borders, meter needle, popular-item-num) |
| Amber light | `#fdf8ed` | `--color-accent-50` | ue-register bg, popular-item hover bg |
| Amber mid | `#f5d98e` | `--color-accent-200` | ue-register border |
| Amber dark | `#ab6220` | `--color-accent-700` | Hub group title, ue-register strong |
| Amber bright | `#ebb23a` | — | Backdrop meter needle, popular-item-num |
| Grid teal (faint) | `#3c655c` | — | backdrop.svg grid lines |
| Grid teal mid | `#5f847a` | — | backdrop.svg dials, pipe, table hints |
| Grid teal light | `#719e71` | — | backdrop.svg tick marks |
| Body text secondary | `#5c6b62` | — | bill-figure caption, hub-guide-desc |

**Context:** Backdrop.svg uses engineering-drawing strokes (teal-on-ink), meter dials, pipe runs, transmission towers, rate table outlines — all at ~15–50% opacity for depth without distraction.

---

## 3. FONT STACK (from CSS)

- **Body (implied):** Sans-serif system stack (Tailwind / Athena framework default)
- **Numbers / register:** `var(--font-mono, ui-monospace, "SF Mono", Menlo, Consolas, monospace)` — `.ue-register` class at 0.78rem, 0.08em letter-spacing, uppercase, tabular-nums
- **Headings:** Likely sans-serif, bold (not explicitly overridden — follows design-system.css)
- **Figure captions:** 0.85rem, `#5c6b62`

---

## 4. IMAGE CATEGORIES & NAMING CONVENTIONS

### 4a. Hero Images (frontmatter `image:` field)

**Post Cycle-4 convention (standard, ~66 articles):**
```
{slug}/{slug}_hero_v2.webp
```
Example: `21-past-due-balance-utility-bill-explained/21-past-due-balance-utility-bill-explained_hero_v2.webp`

**Older hero conventions (pre-August 10):**
```
{slug}/{slug}_hero_00001_.webp    # Magica slot naming
{slug}/custom_hero.webp           # Custom-generated, pre-Cycle-4
```

**Generic stock survivors** (9 files, 27 articles):  
`utility-*.jpg` — e.g., `utility-paperwork.jpg`, `utility-home.jpg`, `utility-electricity.jpg` — stored in `static/images/` (not in article dirs)

### 4b. Inline / Body Images

**Standard generic inline:** `custom_inline.webp` (applies to ~90+ articles, likely gpt-image-2 text/educational diagram)

**Article-specific inline names (descriptive):**  
- `past-due-bill-anatomy.webp`  
- `past-due-disconnection-timeline.webp`  
- `dial-meter-reading.webp`  
- `leak-indicator-dial.webp`  
- `decision-tree.webp`  
- `sewer-flow.webp`  
- `sewer-3-ways.webp`  
- `reconnect-process.webp`  
- `taxes-fees-breakdown.webp`  
- `bill-anatomy.webp`  
- `energy-hogs-hero.webp`  
- `phantom-load-cut.webp`  
- `ccf-convert.webp`, `ccf-normal.webp`  
- `reconnect_avoid.webp`, `reconnect_fees.webp`  
- `sewer-hero-explained.svg` (hand-built branded SVG)  
- `ebill-4numbers.webp`, `ebill-tou.webp`  
- `ev-charge-math.webp`  
- `thermostat-setback.webp`  
- `duct-leak-house.webp`  
- `gas-bill-split.webp`  
- `img-1.webp`, `img-2.webp`, `img-3.webp` (3-article anomaly: can-utility-shut-off-service, how-to-dispute-utility-bill, moving-utilities-checklist)  
- `image.webp` (used in ~6 older/simple articles)  

### 4c. Section Splits (rare — 3 articles)
```
{slug}/{slug}_section-1_00003_.webp
{slug}/{slug}_section-2_00003_.webp
```
Articles: `7-states-with-worst-utility-spikes-2026`, `average-utility-bills-by-state-2026`, `how-to-read-your-utility-bill`, `why-your-electric-bill-keeps-rising-2026`

### 4d. Naming Pattern Summary

| Intent | Pattern | Notes |
|--------|---------|-------|
| Hero (current standard) | `{slug}/{slug}_hero_v2.webp` | Post Cycle-4, editorial scenes, no text cards |
| Hero (cycle-3 or earlier) | `{slug}/{slug}_hero_0000N_.webp` | Magica slot naming, still live |
| Hero (custom, pre-cycle-4) | `{slug}/custom_hero.webp` | ~14 articles still use this |
| Generic stock hero | `utility-*.jpg` | 9 files, 27 articles, `static/images/` root |
| Generic inline | `{slug}/custom_inline.webp` | ~90+ articles |
| Specific inline | `{slug}/{descriptive-name}.webp` | Process diagrams, bill anatomies, flow charts |
| Section split | `{slug}/{slug}_section-N_00003_.webp` | Long-form articles only (4 articles) |
| Hand-built branded SVG | `{slug}/{descriptive}.svg` | + PNG fallback (1 current: sewer-hero-explained) |
| Generic fallback | `{slug}/image.webp` | ~6 pre-system articles |
| Sequential (img-N) | `{slug}/img-1.webp` etc. | 3 articles, likely stock or manual uploads |

---

## 5. REUSABLE VISUAL ASSETS (SVGs)

### 5a. `annotation-sprite.svg` (display:none sprite, 4 symbols)

| Symbol ID | Purpose | Visual |
|-----------|---------|--------|
| `ann-needle` | Annotation pointer / callout marker | Circle + needle line + dot. stroke=currentColor, 24×24 |
| `ann-check` | Verification stamp / completion | Star-like 5-point shape. stroke=currentColor, 24×24 |
| `ann-divider` | Section tear-off / perforation | Horizontal line with amber diagonal cross at center. 200×16, preserveAspectRatio="none" |
| `ann-stamp` | Approval / confirmation | Dashed circle + checkmark. stroke=currentColor, 24×24 |

**All:** `fill="none"`, `stroke="currentColor"`, `stroke-width="1.4-1.8"` — thin-line style inheriting parent color.

### 5b. `topic-icons.svg` (display:none sprite, 11 symbols)

| Symbol ID | Topic | Design |
|-----------|-------|--------|
| `i-electricity` | Electricity | Lightning bolt, 24×24 |
| `i-gas` | Gas | Flame curve, 24×24 |
| `i-water` | Water | Drop shape, 24×24 |
| `i-fees` | Fees / charges | Diamond with $, 24×24 |
| `i-hvac` | HVAC / heating | Circle with cross + center dot, 24×24 |
| `i-troubleshoot` | Troubleshooting | Wrench shape, 24×24 |
| `i-budgeting` | Budgeting / planning | Clipboard + amber circle accent (`#e8a33d`), 24×24 |
| `i-rates` | Rates / pricing | Bar chart ascending, 24×24 |
| `i-billing` | Billing | Document with lines, 24×24 |
| `i-meter` | Meter reading | Gauge dial, amber needle + dot (`#e8a33d`), 24×24 |
| `i-book` | Glossary / reference | Open book, 24×24 |

**All:** `stroke="currentColor"`, `stroke-width="1.6"`, thin-line sans-serif.  
**Usage pattern:** Used in article category headers / callout boxes (observed in rendered HTML, referenced by ID via `<use>`).

### 5c. `backdrop.svg`

| Element | Visual |
|---------|--------|
| Base | `#0E201C` rect 1600×1000 |
| Grid | Faint teal (#3c655c, opacity 0.25) 50px engineering grid |
| Meter dial (large) | 280,260 — 3 concentric circles, 12 tick marks, amber (#ebb23a) needle at ~120°, top-left |
| Meter dial (small) | 1280,760 — 3 concentric circles, 10 tick marks, amber needle at ~300°, bottom-right |
| Transmission tower | 1100,120 — silhouette lines + arcs, teal strokes |
| Pipe run | 40,820 — dual horizontal+vertical pipe with flange circles |
| Rate table | 760,420 — 4×2 grid table hint |
| 3× dimension ticks | Scattered horizontal measure lines |

**Purpose:** Fixed-page background, always visible, engineering/utility motif.

### 5d. `sewer-hero-explained.svg` (hand-built branded SVG)

Article-specific, hand-authored SVG flow diagram for sewer-charge explanation. Only article-specific branded SVG in the tree. Has a PNG twin at same path for fallback.

---

## 6. DESIGN ELEMENTS FROM site-overrides.css

### 6a. Signature Components

| CSS Class | Visual Description |
|-----------|-------------------|
| `.ue-register` | Number callout box. Mono font, 0.78rem, uppercase, 0.08em spacing. Amber bg `#fdf8ed`, amber border `#f5d98e`. `tabular-nums`. Strong numbers in `#ab6220`. Display: inline-block. |
| `.ue-tear-off` | Section divider. 2px dashed `#0e201c` at 25% opacity. `::after` content `···` right-aligned in 0.4em letter-spacing. |
| `.bill-figure` | Annotated bill diagram container. Max-width 540px, centered. 1px border `rgba(14,32,28,0.12)`, 6px radius, white bg. Caption in `#5c6b62` at 0.85rem. |
| `.quick-answer` | Answer block. Paper-raised `#fffcfa`, 1px border, 4px amber left border. No shadow. |
| `.popular-item` | Homepage most-read card. Flex, 1px border, `#fffcfa` bg, 6px radius. Hover: amber border + `#fdf8ed` bg. Number in `#0e201c` bg, amber text. |
| `.hub-cross-link` | Topic cross-link pill. Pill border, `#fffcfa` bg, `#0e201c` text. Hover: amber border. |

### 6b. Motion & Surface Rules

- **No card hover lifts** (`transform: none !important`)
- **No image zooms** on card hover
- **No backdrop-filter** on mobile (scroll repaint cost)
- **No gradients** — solid ink surfaces only (`#16302b`, `#0e201c`)
- **Reduced motion** respected via `@media (prefers-reduced-motion: reduce)`

---

## 7. GPT-IMAGE-2 PARAMETERS (From Audit Addenda)

**From Cycles 2–4 (commit `fe6a739f`, `2d605bb8`, `2c4dbdb4`):**

| Parameter | Value |
|-----------|-------|
| Engine | Magica API → `gpt-image-2-text` |
| Quality | High |
| Dimensions | 1536×1024 |
| Output format | WebP q85 |
| Style (Cycle 2 diagrams) | Warm cream `#FEFAF2` base, terracotta/warm-brown flat vector, red warnings |
| Style (Cycle 4 heroes) | Editorial scenes, single focal subject, minimal/no text, text-card prompts explicitly avoided |
| Theme palette (Cycle 4) | Alternating deep-green `#0e201c` / cream `#fffdf8` backgrounds, amber `#ebb23a` / teal `#5eead4` accents |
| QA method | Vision-QA via `gpt-5.5`, text transcription verification |
| QA pass criteria | 6/6 criteria per image (Cycle 2); 66/66 PASS (Cycle 4) |

---

## 8. ARTICLE VISUAL STRUCTURE (De-facto House Style)

From 4 best-served articles (21-past-due, 05-how-to-lower, 28-reconnection-fee, how-sewer-charges):

1. **Frontmatter hero** (`image:` field → `hero-image.html` partial) — editorial scene, minimal text overlay
2. **Quick Answer** — `.quick-answer` block with 4px amber left border, `#fffcfa` bg
3. **Tables** — As primary visual for structured data (reconciliation tables, comparison tables, cost tables)
4. **Bill Anatomy Figures** (where applicable) — `.bill-figure` container, max-width 540px, annotated bill screenshots with callouts
5. **Process Flow Diagrams** — `.webp` illustrations showing step sequences (reconnect-process, sewer-flow, disconnection-timeline)
6. **Meter/Indicator Diagrams** — close-up annotated illustrations (dial-meter-reading, leak-indicator-dial)
7. **Decision Trees** — flow-chart style (decision-tree.webp)
8. **Number callouts** — `.ue-register` inline boxes for key figures
9. **Tear-off section dividers** — `.ue-tear-off` between sections
10. **Product boxes** — `{{< product-box >}}` affiliate inline (one per article, placed with labeled call-to-action)

**All body images** are inline `<img>` tags embedded in markdown, not shortcode-wrapped. Images center within content column (implicit from `bill-figure` or standard `<img>` styling).

---

## 9. FILE INVENTORY SUMMARY

| Category | Count | Total Weight | Location |
|----------|-------|-------------|----------|
| Article-specific heroes (v2) | ~66 | — | `static/images/articles/{slug}/` |
| Article-specific heroes (older) | ~22 | — | `static/images/articles/{slug}/` |
| Generic stock heroes | 9 | — | `static/images/` utility-*.jpg |
| Generic inline (custom_inline) | ~90+ | — | `static/images/articles/{slug}/` |
| Article-specific inline | ~40 | — | `static/images/articles/{slug}/` |
| Section-split images | ~10 | — | `static/images/articles/{slug}/` |
| Theme SVGs | 4 | — | `static/images/` |
| OG image | 1 | 283KB | `static/images/og-default.png` |
| Hand-built SVG+PNG | 1 | ~155KB | `static/images/articles/how-sewer-charges/` |
| **Total** | **~249** (102 referenced in audit report) | **10.2MB** | — |

---

## 10. TEN STYLE PARAMETERS FOR GPT-IMAGE-2 BRIEF

These 10 must be carried verbatim to any image-generation brief to maintain brand consistency:

| # | Parameter | Value | Evidence |
|---|-----------|-------|----------|
| 1 | **Output format** | WebP q85, 1536×1024 | Audit addenda (Cycles 2–4) |
| 2 | **Base palette** | `#0e201c` (deep ink) / `#fffdf8` or `#fffcfa` (cream) alternating | site-overrides.css, backdrop.svg, Cycle 4 notes |
| 3 | **Accent color** | `#e8a33d` / `#ebb23a` (amber) — single accent, never blue | site-overrides.css, annotation-sprite.svg, topic-icons.svg |
| 4 | **Secondary accent** | `#5eead4` (teal) — sparingly, for secondary data points | Cycle 4 audit note |
| 5 | **Red/alert** | `#dc2626` or similar — used only for warnings/danger states | Cycle 2 note "red warnings" |
| 6 | **Drawing style** | Flat vector, thin-line SVG aesthetic, no gradients, no glassmorphism, no photoreal | site-overrides.css line 19-21, annotation-sprite stroke widths |
| 7 | **Scene approach (heroes)** | Single focal subject, editorial scene, minimal/no embedded text, no text-card compositions | Cycle 4 sweep: 66 heroes regenerated to eliminate text cards |
| 8 | **Scene approach (diagrams)** | Annotated bill, flow chart, timeline, decision tree, meter dial — 1 concept per image | Body image names (sewer-flow, decision-tree, past-due-bill-anatomy) |
| 9 | **Background / surface** | Warm cream paper (`#fffcfa` or `#FEFAF2`) for diagrams; deep ink (`#0e201c`) for hero alt-bg | site-overrides.css `.quick-answer`, `.popular-item`, Cycle 2 notes |
| 10 | **Typography (embedded)** | Sans-serif, no decorative fonts. Numbers in tabular (monospace if standalone). Max 1-2 short labels per diagram. No title cards. | site-overrides.css `.ue-register`, Cycle 4 directive "no text-card prompts" |

---

## 11. NOTES & ANOMALIES

1. **`img-1.webp`/`img-2.webp`/`img-3.webp` (3 articles):** can-utility-shut-off-service, how-to-dispute-utility-bill, moving-utilities-checklist — these use generic sequential naming, likely stock or manual uploads predating the image generation system. These do not match the current naming convention.

2. **`image.webp` (~6 articles):** Similar legacy pattern — ac-short-cycling, budget-billing-level-pay, ductless-mini-split, how-to-read-gas-meter, how-utility-rates-fees, utility-connection-fee, utility-reconnection-fee. These predate the descriptive naming convention.

3. **`slots/` directory:** Empty — all slot-based articles and their images were deleted in the Aug 10 audit (Phase 1 cleanup). The directory remains as a structural remnant.

4. **`how-sewer-charges-work-on-your-water-bill/` directory:** Has 6 files — the most of any article. Includes a hand-authored branded SVG (`sewer-hero-explained.svg` + PNG fallback) alongside three different inline webps and an old hero v1. This is the only article with hand-authored visual assets.

5. **Generic stock heroes still present (27 articles):** 9 utility-*.jpg files. The Cycle 3 audit claimed "hero task closed" and 63 custom AI heroes replaced sitewide. The remaining 27 may have been intentionally retained as topically appropriate, or they may predate Cycle 4. The audit recommends article-specific replacements for 7 high-priority articles.

6. **Inline image density varies dramatically:** Some articles (21-past-due, 05-how-to-lower, how-sewer-charges) have 2-5 body images. Others (utility-reconnection-fee, how-to-lower-electric-bill-complete-guide) have 1. The SQ-045 verifier found 90+ pages lack diagrams where topical.

---

## 12. RECOMMENDATION TEMPLATE (for Commander)

Any future GPT-Image-2 brief should:
- Use the 10 parameters above as envelope headers
- Reference style by name: "Utility Explained house style — the Independent Bill Auditor"
- Specify which article slug the image belongs to (for naming convention)
- Call out which existing SVG sprite symbol could be composited into the scene (from `topic-icons.svg` or `annotation-sprite.svg`)
- Declare intended placement: hero vs inline vs section figure
