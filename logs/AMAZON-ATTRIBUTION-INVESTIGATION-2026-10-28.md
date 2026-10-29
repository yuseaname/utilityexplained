# Amazon Attribution Investigation — 2026-10-28

Trigger: owner reports "traffic growing but affiliate purchases going down; utility tag shows no purchases."
Input data: 3 Associates CSV exports (Tracking-Id, Linked-Product, Category) — ALL DATED 10-27-2026 ONLY (1-day window).

## Headline numbers (10/27/2026, single day)

| Tracking ID | Clicks | Items Ordered | Ordered Revenue | Earnings |
|---|---|---|---|---|
| utexplained-20 | 62 | 0 | 0 | 0 |
| Other (untagged) | 54 | 6 | $455.87 | $10.26 (1 return -$179) |

Purchases ARE happening. They land in the unattributed "Other" bucket, not under the site tag.

## Verified findings

1. ON-SITE ATTRIBUTION IS CLEAN — verified four independent ways:
   - Repo: render-link hook, amazon/product-box shortcodes, sidebar-pick/infeed partials all pull
     `site.Params.amazon_tag` (hugo.toml = 'utexplained-20', single swap point).
   - Full local build (896 pages): 421 clickable Amazon hrefs, ZERO untagged.
   - Live sampling (6 money pages incl. heating-bill, january-electric, water-heater-blankets,
     vue-vs-sense, water-bill-leak): all tagged, all carry data-rybbit-event=affiliate_click.
   - ustxtaddt-20 (old add-to-cart experiment tag): 0 uses in live code — exists only in .squad/.agency artifacts.
   - tag=se (5,293 hits) = saved Amazon search pages in .agency/staging research, not content.
2. The 54 untagged clicks/day originate OFF-SITE. Remaining vectors:
   a. 17 raw untagged Amazon URLs in citation JSON-LD schema (layouts/partials/head.schema.html
      emits frontmatter sources verbatim). AI engines ingest schema; AI-relayed links land untagged.
   b. Manually posted Amazon links off-site (Reddit/social/groups/email) — r/Frugal 1wn9ww4 checked,
      contains none; cannot enumerate the rest from here.
3. Volume anomaly: 62 tagged clicks in ONE day vs 10/11 baseline ~68 clicks/30d (Rybbit affiliate_click
   events). 27x gap. Explanations: click rate surged with winter traffic, a large share of tagged clicks
   is also off-site, or Rybbit undercounts badly. RECONCILIATION BLOCKED: Rybbit API key stale (401 via
   curl) and app.rybbit.io WAF returns 403 to Python urllib clients regardless of UA.
4. Content-phase flags found during sweep:
   - /blog/space-heater-running-cost/ — prime winter buyer page, ZERO affiliate placements.
   - Comparison page citation URL list exposes competitor+product URLs untagged (see 2a).

## Ready-to-ship fixes (awaiting owner go)

- Fix A: head.schema.html appends tag to every amazon.com URL emitted in citation schema; add CI/build
  gate "untagged amazon.com URL anywhere in build = 0" (any context, not just hrefs).
- Fix B (needs fresh Rybbit key): click reconciliation + seasonal page/traffic analysis feeding the
  5-article fall/winter batch.
- Fix C (owner policy): every Amazon link posted anywhere off-site must be built as
  amazon.com/dp/ASIN?tag=utexplained-20; agent generates tagged links on demand.

## Owner asks

1. Fresh Rybbit API key (Settings → API Keys) → ~/.config/rybbit/api_key.
2. Re-export Tracking-Id report for Sep 1 → Oct 28 (today's zips were 1-day views).
3. Disclosure: any Amazon links posted off-site (Reddit/FB/YouTube/email), tagged or raw?

## ROUND 2 — 2026-10-28 evening (key + 2nd export day received)

- Rybbit key: paste had 65 chars (one extra); first 64 authenticate. Fixed in ~/.config/rybbit/api_key.
  WAF still 403s Python urllib; all pulls via curl + browser UA.
- 2nd export day (10/28, partial: order set identical carryover from 10/27): utexplained-20 78 clicks/0
  orders; Other 41 clicks/6 orders. Two-day click volume consistent: 116-119/day total.
- RYBBIT RECONCILIATION (site d5b63e065e9d):
  - Sessions: prior-30d 3,239 → trailing-30d 4,246 (+31%); Sep 3,187 → Oct 1-28 3,842 (+21%).
    (10/11's 6,986 was an early-Oct spike window; normalized since, still growing MoM.)
  - Bounce 87.1→84.2, session duration 126→188s. affiliate_click events 40→61/30d (+52%).
  - events/outbound (30d): 105 Amazon clicks, ALL 105 tagged, 0 untagged. Top non-Amazon: energy.gov 6,
    epa.gov 3, ecobee.com 2, sense.com 1 — no brand-direct leak of consequence.
- VERDICT: ~97% of the account's Amazon click flow (~113-116/day) does NOT originate on the website
  (site produces ~3.5/day). Two off-site flows: tagged 62-78/day @ 0% conversion (relay of tagged links —
  AI assistants citing pages, or mirrors; invisible to search engines) and untagged 41-54/day @ 11-15%
  conversion carrying ALL orders ($455.87/6 items, $10.26 earnings on 10/27). Schema citation URLs were
  the only on-site untagged surface — exactly what AI engines ingest and relay.
- EARNINGS REFRAME: early-Oct implied run-rate was ~$11/mo (68 clicks x $0.165 EPC); 10/27-28 sample
  shows ~$10/day. "Purchases going down" is not supported by any data; attribution invisibility is.
- FIXES SHIPPED (ad7063a1, CI green, live-verified fresh via /index.html; clean-URL CDN copy stale
  briefly): citation schema tags all amazon.com URLs; render hook covers ALL amazon paths (search links
  previously escaped); check_rendered_output.py fails on ANY untagged amazon URL in rendered output.
- Top-pages trailing-30d (for winter plan): lower-electric-guide 1,281pv; 06-water-bill-too-high 449pv
  (132s dwell); sudden-spike-electric ~700pv combined; how-to-read-water-meter 322; electric-bill-
  breakdown 269; water-meter-running 240; CCF 178; sense-energy-monitor-alternatives 118 (62s dwell,
  buyer page). GAS/HEATING NOT IN TOP-25 → winter demand still ahead.
- Open: ranged Associates export (Sep1-Oct28) still owed; owner checking Reddit history for amazon
  links; watch Other-vs-tag split over next 1-2 weeks post-fix.

## ROUND 3 — CORRECTION (2026-10-28 evening, owner dashboard screenshot)

The CSV exports were MONTH-TO-DATE CUMULATIVE rows, NOT single-day windows. Owner's dashboard
(Sep 27 - Oct 28, all tracking IDs): 119 clicks, 6 ordered, 6 shipped, $10.26 total, 5.04% CV.
The 10/28 CSV (119 clicks / 6 items / $10.26) = the full-month total. Supersedes Round 2's
"$10/day / 27x run-rate / ~110 off-site clicks per day" — all WRONG. Corrected picture:

- Month earnings $10.26 ≈ FLAT vs 10/11 baseline (~$11/mo implied) despite sessions +31%.
  "Traffic up, purchases flat" is the true shape of the owner's complaint.
- Month tag split: utexplained-20 78 clicks / 0 orders; Other (untagged) 41 clicks / 6 orders (14.6% CV).
- Site side reconciles cleanly now: Rybbit 105 clicks/30d all-tagged -> Amazon 24h-dedup -> 78 tagged.
  No large off-site flow exists. The 41/mo untagged trickle = AI/schema relay (17 URLs, now fixed)
  + possibly old Reddit links. That trickle carries ALL 6 orders.
- REAL DIAGNOSIS: the on-site funnel converts 0/78 while relayed product-intent converts 14.6%.
  On-site clickers are browsers; buyers currently arrive via product URLs relayed off-site.
  Growth levers: buyer-intent winter content, decision-stage CTAs (cart links), schema fix
  (shipped ad7063a1) so relayed orders at least attribute.
- Dashboard daily bars: earnings landed on ~5 days (Oct 1, 2, 10-11 = biggest, 14-15); $0 otherwise.
  Oct 10-11 spikes immediately follow Track 1+2 ship (10/9-10) — suggestive, not provable (orders
  sit in Other; no per-tag per-day split available).
