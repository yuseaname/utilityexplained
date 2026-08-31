# SQ-066 side-quest — GSC "Unparsable structured data: Invalid top level element \"string\"" — diagnosis & verification report

**Seat:** Lieutenant (glm-5.3-flash) · **Date:** 2026-08-30 · **Status:** RESOLVED (fix already in codebase; verified exhaustively, no further layout change required)

---

## TL;DR

The error is real but **historical**. It was caused by one template line emitting JSON-LD without escaping protection; that line was fixed on 2026-08-14 (theme) and 2026-08-21 (site override, SQ-013), both ancestors of current HEAD. The rendered `public/` tree and the **live site** now serve 100% valid JSON-LD. Nothing in `layouts/**` needs changing; the remaining work is Google-side ("Validate Fix" in Search Console).

---

## 1. Root cause (one sentence)

The broken-era emitter `themes/adsense-base/layouts/partials/head.schema.html` ended with:

```
{{- $schemas | jsonify -}}
```

…with **no `safeJS` escaping marker**, so Hugo's contextual auto-escaping in a `<script>` context JS-escaped the already-quoted JSON string, double-encoding the whole schema array into a bare JSON *string*, e.g.:

```
"[{\"@context\":\"https://schema.org\",\"@type\":\"Article\",...}]"
```

A top-level JSON string is exactly what GSC reports as `Invalid top level element "string"`.

### Evidence that this is the emitter

| Probe | Result |
|---|---|
| Old snapshot `utilityexplained_public.tar.gz` (deploy era 2026-08-11, commit `0c3a42c9`) | 439 ld+json blocks, **372 invalid — every single one `TOPLEVEL_str`** with the `"[{\"@context\"...}]"` signature |
| Emitter at that commit | `git show 0c3a42c9:themes/adsense-base/layouts/partials/head.schema.html` → ends `{{- $schemas | jsonify -}}` (no safeJS) |
| FAQPage partial (`faq-schema-render.html`) in the **same old snapshot** | **67/67 valid** — it writes literal template text with per-field `jsonify`, unaffected → isolates the failure to the single `head.schema.html` emit line |
| Broken values inside the wrapped string | `"dateModified":"2024-12-01 00:00:00 +0000 UTC"` (Go-time `printf %s` form) matches the dict-built `$schemas` of that era — confirms provenance |
| Failure distribution in old snapshot | 220 tag pages, 127 blog posts, 6 author pages, categories, hubs (water/utility-bills/glossary/terms/privacy/methodology/search/homepage) — matches GSC's reported page families (posts/hubs/category/about/terms) and the ~40 live-URL count (220 tag URLs are noindex/not-indexed; live affected set ≈ 40) |

## 2. The fix (already landed — lineage)

1. `ecc1dcdb` **2026-08-14** — "Session: theme schema repair, full FAQ coverage, 4 thin-page rebuilds, deploy prep" added the guard in the theme partial (`git log -S 'safeJS' -- themes/adsense-base/layouts/partials/head.schema.html`).
2. `7bdd9f39` **2026-08-21 (SQ-013)** — created the site override `layouts/partials/head.schema.html` with the same guard (plus ProfilePage/Person author-schema upgrade).
3. Both are ancestors of HEAD (`git merge-base --is-ancestor 7bdd9f39 HEAD` → true).

### Current (correct) emission lines

- `layouts/partials/head.schema.html:173` → `{{- $schemas | jsonify | safeJS -}}`
- `themes/adsense-base/layouts/partials/head.schema.html:137` → `{{- $schemas | jsonify | safeJS -}}`

with the in-template comment explaining `safeJS` is required because script content is a JS context and any other escaping mark double-encodes the JSON.

## 3. Before / after samples

**BEFORE — old snapshot `about/index.html` block#0 (`json.loads` → `str`, GSC-critical):**

```
"[{\"@context\":\"https://schema.org\",\"@type\":\"Article\",\"dateModified\":\"2024-12-01 00:00:00 +0000 UTC\",\"datePublished\":\"2024-12-01T00:00:00+00:00\",\"description\":\"Wh…
```

(type after `json.loads`: `str` → "Invalid top level element: string")

**AFTER — current build `public/about/index.html` block#0 (`json.loads` → `list`, valid):**

```
[{"@context":"https://schema.org","@type":"Article","dateModified":"2026-08-12","datePublished":"2024-12-01T00:00:00+00:00","description":"Why Utility Explained exists, who it\u002…
```

(type after `json.loads`: `list` → parses clean)

## 4. Verification (full-tree sweep, per mission)

1. Clean rebuild: `hugo --gc --quiet` → **exit 0** (hugo v0.141.0 extended, same as CI, `~/.local/bin/hugo`).
2. Full-tree sweep — extracted every `<script type="application/ld+json">` block from **every** `public/**/*.html` and ran `python3 json.loads` on each:

   > **TOTAL_BLOCKS=412 · FAILURES=0**

   (scanner: `/tmp/squad-workspaces/20260830-185858-lieutenant/scan066.py`; identical 412/0 before and after the rebuild — the tree was already fixed.)
3. Script-tag census cross-check: 2,932 total `<script>` tags vs 412 `ld+json` occurrences — the extractor caught every schema block (no regex blind spot).
4. Named GSC page types on the current build — all valid:
   - hubs `electricity-explained`, `water-explained`, `gas-explained`, `utility-bills-costs-explained` → `[Article, BreadcrumbList]` (+FAQPage dict where FAQs exist)
   - `blog/category/heating-cooling` → `[BreadcrumbList]`
   - `about`, `contact`, `terms`, `utilities-glossary` → `[Article, BreadcrumbList]`
   - posts `afue-vs-seer-vs-hspf-vs-cop`, `49-demand-charges-electricity-bill-explained` → `[Article, BreadcrumbList]` + FAQPage
   - homepage → `[Organization, WebSite]`
5. **Live-site verification** (GSC validates the deployed copy): `curl` of raw HTML + `json.loads` on served blocks —
   - `/about/`, `/blog/afue-vs-seer-vs-hspf-vs-cop/`, `/blog/category/heating-cooling/`, `/electricity-explained/` → HTTP 200, all blocks valid
   - All 7 GSC-listed retired aliases (`41-how-to-read-electricity-bill`, `02-average-utility-costs-2026`, `stormwater-fee-on-water-bill-explained`, `demand-charge-electricity-bill-explained`, `7-states-with-worst-utility-spikes-2026`, `why-is-my-electricity-bill-so-high-in-summer`, `…-winter`) → HTTP 200 (redirect targets) with **0 invalid blocks** out of 0–2 blocks each (several serve no ld+json at all — zero risk; they age out of GSC as the packet notes)

## 5. Files changed by this run

**None.** The failing line no longer exists in `layouts/**` or `themes/**` at HEAD; re-breaking nothing was the only correct change. (Had a fix been needed, the planned route was python3 in-place edits via run_command with failing→passing `json.loads` quotes — not exercised because no failing template exists.)

## 6. What remains (operator actions, not code)

1. In Search Console, for each affected page group (hubs, category pages, static pages, posts): **Validate Fix** — GSC will re-crawl the now-valid markup; with 100% valid JSON-LD deployed and live-verified, the critical should clear within the normal re-validation window.
2. Retired aliases will keep reporting until Google processes their redirects; expect them to age out — no template or content action.
3. Regression guard (future sprint recommendation): add the reusable scanner (see §7) to `tests/` as a post-build check that `json.loads()` every ld+json block in `public/`, so an unmarked `jsonify` can never ship again.

## 7. Verification commands (quoted from run)

- `hugo --gc --quiet` → exit 0
- `python3 scan066.py` → `TOTAL_BLOCKS=412` / `FAILURES=0` (local, post-rebuild)
- same scanner on extracted 2026-08-11 snapshot → `TOTAL_BLOCKS=439` / `FAILURES=372` (all `TOPLEVEL_str`) — reproduction
- FAQPage-only sweep of old snapshot → `{'valid_dict': 67}` — control group
- `git log -S 'safeJS'` / `git merge-base --is-ancestor` → fix lineage `ecc1dcdb` (theme, 08-14) and `7bdd9f39` (override, 08-21) in HEAD
- `curl + json.loads` → live `/about/`, hub, category, post samples + 7 retired aliases → 0 invalid blocks
