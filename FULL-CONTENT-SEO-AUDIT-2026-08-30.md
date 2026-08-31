# Full Content, SEO & UX Audit — utilityexplained.com
**Date:** 2026-08-30 · **Scope:** all 114 source pages (89 blog + 25 core) · Eight-seat wave-1 evidence, wave-2 synthesis

## 0. Audit Scope & Method

This audit covers **all 114 markdown pages** of utilityexplained.com read directly from source (89 blog posts + 25 core/system pages incl. hubs, author pages, policies, home, blog index, search). Every rating below traces to a per-seat entry in `.squad/SQ-065/wave1/`; per-page detail (purpose, quoted weaknesses, sources, evidence) lives there, not here. This report is the synthesis: verdicts, patterns, priorities, and actions.

**Seat coverage (8 dispatches, full census):** 12 money+flagship pages — lieutenant; 22 bills/fees cluster — prospector (incl. 13-pair overlap map); 14 journey pages — tracer (pathway graph, dead ends); 19 HVAC/efficiency — prospector#2 (mason artifact); 22 water/rates — cartographer Part B; 25 core — lieutenant#2 (cartographer-core) with double-coverage from cartographer Part A; 12-page judgment sample + AI-slop patterns — twin_q; 10 site claims re-derived against primary sources — verifier/twin_q claims rescue. Original cartographer (25.7K, Parts A–C) and original mason seats died of protocol failure; every slice was rescued and covered. prospector#3 died redundant (Part B already covered its slice).

**Verified site facts:** production sitemap is **healthy — 121 URLs** (89 posts + 6 author + 7 category + 18 core + home); the reported "1 URL" was a `grep -c` line-count artifact on single-line minified XML, re-verified live. Analytics (Rybbit, 7d): 867 sessions, 1.14 pages/session, **91% bounce**, ~65s dwell, Bing-heavy, Google ≈ 0. All audited money links carry rel=sponsored/nofollow; zero broken internal links (302 content hrefs checked; aliases resolve).

**Tooling caveats (material to any re-audit):** (1) `.squad/content-metrics.md` counts only markdown `##` headings and `](/…)` links — pages using HTML `<h2>/<h3>`/`<a href>` or `{{< ref }}` shortcodes are **falsely flagged "0 h2 / 0 ilinks"** (e.g. ac-running-but-not-cooling shows 0/0 but has 14 H2 sections + links). The three true dead ends (net-metering-explained, ev-charging-impact-electric-bill, water-service-charge-explained) were **grep-verified as 0 outbound links in ALL formats** — that finding stands; any other "0 ilinks/0 h2" flag must be re-checked before citing. (2) Most "stale-year" flags are legitimate dated primary citations (NIPSCO IURC order Apr 2025, CPSC 2023/2024, San Antonio 2024) with retrieval dates — old citation year ≠ stale content; each was judged individually. (3) Two web claims returned un-verifiable (EIA price-cell XLSX truncation; NIPSCO docket PDF 403) — marked OPEN in §9.

## 1. Executive Summary

**What the site is:** a 114-page Hugo utility-bill explainer site with genuinely strong primary research — verified tariff line amounts (SMUD, PG&E, ConEd, Austin), tariff-first verification methods, worked arithmetic, a real corrections log with figures and retrieval dates, and honest AI-assistance disclosure. Its best pages (42-best-energy-efficient-space-heater 9/10, do-home-energy-monitors 9/10, ductless-mini-split 9/10, 48-heat-pump-vs-gas-furnace 9/9) are better than the genre's median by a wide margin.

**What it is not yet:** a site search engines can trust at scale or readers can journey through. The evidence shows three systemic problems: (1) **credibility leaks on the money pages themselves** — two claims refuted against primary sources, an impossible stacked-savings promise, a silently-dropped frontmatter sources block, and a fee table claimed as "verified" with no checkable source; (2) **structural template slop** — the Quick-Answer→echo→FAQ triple-telling, batch-dated (2025-12-25) old-cohort intros, and link-stuffed sentences, which is the likeliest driver of the 91% bounce together with Quick-Answer query satisfaction; (3) **a broken journey graph** — two absolute dead-end pages, a third confirmed later, a 9/10 apex hub that never links to the site's own dispute/shutoff/assistance pages, and ~85–88% of posts that never link up to their hub. The site's most valuable cluster (Savings & Efficiency — the strongest money pages) has **no hub at all**.

**Highest-leverage moves (in order):** fix the two refuted claims and the complete-guide arithmetic/frontmatter defects (days of work, removes the site's worst credibility exposure); wire the act-cluster edges and revive the dead ends (dozens of single-line edits that convert bounce into session depth); merge the two proven cannibalization pairs (gas-delivery→12, kWh pair); rewrite the five briefed weak pages (§8); build the Savings & Efficiency hub; and complete the author-honesty arc (named humans or pure desk labels) before Google's helpful-content systems finish de-rating the persona layer. None of this requires new content volume; it requires repair, wiring, and five rewrites.

## 2. Critical Issues (severity-ranked)

**C1 — REFUTED claim on a money page (FIX NOW).** 05-how-to-lower-utility-bills claims water-heater blankets cut standby loss "~25% per DOE." DOE/Energy Star cap blanket savings at **4–9%** of water-heating energy; ~25% applies only to pre-1980s uninsulated tanks (claims-verification #5, energy.gov, retrieved 2026-08-30). The page sits in the savings cluster and contradicts sister pages (07 says 5–10%, the guide 4–7%) — three figures for one fix across three money pages.

**C2 — REFUTED claim + internal contradiction on 07-gas-bill-too-high.** Quick Answer says heating is "40–50% of household gas"; Cause 1 says "60–70%", both cited to the same source. EIA RECS: space heating ≈ **40–45%** of residential gas (claims-verification #7). The 60–70% figure is refuted; the page cites one source for two numbers.

**C3 — Broken frontmatter on the revenue-core guide.** how-to-lower-electric-bill-complete-guide.md has a **duplicate `sources:` key** (lines 8 and 19); Hugo silently keeps one block, so the body's "see Sources in the frontmatter" promise is unreliable and any schema/frontmatter consumer is non-deterministic (grep-verified, live render confirmed build).

**C4 — Impossible savings arithmetic on the flagship.** The same guide's section banners sum to **$200–$450/month** against its own $164.88 average bill; two phantom-load tables on the same page disagree (console $22–30 vs $15–25/yr; totals $75–220 vs $50–100/yr); thermostat savings band conflicts with 07's. The page cannot be executed as written; this is the site's most visible overpromise and a spam-classifier smell.

**C5 — Unverifiable "verified" claim (28-utility-reconnection-fee).** The state fee table claims "verified via state PUC dockets 2024–2026" with **no checkable URL**, contradicting the cluster's own doctrine (27: "do not rely on a national fee range"); winter-moratorium claims conflict with 21's statute-cited Minnesota rules. UNVERIFIED by claims verification (#8).

**C6 — Three absolute dead ends.** net-metering-explained, ev-charging-impact-electric-bill, water-service-charge-explained have **zero outbound internal links in any format** (grep-verified). All three receive inbound traffic paths (net-metering: 3 inbound; ev: 2 inbound incl. from 03) and send every reader off-site. Two of them are the site's only solar/EV pages — its forward-look topic is stranded.

**C7 — Visible rendering breakage.** aux-heat-vs-emergency-heat-meaning.md has truncated `<h2 id="the-problem">The problem: \` and `<h2 id="emergency-heat">…when it` — broken headings render on the live page. gas-vs-electric-heating has a malformed nested-markdown link at top.

**C8 — Title/count/payback contradictions on 07.** Title says "10 Causes"; body numbers causes 1–11; furnace payback appears as 5–8y, 3–8y, and ~23y (the page's own worked example) in one article.

**C9 — Persona/E-E-A-T exposure.** Five named author personas are not real people (disclosed, creditably), but About names no operator, Terms states no principal place of business, one persona carries 43/89 bylines, and bios retain credentials-style framing. Currently honest; still a latent de-ranking liability for money-adjacent queries.

**C10 — Safety/financial warning gaps (narrower than first reported).** which-rate-plan advises variable-rate commitments without a financial-risk disclaimer (verified). But the two safety cases were overstated by wave-1 and are corrected here: 47-check-energy-leaks never mentions panel-opening (0 occurrences; it already carries DIY-limit warnings and describes only non-contact breaker observation) and 13-ac-short-cycling explains capacitor testing with warnings in place. Remaining action: verify the existing warnings render prominently; add the which-rate-plan financial disclaimer.

**C11 — Batch-generation fingerprint.** Many old-cohort posts share date: 2025-12-25 with bulk updated: 2026-08-21 stamps; Phantom-Philosophy intros (aux-heat, afue) are a machine fingerprint; Quick-Answer echo blocks repeat every answer 3×.

**C12 — Cannibalization and drift.** 13 adjudicated fees-cluster overlap pairs (top: gas-delivery→12, ~70% duplication); 11-understanding-kwh vs what-is-a-kilowatt-hour (~50%); lower-electric-bill trio; 09-apartment's state table duplicates average-utility-bills-by-state; site-wide drift on EPA leak-gallons (9,400 vs 10,000+/9,300) and 03's anchor misdescribing 42's thesis.

## 3. Page-by-Page Content Audit — Master Table (all 114 pages)

*One compact row per page. Full per-seat entries — purpose, quoted evidence, sources, visual notes — live in `.squad/SQ-065/wave1/`: lieutenant-pages.md (money+flagship), tracer-journey.md (journey), prospector-pages.md (fees), mason-pages.md (HVAC), cartographer-map.md (water/rates B1–B22), cartographer-core.md (25 core). Ratings are Quality/SEO 1–10; Q·S = both. Where two seats rated the same page, the range is shown with both cited (see reconciliation note at end of table).*

### 3A. Money & Flagship (12) — detailed entries: wave1/lieutenant-pages.md

| Path | Intent | Q·S | Action |
|---|---|---|---|
| /blog/42-best-energy-efficient-space-heater/ | Commercial-investigation, anti-listicle physics + safety checklist | 9·7 | keep→improve: add product box for recommended model; fire-stat chart; decide slug tension |
| /blog/do-home-energy-monitors-save-money/ | Commercial-investigation by device class (CT/plug-in/app) | 9·7 | keep→improve: make Emporia-vs-Sense table real; soften unverified "reconcile close" claim |
| /blog/point-sensor-vs-whole-home-water-leak-when-to-upgrade/ | Decision ladder: point→meter→inline shutoff | 8·7 | keep (light): faq-schema; replace Amazon-listing sources; canonical leak-gallons w/ 06; price-check date chip |
| /blog/do-thermal-curtains-really-work/ | Informational w/ affiliate endpoint; tiered evidence | 8·7 | keep: anchor tier-3 claim to a named SKU; score pick vs 4 fit rules; orphan (1 inbound) — link from seal-drafts + 42 |
| /blog/06-water-bill-too-high/ | Water diagnostic anchor (ranked causes, tests-first) | 8·8 | keep: add one non-EPA source; cite or drop 105 dB; probability-vs-cost quadrant chart |
| /blog/01-how-to-read-your-electric-bill/ | Read-your-bill cornerstone (zero commerce) | 8·8 | improve (light): delete duplicated transition ¶; cap breakdown links at 2; worked-bill table |
| /blog/03-why-is-my-electric-bill-so-high/ | Electric diagnostic anchor | 7–8·7–8 | improve: fix 42 anchor (mischaracterizes thesis); dedupe sources; verify task-list rendering; add act edges (§6) |
| /blog/how-to-lower-electric-bill-complete-guide/ | Savings flagship ("20+ ways", 4 boxes, heaviest linking) | 7·7 | improve (URGENT): fix dup `sources:` key (C3); rebuild stacked-percentages math (C4); reconcile phantom tables; move post-FAQ Emporia box; renumber "20+" |
| /blog/07-gas-bill-too-high/ | Gas diagnostic anchor (3,892w, 29 ilinks, 10 FAQs) | 6·7 | improve (URGENT): 10-vs-11 causes; 60–70% REFUTED (C2); payback trio 5–8/3–8/~23y; 2 mislabeled + 2 dup sources; cite or cut EIA rate claim; annotated gas-bill image |
| /blog/05-how-to-lower-utility-bills/ | Cross-utility savings prioritizer (8 tables) | 6·5 | improve (URGENT): blanket ~25%→4–9% (C1, REFUTED); air-sealing row mis-cite; retitle vs "20+ ways" anchor expectation; payback-ladder visual; else merge into guide |
| /blog/do-programmable-thermostats-cut-heating-bills/ | Commercial: DOE setback math vs product costs | 7·6 | improve: fix mislabeled DOE→ENERGY STAR source; 3–5 internal links; FAQ+schema; annotated setback-schedule graphic |
| /blog/50-best-smart-plugs-standby-power/ | Intent split-brain: "50 best" slug vs measure-first body | 7·5 | improve: 301 to honest standby-power slug OR build genuine list; cut 1 of 3 redundant process sections; ASINs out of spec table; scope-divide w/ phantom-power; meter diagram |

### 3B. Journey Cluster (13 tracer entries + 1 twin_q-audited page; 03's row lives in 3A) — detailed entries: wave1/tracer-journey.md, twinq-verdict.md

| Path | Intent | Q·S | Action |
|---|---|---|---|
| /blog/complete-guide-understanding-utility-bill/ | Apex pillar: 5-step verify workflow, charge map (28 ilinks) | 9·9 | improve (TOP FIX): add 4 act-cluster links from "When to escalate safely" — dispute, shutoff, assistance, rate-plan |
| /blog/average-utility-bills-by-state-2026/ | State-rate benchmark (vanity-metric risk) | 6·6 | improve/noindex-decision: twin_q 4th-weakest page — consolidate toward calculator/interactive map or add per-state action; **provenance: twin_q 12-sample audit; tracer examined links only per packet** |
| /blog/30-sudden-spike-in-electricity-bill-no-usage/ | Deepest diagnostic: 10-cause table + 12-step investigation | 9·8 | keep (minor): add 04-hidden-fees edge + shutoff edge near dispute path |
| /blog/electric-bill-breakdown-understanding-line-items/ | Line-item hub (18 ilinks, 9 FAQs) | 8·8 | keep (minor): add complete-guide link; add which-rate-plan to TOU section |
| /blog/moving-utilities-checklist/ | Move planning/deposits/meter reads | 8·8 | keep — best-wired plan page; optional direct dispute link |
| /blog/can-utility-shut-off-service/ | Crisis action page (protections, deadlines) | 8·8 | keep — best-wired act page |
| /blog/how-to-dispute-utility-bill/ | Escalation ladder, template letter, state PUCs | 8·8 | improve: link internal utility-assistance-programs-liheap (external liheap.org only today); add 03/30 backlinks |
| /blog/ev-charging-impact-electric-bill/ | Forward EV: cost math, TOU planning, charger hardware | 7·4 | **DEAD END (C6):** 0 outbound links in any format — add which-rate-plan, 08-TOU, 46, 49-demand, energy-monitors links urgently |
| /blog/why-did-my-utility-bill-go-up-this-month/ | Month-over-month cause ranking (HTML body) | 6·6 | improve: add dispute/rate-plan edges; replace wrong-target alias link (why-electric-bill-changes→03) |
| /blog/utility-assistance-programs-liheap/ | Assistance hub (LIHEAP/WAP, Day-1 crisis actions) | 7·7 | improve: link can-utility-shut-off-service from Emergency section (crisis loop 2/3 wired) |
| /blog/how-to-budget-for-utilities-in-your-first-apartment/ | First-apartment budgeting/deposits | 7·7 | improve: add which-rate-plan + utility-assistance edges |
| /blog/which-rate-plan-is-right-for-me/ | Plan decision page (thin, 702w) | 7·8 | improve: link ev-charging from Decision List #1 (mentions EV overnight); add worst-case summer math; disclaimer (C10) |
| /blog/net-metering-explained/ | Solar forward: NEM 2.0/3.0, export crediting | 6·4 | **DEAD END + CA-bias:** rebuild link layer (which-rate-plan, 08-TOU, 46, 49, breakdown); split California detail to sub-article |
| /blog/how-utility-rates-fees-usage-work-together/ | Three-bucket model page (808w, HTML body) | 5·5 | CONFLICT adjudicated improve (tracer) over delete/301 (twinq): convert to Markdown headings, add which-rate-plan edge; if unimproved next pass, 301 to electric-bill-breakdown |

### 3C. Bills & Fees Cluster (22) — detailed entries: wave1/prospector-pages.md

| Path | Intent | Q·S | Action |
|---|---|---|---|
| /blog/17-what-is-customer-charge-on-utility-bill/ | Verify one line; strongest original data in cluster | 9·8 | keep: canonical fixed-charge amounts; 22/24 should link here for those facts |
| /blog/23-utility-billing-cycle-explained/ | Billing-cycle understanding, daily-average method | 9·8 | keep: trim estimate section to summary → link 14; cluster linking spine |
| /blog/24-delivery-charge-vs-supply-charge-utility-bill/ | Two-bucket bill model, verified per-utility split | 9·8 | keep: electricity canonical; cross-link gas version; verify EIA stats |
| /blog/14-estimated-utility-bill-explained/ | Estimated-read diagnostic, force-actual workflow | 9·7 | keep: de-dup trigger tables w/ 23 (keep 14 as specialist) |
| /blog/21-past-due-balance-utility-bill-explained/ | Prevent-shutoff action; verified MN/TX statutes | 9·7 | keep: canonical LIHEAP/assistance block for 26/27/28 to link to |
| /blog/04-hidden-fees-utility-bill/ | Fees cluster hub; 7-row taxonomy | 9·7 | keep (hub): rename slug to match H1 w/ redirect; keep table summary-level |
| /blog/10-fixed-vs-variable-utility-rate/ | Plan comparison, deregulated-state shopping | 9·7 | keep: cite or soften ETF range; link which-rate-plan |
| /blog/25-utility-bill-taxes-fees-franchise-charges-explained/ | Tax/fee/franchise authority matrix | 8·7 | keep: keep 19/25 boundary explicit; add a state-cap teaser if later content exists |
| /blog/18-fuel-adjustment-charge-on-utility-bill-explained/ | Tariff-first fuel-line verification | 8·7 | keep: preserve 18/19 mechanism-vs-line-item split |
| /blog/26-utility-deposit-explained/ | Deposit rules, caps, waivers, refund timing | 8·7 | keep: add state PUC complaint-path link |
| /blog/27-utility-connection-fee-explained/ | Service-start fee verification + fee-router | 8·7 | keep: refresh SRP pricing points; extend fee-router to 26/28 |
| /blog/16-budget-billing-level-pay-explained/ | Level-pay mechanics + worked 12-mo example | 8·6 | improve: fix incomplete frontmatter sources; category→Bills & Fees; add FAQ |
| /blog/22-minimum-bill-utility-bill-explained/ | Minimum-charge floor w/ verified clauses | 8·7 | keep: add floor-vs-usage chart; canonicalize PG&E restructure fact (w/ 17) |
| /blog/46-what-time-is-electricity-cheapest/ | Quick-reference TOU hours answer | 8·7 | keep: strong 08 handoff already in place |
| /blog/12-how-to-read-your-gas-bill/ | Gas bill walkthrough, therm/CCF math (merge target) | 8·7 | improve/merge-target: absorb gas-delivery page as deep-dive section (301) |
| /blog/20-utility-bill-proration-explained/ | Partial-period billing + SMUD tariff rule | 8·7 | keep: add calendar graphic |
| /blog/19-utility-bill-surcharges-and-riders-explained/ | Rider mechanism w/ named real riders | 8·7 | keep: add per-row source links |
| /blog/49-demand-charges-electricity-bill-explained/ | Demand-charge verification (kW vs kWh, ratchet) | 7·7 | improve: fix duplicate source line; add "does this apply to me" residential gate |
| /blog/11-understanding-kwh-usage/ | kWh on the bill, appliance cost context | 8·7 | improve: dedupe vs what-is-a-kilowatt-hour (§2 C12 merge pair) |
| /blog/gas-delivery-charge-vs-supply-charge/ | Gas two-bucket explainer | 8·7 | **MERGE → 12** (~70% duplication, top overlap pair); preserve correction note; 301 |
| /blog/09-apartment-utilities-cost/ | Renter budget guide (thin, 98 lines) | 6·6 | improve: cut state table to 3 rows + link state page; add FAQ (RUBS, sub-metering); visual; else risk noindex for thinness |
| /blog/28-utility-reconnection-fee-explained/ | Reconnection fee + restoration process | 6·5 | improve-or-rewrite: strip/add citations to "verified" table (C5); align moratorium w/ 21; cite restore timings |

### 3D. HVAC & Efficiency Cluster (19) — detailed entries: wave1/mason-pages.md

| Path | Intent | Q·S | Action |
|---|---|---|---|
| /blog/ac-running-but-not-cooling/ | Panic troubleshooting, 13 causes, safe fixes | 9·8 | keep (do NOT rebuild — metrics "0/0" is a tools artifact; convert HTML→Markdown headings for parity) |
| /blog/why-is-my-furnace-blowing-cold-air/ | Safety-first furnace troubleshooting, 15-min table | 9·9 | keep — optional CO-alarm placement diagram |
| /blog/ductless-mini-split-vs-central-air/ | System purchase comparison, 17 sources | 9·8 | keep/improve: fix source-order swap; add zone-cost chart |
| /blog/48-heat-pump-vs-gas-furnace-savings/ | Decision math w/ breakeven formula | 9·9 | keep/improve: add breakeven-ratio chart; retrieval-date note for rate figures |
| /blog/what-merv-rating-do-i-need/ | Filter purchase guide | 9·8 | keep — but orphan (2 inbound): add to HVAC hub library (missing today) |
| /blog/47-check-energy-leaks-home-diy/ | DIY energy audit walk-through | 9·8 | keep: warnings already present and DIY-limited — verify they render prominently (C10 corrected) |
| /blog/how-to-find-and-seal-drafts-in-your-home/ | Draft detection + sealing methods | 9·8 | keep: should link thermal-curtains + 42 (orphan repair) |
| /blog/13-ac-short-cycling-causes-fixes/ | AC short-cycle diagnostic (Record-Pattern method) | 8·8 | improve: add FAQ block; verify capacitor-testing warnings render prominently (C10 corrected) |
| /blog/duct-leaks-symptoms-hvac-running-all-day/ | Duct symptom list + CFM25 test explainer | 9·8 | keep — metrics ilinks=0 is a `{{< ref }}` artifact |
| /blog/what-is-a-kilowatt-hour/ | Foundational kWh definition + calculator | 8·8 | keep/improve: dedupe decision vs 11-understanding-kwh (§2 C12); add example-equivalences visual |
| /blog/how-do-smart-meters-work/ | Meter tech + trust/verification explainer | 8·8 | keep: convert HTML headings for tooling parity |
| /blog/phantom-power-draw-explained/ | Standby-power education/audit | 8·7 | improve: add FAQ block; scope-divide vs 50-best-smart-plugs |
| /blog/45-whole-house-generator-vs-portable-cost/ | Generator decision, CO safety emphasis | 8·7 | keep/improve: verify 4 stale-year refs; add CO-placement diagram |
| /blog/single-stage-vs-two-stage-vs-variable-speed-hvac/ | Staging buyer education | 8·7 | improve: add FAQ block; cite humidity ranges; orphan (2 inbound) — add to HVAC hub library |
| /blog/afue-vs-seer-vs-hspf-vs-cop/ | Ratings explainer (legacy cohort) | 7·6 | rebuild: add ratings matrix table, 2+ sources (ENERGY STAR/AHRI), drop link-stuffing (Pattern C); link 48/ductless |
| /blog/gadgets-that-lower-utility-bills/ | Gadget purchase guidance | 7·7 | improve: title/slug promises "lower," content delivers "understand" — realign; add FAQ; orphan (2 inbound) |
| /blog/gas-vs-electric-heating-cost-comparison/ | Gas-vs-electric cost comparison (legacy) | 6·6 | **MERGE → 48-heat-pump-vs-gas-furnace-savings** (1 source, broken nested link, HTML table, AFUE inconsistency) — or rebuild w/ 6–8 sources + rate chart |
| /blog/heat-pump-running-all-day-in-winter/ | Runtime reassurance diagnostic (958w) | 6·7 | improve: extend w/ runtime-vs-temp data; fix weak Related-Reading tail |
| /blog/aux-heat-vs-emergency-heat-meaning/ | Two-mode thermostat explainer (legacy) | 6·8 | improve (render bugs, C7): fix 2 truncated H2s; de-slop intro (Pattern A); thermostat-label mockup |

### 3E. Water, Rates & Meters (22) — detailed entries: wave1/cartographer-map.md (B1–B22)

| Path | Intent | Q·S | Action |
|---|---|---|---|
| /blog/08-time-of-use-electricity/ | TOU mechanism explainer (cluster anchor) | 8·8 | keep — includes corrections-log ConEd TOU fixes |
| /blog/44-how-to-lower-water-bill/ | Water savings guide (stormwater alias target) | 7·8 | improve: add printable checklist; hub link |
| /blog/tiered-water-rates-explained/ | Water tiering canonical | 8·8 | keep: pair with tiered-electricity cross-cluster |
| /blog/what-is-ccf-on-a-water-bill/ | Water unit anchor (12 inbound) | 8·7 | keep: the water CCF canonical |
| /blog/water-service-charge-explained/ | Service-charge explainer, strong tariffs | 8·4 | **DEAD END (C6, grep-verified 0 outbound all formats)** + orphan — link from water hub + 17 |
| /blog/why-did-my-water-bill-suddenly-increase/ | Water spike diagnostic | 8·7 | improve: smooth the free→paid product-box transition (twin_q Gap 3) |
| /blog/drought-surcharge-on-water-bill-explained/ | Drought fee mechanisms (EBMUD/SAWS) | 8·3 | ORPHAN (1 inbound): link from water hub + 06 — good content, invisible |
| /blog/mcf-vs-ccf-vs-therms-on-gas-bill/ | Gas unit explainer (3,060w) | 8·7 | keep — CORRECTED (was flagged ORPHAN by a metrics-tool artifact): actually 12 outbound internal links + inbound from 5 files incl. the gas hub and 12; HTML-only links make it read as "0 ilinks" in markdown-only tooling |
| /blog/how-to-read-gas-meter/ | Gas meter reading (2,873w) | 8·7 | keep: low inbound — pair with 12 |
| /blog/tiered-electricity-rates-explained/ | Electric tiering (cross-cluster) | 7·7 | keep: link to water-tier twin |
| /blog/water-meter-leak-indicator-explained/ | Leak-indicator DIY | 7·7 | improve: add sources |
| /blog/water-meter-running-when-no-water-used/ | Meter-flow leak check | 7·7 | keep: add "start here → 06" pointer (leak trio, §6) |
| /blog/is-your-toilet-running-leak-test/ | Toilet dye-test guide | 7·7 | keep: add "start here → 06" pointer (leak trio, §6) |
| /blog/how-to-read-a-water-meter/ | Water meter reading | 7·7 | keep |
| /blog/how-sewer-charges-work-on-your-water-bill/ | Sewer charge mechanics | 7·7 | keep: link sewer-averaging spoke |
| /blog/how-to-lower-electric-bill-without-solar/ | No-solar electric savings (thin, 985w, 10 sources) | 7·8 | MERGE-DECISION: overlaps complete-guide (§2 C12) — merge outward or convert to tools/FAQ page |
| /blog/how-to-read-electric-meter/ | Electric meter reading | 7·7 | keep |
| /blog/average-water-usage-per-person/ | Usage benchmark | 6·6 | improve: strengthen sources (USGS/EIA) |
| /blog/why-is-my-water-bill-higher-in-summer/ | Seasonal usage causes | 6·6 | improve: cross-link winter twin |
| /blog/why-is-my-water-bill-higher-in-winter/ | Seasonal causes (near-orphan, 1 inbound) | 6·4 | improve: cross-link summer twin; link both from 06 |
| /blog/ccf-calculator/ | Unit conversion tool | 6·7 | improve: deepen surrounding text + sources |
| /blog/sewer-averaging-water-bill-explained/ | Sewer averaging (Austin/SAWS) | 7·4 | ORPHAN (2 inbound): link from water hub + sewer article |

**Table reconciliation notes:** (1) 03-why-is-my-electric-bill-so-high rated 7/10 quality by lieutenant (defect list) vs 8/8 by tracer (structure/linking) — both stand; the defect list is the operative one for fixes. (2) ac-running-but-not-cooling, duct-leaks, single-stage, what-is-a-kilowatt-hour, how-do-smart-meters work: mason-corrected ratings supersede any metrics-derived "0 h2/0 ilinks" flags (§0 tooling caveats). (3) water-service-charge-explained counted as a dead end per Commander grep (0 outbound links in all formats), which supersedes the artifact's 4-ilink stat.

### 3F. Core, Hubs, Trust & Author Pages (25) — detailed entries: wave1/cartographer-core.md

| Path | Intent | Q·S | Action |
|---|---|---|---|
| / (home) | Brand front door routing to 4 hubs | 8·7 | improve: "Why trust" strip; feature the two 9/10 money pages in Most Read |
| /blog/ (blog index) | Browse gateway | 6·6 | improve: fix "97 guides" stale count (actual 89); 1-line category intros |
| /about/ | Mission + funding model | 7·6 | improve: name operator entity + location (trust hinge, C9) |
| /contact/ | Error reports/suggestions | 7·5 | keep/improve: add simple form if spam appears |
| /search/ | Client-side search | 6·7 | keep — correctly noindexed, excluded from sitemap (verified) |
| /corrections/ | Public corrections log | 9·6 | keep + feed it — strongest trust page; strip SQ-0xx jargon; link from every Sources block |
| /disclaimer/ | Not-professional-advice limits | 6·4 | keep |
| /privacy-policy/ | Consent-mode, GA4+Rybbit declared | 8·5 | keep — unusually specific, matches live banner behavior |
| /terms/ | Terms of service | 6·4 | improve: name governing-law jurisdiction (pairs with About fix) |
| /affiliate-disclosure/ | Amazon Associates disclosure (ad-free page) | 8·5 | keep: link it from money-page bodies (42, 50, monitors) — FTC hygiene |
| /editorial-policy/ | Method + AI-assistance disclosure | 8·6 | keep + improve: publish review-progress count ("N/89 verified") |
| /editorial-team/ | 5-desk roster + 4-step process | 7·6 | keep + improve: add "why desk bylines" explainer |
| /methodology/ | Sources + formulas + limitations | 8·6 | keep + improve: hyperlink the named EIA/DOE series (description → proof) |
| /author/ (index) | Roster + byline honesty statement | 6·5 | keep + improve: anchor of the byline-policy decision (C9) |
| /author/david-chen/ | Efficiency desk persona | 6·6 | improve: desk-label OR real human bio — current half-state is weakest (C9) |
| /author/marcia-washington/ | Affordability desk persona (thinnest) | 5·5 | improve: same decision; add "writes about" section |
| /author/margaret-harrington/ | Bills & Rates desk persona (43/89 bylines) | 6·6 | improve: same; single point of trust failure — resolve C9 first |
| /author/roberto-mendoza/ | HVAC desk persona | 6·6 | improve: same decision |
| /author/tanya-patterson/ | Consumer-rights desk persona | 6·6 | improve: same; fix gendered-pronoun inconsistency |
| /electricity-explained/ | C1 pillar (2,448w, 23-link library) | 8·7 | improve: swap generic tips list for spoke links; appliance-share chart; fix 2 aliased links |
| /gas-explained/ | C2 pillar (weakest hub: 6 inbound, 9 spokes) | 8·7 | improve: expand library (missing spokes); fix $1.50-vs-$1.91 example; seasonal chart |
| /water-explained/ | C3 pillar (19-link library) | 8·7 | improve: fix stormwater alias slot (points at savings post); indoor-use pie chart |
| /heating-cooling-explained/ | C4 pillar (14-link library) | 8·7 | improve: ADD what-merv-rating + duct pages to library (MERV is a 2-in orphan today); dedupe AFUE example w/ gas hub |
| /utility-bills-costs-explained/ | C5 pillar + biggest router (38 links) | 8·8 | improve: fix duplicate complete-guide entry + 04 anchor mismatch — model hub |
| /utilities-glossary/ | C0 semi-hub (30+ term cards, 1,882w) | 7·8 | improve (cheapest big win): make bottom "full guides" list real links (5 hub links currently dead as plain text); first-use term links in thin posts |

## 4. Thin Content & AI-Slop Findings

**Structural fingerprints (twin_q, sampled 12 cross-generation):**

- **Pattern A — "Phantom Philosophy" intros (CRITICAL, old cohort):** the External/Internal/Philosophical tripartite opening ("The external problem is obvious: higher usage. The internal problem is the one that keeps you up… And the philosophical problem is fair: this shouldn't require a dictionary.") — observed verbatim in aux-heat and afue. A machine-writing fingerprint; new cohort (monitors page hook) proves the team writes well without it.
- **Pattern B — "Echo-Bloop" triple-telling (HIGH, sitewide):** hero → Quick Answer bullets → prose paragraph rephrasing the same bullets → FAQ repeating the answer a third time. Hurts scannability, buries diagnostic detail two screens down, and reads as automated repetition to classifiers. 22/22 fees-cluster pages open with the same scaffold (though each carries distinct verified content — the skeleton is templated, not the flesh).
- **Pattern C — link-dense guidance blocks (MEDIUM):** afue's "these guides help" block stacks 6 internal links across consecutive short lines (2 per sentence: "…[winter] and [summer]") — milder than first reported (not 4-links-in-one-sentence), but still a link carpet that exhausts scanners; a plausible minor bounce contributor.
- **Batch metadata:** diverse-topic posts share date: 2025-12-25 with bulk updated: 2026-08-21 edits — the "zombie content revived" fingerprint. Sitemap lastmods confirm a 14-post Dec-2025 batch (AFUE/aux-heat/smart-meter/water-meter family) = rewrite cohort B.
- **Factual hallucination: LOW.** Facts are solid and sourced; the slop is structural, not evidentiary. This is a repair job, not a teardown.

**Thin pages (action per §3 rows; counts from wave-1 word counts):** which-rate-plan (702w, decision page without worst-case math) · how-utility-rates-fees-usage (808w, HTML-structured) · how-to-lower-electric-bill-without-solar (985w, cannibalized by complete-guide) · how-to-budget-first-apartment (1,217w, missing act edges) · ccf-calculator (920w tool with thin support) · heat-pump-running (958w) · 09-apartment (98 lines) · 22-minimum-bill (98 lines but complete) · 46-what-time (80 lines but earns its URL as an answer page). Thinness judged by purpose coverage, not word count — 46 and 22 show small pages can be complete when scoped honestly.

**Legacy rebuild cohort (old formatting, pre-2026 templates — ranked):** gas-vs-electric-heating (merge→48: broken nested link, HTML tables, 1 source) · afue (rebuild matrix + sources; drop Pattern C links) · aux-heat (render bugs + Pattern A intro) · heat-pump-running (thin) · average-utility-bills-by-state (twin_q: vanity-metric risk — consolidate toward calculator) · plus the dead-end orphans (§6), which are quality pages stranded by zero wiring.

**Cannibalization consolidation (from §2 C12 + prospector 13-pair map, adjudicated by stronger evidence):**

1. **gas-delivery-charge-vs-supply-charge → 12-how-to-read-your-gas-bill** — ~70% duplication (identical SCO worked example + EIA seasonality); preserve the correction note; 301. Top merge.
2. **what-is-a-kilowatt-hour ↔ 11-understanding-kwh-usage** — ~50% overlap; keep kWh page as definition canonical, fold 11's calculator/usage-tracking in, redirect.
3. **how-to-lower-electric-bill-without-solar → how-to-lower-electric-bill-complete-guide** — same SERP intent, 985w vs 3,593w; merge or convert to tools/FAQ page.
4. **05 vs complete-guide** — cross-utility vs electric-only savings: accept guide as the ranking page, scope-banner 05, or merge with a cross-utility section.
5. **09-apartment state table → average-utility-bills-by-state** — keep apartment frame, cut duplicate table, link out.
6. **no-merge pairs** — 24 vs gas-delivery (fuel-specific canonicals; gas side folds into 12); 18/19 (mechanism-vs-line-item, FAQs already route); 26/27 (deposit vs connection, fee-router separates); 14/23 (specialist vs overview — trim 23's estimate section to a link); 18↔19, 20↔23 (20 stays partial-period subset); the three "why is my bill up" angles (03 / 30 / why-did — distinct intents, but why-did must fix its wrong-target alias link); three water-leak angles (meter/indicator/toilet — each needs a "start here → 06" pointer).

**Indexation verdicts summary (per operator's taxonomy):** improve-and-keep-indexed — the large majority (including all 9/10 pages); merge+redirect — gas-delivery, kWh pair, without-solar, (decide) gas-vs-electric; rewrite — 07, 05, 28, net-metering link layer, afue, aux-heat, how-utility-rates (conditional); **noindex candidates** — none forced today; 09-apartment joins the noindex list *only* if its thin-state pass fails; remove — nothing (no page is valueless).

## 5. Visual Content Opportunities (by page — asset · placement · purpose)

The site's visual discipline is already excellent where it exists (42-space-heater, point-sensor, thermal-curtains, seal-drafts are near-model). The pattern in the deficits: **data-bearing pages with zero in-body visuals**, and two pages whose very subject is physical observation with no diagram. No decorative stock anywhere — every asset below carries a job.

| Page | Asset | Placement | Purpose |
|---|---|---|---|
| 42-best-energy-efficient-space-heater | Labeled safety-checklist diagram (tip-over, clearance, outlet) + radiant-vs-convection "same 1,500 W" strip | After "The Purchase Checklist" | The page's core argument is a physical checklist — visualize the inspection; kill the "efficiency model" myth visually |
| how-to-lower-electric-bill-complete-guide | One top-of-page savings-vs-cost summary chart | Top, before Quick Answer | Anchors the guide AND defuses the stacked-percentages overpromise (C4) with a realistic single-home ceiling |
| 07-gas-bill-too-high | Annotated real gas statement (01's pattern) + 12-month therm-usage chart + cause-probability graphic | Statement image at walkthrough H2; chart at seasonal table | 3 visuals for 3,892 words; grounds 11 causes; the page's missing anchor asset |
| 05-how-to-lower-utility-bills | Payback-ladder graphic (pattern exists: guide's payback-timeline.webp) + baseline worksheet | Top + "Establish a Baseline" | The weakest visual set of the money pages (hero only for 8 tables); gives the hub its anchor asset |
| net-metering-explained | Import/export/settlement flow diagram + annotated solar-bill image | Top of mechanics section | The page's subject is a bidirectional flow with no diagram; strongest single comprehension lift in the audit |
| ev-charging-impact-electric-bill | Charging-curve/TOU-window chart | At TOU-plan section | Turns its 9 tables' key insight (charge at 2am) into one glance |
| 50-best-smart-plugs | 3-step meter-assess-automate diagram | At Step 1 | A page teaching meter-reading with zero diagrams (split-brain fix) |
| do-programmable-thermostats | Annotated weekly setback-schedule graphic (07 already ships thermostat-setback-schedule.webp) | At "How to Use a Schedule Safely" | Shows the DOE-referenced schedule the page describes; visual is site-proven |
| afue-vs-seer | Ratings-comparison matrix (measure · unit · applies-to · example) | Replacing/above prose definitions | The page is a comparison with zero tables (metrics tbl=0 real here) |
| aux-heat | Thermostat-display mockup (AUX/EMER labels) + resistance-vs-heat-pump cost strip | At mode definitions | Readers panic at the exact label; show it |
| 30-sudden-spike / 06-water-bill | Probability-vs-cost quadrant charts | At ranked-causes H2s | Turns ranked cause lists into prioritized triage at a glance |
| 01-how-to-read-your-electric-bill | Second annotated statement with tiered/TOU block | At "Check for Tiers or Time-of-Use" | Gives the flat-bill visual a tiered twin |
| 13-ac-short-cycling | Cause-priority diagnostic diagram (frozen coil vs low charge vs capacitor) | At decision tables | Extends the Record-Pattern method into the visual layer |
| ac-running-but-not-cooling | Supply-vs-return-air graphic + frozen-coil photo | First screen | First-screen comprehension for a panic query |
| 48-heat-pump-vs-gas-furnace + 45-generator | Breakeven-ratio chart (¢/kWh÷$/therm vs COP); CO-alarm 20-ft placement diagram | Formula section; safety section | Make the formula visual; the 20-ft rule is spatial, show it spatially |
| 04-hidden-fees (hub) | Fee-taxonomy tree already present — extend to per-utility variants | Hub body | Keeps hub table summary-level while giving spokes a visual home |
| Site-wide | Author/trust imagery for money pages | About/author pages | Only after C9 decision — imagery would deepen the persona fiction today |

## 6. Internal Linking & Topic-Cluster Opportunities

**Journey graph verdict: the diagnose→act→plan→forward spine exists on paper and stalls in execution.** Tracer's rg-verified graph: every diagnosed "bill is wrong" path splits with no edge into act pages; the two forward-looking pages are absolute dead ends; the crisis assistance loop is 2/3 wired. The tree also grows trunks without branches — ~85–88% of articles never link up to their hub.

**The 4 highest-value edits in the audit (tracer):**

1. **complete-guide-understanding-utility-bill → dispute / shutoff / assistance / rate-plan** — the apex hub's "When to escalate safely" section tells readers to "follow the provider's written billing-review process" without linking the site's own dispute guide. One section, four links; the site's most-linked page currently funnels no one into the action layer.
2. **Revive both dead ends (C6):** net-metering-explained and ev-charging-impact-electric-bill each get an internal-link layer → which-rate-plan, 08-TOU, 46-what-time, 49-demand, electric-bill-breakdown (+ ev → do-home-energy-monitors). Strong content, zero onward paths; the site's only solar/EV pages strand every solar/EV-curious reader.
3. **03's act edges** at "When to Contact the Utility": dispute, shutoff, which-rate-plan. The diagnosis cluster tells readers to "contact the utility / dispute" and links none of the act pages. (30-sudden-spike: add 04-hidden-fees + shutoff edges.)
4. **Close the crisis loop:** how-to-dispute links external liheap.org but not the site's own utility-assistance-programs-liheap; the LIHEAP page's Emergency section omits can-utility-shut-off-service — can-utility-shut-off does it right. Two edits complete the dispute⇄shutoff⇄assistance loop.

**Named missing edges (tracer's full list):** complete-guide→{dispute, shutoff, assistance, rate-plan}; 03→{dispute, shutoff, rate-plan}; which-rate-plan→ev-charging (Decision List #1 literally discusses EV overnight charging); dispute→internal LIHEAP; LIHEAP→shutoff; why-did→dispute/rate-plan; rates-fees→which-rate-plan; budget-first-apartment→{which-rate-plan, assistance}; electric-breakdown→complete-guide.

**Cluster program (cartographer-core §1, C0–C6):** five trunked clusters (Electricity 23 spokes, Gas 9, Water 19, HVAC 14, Bills & Fees 38) + **C6, the headless Savings & Efficiency cluster — the site's best content with no hub** (05, without-solar, complete-guide-electric, 47, seal-drafts, thermal-curtains, programmable-thermostats, monitors, gadgets, 50-plugs, phantom-power, 42, merv, 44-water). Recommendation: promote 05 to hub (retitle/re-scope honestly) or build a dedicated "Lower Your Bills" landing hub; fan money pages to it.

**Hub repairs:** glossary (C0) — convert bottom "full guides" plain-text list to real links (five hub links' equity currently dead) and add first-use term links in the 10 thinnest posts; bills hub — fix duplicate complete-guide entry + 04 anchor mismatch; water hub — stormwater slot is an alias to a savings post (write a real stormwater page or relabel); HVAC hub — add MERV + duct spokes; gas hub — thinnest library (9) and only 6 inbound; category taxonomy pages get 0 editorial links (link from hubs or drop from sitemap; do not noindex).

**Missing spokes worth building (evidence-based, keyword probes):** "how many kWh does a home use per day" (6 pages mention, none owns it) · "electric supplier scams" (2 mentions) · "gas leak signs & bill impact" (safety gap) · "furnace tune-up cost/schedule" (3 mentions) · "stormwater fee explained" (hub slot exists but aliases away) · "thermostat settings by season" (0 pages, 5+ posts touch it) · "average electric bill for X sq ft home" (0 mentions, big SERP family).

**Orphan repair list (grep-verified inbound counts):** do-thermal-curtains (1) · drought-surcharge (1) · why-higher-in-winter (1) · 09-apartment (2) · ev-charging (2, dead end) · gadgets (2) · single-stage (2) · what-merv-rating (2) · sewer-averaging (2) · water-service-charge (0-out dead end) — each named with its repair link in §3 rows. (Corrected on verification: mcf-vs-ccf initially listed here — it actually carries 12 outbound HTML links + 5 inbound files; the "0 ilinks" flag was the markdown-only metrics artifact.)

**Wrong-target link (alias)**: two pages link /blog/why-electric-bill-changes-month-to-month/ (alias→03) — resolves, but anchors promise "changes month-to-month" content on a "why so high" page; retarget to 03 directly or write the month-to-month page the anchors imply.


## 7. Priority Action Plan

### Fix Immediately (this week — credibility & render integrity)

| # | Action | Why (evidence) | Impact | Effort |
|---|---|---|---|---|
| 1 | Correct the REFUTED water-heater blanket claim on 05: ~25% → 4–9% (pre-1980s tanks excepted); propagate one canonical figure to 07 (5–10%) and complete-guide (4–7%) | claims-verification #5, energy.gov, retrieved 2026-08-30 | Very high (credibility) | XS |
| 2 | Fix 07-gas-bill: heating-share 60–70% → 40–45% (EIA RECS); resolve 10-vs-11 title/body count; make the ~23y worked example the authority line; correct the 5–8y/3–8y rows | claims-verification #7; lieutenant defect list | Very high | S |
| 3 | Repair how-to-lower-electric-bill-complete-guide: delete duplicate `sources:` key (keep the quoted 5-entry block); rebuild Quick-Answer/checklist totals to a realistic single-home ceiling; reconcile the two phantom-load tables; move the post-FAQ Emporia box | grep-verified lines 8/19; banner sums $200–450 vs its own $164.88 bill | Very high | M |
| 4 | Fix aux-heat truncated H2 markup (renders broken today); fix gas-vs-electric nested-link malformation | prospector#2 render review | High (UX/trust) | XS |
| 5 | 28-reconnection: strip the "verified via state PUC dockets" table to structure-only (27's pattern) or add real per-row tariffs; align moratorium text with 21's statute-cited rules | C5; claims UNVERIFIED #8 | High | S |
| 6 | Add the which-rate-plan variable-rate financial disclaimer; verify 47's and 13's existing safety warnings render prominently (C10, corrected scope) | twin_q Gap 2 + spot-check re-derivation | Medium | XS |
| 7 | Submit the sitemap in Google Search Console and verify indexing status (IndexNow covers only the Bing/DDG ecosystem — the site pings no Google surface, which fits the Bing-heavy / Google-0 analytics split). Note: the IndexNow key in deploy.yml is public BY PROTOCOL DESIGN (it must match the served static/f8c073ef….txt file) — do NOT rotate it into a secret; that would break the ping. | cartographer-core §5; Commander verification of static/ key file | High | XS |
| 8 | Revive the three dead ends with outbound link layers: net-metering + ev-charging (which-rate-plan, 08-TOU, 46, 49-demand, electric-bill-breakdown; ev → energy-monitors) and water-service-charge (water hub, 17-customer-charge); add the apex-hub act edges (item 10) this week if capacity allows | C6 — grep-verified 0 outbound in all formats; strong content, zero onward paths | Very high | XS |
| 9 | Canonicalize the site-wide EPA leak-gallons figure (9,400 vs 10,000+/9,300) across 06 and point-sensor; source or drop the 105 dB claim | claims #4; lieutenant 06 entry | Medium | XS |

### Improve Next (next 2–4 weeks — journey & consolidation)

| # | Action | Why | Impact | Effort |
|---|---|---|---|---|
| 10 | Wire the 4 apex-hub act edges (complete-guide → dispute/shutoff/assistance/rate-plan) + 03's act edges + crisis-loop pair (dispute→internal LIHEAP; LIHEAP→shutoff) | §6 items 1–4; one-edit fixes on the highest-authority pages | Very high (bounce→depth) | XS–S |
| 11 | Execute the merge pairs: gas-delivery→12 (301, preserve correction note); kWh pair consolidation; without-solar→complete-guide decision | §4 consolidation list | High | M |
| 12 | Rewrite the 5 briefed pages (§8) | Lowest-rated pages with strategic value | High | M–L |
| 13 | Rebuild legacy cohort: afue (matrix + sources, drop 4-link sentences), aux-heat, heat-pump-running | §4 Pattern A/C carriers | Med–High | M |
| 14 | Convert HTML-headed pages to Markdown (ac-running, rates-fees, smart-meters, kWh, aux-heat) | Ends metrics false-negatives; parity for future audits | Medium | S–M |
| 15 | Glossary: make bottom "full guides" list real links; first-use term links in the 10 thinnest posts | 30-minute fix, permanent equity | Med–High | XS |
| 16 | Fix metadata defects: 16-budget-billing sources field; wrong-target alias link; 49 duplicate source; 04 anchor mismatch; bills-hub duplicate entry; blog-index "97 guides" count | Per §3 rows/notes | Medium | XS–S |

### Build Over Time (1–3 months — structure & authority)

| # | Action | Why | Impact | Effort |
|---|---|---|---|---|
| 17 | Build the Savings & Efficiency hub (headless C6) — promote 05 or build a new landing page; fan all 14 spokes to it | Site's best pages have no parent | Very high | M |
| 18 | Complete the byline-identity decision (C9): named humans with verifiable credentials OR pure desk labels everywhere; name operator/jurisdiction on About+Terms; publish review-progress count | E-E-A-T liability vs honesty arc | Very high (trust) | M |
| 19 | Publish missing spokes (§6 list: kWh/day first, then supplier scams, gas-leak safety) | Keyword probes with zero owners | High | M each |
| 20 | Hub library expansions (gas hub 9→12+; HVAC hub + MERV/ducts; water hub stormwater) | Weakest hub sponsorship sitewide (1–7 files link up) | Med–High | S each |
| 21 | GSC performance monitoring cadence; re-run this audit's metrics tool after the HTML→Markdown conversion | Measure the fixes | Medium | XS |
| 22 | Write the stormwater-fee spoke (hub slot currently aliases a savings post) | Named C3 gap | Medium | S |
| 23 | Decide 28's fate (rewrite vs structure-only) + 09-apartment thin-state pass | §3 3C rows | Medium | S |
| 24 | Consider a state/zip "your rate" interactive on 46 or average-by-state (twin_q calculator concept) | Vanity-metric mitigation | Medium | L |

## 8. Rewrite Briefs — 5 Highest-Priority Weak Pages

*Selection rationale: the two pages carrying REFUTED claims (07, 05), the page with an uncheckable "verified" table (28), the SEO-4 dead end on a forward topic (net-metering), and the thin decision page with liability exposure (which-rate-plan). how-utility-rates-fees (twinq's #2 weakest) is adjudicated as conditional-improve rather than rewrite — see §3B.*

### 8.1 /blog/07-gas-bill-too-high/ (quality 6 · seo 7)
- **Audience & intent:** homeowner with a gas-bill shock (usually winter) seeking validation of the size and a cause ranking; expects "10 causes and fixes."
- **Missing value:** accuracy. The page's raw material (HDD math, WNA explainer, leak protocol) is excellent; it currently undermines itself with the refuted 60–70% heating share, a 10-vs-11 count, three payback figures (5–8y / 3–8y / ~23y), two mislabeled and two duplicated sources, and an uncited EIA 15–30% rate claim — on a page carrying a dozen dollar figures.
- **Structure:** keep the cause ranking; make the worked example the authority: recompute payback rows from one consistent method, delete or correct the 5–8-year claim; retitle to "11 Causes" or fold cause 11 into 10; deduplicate the WNA paragraph (body + FAQ carry it twice); trim the mid-sentence bare-keyword links toward the 04/12 fee explainers.
- **Evidence to add:** EIA RECS heating-share table (one figure, one source); a citation for the FAQ $40–80/$100–250 seasonal band or its removal; a derivation note for the 344%/445% seasonal rows; source [3] relabeled to its actual ENERGY STAR home; deduped entries 2/4.
- **Visuals:** annotated real gas statement (the 01 pattern) at the walkthrough H2; 12-month therm-usage chart beside the seasonal table; cause-probability graphic at the ranked list.
- **Internal links:** keep the 29-link web but route fee-line readers to 04-hidden-fees and therm/CCF readers to mcf-vs-ccf. Propagate the canonical blanket figure from Fix #1.
- **Desired outcome:** the gas cluster's credibility anchor — a page a utility analyst could read without finding a number to dispute.

### 8.2 /blog/05-how-to-lower-utility-bills/ (quality 6 · seo 5)
- **Audience & intent:** the cross-utility savings seeker at prioritization stage; arrives via "lower utility bills," often funneled by the complete-guide's "20+ ways" footer anchor expecting a ranked checklist.
- **Missing value:** the ranking promise. The page is titled as a prioritizer but reads as compliance prose ("request a written scope that identifies the condition addressed…"); its payback table is the real asset; the refuted 25% blanket row and the air-sealing row's paste-error citation break its evidentiary spine.
- **Structure:** fix the mis-cited air-sealing row (thermostat statistic on the wrong line); set blanket savings to the canonical 4–9%; retitle toward what the anchor promises ("20+ ways" checklist framing) or add a scope banner acknowledging the guide as the electric-only deep dive; if two savings tables cannot be maintained, merge into the complete-guide with a cross-utility section.
- **Evidence to add:** a per-row source column in the payback table; state/utility-program specifics only where linkable.
- **Visuals:** payback-ladder graphic + baseline-worksheet graphic (§5).
- **Internal links:** into the future Savings & Efficiency hub; to gadgets/monitors for the measure-first path; keep the guide as the electric depth link.
- **Desired outcome:** either the promoted hub of C6 with an honest title, or graceful retirement into the guide — no third option.

### 8.3 /blog/28-utility-reconnection-fee-explained/ (quality 6 · seo 5)
- **Audience & intent:** household just shut off or about to be; needs the real fee range and the restore process, fast.
- **Missing value:** verifiability. Eight state fee ranges claim "verified via state PUC dockets 2024–2026" with zero checkable URLs — the only page in its cluster violating the tariff-first doctrine; moratorium claims conflict with 21's cited statutes; restore timings (1–4h electric, 1–2h relight) are asserted without source.
- **Structure:** two honest paths — (a) rebuild the table with per-row tariff citations (the 17/26 evidence style), or (b) strip to structure-only like 27 ("point examples, not a national range"); align the winter-moratorium section with 21 + can-utility-shut-off (link, don't restate); cite or cut the restore-timing specifics.
- **Evidence to add:** one real tariff citation per retained row, or none and no ranges.
- **Visuals:** keep the page's rich visual set (it's the cluster's most visual page); make the avoidance-timeline the anchor.
- **Internal links:** canonical LIHEAP/notice/protection facts → 21; keep 26/27 fee-router cross-links; route the disputation path to how-to-dispute.
- **Desired outcome:** the same reader trust as its siblings 21/26/27 — currently the only fees-cluster page that would fail a spot-check.

### 8.4 /blog/net-metering-explained/ (quality 6 · seo 4 — absolute dead end)
- **Audience & intent:** "solar is on my roof or in my plans — how does the bill change?" National question; the page answers mostly for California.
- **Missing value:** geographic neutrality + onward journey. Nearly half the article drills NEM 3.0/SCE/CPUC detail; and the page ships readers nowhere (0 outbound links, grep-verified). It receives traffic from which-rate-plan and rates-fees and strands all of it.
- **Structure:** rebuild the link layer first — a "Where this lands on your bill" section linking which-rate-plan, 08-TOU, 46-what-time, 49-demand, electric-bill-breakdown; then split California specifics into a sub-article linked where NEM 3.0 is mentioned; keep the 400-kWh × 6¢ worked example (it's good).
- **Evidence to add:** one non-CA state example (NEM-successor or buy-all/sell-all tariff) so the main page is nationally representative.
- **Visuals:** import/export/settlement flow diagram + annotated solar-bill image (§5) — the page's subject is a bidirectional flow with no diagram.
- **Internal links:** as above; get it into the electricity hub's library (cartographer link sweep shows the hub lists neither it nor ev-charging).
- **Desired outcome:** the site's solar entry point becomes a journey node, not an exit.

### 8.5 /blog/which-rate-plan-is-right-for-me/ (quality 7 but thin at 702w · seo 8)
- **Audience & intent:** deregulated or TOU-exposed customer at a decision point; will commit real money to a plan today.
- **Missing value:** the worst-case. twin_q's verdict is correct: advising "price a TOU plan against your current bill" without showing a summer-peak failure mode is under-served advice with real dollar stakes; the page also lacks any financial-risk disclaimer (C10) and its Decision List mentions EV charging without linking the ev page.
- **Structure:** add a worked "Summer Trap" case (a shift-able schedule that fails one afternoon at peak price — show the delta); a decision table by usage pattern (high-day / high-evening / shift-able / EV overnight); keep it honest at 900–1,100 words — this is a fix-by-addition-of-math, not padding.
- **Evidence to add:** one utility's actual peak-vs-off-peak multiplier (PG&E or ConEd, per corrections-log figures) plus the ETF context from 10-fixed-vs-variable.
- **Visuals:** the existing decision-clock graphic + a worst-day price-curve overlay.
- **Internal links:** ev-charging-impact (the named gap), 10-fixed-vs-variable, 08-TOU, 46 (all present); add a financial-advice disclaimer line per C10.
- **Desired outcome:** the rate-plan decision page a skeptic would trust with a 12-month commitment — decision-complete and risk-disclosed.

## 9. Prioritized Checklist — What to Do First

*Exactly what to do first, in order. Items 1–9 are same-sitting/this-week fixes; 10–16 are the next two weeks; 17–24 are the build phase. Success criteria: items 1–5 remove every REFUTED/unverifiable claim; items 6–10 end every dead end and wire every act path.*

1. **05-how-to-lower-utility-bills:** change water-heater blanket "~25%" → 4–9% (DOE/Energy Star cap; only pre-1980s uninsulated tanks reach higher); propagate the canonical figure to 07 and the complete-guide. [REFUTED claim — C1]
2. **07-gas-bill-too-high:** heating share 60–70% → 40–45% (EIA RECS) and remove the same-source contradiction; retitle "10 Causes" → "11 Causes" (or fold cause 11); make the ~23-year furnace payback the authority line and correct/delete the 5–8y and 3–8y rows; relabel mislabeled sources 3 and dedupe 2/4; cite or cut the "rates 15–30% (EIA 2026)" line. [REFUTED claim — C2]
3. **how-to-lower-electric-bill-complete-guide:** delete the first (bare) duplicate `sources:` frontmatter block; rebuild the Quick-Answer + section-banner savings so the tiers sum to a plausible single-home ceiling vs the page's own $164.88; reconcile the two phantom-load tables to one; move the post-FAQ Emporia box beside step 3; fix the "20+" ways count. [C3/C4]
4. **aux-heat-vs-emergency-heat-meaning:** repair the two truncated `<h2>` tags (rendering visibly broken); replace the Pattern-A intro. [C7]
5. **28-utility-reconnection-fee:** remove "verified via state PUC dockets 2024–2026" or publish the citations; align moratorium language with 21; cite or cut restore timings. [C5]
6. **complete-guide-understanding-utility-bill:** add the 4 act links (dispute, shutoff, assistance, rate-plan) to "When to escalate safely." One edit; highest structural ROI in the audit. [§6.1]
7. **net-metering-explained + ev-charging-impact-electric-bill:** add each page's internal-link layer (which-rate-plan, 08-TOU, 46, 49-demand, electric-bill-breakdown; ev → energy-monitors). [C6]
8. **03-why-is-my-electric-bill-so-high:** fix the 42-space-heater anchor text (drop the "roundup compares units" claim); add dispute/shutoff/rate-plan links at "When to Contact the Utility"; dedupe sources. [C12/§6.3]
9. **Wire the crisis loop:** how-to-dispute → internal utility-assistance-programs-liheap; LIHEAP Emergency section → can-utility-shut-off-service. [§6.4]
10. **Disclaimers:** add the which-rate-plan financial-risk line; verify 47's and 13's existing safety warnings render prominently (C10 corrected — neither page is missing warnings). [C10]
11. **Repo hygiene:** submit the sitemap in Google Search Console (IndexNow only reaches the Bing ecosystem); add the water-service-charge outbound links; fix the wrong-target alias link on why-did/rates-fees. Do NOT rotate the IndexNow key — it is public by protocol design and must keep matching the served static/ key file. [C6/§6]
12. **Canonical figures pass:** EPA leak-gallons one number site-wide (06/point-sensor); $1.50-vs-$1.91 therm on gas hub; AFUE 95% vs 96% cross-page note. [C12]
13. **Merge pair #1:** gas-delivery-charge-vs-supply-charge → 12-how-to-read-your-gas-bill (absorb two-category table + correction note; 301). 
14. **Merge decision:** what-is-a-kilowatt-hour ↔ 11-understanding-kwh-usage (definition page canonical); decide how-to-lower-electric-bill-without-solar (merge → guide or convert to tools/FAQ). [C12]
15. **Metadata defects batch:** 16-budget-billing sources field; 49 duplicate source; 04 anchor mismatch + hub slug; bills-hub duplicate entry; blog-index "97 guides" → 89; corrections-page SQ-0xx headings. [§3]
16. **Tooling:** fix content-metrics.py to count HTML h2/h3 + `{{< ref }}` links (prevents future "thin" false positives on strong pages). [§0]
17. **Glossary:** make the bottom "full guides" list real links; add first-use term links in the 10 thinnest posts. [§6]
18. **Rewrites 8.1–8.5** (07 accuracy pass; 05 retitle-or-merge; 28 table rebuild; net-metering link layer + CA split; which-rate-plan worst-case math). [§8]
19. **Savings & Efficiency hub:** promote 05 or build the "Lower Your Bills" landing hub; fan the 14 spokes to it. [§6 C6]
20. **Byline decision:** named humans with verifiable credentials OR pure desk labels everywhere; rewrite author pages to match; name operator + jurisdiction on About/Terms; publish review-progress count. [C9]
21. **Legacy rebuilds:** afue (matrix + sources + de-stuff links), aux-heat visuals, heat-pump-running depth, gas-vs-electric merge→48. [§4]
22. **HTML→Markdown conversion** for tooling parity on the six flagged pages. [§0]
23. **Build the top missing spokes:** kWh-per-day, supplier scams, gas-leak safety, furnace tune-up, stormwater fee. [§6]
24. **24-hour re-check:** after items 1–9 ship, re-run the metrics tool and a link-graph sweep to verify dead ends are gone and no new contradictions entered. [§0/§6]

---

*End of audit. Per-page evidence trail: `.squad/SQ-065/wave1/` (8 artifacts) + `.squad/SQ-065/evidence-brief.md`. Conflicts carried OPEN: none unresolved — the three flagged conflicts (rates-fees improve-vs-delete, tracer-vs-twinq dead-end inbounds, metrics 0-ilink flags) are adjudicated in §3 notes with the stronger evidence cited; EIA price-cell and NIPSCO docket claims remain UNVERIFIED pending primary-source access (claims #1, #9).*
---

## Verification Log (post-synthesis)

- **Master-table coverage:** 114 rows mechanically diffed against the repo inventory — complete (Commander).
- **Uncorrelated spot-check** (.squad/SQ-065/wave2-spotcheck.md): 10 sampled claims re-derived — 9 CONFIRMED, 3 defects found (verdict: FIX). All three defects — the false mcf-vs-ccf ORPHAN flag (actually 12 outbound links + 5 inbound files), the overstated "4 links in one sentence" (actual: 2/sentence across a 6-link block), and the C10 panel-opening/capacitor framing (47 has zero panel mentions and warnings already present) — were **Commander-verified by grep and corrected in this document** on 2026-08-30.
- **External claims:** 10 load-bearing figures verified against primary sources — final tally **7 CONFIRMED / 2 REFUTED / 1 UNVERIFIED** after the Commander's closure pass (see final bullet below) — .squad/SQ-065/wave1/claims-verification.md.
- **Known tooling caveat:** the deterministic metrics table counts markdown-only links/headings; pages using HTML markup read as false zeros. Every "0 ilinks/0 headings" flag in this report was re-checked in both formats before being asserted.
- **Post-spot-check closures (Commander, primary sources):** EIA 18.34¢/kWh June 2026 CONFIRMED from Table 5.3 (2026 YTD 18.16¢); NIPSCO IURC FAC order CONFIRMED from the cited in.gov PDF (verbatim rate match). External-claims final tally: **7 CONFIRMED / 2 REFUTED / 1 UNVERIFIED** (the 28-reconnection table — unverifiable because the page cites no URLs). See .squad/SQ-065/wave1/claims-verification.md addendum.
