# BATCH: Winter Buyer-Intent Wave — 2026-10-28

Trigger: owner directive — 5 new full articles with images, fall/winter seasonal focus,
following the attribution investigation (traffic growing, on-site funnel converting 0/78 —
buyer-intent content is the prescribed lever).

## Topic selection (cannibalization-checked)

Dropped after slug audit: "best space heater for one room" (42-best exists), "electric bill
high in winter" (aliased to 03-why page), "how to prevent frozen pipes" (exists, 2,127w).
Final five — all verified distinct intents with existing cluster gaps:

| # | Slug | Words | Intent | Placements (cart=true) |
|---|------|-------|--------|------------------------|
| 1 | best-smart-thermostats-winter-savings | 2,536 | buyer comparison | Amazon B08J4C8871, ecobee Essential B0DT9MC2Z9, ecobee Premium B09XXS48P8, Nest 4th B0D5BBYRJM (all 4 cart) |
| 2 | heat-tape-vs-pipe-insulation | 2,366 | decision-stage | heat tape B0HB3Z851P + Frost King B017ISQYE2 (cart) |
| 3 | cheaper-to-heat-one-room-vs-whole-house | 2,260 | cost-economics | Dreo B0B3MXGBVT (box) + Kill A Watt inline |
| 4 | what-temperature-thermostat-winter | 2,107 | settings guide | ecobee Essential box (no cart; links #1 for decision) |
| 5 | christmas-lights-electricity-cost | 2,336 | cost + buyer | GE LED C9 B081DNT98S + Kasa KP115 B08LN3C7WK (cart) |

## Verification ledger

- ASINs: all verified against live/indexed Amazon listings Oct 2026 (B0HB3Z851P reused from
  existing site placement). No fabricated ASINs or prices (price classes, not exact prices).
- Math: 19/19 machine-checked figures (rate 18.31c/kWh Jul-2026 EIA, gas $1.92/therm Sep-2026
  — both match site stats.yaml).
- Internal links: 57 links across the 5 articles — 0 dead, 0 self-referential, 0 .md links.
  Inbound: 9 links added from 7 existing pages (incl. the 1,281-pv lower-your-bill guide).
- Sources: all frontmatter sources curl-verified or reused from site-vetted lists (DOE pages
  via existing archive.org snapshots; ESFI verified live; Red Cross verified 200).
- FAQ: balanced shortcodes; FAQPage JSON-LD confirmed in rendered HTML (head.schema partial).
- Images: 3/article via Magica nano-banana-2-1 (2K heroes, 1K supportings) → webp; vision-QA
  gate per image (no legible text, concept reads, no artifacts).
- llms.txt: 129 → 134 entries.
- Build: 923 pages, gate check_rendered_output.py PASS (zero untagged Amazon URLs — the new
  attribution gate from ad7063a1 holds on the new content).

## Gotchas logged this batch

- Magica model bump: nano-banana-2-text → nano-banana-2-1-text (old ID rejected by MCP);
  generate takes resolution TIERS (1K/2K/4K) + aspect_ratio strings.
- RunIDs are ALPHANUMERIC — the pipeline skill's hex-only regex `([a-f0-9-]+)` truncates them
  and get_run_status returns "Run not found" (looks like a stuck run; it's a parsing bug).
- Actual gen time ~45-60s/image at 2K, 0.077 credits each; no rate-limit pause needed at
  natural 60-90s spacing.
