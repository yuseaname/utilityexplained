# SQ-065 Wave 1 — CORE 25 Audit + Sitewide Topic-Cluster Map
Seat: lieutenant (rescuing cartographer core slice) · 2026-08-30 · Reads grounded this run: all 25 core files, hugo.toml, deploy.yml, public/sitemap.xml, live site, link-graph grep sweep. Blog 89 audited by sibling seats; their link graph is folded in here. Fresh-eyes mandate honored (no prior audit/report files read).

## 0. Verdicts up front

**Sitemap verdict: PRODUCTION SITEMAP IS NOT BROKEN.** The brief's "local public/sitemap.xml contains only 1 URL" is a counting artifact: the file is one LINE of minified XML. `grep -c '<loc>'` = 1 (lines); `grep -o '<loc>' | wc -l` = **121 URLs**. Live https://utilityexplained.com/sitemap.xml matches: 89 posts + 6 author incl. index + 7 category + 18 core + home = 121. Correctly excludes noindex `/search/` and all thin `/tag/` pages; robots.txt declares it. Build: Hugo `[sitemap]` block (changefreq weekly, priority 0.5 across the board — priority unused as a signal). Deploy: GitHub Actions (`deploy.yml`) on push to main → hugo 0.141.0 extended `--minify --gc` → image/render check scripts → rsync to Hostinger public_html → **IndexNow ping to Bing** (hardcoded key in workflow). No Google ping anywhere — consistent with Rybbit: Bing-heavy, Google near-zero. Minor flags: IndexNow key committed in plaintext; sitemap `lastmod` trails content `updated` on old pages (about/pages 2024-12-01) but fresh posts carry 2026-08 dates.

**Link-graph method (all counts quoted from commands this run):** inbound editorial links per slug via `grep -rc "/<path>/" content/ --include='*.md'` (theme nav/footer excluded; raw sweep in /tmp/squad-workspaces/20260830-152225-lieutenant/blog_inbound.txt + linkgraph-raw.txt). Total internal content hrefs = 302. Hugo `aliases:` were checked before calling anything broken: **zero broken internal links** — all 8 suspicious hrefs resolve to aliased posts (e.g. `/blog/02-average-utility-costs-2026/` → average-utility-bills-by-state-2026).

**Orphans (0–2 inbound, grep-verified):** do-thermal-curtains-really-work (1) · 09-apartment-utilities-cost (2) · ev-charging-impact-electric-bill (2, also a dead end: 0 outbound) · gadgets-that-lower-utility-bills (2) · single-stage-vs-two-stage-vs-variable-speed-hvac (2) · what-merv-rating-do-i-need (2) · plus blog `net-metering-explained` (3 inbound but 0 outbound = dead end, not orphan). `_index` shows 0 because the blog nav link lives in theme chrome.
**Core near-orphans:** `/terms/` (0 inbound), `/author/` index (0 inbound), author bios exactly 2 each, `/search/` 1 (by design). Legal/trust rail lives in the FOOTER (theme), not editorial links — verified live: privacy/terms/disclaimer/corrections/methodology all present in footer; acceptable for legal pages, but glossary at 3 editorial inbound is weak for a nav-level hub.

---

## 1. SITEWIDE TOPIC-CLUSTER MAP (derived from link counts + front-matter categories, not vibes)

Cluster anatomy summary: hub body "Browse" libraries measured by hrefs — electricity 23, gas 9, water 19, hvac 14, bills 38 (1 duplicate: complete-guide listed twice), glossary 19. Upward links (blog → hub) are scarce: 2 files → electricity hub, 1 → gas, 4 → water, 7 → hvac, 4 → bills. **~85–88% of articles never link up to their hub** — the trees have trunks and leaves but few branches.

### C1 ELECTRICITY — hub: /electricity-explained/ (hub quality 8/10)
Inbound to hub: 8. Spokes (23 linked in hub library): 01-how-to-read-your-electric-bill, electric-bill-breakdown, 24-delivery-vs-supply, 03-why-is-my-electric-bill-so-high, 30-sudden-spike, tiered-electricity-rates, 08-time-of-use, 46-what-time-is-electricity-cheapest, 10-fixed-vs-variable, 49-demand-charges, what-is-a-kilowatt-hour, 11-understanding-kwh-usage, how-to-read-electric-meter, how-do-smart-meters-work, how-to-lower-electric-bill-without-solar, how-to-lower-electric-bill-complete-guide, 47-check-energy-leaks, 50-best-smart-plugs, phantom-power-draw, net-metering-explained, ev-charging-impact, why-did-my-utility-bill-go-up-this-month + 2 aliased.
Missing spokes (keyword probes): meter-accuracy/disputed estimate beyond 14-estimated (no dedicated page), "how many kWh per day is normal / appliance usage table" (6 pages mention, none owns it), "electric supplier scam / door-to-door switching" (2 mentions, no page), solar standalone economics (only skimmed inside without-solar).
Orphan in cluster: ev-charging-impact-electric-bill (2 in, 0 out).

### C2 GAS — hub: /gas-explained/ (hub 8/10)
Inbound to hub: 6 (weakest hub sponsorship). Spokes (9): 12-how-to-read-your-gas-bill, 07-gas-bill-too-high, gas-delivery-charge-vs-supply-charge, mcf-vs-ccf-vs-therms, how-to-read-gas-meter, gas-vs-electric-heating-cost-comparison, 48-heat-pump-vs-gas-furnace, 18-fuel-adjustment-charge + 1 aliased.
Missing spokes: "gas leak — what to do / does a leak raise my bill" (2 mentions, no page), heating-degree-days / why winter bills vary by state, pilot light vs electronic ignition, estimated gas read. Only 1 blog file links up to the gas hub — thinnest sponsorship of the five.

### C3 WATER & SEWER — hub: /water-explained/ (hub 8/10)
Inbound to hub: 9. Spokes (19): what-is-ccf-on-a-water-bill, how-sewer-charges-work, sewer-averaging, water-service-charge, drought-surcharge, tiered-water-rates, 06-water-bill-too-high, why-did-my-water-bill-suddenly-increase, why-higher-in-summer, why-higher-in-winter, water-meter-leak-indicator, water-meter-running-when-no-water-used, how-to-read-a-water-meter, is-your-toilet-running-leak-test, 44-how-to-lower-water-bill, average-water-usage-per-person, ccf-calculator, point-sensor-vs-whole-home, + stormwater alias entry. NOTE: hub lists /blog/stormwater-fee-on-water-bill-explained/ — that path is an ALIAS of 44-how-to-lower-water-bill, so the stormwater library slot points at a savings post; no true stormwater page exists (3 in-body mentions only).
Missing spokes: "stormwater fee explained" (own page), water softener/hardness cost, pool & irrigation seasonal billing, sprinkler leak, water pressure vs usage.
Strongest interlinking of the five clusters (4 files link up); the 22 water/rates blog pages themselves are the sibling seat's slice.

### C4 HEATING & COOLING — hub: /heating-cooling-explained/ (hub 7/10)
Inbound to hub: 10. Spokes (14): ac-running-but-not-cooling, 13-ac-short-cycling, why-is-my-furnace-blowing-cold-air, heat-pump-running-all-day-in-winter, duct-leaks-symptoms, ductless-mini-split-vs-central-air, gas-vs-electric-heating, 48-heat-pump-vs-gas-furnace, single-vs-two-vs-variable-speed, afue-vs-seer-vs-hspf-vs-cop, aux-heat-vs-emergency-heat, 42-best-space-heater, 47-check-energy-leaks, 50-best-smart-plugs.
Missing spokes: "furnace tune-up cost / maintenance schedule" (3 mentions, no page), winter thermostat settings (0 dedicated pages), AC sizing / square-footage load calc (0 mentions), heat pump vs baseboard. Orphan in cluster: single-stage-vs-two-stage-vs-variable-speed-hvac (2 in).

### C5 UTILITY BILLS & FEES — hub: /utility-bills-costs-explained/ (hub 8/10)
Inbound to hub: 8. Spokes (38, 1 dup): complete-guide-understanding-utility-bill (listed twice), electric-bill-breakdown, how-utility-rates-fees-usage-work-together, 03, 04-hidden-fees, 17-customer-charge, 18-fuel-adjustment, 19-surcharges-riders, 22-minimum-bill, 25-taxes-fees-franchise, 27-connection-fee, 26-deposit, 28-reconnection, 21-past-due, 23-billing-cycle, 14-estimated, 20-proration, 16-budget-billing, 02(avg-costs alias), average-utility-bills-by-state, 09-apartment-utilities-cost, how-to-budget-first-apartment, 05-how-to-lower, can-utility-shut-off, how-to-dispute, moving-utilities-checklist, utility-assistance-liheap, 03 again-as-different-title, + 10 more aliased/fees.
Missing spokes: "help paying bill with credit card / payment arrangement app" (credit-card probe 0), "average deposit refund timing" (covered inside 26), "senior / fixed-income discounts" (inside liheap only), "paywall / paper bill fee" — all low effort, real searches.
Orphans in cluster: 09-apartment-utilities-cost (2 in), gadgets-that-lower-utility-bills (2 in).

### C6 SAVINGS & EFFICIENCY (de-facto cluster, NO hub)
No hub page owns this cluster. Spokes scattered: 05-how-to-lower-utility-bills, how-to-lower-electric-bill-without-solar, how-to-lower-electric-bill-complete-guide, 47-check-energy-leaks, how-to-find-and-seal-drafts, do-thermal-curtains (1 in), do-programmable-thermostats, do-home-energy-monitors, gadgets-that-lower-utility-bills, 50-best-smart-plugs, phantom-power-draw, 42-best-space-heater, what-merv-rating, 44-how-to-lower-water-bill. Front-matter category "Savings & Efficiency" has only 4 pages; the other ~10 have no common parent. This is the highest-value gap: the site's best content (per wave1: 42-space-heater, do-home-energy-monitors at 8–9/10) lives here with a 2-inbound orphan at its edge (thermal curtains).
Missing: dedicated "lower your bills" landing hub OR promote 05 to that role; internal-link fan from each money page to the hub.

### C0 GLOSSARY — /utilities-glossary/ (semi-hub, 3 inbound)
1,882 words, 30+ h3 term definitions with sparse "Read the full guide" links into 8 posts. Its "full guides" footer list at the bottom is PLAIN TEXT, not links — five hub links worth of equity dead. Hub cross-links from other hubs exist (hubs say "see our glossary" only occasionally; 3 editorial inbound total).

### Cluster cross-linking reality check
Hub→hub cross-links: only utility-bills hub links out to all four utility hubs; electricity/gas/water/hvac hubs do NOT link to each other's hubs in body (they mention "our guides on gas, water" as plain text or omit). Category taxonomy pages (7 in sitemap) receive ZERO editorial inbound links from content (0 category hrefs in any front matter/body link sweep) — they exist for Bing only.

### CANNIBALIZATION CANDIDATES (intent overlap, link-verified)
1. how-to-lower-electric-bill-without-solar vs how-to-lower-electric-bill-complete-guide vs 05-how-to-lower-utility-bills — three "lower bill" guides, two scoped electric + one sitewide; complete-guide (3,593 w) vs without-solar (985 w): same SERP intent, thin one should merge outward or become a tools/FAQ page.
2. why-is-my-electric-bill-so-high (03) vs 30-sudden-spike-no-usage vs why-did-my-utility-bill-go-up-this-month vs why-your-electric-bill-keeps-rising (alias of the last) — four "why is my bill up" angles; 03 and go-up-this-month (1,145 w, 2 internal links) overlap most; consider go-up-this-month → merge into 03 or retitle strictly to "rates went up" angle.
3. 24-delivery-vs-supply vs gas-delivery-charge-vs-supply-charge — gas version is gas-specific; fine IF titles/H1s stay utility-specific (they currently do) — watch only.
4. average-utility-bills-by-state-2026 vs aliased 02-average-utility-costs-2026 (same page, alias OK) vs 09-apartment-utilities-cost — apartment one is distinct intent; OK.
5. what-is-a-kilowatt-hour vs 11-understanding-kwh-usage — near-duplicate intent (definition vs usage tracking); candidates to merge (kwh page keeps def, 11 keeps calculator/usage tracking) or strict retitle.
6. water-meter-running-when-no-water-used vs water-meter-leak-indicator-explained vs is-your-toilet-running-leak-test — three leak-detection angles with distinct intents (meter flow vs indicator vs toilet); keep, but each needs a "start here" pointer to 06-water-bill-too-high — currently none links to 06 from that trio except via hub.
7. do-thermal-curtains-really-work vs how-to-find-and-seal-drafts — adjacent intent; not cannibalizing, but thermal curtains (1 in) must be linked from drafts post + space-heater money page.

### MISSING SPOKES (best candidates, evidence-based)
- "How many kWh does a home use per day?" — 6 pages mention kWh/day, none owns the query; natural spoke of electricity hub.
- "Electric supplier scams" — 2 incidental mentions, no page; evergreen money-adjacent trust topic.
- "Gas leak signs & bill impact" — 2 mentions, no page; also a safety/trust gap.
- "Furnace maintenance schedule / tune-up cost" — 3 mentions, no page.
- "Water bill stormwater fee" — hub links an alias; own the term properly.
- "Thermostat settings by season" — 0 dedicated pages though thermostats appear across 5+ posts.
- "Average electric bill for X sq ft home" — 0 pages mention square foot; big SERP family.

---

## 2. CORE 25 — PAGE-BY-PAGE ENTRIES

### / — "Utility Explained" (home, content/_index.md)
- Purpose/intent: brand front door routing to 4 utility hubs + blog. Live render verified (nav: 6 topics, secondary 3, footer trust rail incl. Editorial Team/Policy/Methodology/Corrections + cookie banner with Decline/Accept).
- Quality: 8/10 · SEO: 7/10
- Weaknesses: body copy is 2 sentences (69 words) — hub layout carries it; "Most Read" and "Searchers want" modules expose water/bill posts but not the two strongest money pages; title/desc fine; brand H1 only on hero.
- AI slop: none · Visual gaps: hero present; no trust badges beyond footer text.
- Action: **improve** — add "How it works/Why trust" strip + featured-cluster grid; ensure analytics modules include money pages.
- Next: home is fine; channel equity via blog/_index (see below).

### /blog/ — Blog index (blog/_index.md)
- Purpose/intent: "Browse by Topic" gateway; 97-guide claim + 5 category cards linking to hub anchors + "All Guides newest first" (rendered by theme).
- Quality: 6/10 · SEO: 6/10
- Weaknesses: claims "97 guides" — actual posts = 89 (front matter copy stale); category cards point to HUB anchors not to /blog/category/... taxonomy pages (defensible but leaves category pages 0 editorial links); hard-coded inline styles.
- AI slop: none · Visual gaps: none (cards exist).
- Action: **improve** — fix guide count dynamically or to 89; add 1-line intros per category; consider linking both hub anchor AND category page.
- Next: keep as hub-router; it's good UX.

### /about/ — About (309 w)
- Purpose/intent: mission, audience (renters/first-time buyers), funding model (ads + Amazon), "how we're different".
- Quality: 7/10 · SEO: 6/10
- Weaknesses: no operator/owner entity named (terms explicitly say "does not state a principal place of business"); no founding date or address; 1 inbound editorial link; funding section duplicated on editorial-team + affiliate-disclosure (3rd repetition sitewide).
- AI slop: none (human, specific) · Visual gaps: no founder/team photo or company footprint.
- Action: **improve** — name the operator entity + location; add "last reviewed by" trail.
- Next: trust hinge — skeptical users and Google E-E-A-T checks land here.

### /contact/ — Contact (172 w)
- Purpose/intent: topic suggestions/error reports via mailto widget; sets expectations (no account lookups).
- Quality: 7/10 · SEO: 5/10
- Weaknesses: mailto-only, no form (hosting is static — acceptable but friction); "we read every message" vs "can't always reply individually" slightly contradicts; 5 inbound (good, linked from corrections/methodology/policies).
- AI slop: none · Visual gaps: none needed.
- Action: **improve** (add simple form or Web3Forms if spam becomes an issue) — otherwise keep.
- Next: keep.

### /search/ — Search (24 w, layout: search, noindex:true)
- Purpose/intent: client-side search utility; noindex correct; correctly EXCLUDED from sitemap (verified).
- Quality: 6/10 (works; can't verify JS here) · SEO: 7/10 (noindex + sitemap-excluded = correct hygiene)
- Weaknesses: 1 editorial inbound (contact links it — good); page itself zero-content by design.
- AI slop: none · Visual gaps: n/a.
- Action: **keep** (correctly noindexed, not in sitemap).
- Next: verify client-side index isn't bloated; no further work.

### /corrections/ — Corrections Policy (404 w)
- Purpose/intent: report-an-error workflow + public correction log with two dated entries (Con Edison TOU rates fixed to 27.86¢/5.22¢ with retrieval dates; DOE heat-pump 65% figure swap). Real corrections with specific numbers = rare and credible.
- Quality: 9/10 · SEO: 6/10
- Weaknesses: only 4 editorial inbound; log has 2 entries though site claims ongoing review — expected to grow; SQ-xxx ticket names in headings leak internal ops jargon to readers.
- AI slop: none — this page is a trust asset · Visual gaps: none.
- Action: **keep + improve** — strip "(SQ-0xx)" from public headings; link corrections from every data-heavy guide's Sources block, not just 4 pages.
- Next: this is the strongest trust page on the site. Feed it.

### /disclaimer/ — Disclaimer (116 w)
- Purpose/intent: not-professional-advice limits; effective 2024-12-01, reviewed 2026-08-30.
- Quality: 6/10 · SEO: 4/10 (standard)
- Weaknesses: thin but complete; 2 inbound; duplicated no-advice promise across terms/editorial-policy (expected).
- AI slop: none · Visual gaps: none.
- Action: **keep**.
- Next: none.

### /privacy-policy/ — Privacy Policy (608 w)
- Purpose/intent: consent-mode v2 banner promise, GA4 + Rybbit declared, AdSense cookie mechanics, GDPR/CCPA section.
- Quality: 8/10 · SEO: 5/10
- Weaknesses: none material — unusually specific and matches live footer behavior (decline/accept verified). 2 inbound.
- AI slop: none · Visual gaps: none.
- Action: **keep**.
- Next: keep GA4 id in sync with consent settings if analytics split changes.

### /terms/ — Terms of Service (580 w)
- Purpose/intent: informational-only, reuse rules, affiliate note, no-warranty/liability, governing law "state of the site operator — not identified here" (explicitly vague).
- Quality: 6/10 · SEO: 4/10
- Weaknesses: governing-law vagueness is honest but reads unprofessional to a skeptical reader; "principal place of business not stated" is a trust leak (matches About gap); 0 editorial inbound (footer-only) — acceptable for legal rail but no page links it.
- AI slop: none · Visual gaps: none.
- Action: **keep + improve** (name the jurisdiction once operator identity is decided; that single sentence costs nothing).
- Next: pair fix with About.

### /affiliate-disclosure/ — Affiliate Disclosure (267 w)
- Purpose/dos: Amazon Associates statement, price-same promise, "why gadgets at all", marked-CTA promise. no_ads:true so page itself is ad-free — nice touch.
- Quality: 8/10 · SEO: 5/10
- Weaknesses: 1 editorial inbound (terms links it); no date-last-reviewed visible; Amazon "on our site" placement promise is verifiable on money pages — consistent.
- AI slop: none · Visual gaps: none.
- Action: **keep**; add footer link to it on money pages (currently not linked from any product page body — only terms).
- Next: link 42/50/energy-monitor pages → here (FTC hygiene).

### /editorial-policy/ — Editorial Policy (404 w)
- Purpose/intent: scope, plain-English method, lead-with-answer, **AI-assistance disclosure** ("may be drafted with AI assistance ... does not establish a fact, source, credential"), AdSense independence, accountability links.
- Quality: 8/10 · SEO: 6/10
- Weaknesses: "we are reviewing older guides" is a standing promise with no stated completion date or progress count; 10 editorial inbound (best-linked trust page — good).
- AI slop: none · Visual gaps: none.
- Action: **keep + improve** — publish a review-progress number (e.g. "41/89 verified") to convert promise → proof.
- Next: methodology is its twin; keep both in sync.

### /editorial-team/ — Editorial Team (439 w)
- Purpose/intent: roster of 5 desk editors (linked) + 4-step process (research/AI-assisted draft/verify/publish-or-hold) + independence + contact.
- Quality: 7/10 · SEO: 6/10
- Weaknesses: repeats funding line 3rd sitewide; no photos, no LinkedIn/personal links (by design — bylines are desk personas, see §3); 1 editorial inbound (about only) — the live footer links it, verified.
- AI slop: light (templated "X focuses on...")· Visual gaps: no team imagery (initial-avatars only, by design).
- Action: **keep + improve** — add one-line "why desk bylines" explainer right above the roster.
- Next: §3 trust verdict applies.

### /methodology/ — Methodology (365 w)
- Purpose/intent: sources (EIA, DOE/ENERGY STAR, tariffs), formulas (appliance cost, bill impact, savings), "typical" definition, limitations.
- Quality: 8/10 · SEO: 6/10
- Weaknesses: sources listed but no linked examples from this page itself (no external hrefs in body — the formula promises are shown, but the EIA series isn't hyperlinked); "revisit regularly" unquantified; 8 inbound (good).
- AI slop: none · Visual gaps: one worked-example callout box would help.
- Action: **keep + improve** — add 2–3 live source links (EIA Electric Power Monthly, DOE Energy Saver) to convert description → proof.
- Next: pair with correction-log growth.

### /author/ — Authors index (117 w)
- Purpose/intent: roster + the site's most honest paragraph: "editorial bylines ... are not claims of independently credentialed individuals. Guides may use AI assistance during drafting."
- Quality: 6/10 · SEO: 5/10
- Weaknesses: 0 editorial inbound (footer secondary nav links it, verified live "Our Authors"); if personas are later replaced with real people, this page needs rewrite first.
- AI slop: light · Visual gaps: no avatar imagery.
- Action: **keep + improve** (see §3).
- Next: anchor of the byline-honesty fix.

### /author/david-chen/ — Energy Efficiency Editor (222 w)
- Quality: 6/10 · SEO: 6/10
- Purpose: desk persona page; scope (efficiency/HVAC ratings/air sealing); cites DOE/ENERGY STAR; links representative piece 47-check-energy-leaks.
- Weaknesses: NO bio, photo, credentials, or first-person voice; "editorial byline for the desk" phrasing does the honesty work; 2 inbound; footer boilerplate repeated.
- AI slop: light · Visual gaps: avatar initial only.
- Action: **improve** — either (a) keep persona + strengthen the desk framing (remove name-like presentation, keep desk title), or (b) replace with a real human bio with verifiable creds. Current half-state is the weakest option.
- Next: sitewide byline policy decision (§3).

### /author/marcia-washington/ — Affordability & Assistance Editor (113 w)
- Quality: 5/10 · SEO: 5/10
- Purpose: budgeting/assistance desk; cites EIA state series + CFPB; links first-apartment budgeting post.
- Weaknesses: shortest and thinnest of the five; no "What X writes about" section; same persona limitations.
- AI slop: light · Visual gaps: none.
- Action: **improve** (same sitewide decision).

### /author/margaret-harrington/ — Bills & Rates Editor (242 w)
- Quality: 6/10 · SEO: 6/10
- Purpose: billing-structure desk (43 bylines — the workhorse); cites EIA Electric Power Monthly; flagship link complete-guide.
- Weaknesses: same persona-honesty tension; most bylines ride on this name (43/89) — single point of trust failure if challenged.
- AI slop: light · Visual gaps: avatar initial.
- Action: **improve** (sitewide decision).

### /author/roberto-mendoza/ — HVAC & Systems Editor (208 w)
- Quality: 6/10 · SEO: 6/10
- Purpose: HVAC desk; cites manufacturer docs + DOE; safety guidance tied to CPSC CO materials; links furnace-cold-air post.
- Weaknesses: same pattern.
- AI slop: light · Visual gaps: none.
- Action: **improve** (sitewide decision).

### /author/tanya-patterson/ — Consumer Rights Editor (200 w)
- Quality: 6/10 · SEO: 6/10
- Purpose: fees/disputes/PUC desk; cites state consumer-protection rules + CFPB; links dispute post. "She breaks down..." — the only gendered third-person slip (others avoid pronouns); 16 bylines.
- Weaknesses: same pattern; pronoun inconsistency across pages.
- AI slop: light · Visual gaps: none.
- Action: **improve** (sitewide decision).

### /electricity-explained/ — Electricity hub (2,448 w)
- Purpose/intent: pillar for cluster C1: physics→metering→bill anatomy→rates→usage→savings→FAQ→23-link library.
- Quality: 8/10 · SEO: 7/10
- Weaknesses: dated-verified figures (899 kWh, 18.34¢ June 2026 EIA — matches EIA public series); bill-anatomy image has good alt; byline is generic "Utility Explained team" not a desk persona (inconsistent with blog bylines); 2 aliased links in "Why Your Bill Is High" (resolve, see §1); two 2025-era sections (~"misconceptions") read generic; FAQ present but no FAQ schema visible in body (theme-level, unchecked).
- AI slop: light (reduction-tips list is boilerplate) · Visual gaps: one chart (usage-by-appliance %) and one tier-TOU comparison table missing.
- Action: **improve** — swap generic tips list for links to the 6 spoke guides; add appliance-share chart.
- Next: hub is strong; make body links match the library.

### /gas-explained/ — Gas hub (2,295 w)
- Quality: 8/10 · SEO: 7/10
- Purpose: pillar for C2: therms/BTU/CCF→bill anatomy (annotated image)→AFUE→seasonal→reduction→FAQ→9-link library.
- Weaknesses: $1.50/therm example hedged with parenthetical "near the 2026 average of roughly $1.91" — pick one number; 9-link library is the thinnest hub library; hub-byline generic; FAQ lacks schema.
- AI slop: light · Visual gaps: needs seasonal usage chart.
- Action: **improve** — expand library to cover missing spokes (§1 C2); fix rate example.
- Next: weakest hub of the five; also weakest hub-link sponsorship (6 in, 1 up).

### /water-explained/ — Water hub (2,274 w)
- Quality: 8/10 · SEO: 7/10
- Purpose: pillar for C3: service→CCF/gallons→sewer/stormwater→tiers→indoor shares→meter/leaks→FAQ→19-link library.
- Weaknesses: stormwater library slot is an alias to a savings post (§1 C3); meter-reading section duplicates the dedicated spoke posts' ground; generic team byline; FAQ schema unverified.
- AI slop: light · Visual gaps: indoor-use pie chart missing; bill-anatomy image good.
- Action: **improve** — link stormwater mentions to a real stormwater spoke once written.
- Next: solid; keep.

### /heating-cooling-explained/ — HVAC hub (2,268 w)
- Quality: 8/10 · SEO: 7/10
- Purpose: pillar for C4: system types→ratings (AFUE/SEER/HSPF/COP)→cost drivers→repair-vs-replace→FAQ→14-link library.
- Weaknesses: "70%→95% AFUE saves ~25%" appears in BOTH gas hub and here (self-duplication); MERV spoke (what-merv-rating) missing from hub library despite existing — 2-in orphan; generic byline.
- AI slop: light · Visual gaps: needs side-by-side ratings table (it has text-only).
- Action: **improve** — add what-merv-rating + ducts/air-quality links to library; dedupe AFUE example with gas hub.
- Next: good hub; library gap is the fix.

### /utility-bills-costs-explained/ — Bill Basics hub (2,587 w)
- Quality: 8/10 · SEO: 8/10
- Purpose: pillar for C5 + site's biggest router (38 library links; FAQ shortcode with schema; links to all 4 sibling hubs).
- Weaknesses: ONE DUPLICATE — complete-guide-understanding-utility-bill listed twice ("Complete Guide..." + "How to Read Your Utility Bill" both href it); two FAQ entries use hardcoded numbers ($100–$200 electric) that duplicate 02/average-states data (fine, but refresh together); "04-hidden-fees" linked with title "Delivery charge vs supply charge" (mismatched anchor→target); generic byline.
- AI slop: light · Visual gaps: three-bill anatomy image present and referenced; no per-utility mini-graphics.
- Action: **improve** — fix the anchor mismatch + duplicate list entry; it's the best-constructed hub.
- Next: model for other hubs.

### /utilities-glossary/ — Glossary (1,882 w)
- Quality: 7/10 · SEO: 8/10 (unique SERP capture: "what is CCF", "demand charge", etc.)
- Purpose: 30+ plain-English term cards, selectively deep-linked to 8 spokes; bookmark utility.
- Weaknesses: closing "visit our full guides" list is PLAIN TEXT, not links (5 hub links dead); only 3 editorial inbound for a nav-level hub; term cards would benefit from anchor links from spoke posts ("defined in glossary") — only hubs do this today.
- AI slop: none · Visual gaps: none needed (dictionary format).
- Action: **improve** — make the bottom list real links; add sitewide first-use term linking in the 10 thinnest posts.
- Next: cheapest large win in core (30 minutes of work, permanent equity).

---

## 3. TRUST SURFACE VERDICT (the hard judgment)

**Plainspoken answer: the five "authors" are NOT real people with real expertise — and the site now says so honestly. This is a desk-byline system, and the pages were recently rewritten to stop pretending.** The author index states: "Utility Explained uses editorial bylines to identify the topic desk responsible for a guide. They are not claims of independently credentialed individuals." Every bio page repeats: "Guides may use AI assistance during drafting." Editorial-policy adds: "We do not present AI-generated credentials or fabricated expert qualifications."

**But the residual fabrication signals are real and a skeptic will catch them:**
1. Proper-noun personas with zero biography: 5 named individuals, no photos, no histories, no credentials, no first-person quotes, avatar = first letter (verified in single.html: `author-bio-avatar = substr $authorName 0 1`). Margaret Harrington carries 43/89 bylines; nothing on her page says who she is beyond a desk description, because there is no her.
2. Name-shaped but unverifiable: "Marcia Washington" has 113 words — shorter than most blog intros — with no "What she writes" section while the other four have one.
3. Pronoun slip: tanya-patterson.md says "She breaks down the fees..." — the only gendered pronoun on any author page; the others conspicuously avoid pronouns (a tell of managed fiction, not of lives).
4. No person anywhere: About names no operator, Terms states no principal place of business, no address, no company registration on any page. hello@ is the only contact surface.

**Do the policies read as credible, or theater? Mostly credible — unusually so for this genre.** Editorial policy and methodology are specific about their weaknesses: AI drafting disclosed, "a page without a visible Sources section should be treated as general educational context," publish-or-hold step named. The corrections page is the standout: two logged corrections with exact figures and retrieval dates (Con Edison 22.33¢/44.97¢ corrected to live 27.86¢ / 5.22¢; DOE "up to 50%" corrected to "approximately 65%" with archived source). Fabricated-trust sites do not log their own rate-figure errors with the right numbers. My one policy complaint: promises lack counts ("reviewing older guides" — no progress metric), and methodology lists sources without linking them.

**Would a skeptical reader trust this site with money-adjacent advice?** Qualified yes for *understanding a bill*, guarded no for *acting on money outcomes* — today. The content-side trust spine (correction log, dated sources, consent-honest privacy page, clear affiliate terms, no fear-mongering) is better than 90% of affiliate sites in this vertical. But the persona layer remains a latent credibility bomb: any reader who clicks "Margaret Harrington" (the byline on 48% of all posts) finds a 242-word job description, no human, and a disclaimer that admits she isn't an individual. E-E-A-T for YMYL-adjacent money queries increasingly rewards verifiable humans; the current design converts an honesty virtue into a ranking liability. The fix is not more fake biography — it's completing the honesty: either named humans with verifiable credentials, or fully-impersonal desk labels on bylines AND author pages (e.g. "Bills & Rates Desk — Utility Explained editorial team"), with the team page carrying whatever real-world accountability exists.

---

## 4. WAVE-1 RECONCILIATION NOTES (cross-seat)
- Wave1 claim "two blog dead-ends (net-metering, ev-charging), 0 internal links": CONFIRMED with nuance — outbound links = 0 each (dead ends); INBOUND: net-metering 3, ev-charging 2 (near-orphan, not 0). Both in sitemap; BUT correction below — neither is in the electricity hub's Browse library (link sweep shows the hub lists neither slug; hub-listed claim above was wrong).
- "Strongest pages are newest money pages (42-space-heater, do-home-energy-monitors)": consistent with everything I read this run; my orphans list adds what-merv-rating + thermal-curtains as high-quality-but-invisible siblings.
- "Several 2025-12-25 batch-dated articles": sitemap lastmods confirm the 2025-12-25/26/27 batch (14 posts) — the AFUE/aux-heat/smart-meter/water-meter family; treat as rewrite cohort B.

---

## 5. SITEMAP + DEEP TECHNICAL NOTES
1. Count: 121 URLs = 89 posts + 6 author + 7 category + 18 core + home. The "1 URL" known-fact was `grep -c` (lines) on a single-line XML file. No action on the file itself.
2. Live == local (same 121 set, same lastmods). Hosting rsync lands in `~/domains/utilityexplained.com/public_html/` — no CDN/caching layer in that pipeline (whatever the host configures server-side).
3. IndexNow: Bing-only push notification on every push (hardcoded key in deploy.yml — rotate to a repo secret); nothing equivalent for Google (Google doesn't support IndexNow; GSC meta verification is present, but with Google at near-zero sessions the practical lever is GSC sitemap submit + internal linking quality, not pings).
4. `priority 0.5` uniform = ignored; `changefreq weekly` uniform = ignored. Fine; harmless.
5. `/tags/` exist in build but are excluded from the sitemap (correct — tag pages are thin utility pages); `/categories/` ARE included (7 pages) yet receive no editorial links — either link them from hubs or drop them from the sitemap; do not noindex (they're usable hub-adjacent lists for Bing).
6. noindex chain verified: /search/ has `noindex: true` front matter AND is absent from sitemap (both layers correct).

---

## 6. PRIORITY ACTIONS (highest impact first)
1. **Internal uplink pass (1 day):** add a hub-link line to every post ≤8 internal links (85–88% never link up today); link the 6 orphans (thermal-curtains 1-in, merv 2-in, single-vs-two-vs-variable 2-in, apartment-cost 2-in, gadgets 2-in, ev-charging 2-in+0-out) from 2–3 neighbors each, matching their cluster; link net-metering + ev-charging OUT to something.
2. **Glossary equity + hub-library fixes (1 hr):** convert the glossary's 5 plain-text guide links to real links; fix the bills-hub duplicate entry + the mismatched "Delivery vs supply" anchor; add what-merv-rating to the HVAC hub library.
3. **Savings hub decision (1 day):** either promote 05-how-to-lower-utility-bills as the Savings & Efficiency hub and rewire its 12 siblings to link up, or write a new landing hub; this cluster contains the site's best-performing content and is the only cluster without a trunk.
4. **Trust completion (2–3 days):** name the operating entity + one location on About and Terms; decide desk-byline policy (impersonal desk labels or real, verifiable named humans); add review-progress counts to editorial-policy; strip "(SQ-xxx)" from public correction headings.
5. **Missing spokes for Bing-era topical authority (1–2 weeks, pick 4):** kWh/day normal, gas leak safety, supplier scams, tuning/maintenance schedule, true stormwater page, thermostat-by-season (probes in §1).

**What I could NOT verify this run (uncorrelated seats should re-derive):**
- Rendered FAQ/Article schema on hub/blog pages (theme partial `head.schema.html` exists — needs a rendered-HTML schema check).
- Live category page content quality (I did not fetch /blog/category/* pages live).
- Client-side search index composition on /search/.
- Every aliased URL's HTTP 200 at the CDN/host (aliases verified in Hugo source, not by HTTP probe).
- Actual bounce behavior at hub anchors (UX, needs analytics tooling).

---

## Appendix — commands run for the map (verbatim)
- `grep -rhoE 'href="/blog/[a-z0-9-]+/"' content/ | sed ... | sort | uniq -c | sort -rn` → hub library/spoke counts + top-linked ranking (raw in workspace).
- `for f in content/blog/*.md; do slug=...; grep -rc "/blog/$slug/" content/ --include='*.md' | awk -F: '{s+=$2} END {print s+0}'; done | sort -n | awk '$1<=2'` → orphan sweep.
- `for f in _index about ... utilities-glossary; do grep -rc "/$f/" ...; done` → core inbound table above.
- `grep -o '<loc>' public/sitemap.xml | wc -l` → 121; live fetch of /sitemap.xml → same 121 (2026-08-30).
- `grep -rl '/$hub/' content/blog/ --include='*.md' | wc -l` → upward-link counts (2/1/4/7/4).
- Aliases audit: all 8 suspicious hrefs resolved to alias-owning posts (listed in §1); zero broken internal links found.
- Correction to §4 (verified with grep -rl): net-metering-explained and ev-charging-impact-electric-bill are NOT in the electricity hub Browse library (0 matches in electricity-explained.md). Linking sources: net-metering ← how-utility-rates-fees-usage-work-together, which-rate-plan-is-right-for-me; ev-charging ← 08-time-of-use-electricity, 03-why-is-my-electric-bill-so-high. Both remain near-orphans reachable only through two in-content links each; adding both to the electricity hub Plans/Lower-Your-Bill library is the one-line structural fix.

*— lieutenant, SQ-065 wave 1. Companion artifacts: lieutenant-pages.md (pages slice) + raw sweep files in /tmp/squad-workspaces/20260830-152225-lieutenant/.
