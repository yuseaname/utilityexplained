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
