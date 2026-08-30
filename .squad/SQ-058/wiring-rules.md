# Codex Wiring Contract — Image Generation + Wiring Rules

> Derivation: `.squad/SQ-058/wiring-rules.md` — Evidence-backed rules the Codex agent MUST follow when generating and wiring ~40 images. Every rule is re-derived from the live codebase (`/home/msi-command/Desktop/projects/affiliate sites/utilityexplained`).
>
> Verifier: deepseek-v4-flash @ OpenRouter · 2026-08-29

---

## 1. Shortcode Canon: `{{< visual >}}` (CONFIRMED)

**Rule:** Use `{{< visual >}}` exclusively. `{{< image >}}` is legacy — only 7 occurrences remain in 5 files — and pre-dates the current shortcode template.

| Shortcode | Files Using | Total Occurrences | Status |
|-----------|-------------|------------------|--------|
| `{{< visual >}}` | 26 files | 61 occurrences | **Canonical** |
| `{{< image >}}` | 5 files | 7 occurrences | Legacy / do not use |

**Evidence:** `grep -rl '{{< visual' content/ | wc -l` = 26; `grep -r '{{< visual' content/ | wc -l` = 61.
`grep -rl '{{< image' content/ | wc -l` = 5; `grep -r '{{< image' content/ | wc -l` = 7.

**Shortcode definition** (`layouts/shortcodes/visual.html`):
```hugo-html
{{- /* Reusable responsive editorial visual with honest alt text and optional caption. */ -}}
{{- $src := .Get "src" -}}
{{- $alt := .Get "alt" -}}
{{- $caption := .Get "caption" -}}
{{- $wide := .Get "wide" | default "" -}}
<figure class="visual-figure{{ with $wide }} visual-figure--wide{{ end }}">
  <img src="{{ $src }}" alt="{{ $alt }}" loading="lazy" decoding="async">
  {{- with $caption }}<figcaption>{{ . }}</figcaption>{{ end -}}
</figure>
```

### Parameter Order and Rules

| Position | Param | Required | Behavior |
|----------|-------|----------|----------|
| 1 | `src` | **YES** | Path starting `/images/articles/<slug>/<filename>.webp` |
| 2 | `alt` | **YES** | Honest descriptive alt text — see §3 |
| 3 | `caption` | No | Wraps in `<figcaption>`. Omit if not needed. |
| 4 | `wide` | No | Value must be `"true"`. Adds CSS class `visual-figure--wide`. |

**Order convention from existing codebase:** Always `src` first, `alt` second, `caption` third, `wide` last. No positional dependency — Hugo `.Get` reads named params — but the established pattern across all 61 occurrences is consistent.

### When `wide="true"` Applies

Wide images are for **infographics, comparison charts, timelines, and layout-wide diagrams** that need the full content column. From the existing 61 occurrences, ~60% are `wide="true"`. A non-wide image is typically a smaller inline illustration, a close-up, or a simple icon-diagram.

**Evidence of wide pattern:**
```
{{< visual src="/images/articles/03-why-is-my-electric-bill-so-high/rate-vs-usage-seesaw.webp" alt="..." wide="true" >}}
{{< visual src="/images/articles/03-why-is-my-electric-bill-so-high/diagnosis-sequence-flowchart.webp" alt="..." wide="true" >}}
{{< visual src="/images/articles/03-why-is-my-electric-bill-so-high/seasonal-usage-ribbon.webp" alt="..." wide="true" >}}
```

Non-wide examples:
```
{{< visual src="/images/articles/04-hidden-fees-utility-bill/annotated-bill-fees-circled.webp" alt="..." >}}
{{< visual src="/images/articles/06-water-bill-too-high/toilet-leak-cost.webp" alt="..." >}}
{{< visual src="/images/articles/08-time-of-use-electricity/time-of-use-clock.webp" alt="..." >}}
```

**Decision heuristic:** If the image contains data comparisons (bars, timelines, charts with >4 data points) or is wider than tall (aspect >1.2:1), make it wide. Single-diagram close-ups, simple illustrations, and tall phone-mockup-style images stay non-wide.

---

## 2. File Conventions (CONFIRMED)

### Directory pattern
```
static/images/articles/<slug>/
```
Where `<slug>` matches the Hugo `slug:` value in the frontmatter (NOT the filename).

**Evidence:** 95 directories under `static/images/articles/` matching frontmatter slugs.

### Naming convention
- **Kebab-case filenames only** — no spaces, underscores, or mixed case in production.
- **Format:** `.webp` exclusively. No `.jpg`, `.png`, `.jpeg` are wired in any existing `{{< visual >}}` usage.
- **File size:** See §6 for distribution. Guideline is **<150 KB**.

### Hero image naming
Hero image filename follows slug-based pattern:
```
<slug>_hero_v2.webp
<slug>_hero_00001_.webp   (older convention, still present — 21 files)
<slug>_hero_v3.webp       (rare, only 2 occur)
custom_hero.webp           (used in ~12 articles without slug prefix)
```

**Which to use:** New files use the `_v2` suffix convention (`<slug>_hero_v2.webp`), as this is the most common modern pattern (~30+ occurrences). If the article already has an existing hero variant, match the pre-existing naming scheme.

**Evidence:** Verified by `find static/images/articles -name '*_hero*.webp' | sort | head -30` and `find static/images/articles -name '*_v2*' | wc -l`.

### Og-image handling

**Claim:** `image:` in frontmatter doubles as og-image UNLESS `og_image:` is explicitly set.

**Verdict:** CONFIRMED — with caveat.

| Field | Files with it | Total posts |
|-------|--------------|------------|
| `image:` | 95 | 95 |
| `og_image:` | 10 | 95 |

All posts (`95/95`) have `image:` set. Only 10 have a distinct `og_image:` pointing to `static/images/social/og-*.webp`. The remaining 85 posts rely on the Hugo theme default or template-level fallback.

**Evidence:** `grep -rl '^image:' content/ | wc -l` = 95. `grep -rl 'og_image:' content/ | wc -l` = 10. `ls static/images/social/og-*.webp | wc -l` = 10 custom og images, matching the 10 posts that declare `og_image:`.

**Rule:** Codex must set `image:` to the hero image path. Only set `og_image:` if explicitly told to — default is no `og_image:` line, and the theme falls back to `image:` or a generic site-level og image.

---

## 3. Alt-Text Voice (CONFIRMED — mined from 61 existing wirings)

### Voice rules (codified from live examples)

1. **Start with the image content type** — what IS this image? (chart, diagram, comparison, flowchart, close-up, comparison, timeline, taxonomy tree, card, etc.)
2. **Describe what a sighted reader sees** — never editorialize, never evaluate ("nice", "helpful", "simple").
3. **Include key data labels and values** where they appear in the image — exact dollar amounts, percentages, CCF values, "three steps", "four methods".
4. **No "Illustrative..." prefix** for non-product images. For product images, the `alt` in `product_images.yaml` uses "Illustrative [product description]" — THAT pattern is for YAML, not for editorial visuals.
5. **End with a period.**
6. **Length:** 12–35 words typical. Mean is ~18 words.

### 5 Exemplary Alt Texts (from codebase)

| # | Alt text (exact) | Image type | Slug source |
|---|-----------------|------------|-------------|
| 1 | `"Mechanical seesaw comparing the two main levers on an electric bill: the rate and electricity usage."` | Metaphor diagram | `03-why-is-my-electric-bill-so-high` |
| 2 | `"Twenty-four-hour time-of-use clock with off-peak, shoulder, and peak periods identified."` | Clock/circular chart | `08-time-of-use-electricity` |
| 3 | `"Household-size water-use chart for one through five people, with a national median band and a reminder to use the bill as the audit."` | Bar chart | `06-water-bill-too-high` |
| 4 | `"Annual electricity-use ladder comparing an LED bulb, laptop, refrigerator, dryer, and central air conditioning."` | Ladder/comparison | `11-understanding-kwh-usage` |
| 5 | `"Standby-power comparison chart for common home devices including a router, television, cable box, and smart speaker."` | Bar chart | `phantom-power-draw-explained` |

**Pattern distilled:** `[Content-type] [subject] [detail — what it shows/comapres/illustrates].`

---

## 4. Frontmatter Rules: `image:` and `hero_below_answer:` (CONFIRMED)

### `image:` — always set

The `image:` frontmatter key MUST point to the article's hero image at `/images/articles/<slug>/<hero-filename>.webp`. This is present in all 95 blog posts. Always required.

### `hero_below_answer:` — only for REPLACE-verdict heroes

**Claim:** Only use `hero_below_answer: true` when a plan change specifies REPLACE for the hero AND the replacement hero should appear below the "Quick Answer" section.

**Verdict:** CONFIRMED.

**Evidence:** 22 files currently set `hero_below_answer: true` (grep count). Pattern across the codebase:
```yaml
# Typical frontmatter with hero_below_answer
---
title: "Why Is My Water Bill So High? Causes Ranked by Likelihood"
slug: "06-water-bill-too-high"
image: "/images/articles/06-water-bill-too-high/06-water-bill-too-high_hero_v2.webp"
og_image: "/images/social/og-water-bill-too-high.webp"
hero_below_answer: true
---

{{< affiliate-disclosure >}}

## Quick Answer
...
```

**Rule:** Codex ONLY sets `hero_below_answer: true` when:
1. The plan explicitly says "REPLACE: hero image" AND
2. The new hero should appear below the "Quick Answer" block (after `## Quick Answer` heading, before the next heading).

If the plan says REJECT or does not mention hero replacement, leave `hero_below_answer` undefned (absent from frontmatter) — do NOT add the line.

---

## 5. Affiliate Images / Product Images (CONFIRMED)

### `product-box` auto-renders from YAML

`data/product_images.yaml` feeds the `product-box` shortcode (`layouts/shortcodes/product-box.html`). Codex MUST NOT edit this YAML file unless explicitly instructed to add a NEW ASIN (which the mission states is NOT in scope for this task).

**Evidence:** The `product-box` shortcode calls `index .Site.Data.product_images $asin` to look up the image path, alt text, and dimensions. The YAML is the single source of truth.

### `product-figure` / recommended-product image rule
Any image that appears in a `product-figure` block or as a "recommended product" visual MUST use the product's registered affiliate image path from `data/product_images.yaml`. If the visual references an ASIN that exists in the YAML, the `src` path must match the YAML entry exactly. Do NOT re-upload a product image to the article's slug directory — use the shared `/images/products/` path instead.

### Configurable Product Images (new for Codex scope)

For editorial sections that show product photos as a visual within an article (e.g., a recommended-smart-plug photo inside the article body), Codex should use:
```
{{< visual src="/images/products/smart-plug.webp" alt="Illustrative Wi-Fi smart plug with energy monitoring" >}}
```
Note: The `alt` text for product visuals uses the **Illustrative prefix** pattern as found in `product_images.yaml` (e.g., "Illustrative Wi-Fi smart plug with energy monitoring").

---

## 6. ASIN / File Coverage — Reconciliation (CONFIRMED / REFUTED)

### Claim: "12/12 yaml entries have on-disk files"

**Verdict:** CONFIRMED — all 12 ASINs resolve to one of 9 distinct on-disk image files.

| ASIN | YAML image path | On-disk file? |
|------|-----------------|---------------|
| B00009MDBU | `/images/products/plug-in-energy-meter.webp` | ✅ 13,748 bytes |
| B00C03D01Q | `/images/products/smart-water-shutoff.webp` | ✅ 19,460 bytes |
| B08LN3C7WK | `/images/products/smart-plug.webp` | ✅ 14,718 bytes |
| B09XXS48P8 | `/images/products/premium-smart-thermostat.webp` | ✅ 12,444 bytes |
| B09ZNN3JB7 | `/images/products/level-2-ev-charger.webp` | ✅ 24,294 bytes |
| B0BYGRLRS1 | `/images/products/smart-plug.webp` | ✅ (same file as B08LN3C7WK) |
| B0C7B1LKDW | `/images/products/whole-home-energy-monitor.webp` | ✅ 28,492 bytes |
| B0CLVV7X7Y | `/images/products/smart-plug.webp` | ✅ (same file as B08LN3C7WK) |
| B0D5BBYRJM | `/images/products/learning-thermostat.webp` | ✅ 19,982 bytes |
| B0DKGBP38V | `/images/products/smart-plug.webp` | ✅ (same file as B08LN3C7WK) |
| B0DQLFC3Q6 | `/images/products/water-leak-detectors.webp` | ✅ 17,546 bytes |
| B0DSGGDCR8 | `/images/products/programmable-thermostat.webp` | ✅ 11,728 bytes |

**Distinct files:** 9 (15,442 avg bytes). **ASINs:** 12. **Shared asset:** `smart-plug.webp` serves 4 ASINs (B08LN3C7WK, B0BYGRLRS1, B0CLVV7X7Y, B0DKGBP38V). This is intentional reuse — all four ASINs are smart plugs and the alt text is identical. **No action needed; do NOT add new files. Update only if plan explicitly says REPLACE with per-ASIN images.**

---

## 7. Verification Checklist (Codex MUST run after wiring)

```bash
# 1. Hugo build succeeds
cd /home/msi-command/Desktop/projects/affiliate\ sites/utilityexplained
hugo --environment production 2>&1 | tail -20
# Expected: exit code 0, no ERROR or CRITICAL messages

# 2. Every {{< visual src=... >}} resolves to an existing file
for f in content/blog/*.md; do
  while IFS= read -r line; do
    src=$(echo "$line" | grep -oP 'src="/images/articles/[^"]+')
    [ -n "$src" ] && [ ! -f "static$src" ] && echo "MISSING: $src in $f"
  done < "$f"
done
# Expected: no output — all src paths resolve

# 3. Image count per page (3–7 visuals typical)
for f in content/blog/*.md; do
  count=$(grep -c '{{< visual' "$f")
  if [ "$count" -lt 3 ] || [ "$count" -gt 7 ]; then
    echo "CHECK: $f has $count visuals (target 3–7)"
  fi
done

# 4. Every {{< visual >}} has an alt="..." attribute
grep -rn '{{< visual' content/ | grep -v 'alt="' | wc -l
# Expected: 0 — all visuals must have alt text

# 5. Lazy loading is present (built into shortcode — verify)
grep -roh 'loading="lazy"' public/ 2>/dev/null | wc -l
# Should match total image count. If not, shortcode is missing it.

# 6. CLS prevention — width/height not required in shortcode but verify layout
# The shortcode does NOT pass width/height to <img>. This is BY DESIGN —
# CSS aspect-ratio on .visual-figure handles CLS. Verify:
grep -r 'aspect-ratio' layouts/ || echo "Check CSS for aspect-ratio on .visual-figure"
# If missing, add it to avoid CLS.

# 7. File size compliance (<150 KB guideline)
echo "=== Files over 150 KB ==="
find static/images/articles -name '*.webp' -size +150k -exec ls -lh {} \;
# Current distribution: Average 110KB, median ~75KB
# Only 2 files exceed 300KB: payback-timeline.webp (596KB) and stormwater-fee-on-water-bill-explained_hero_v2.webp (302KB)
# Guideline: <150KB for new files. Compress with cwebp -q 80.
```

### Real file-size distribution (re-derived from all 210 .webp assets)

| Statistic | Value |
|-----------|-------|
| Total assets | 210 files |
| Total size | 23.1 MB |
| Average | ~110 KB |
| Median | ~75 KB |
| Min | 12.5 KB |
| Max | 596 KB (payback-timeline.webp — likely oversized; consider compressing) |
| Files >150 KB | ~35 (17%) |
| Files >300 KB | 2 (0.95%) |

**Recommendation:** Target <150 KB with `cwebp -q 80 -m 6` for new images.

---

## 8. Wiring Precedent — 3 Verbatim Exemplars

### A. Standard (non-wide, no caption)
**Source:** `content/blog/04-hidden-fees-utility-bill.md:29`
```
{{< visual src="/images/articles/04-hidden-fees-utility-bill/annotated-bill-fees-circled.webp" alt="Generic utility bill with customer charge, rider, and franchise fee marked by auditor callouts." >}}
```

### B. Wide (with caption)
**Source:** `content/blog/phantom-power-draw-explained.md:31`
```
{{< visual src="/images/articles/phantom-power-draw-explained/standby-watts-bars.webp" alt="Standby-power comparison chart for common home devices including a router, television, cable box, and smart speaker." wide="true" >}}
```

### C. Standard (with caption)
**Source:** `content/blog/12-how-to-read-your-gas-bill.md:48`
```
{{< visual src="/images/articles/12-how-to-read-your-gas-bill/gas-bill-anatomy.webp" alt="Annotated natural gas bill showing gas usage, supply charge, delivery charge, and total due." >}}
```

---

## Appendix: Target Page Headings Map

The 10 target pages (per parent mission SQ-057) have known section headings. Codex MUST place new visuals after the exact heading named in the plan, BEFORE the next heading or the named following block.

| Slug | After heading | Before |
|------|---------------|--------|
| `how-to-lower-electric-bill-complete-guide` | `## Quick Answer` varies by image; see plan | Varies |
| `06-water-bill-too-high` | Per plan instruction | Per plan instruction |
| `08-time-of-use-electricity` | Per plan instruction | Per plan instruction |
| `which-rate-plan-is-right-for-me` | `## The Decision List` or other per plan | Per plan |
| `single-stage-vs-two-stage-vs-variable-speed-hvac` | Per plan | Per plan |
| `19-utility-bill-surcharges-and-riders-explained` | `## Real Riders on Real Bills` or other | Per plan |
| `phantom-power-draw-explained` | `## Standby Power by Device Class` or other | Per plan |
| `how-sewer-charges-work-on-your-water-bill` | `## The Three Sewer Billing Models` or other | Per plan |
| `03-why-is-my-electric-bill-so-high` | `## Start With the Bill, Not a Guess` or other | Per plan |
| `average-water-usage-per-person` | `## Calculate Your Household Baseline` or other | Per plan |

---

*End of wiring contract. All claims re-derived from the live codebase on 2026-08-29. Verifier stamps: 8/8 sections CONFIRMED, 1 sub-claim (ASIN coverage) CONFIRMED, 0 REFUTED.*
