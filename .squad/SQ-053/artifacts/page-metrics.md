# SQ-053 — Per-Page Content Metrics (30 pages by Rybbit 30d traffic)

One row per page, in traffic order. All counts derived from the markdown source
at `content/blog/<slug>.md`. Columns: **words** = `wc -w` on the full file; **H2/H3** =
Markdown level-2/level-3 headings in the body; **title_len** = frontmatter `title` chars
(strip quote marks); **meta_desc_present/len** = frontmatter `description`; **outbound_http** =
`http(s)://` links in the file excluding `utilityexplained.com` and `/assets/` images; **internal_body** =
relative `/blog/<slug>` contextual links in the body; **images/missing_alt** = `<img>` tags and those
lacking an `alt=` attribute; **quick_answer** = presence of a `## Quick Answer` section; **dated_update** =
frontmatter `updated` (else `date`); **author** = frontmatter `author`.

NOTE: this Hugo site stores internal navigation (site nav / in-body contextual links) and images in
template shortcodes (`{{< internalLink >}}`, `{{< visual >}}`, `{{< product-box >}}`), so raw-markdown
`internal_body`, `images`, and `missing_alt` are 0 for every page — same raw-markdown method SQ-051 used.
outbound_http counts every http(s):// link in the file (including the frontmatter `sources:` block) excluding
utilityexplained.com and /assets.

| # | slug | words | H2 | H3 | title_len | meta_desc_present | meta_desc_len | outbound_http | internal_body | images | missing_alt | quick_answer | dated_update | author |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 01-how-to-read-your-electric-bill | 1709 | 11 | 2 | 51 | y | 139 | 14 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 2 | 21-past-due-balance-utility-bill-explained | 536 | 7 | 0 | 50 | y | 148 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 3 | 26-utility-deposit-explained | 501 | 6 | 0 | 43 | y | 140 | 2 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 4 | 14-estimated-utility-bill-explained | 444 | 5 | 0 | 39 | y | 149 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 5 | how-to-read-gas-meter | 3284 | 1 | 0 | 75 | y | 163 | 0 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 6 | water-service-charge-explained | 1425 | 0 | 0 | 84 | y | 144 | 0 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 7 | 43-understand-natural-gas-bill-charges | 440 | 5 | 0 | 46 | y | 134 | 4 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 8 | 17-what-is-customer-charge-on-utility-bill | 418 | 5 | 0 | 49 | y | 155 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 9 | 11-understanding-kwh-usage | 1281 | 10 | 0 | 45 | y | 144 | 12 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 10 | sewer-averaging-water-bill-explained | 924 | 1 | 0 | 74 | y | 131 | 2 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 11 | complete-guide-understanding-utility-bill | 922 | 9 | 0 | 56 | y | 160 | 6 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 12 | 16-budget-billing-level-pay-explained | 1024 | 8 | 3 | 43 | y | 143 | 4 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 13 | why-is-my-water-bill-higher-in-winter | 846 | 2 | 0 | 54 | y | 134 | 4 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 14 | 20-utility-bill-proration-explained | 484 | 5 | 0 | 43 | y | 149 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 15 | why-is-my-water-bill-higher-in-summer | 1280 | 1 | 0 | 78 | y | 153 | 0 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 16 | tiered-water-rates-explained | 3092 | 0 | 0 | 68 | y | 148 | 0 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 17 | 44-how-to-lower-water-bill | 1758 | 6 | 5 | 28 | y | 173 | 6 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 18 | moving-utilities-checklist | 2451 | 10 | 0 | 71 | y | 207 | 0 | 0 | 0 | 0 | y | 2026-08-19 | "Margaret Harrington" |
| 19 | why-did-my-utility-bill-go-up-this-month | 923 | 1 | 0 | 67 | y | 147 | 2 | 0 | 0 | 0 | n | 2026-08-21 | "Marcia Washington" |
| 20 | 24-delivery-charge-vs-supply-charge-utility-bill | 424 | 5 | 0 | 60 | y | 154 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Marcia Washington" |
| 21 | how-to-lower-electric-bill-without-solar | 587 | 7 | 0 | 58 | y | 153 | 6 | 0 | 0 | 0 | y | 2026-08-23 | "Margaret Harrington" |
| 22 | 12-how-to-read-your-gas-bill | 1083 | 8 | 2 | 25 | y | 145 | 8 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 23 | 50-best-smart-plugs-standby-power | 1794 | 9 | 3 | 39 | y | 145 | 12 | 0 | 0 | 0 | y | 2026-08-28 | "David Chen" |
| 24 | gas-delivery-charge-vs-supply-charge | 3118 | 0 | 0 | 68 | y | 159 | 0 | 0 | 0 | 0 | n | 2026-08-21 | "Margaret Harrington" |
| 25 | 22-minimum-bill-utility-bill-explained | 445 | 5 | 0 | 48 | y | 158 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 26 | can-utility-shut-off-service | 3002 | 11 | 0 | 77 | y | 169 | 0 | 0 | 0 | 0 | y | 2026-08-19 | "Tanya Patterson" |
| 27 | 46-what-time-is-electricity-cheapest | 966 | 6 | 0 | 34 | y | 136 | 6 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 28 | 10-fixed-vs-variable-utility-rate | 860 | 6 | 1 | 39 | y | 154 | 8 | 0 | 0 | 0 | y | 2026-08-28 | "Margaret Harrington" |
| 29 | how-to-dispute-utility-bill | 603 | 7 | 0 | 36 | y | 164 | 4 | 0 | 0 | 0 | y | 2026-08-23 | "Tanya Patterson" |
| 30 | 09-apartment-utilities-cost | 908 | 7 | 1 | 37 | y | 134 | 3 | 0 | 0 | 0 | y | 2026-08-28 | "Marcia Washington" |

_Generated from line-split frontmatter parsing (title/description/date/updated/author) and file-wide img/link counts. outbound excludes utilityexplained.com and /assets; internal counts raw /blog/ http links; images/missing_alt count raw <img> tags._
