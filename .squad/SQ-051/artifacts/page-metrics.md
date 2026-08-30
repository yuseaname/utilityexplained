# SQ-051 — Per-Page Content Metrics (30 pages by Rybbit 30d traffic)

One row per page, in traffic order. All counts derived from the markdown source
at `content/blog/<slug>.md`. Columns: **words** = `wc -w` on the full file; **H2/H3** =
Markdown level-2/level-3 headings in the body; **title_len** = frontmatter `title` chars
(strip quote marks); **meta_desc_present/len** = frontmatter `description`; **outbound_http** =
`http(s)://` links in the body excluding `utilityexplained.com` and `/assets/` images; **internal_body** =
relative `/blog/<slug>` contextual links in the body; **images/missing_alt** = `<img>` tags and those
lacking an `alt=` attribute; **quick_answer** = presence of a `## Quick Answer` section; **dated_update** =
frontmatter `updated` (else `date`); **author** = frontmatter `author`.

| # | slug | words | H2 | H3 | title_len | meta_desc_present | meta_desc_len | outbound_http | internal_body | images | missing_alt | quick_answer | dated_update | author |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | how-to-lower-electric-bill-complete-guide | 4098 | 13 | 30 | 58 | y | 112 | 5 | 24 | 0 | 0 | y | 2026-08-28 | "David Chen" |
| 2 | 30-sudden-spike-in-electricity-bill-no-usage | 3895 | 17 | 0 | 71 | y | 177 | 3 | 9 | 0 | 0 | n | 2026-08-28 | "Tanya Patterson" |
| 3 | how-sewer-charges-work-on-your-water-bill | 1600 | 9 | 9 | 50 | y | 125 | 4 | 5 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 4 | water-meter-running-when-no-water-used | 1299 | 9 | 5 | 65 | y | 164 | 2 | 9 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 5 | what-is-ccf-on-a-water-bill | 1621 | 10 | 0 | 68 | y | 188 | 1 | 5 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 6 | 28-utility-reconnection-fee-explained | 1754 | 10 | 9 | 43 | y | 155 | 3 | 2 | 0 | 0 | y | 2026-08-28 | "Tanya Patterson" |
| 7 | water-meter-leak-indicator-explained | 1768 | 10 | 0 | 92 | y | 145 | 1 | 3 | 0 | 0 | n | 2026-08-28 | "Margaret Harrington" |
| 8 | 06-water-bill-too-high | 1176 | 6 | 2 | 52 | y | 156 | 4 | 6 | 0 | 0 | y | 2026-08-28 | "Tanya Patterson" |
| 9 | 05-how-to-lower-utility-bills | 1199 | 8 | 0 | 43 | y | 164 | 5 | 6 | 0 | 0 | y | 2026-08-28 | "David Chen" |
| 10 | 23-utility-billing-cycle-explained | 1355 | 9 | 6 | 53 | y | 139 | 3 | 8 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 11 | electric-bill-breakdown-understanding-line-items | 2146 | 11 | 1 | 47 | y | 205 | 4 | 2 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 12 | 03-why-is-my-electric-bill-so-high | 1466 | 8 | 3 | 69 | y | 121 | 7 | 2 | 0 | 0 | y | 2026-08-28 | "Tanya Patterson" |
| 13 | 07-gas-bill-too-high | 4029 | 10 | 19 | 68 | y | 170 | 4 | 25 | 0 | 0 | y | 2026-08-28 | "Tanya Patterson" |
| 14 | 25-utility-bill-taxes-fees-franchise-charges-explained | 467 | 5 | 0 | 62 | y | 138 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 15 | stormwater-fee-on-water-bill-explained | 3034 | 0 | 0 | 43 | y | 160 | 0 | 4 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 16 | average-utility-bills-by-state-2026 | 2666 | 1 | 0 | 54 | y | 115 | 4 | 0 | 2 | 0 | n | 2026-08-28 | "Margaret Harrington" |
| 17 | average-water-usage-per-person | 524 | 5 | 0 | 52 | y | 159 | 2 | 5 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 18 | how-do-smart-meters-work | 1057 | 1 | 0 | 54 | y | 128 | 2 | 4 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 19 | 19-utility-bill-surcharges-and-riders-explained | 446 | 5 | 0 | 53 | y | 135 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 20 | mcf-vs-ccf-vs-therms-on-gas-bill | 2830 | 0 | 0 | 67 | y | 158 | 0 | 0 | 0 | 0 | n | 2026-08-28 | "Margaret Harrington" |
| 21 | why-your-electric-bill-keeps-rising-2026 | 2406 | 1 | 0 | 58 | y | 120 | 0 | 9 | 2 | 0 | y | 2026-08-21 | "Margaret Harrington" |
| 22 | 49-demand-charges-electricity-bill-explained | 433 | 5 | 0 | 52 | y | 160 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 23 | why-did-my-water-bill-suddenly-increase | 1887 | 3 | 0 | 40 | y | 84 | 2 | 3 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 24 | is-your-toilet-running-leak-test | 1634 | 1 | 0 | 83 | y | 155 | 2 | 11 | 0 | 0 | n | 2026-08-28 | "Margaret Harrington" |
| 25 | 18-fuel-adjustment-charge-on-utility-bill-explained | 452 | 5 | 0 | 56 | y | 127 | 2 | 0 | 0 | 0 | y | 2026-08-28 | "Tanya Patterson" |
| 26 | 27-utility-connection-fee-explained | 412 | 5 | 0 | 44 | y | 146 | 1 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 27 | how-to-read-electric-meter | 1071 | 3 | 0 | 52 | y | 123 | 1 | 1 | 0 | 0 | y | 2026-08-21 | "Margaret Harrington" |
| 28 | how-to-read-a-water-meter | 1487 | 2 | 1 | 52 | y | 79 | 2 | 3 | 0 | 0 | y | 2026-08-21 | "Margaret Harrington" |
| 29 | 08-time-of-use-electricity | 867 | 7 | 1 | 44 | y | 125 | 3 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 30 | tiered-electricity-rates-explained | 488 | 6 | 0 | 51 | y | 144 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |

---

_Generated from grep/wc/awk against content/blog/<slug>.md (full-file wc -w; frontmatter title/description/date/updated/author; body-only img/link counts; outbound excludes utilityexplained.com and /assets; internal excludes /assets and /blog index)._
