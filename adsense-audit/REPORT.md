# AdSense "Low Value Content" Audit — utilityexplained.com

Audit date: 2026-11-07 · Scope: ALL 174 sitemap URLs (145 blog articles, 9 taxonomy, 2 listings, 1 calculator, 17 standalone pages) · Method: live crawl of every URL + source-file analysis + shingle-based duplicate detection + 90-day Rybbit traffic (site 4987)

Per-page results: `INVENTORY.md` (master tracker — every URL has a row). Machine state: `data/inventory.json`. Evidence: `data/crawl-results.json`.

## Verdict

The site is NOT a thin-content site — but it carries three visible fingerprints of batch/template production that map directly onto Google's stated rejection reasons, plus a handful of template bugs. 94 of 174 pages pass every gate. 80 carry at least one open issue; almost all of those are P1/P2. One cluster is a true P0.

## Root-cause analysis (most → least likely to have driven the rejection)

### 1. P0 — Cookie-cutter state pages (5 pages, duplicate content)
`average-utility-bills-in-{california,florida,new-york,pennsylvania,texas}` are 57–66% duplicated with each other by 8-word shingle containment. Same 6-section template, 3 of 6 headings verbatim-identical across all five, ~35% of paragraphs byte-identical, and where text differs it is only the state name and EIA rates swapped into identical sentences. At ~1,070 words each they are also the thinnest articles on the site (site median ≈ 2,200). Google's spam policy names this pattern explicitly ("pages generated with the same template with minimal changes between them"). A reviewer sampling these five sees a content farm.
**Fix:** rewrite each as a genuinely state-specific page — unique section structure, the state's actual utility landscape (IOUs vs munis vs deregulation), climate-driven usage patterns, state programs (e.g. CA medical baseline / CARE, TX deregulated-provider shopping), state-specific FAQs, 1,800+ words. Keep the EIA data and citations.

### 2. P1 — 35 numbered-slug URLs (batch fingerprint)
`/blog/01-how-to-read-your-electric-bill/` … `/blog/50-best-smart-plugs-standby-power/`. The 01–50 series numbering leaks an internal production spreadsheet into public URLs, with gaps (02, 15, 29, 31–41, 43 missing). Content behind them is fine; the URL pattern reads as mass-produced.
**Fix:** rename slugs to drop the prefix, add 301 aliases (plus `.htaccess` bare-path rules — Hostinger serves alias dirs only with trailing slash). One scripted wave.

### 3. Site age + traffic mix ("consistent presence", "user interest")
First articles date to Dec 2025; ~11 months old. Traffic is real but lopsided: 90d organic sessions = 7,340 (DDG 3,042 · Bing 2,284 · Yahoo 780 · **Google only 841** — new-domain suppression). Bounce averages ~85% with 30–70s on page (quick-answer behavior). A reviewer sees a young domain whose Google-indexed footprint is small.
**Fix (partial, slow):** keep shipping; the P2/P3/P4 enhancement waves already in git history are the right medicine. Do NOT delete zero-traffic pages — only 7 exist and content quality is verified.

### 4. Template bugs (signal sloppiness to a reviewer)
- Related-post card images render a bare `alt` attribute with no value (`alt class=card-image`) — on 144/145 articles. The card template passes no alt; should be the post title. One partial fix.
- 8 trust/policy pages (privacy, about, contact, corrections, disclaimer, editorial-policy, methodology, terms) render **two `<h1>` tags** each.
- 123 page titles exceed 65 chars (mostly the "| Utility Explained" suffix) — SERP truncation, cosmetic.

### 5. Gaps (minor)
- 33 articles lack FAQPage schema (all others have it — inconsistent coverage).
- 3 thin listings: `/calculators/` (46w), `/categories/` (82w), `/blog/category/consumer-rights/` (62w).
- 2 articles >75 days old with zero 90d traffic (`furnace-tune-up-cost-schedule`, `do-programmable-thermostats-cut-heating-bills`).

## What is healthy (verified — do not "fix" these)

- All 174 URLs return 200, no redirect chains, no 404s, no invalid JSON-LD.
- No thin articles: 0 under 1,000 words; 74 at 1,500–2,499; 66 at 2,500+.
- Duplicate scan across all 145 articles: average site-wide boilerplate share 0.0% — every article is genuinely unique prose apart from the state cluster.
- 128/145 articles cite .gov sources (eia.gov 59, energy.gov 47, epa.gov 37, energystar.gov 24).
- Curation is visible: 54 pages updated in Oct, 37 in Sep, 52 in Aug 2026.
- ads.txt correct (`google.com, pub-5566942094411042, DIRECT, f08c47fec0942fa0`), robots.txt clean, sitemap = 174 live URLs, llms.txt 200, RSS live.
- Full trust-page set present incl. editorial-team (866w), methodology, corrections.
- AdSense loader is intentionally suppressed on the 89 affiliate-monetized pages (ads/affiliate never mixed) — by design, policy-safe, keep.
- All 89 Amazon-link pages carry affiliate disclosures. Amazon tag `utexplained-20` injected centrally.
- No AI-tell phrasing (3 innocuous "unlock" hits in 145 articles).

## Remediation order

| # | Item | Pages | Effort | Gate |
|---|------|-------|--------|------|
| 1 | Rewrite 5 state pages (P0) | 5 | high | re-run `crawl.py` + shingle scan: max pairwise containment < 0.15 |
| 2 | Slug renames + 301s | 35 | med | sitemap clean, aliases 301 live, internal links updated |
| 3 | Related-post alt fix | 1 template | low | 0 bare `alt` in built tree |
| 4 | Double-H1 fix | 1 template | low | exactly 1 h1 on all 174 |
| 5 | FAQ schema wave | 33 | med | FAQPage on 100% of articles |
| 6 | Listing intro copy | 3 | low | ≥100w each |
| 7 | Title trim (drop/shorten suffix) | sitewide | low | ≤65 chars |
| 8 | Zero-traffic: interlink or merge | 2 | low | — |

Re-review request only after items 1–4 are verified live (2–3 weeks of clean serving after deploys is the realistic minimum before asking Google to look again).

## Reproduce / re-verify

```bash
python3 adsense-audit/crawl.py            # re-crawl all URLs, refresh data/crawl-results.json
# shingle duplicate scan + traffic join: see adsense-audit/ scripts; inventory statuses in data/inventory.json
```
