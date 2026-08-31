# SQ-065 Wave1 Prospector Audit — 22-page bill-anatomy/fees cluster

Manifest: 22 pages. Read in full: 22/22 (0 skipped). Evidence format: quoted phrases from markdown source under content/blog/. Rates are 1-10; every weakness is quoted.

---

### /blog/04-hidden-fees-utility-bill/ — Every Charge on Your Utility Bill, Explained
- purpose/intent: cluster hub; 7-row fee taxonomy table + directory of site explainers. Quick Answer: 'A quoted energy price is not the same as the final amount due.'
- quality: 9/10
- seo: 7/10
- weaknesses: H1/title says 'Every Charge...' while slug is '04-hidden-fees-utility-bill' — keyword mismatch on the hub URL; table row for customer charge says 'described by DOE rate design' but the real verified amounts live on 17; page is a TOC, its own table necessarily restates each spoke — acceptable architected overlap, but meta description is a launch-pad description, not a ranking H1.
- ai_slop: none — original framing ('Why This Page Does Not Give You a National Price Range') and sourced caveat ('confirm the amount on YOUR bill against YOUR utility's current tariff, not against an article on the internet').
- visual_gaps: has annotated bill + fee-taxonomy tree; no gap.
- action: keep (hub). Next: rename slug to a keyword hub (e.g. every-charge-on-your-utility-bill-explained) with redirect; keep table summary-level only so it does not compete with spokes.

---

### /blog/09-apartment-utilities-cost/ — How to Budget for Apartment Utilities
- purpose/intent: renter decision-stage budget guide; EIA evidence + first-apartment checklist.
- quality: 6/10
- seo: 6/10
- weaknesses: thin (98 lines / 7.1KB vs 12-13KB spokes); 10-state table 'statewide averages for all homes ... apartments typically run below these figures' duplicates the linked /blog/average-utility-bills-by-state-2026/; no FAQ block, no {{< visual >}}, no product/action anchor; only 2 sources cited.
- ai_slop: medium-low — generic checklist phrasing ('Budget by service, not by one total'), but the EIA single-family-vs-apartment 'nearly three times more energy' claim is specific and sourced.
- visual_gaps: no bill/unit anatomy; a lease-responsibility infographic or sample first-bill callout would materially help.
- action: improve. Next: cut/compress state table to a 3-row illustration and link out; add FAQ (RUBS, sub-metering, first-bill timing); add one visual; target apartment-specific long-tails ('which utilities do renters pay').

---

### /blog/10-fixed-vs-variable-utility-rate/ — Fixed vs. Variable Utility Rates: Which to Pick
- purpose/intent: plan-comparison commercial intent in deregulated states; break-even math + worked 12-month table.
- quality: 9/10
- seo: 7/10
- weaknesses: 'In deregulated states you shop competing offers...' — the state-portal section (TX/PA/OH) is a genuinely useful differentiator; early-termination fee range '$150–295' is stated as 'typical industry range' without a citation anchor (only source 1-2 in Sources are DOE); overlaps and links the TOU/plan-selection cluster (08, 46, which-rate-plan) which the Commander should audit as a second pass.
- ai_slop: none — the worked 12-month table and '$27 edge' variance lesson are original.
- visual_gaps: no chart of the illustrative rate curves; a small line chart of Plan A vs Plan B would make the variance point visual.
- action: keep. Next: add a citation or soften the ETF range; consider interlinking to which-rate-plan-is-right-for-me.

---

### /blog/11-understanding-kwh-usage/ — Understanding kWh Usage on Your Electric Bill
- purpose/intent: informational; define kWh, appliance cost context, rate vs usage leverage.
- quality: 8/10
- seo: 7/10
- weaknesses: 10-appliance table cites RECS/DOE but per-row sources are not listed row-by-row; overlaps the site's own what-is-a-kilowatt-hour.md (cross-shard lead — likely cannibalization on 'kilowatt hour' query space); carries affiliate product box which is fine but the page's best original value is the '18.34 cents per kWh' cost-equation table.
- ai_slop: none notable — 'Rate is mostly out of your control. Usage is where you have leverage.' is genuinely useful framing.
- visual_gaps: has appliance kWh ladder graphic; could add a meter-reading-to-kWh diagram (short version already links out).
- action: improve. Next: dedup against what-is-a-kilowatt-hour (recommend single canonical kWh page + redirect); verify the national 18.34¢ figure against .squad/content-metrics.md.

---

### /blog/14-estimated-utility-bill-explained/ — How to Review an Estimated Utility Bill
- purpose/intent: diagnostic on estimated reads; force-an-actual-read workflow with ConEd + Texas rules.
- quality: 9/10
- seo: 7/10
- weaknesses: high-quality verified triggers table (Pend Oreille PUD 'Power outages, severe weather, locked gates'; National Grid 'software updates'; NJ Rate Counsel); overlaps 23's estimated-vs-actual table on the same trigger facts ('locked gate, dog, weather'); Texas-specific depth is great but national searchers may bounce.
- ai_slop: none — 'An estimate is a placeholder, not a final number' with worked true-up arithmetic.
- visual_gaps: has side-by-side table; a sample annotated bill showing the 'E/EST' notation would help.
- action: keep. Next: with 23, de-duplicate trigger lists (keep 14 as specialist); already cross-links 30-sudden-spike and 16-budget-billing well.

---

### /blog/16-budget-billing-level-pay-explained/ — How to Review a Utility Budget-Billing Plan
- purpose/intent: explain level-pay mechanics; provider-specific plan table + worked 12-month example.
- quality: 8/10
- seo: 6/10
- weaknesses: frontmatter sources field lists only CFPB while body cites National Grid [2], PG&E [3], FPL [4] — frontmatter metadata is incomplete; category is 'Electricity' although budget billing applies to gas and water too; no FAQ block; page says 'It is a payment plan, not a discount' — good anti-slop line.
- ai_slop: low — worked $95-to-$280 / $165 level-pay table is concrete and useful.
- visual_gaps: no chart of actual vs level payment; the 12-month table could be rendered as a dual-line chart.
- action: improve. Next: fix frontmatter sources; set category to Bills & Fees; add FAQ (what happens if I move; is it a discount).

---

### /blog/17-what-is-customer-charge-on-utility-bill/ — How to Review a Customer Charge on a Utility Bill
- purpose/intent: verify one line; published-rate evidence table + rate-case example.
- quality: 9/10
- seo: 8/10
- weaknesses: over-perfect example page; the verified amounts (SMUD $27.00/$17.00 Low Use, Austin $16.50, PG&E ~$24/~$6 CARE/~$12 FERA, Consumers $8.00, PPL $14.09→$15.00 June 4 2026) are the strongest original data in the cluster and are partly repeated in 24 (Consumers $8) and 22 (PG&E March 2026 restructure) — canonicalize to this page.
- ai_slop: none — 'if the amount changes with your kWh or therms, it is not the customer charge' is a sharp decision rule.
- visual_gaps: fixed-share table (600/200/50 kWh, 17%/38%/71%) could become a bar chart.
- action: keep. Next: have 24 and 22 link to this page for the fixed-charge facts instead of restating; add FAQ schema already present — good.

---

### /blog/18-fuel-adjustment-charge-on-utility-bill-explained/ — How to Review a Fuel Adjustment Charge on a Utility Bill
- purpose/intent: tariff-first verification of the fuel line; state examples (Kentucky dollar-for-dollar, NIPSCO April 30 2025 credit→charge).
- quality: 8/10
- seo: 7/10
- weaknesses: overlaps 19 by design (FAQ: 'Is the fuel adjustment charge the same as a rider? — Adjacent, not identical: the rider is the commission-approved mechanism; the fuel adjustment charge is the line item it produces'); the symbolic check and effective per-unit rate reverse check are strong but some will find the tariff-first method abstract without a concrete real-bill scan.
- ai_slop: none — NIPSCO direction flip is dated, specific, quoted.
- visual_gaps: has two visuals (tariff excerpt, two-bill compare) — adequate.
- action: keep. Next: keep 18/19 differentiated with the mechanism-vs-line-item split taught on both sides; add a real annotated fuel line if one can be sourced.

---

### /blog/19-utility-bill-surcharges-and-riders-explained/ — How to Review Surcharges and Riders on a Utility Bill
- purpose/intent: rider mechanism; real named riders table (Duke fuel/DSM/storm, Ohio infrastructure + $10M vegetation cap).
- quality: 8/10
- seo: 7/10
- weaknesses: 'Real Riders on Real Bills' table lists Duke/Ohio examples but no per-row published URL; FAQ 'How is this different from the fuel charge I already have?' mirrors 18's FAQ verbatim in function; overlaps 25 on the tax-vs-rider boundary (FAQ: 'Is a rider the same as a tax or fee? — see utility bill taxes...').
- ai_slop: none notable — 'actually are' framing with PUCO/ORC citations is concrete.
- visual_gaps: has base-rate-vs-rider anatomy + 4-step verify; strong visual set.
- action: keep. Next: add per-row source links for the rider table; keep cross-link to 25 for tax boundary.

---

### /blog/20-utility-bill-proration-explained/ — How to Review a Partial-Period Utility Bill
- purpose/intent: proration mechanics; verified SMUD tariff rule + day-count math.
- quality: 8/10
- seo: 7/10
- weaknesses: very strong on method ('SMUD: the electricity usage charge is not prorated... System Infrastructure Fixed Charge is prorated when the bill period is shorter than 27 days'); overlaps 23 billing-cycle dates and 27/28 move events; 'the 10th through the 28th inclusive is 19 days, so a bill printing 18 carries an off-by-one error' is a memorable original detail.
- ai_slop: none.
- visual_gaps: no diagram of a month calendar with service dates; a start/stop timeline would help.
- action: keep. Next: add a small calendar graphic; keep FAQ and the SCE 30-day deposit close-out reference (good cross-link to 26).

---

### /blog/21-past-due-balance-utility-bill-explained/ — How to Review a Past-Due Balance on a Utility Bill
- purpose/intent: prevent-shutoff action guide; reconcile → verify notice → assistance → protect service.
- quality: 9/10
- seo: 7/10
- weaknesses: excellent verified state rules (MN 216B.096/097 Cold Weather: Oct 1–Apr 30, 10 working days mail / 7 personal / 30 / 15; TX 10-day + no-disconnect-on-disputed + deferred plan); overlaps 28 on LIHEAP + payment-plan guidance and can-utility-shut-off-service.md (outside shard) — the assistance block is repeated on 26/27/28 ('LIHEAP assists roughly 6.7 million households', hotline (866) 674-6327).
- ai_slop: none — deadline-first framing ('the date printed on a disconnection notice — not the balance itself — is the deadline that matters') is original and actionable.
- visual_gaps: has bill anatomy + notice timeline; strong.
- action: keep. Next: canonicalize LIHEAP/assistance block once (likely on utility-assistance-programs-liheap) and link from 26/27/28.

---

### /blog/22-minimum-bill-utility-bill-explained/ — How to Review a Minimum Charge on a Utility Bill
- purpose/intent: explain minimum-bill floor with verified tariff clauses.
- quality: 8/10
- seo: 7/10
- weaknesses: compact (98 lines) but complete; verified clauses (Avista Schedule 1 $10.00 min, Schedule 11 $30.00/$37.35, PG&E gas $0.13151/day, PG&E electric $0.41373/day EM; PG&E March 2026 'replaces the monthly Minimum Electric Charge') — the PG&E restructure fact is repeated on 17/24 and should be canonicalized on 22 or 17; FAQ 'Is a minimum bill the same as a customer charge?' explicitly distinguishes equality vs identity (also on 17's FAQ).
- ai_slop: none — 'A minimum bill is the least you owe for service in a billing period no matter how little you use' is a crisp definition.
- visual_gaps: no visual; a floor-vs-usage chart (same shape as 17's fixed-share table) would help.
- action: keep. Next: add a small floor/usage chart; ensure 17 links here for the same-number explanation.

---

### /blog/23-utility-billing-cycle-explained/ — How to Read the Billing Period on a Utility Statement
- purpose/intent: billing-cycle understanding; daily-average method; normal-vs-worry gate.
- quality: 9/10
- seo: 8/10
- weaknesses: longest in cluster (211 lines) and best structured (long/short month math table 28d vs 33d $130.20/$153.45 flat 30.0 kWh/day); overlaps 14 (estimated-vs-actual table with identical trigger facts), 20 (proration), 21 (deadline), 22 (minimum keeps bill from dropping); the estimated-read section could defer to 14 more aggressively.
- ai_slop: none — 'Billing periods rarely match calendar months, and most differences between two bills are routine' with a decision gate table.
- visual_gaps: strong visual set (4+ timeline/diagram visuals).
- action: keep. Next: trim the estimate section to a summary + link to 14; this page is a good internal-linking spine for the cluster.

---

### /blog/24-delivery-charge-vs-supply-charge-utility-bill/ — Delivery Charge vs Supply Charge on a Utility Bill
- purpose/intent: explain the two-bucket bill structure; verified per-utility split table; shopping guidance.
- quality: 9/10
- seo: 8/10
- weaknesses: strong verified data (ConEd TOU supply 27.86/17.11/5.22¢, delivery 16.402¢, $21.00; Austin PSA 4.118¢ net 3.912¢; PAPowerSwitch '1,429,674 Pennsylvanians have switched suppliers as of July 2026'); worked 899 kWh month is a model of applied math; overlaps gas-delivery (same two-bucket model, different fuel — correct to keep both) and 17 (fixed charge canonicalization), 18 (supply mechanism), 49 (demand inside delivery).
- ai_slop: none — 'If you use exactly zero kWh, the delivery bucket's fixed charge still appears; the supply bucket does not' is the sharpest tell in the cluster.
- visual_gaps: has split diagram + table; strong.
- action: keep. Next: emphasize it as the electricity canonical and cross-link gas-delivery for the fuel-specific version; verify EIA 18.34¢/899 kWh stats against metrics file.

---

### /blog/25-utility-bill-taxes-fees-franchise-charges-explained/ — Taxes, Fees, and Charges on Your Utility Bill
- purpose/intent: authority matrix for non-usage lines (tax vs fee vs franchise).
- quality: 8/10
- seo: 7/10
- weaknesses: verified examples are excellent (Pasadena 7.67%/7.9%/7.67%, WA cap 6% RCW 35.21.870, Cheney 14.75%, FL cap 10% 166.231, MN 216B.36 gross-operating-revenue franchise); overlaps 19 on rider-vs-tax boundary; the gross-receipts $100→$11.11 example is the kind of original teaching the cluster needs more of.
- ai_slop: none.
- visual_gaps: has 3 visuals (annotated lines, gross-receipts example, verify steps) — one of the best visual sets.
- action: keep. Next: keep 19/25 boundary explicit; add a map-style 'your state's cap' teaser if later content exists.

---

### /blog/26-utility-deposit-explained/ — How to Review a Utility Deposit Requirement
- purpose/intent: deposit verification; state caps, waivers, refund timing.
- quality: 8/10
- seo: 7/10
- weaknesses: verified state rules (TX 1/5 annual or next-2-months; SCE currently not billing deposits / if resumed 2×12-mo avg; SCE refund after 12 on-time + 30-day closing; MN 216B.098 bars new deposit on accepted payment agreement); overlaps 21 and 27 on assistance/lifecycle; 'Texas caps deposits tightly... an amount above that cap is itself grounds for a question' is a strong CTA but no complaint-form link anywhere.
- ai_slop: none — cap ruler visual is original.
- visual_gaps: has deposit lifecycle timeline; good.
- action: keep. Next: add a direct link to the state PUC complaint path; keep the fee-router cross-link with 27.

---

### /blog/27-utility-connection-fee-explained/ — How to Review a Utility Service-Start Charge
- purpose/intent: service-start fee verification; published point examples + fee-router.
- quality: 8/10
- seo: 7/10
- weaknesses: good discipline line — published examples (Georgia Power $30, Alabama Power $40, SRP $30/$45 + $35 field visit, TCEC $20, MTE structure distinction) explicitly 'not a national range'; fee-router figure is a genuinely helpful UX pattern; overlaps 26 (deposit: FAQ 'Is a connection fee the same as a deposit? — No...'), 28 (reconnection), how-to-budget-for-utilities-in-your-first-apartment, moving-utilities-checklist.
- ai_slop: none — 'a deposit is refundable or creditable under the provider's rules, while a service-start charge may be final' draws a clean line.
- visual_gaps: has router + first-statement anatomy; strong.
- action: keep. Next: keep point-examples current (SRP 'next day'/'same day' pricing may drift); extend the fee-router pattern to 26/28 if not already mirrored.

---

### /blog/28-utility-reconnection-fee-explained/ — How to Verify a Utility Reconnection Charge
- purpose/intent: reconnection fee + restoration process after shutoff.
- quality: 6/10
- seo: 5/10
- weaknesses: the weakest page in the cluster. The 'Typical Reconnection Fee Table by State' (PG&E $75–300 Rule 23, SCE $15–200, ConEd $75–150, PECO $50–100, PSE&G $75–200, Consumers $25–85, Georgia Power $25–70, CPS $25–50) carries an unsupported claim — 'each verified via state PUC dockets 2024–2026' — but the Sources section lists only CFPB, LIHEAP, DOE; no per-row citation exists on the page. This contradicts the house doctrine used by sibling 27 ('Do not rely on a national fee range') and the cluster's tariff-first standard. Generified claims throughout: 'Reconnection fees typically range from $10 to $300', 'Gas ... Fees can be $50–$250', 'Water ... generally $25–$150'. Winter-moratorium claims ('New York, Michigan, Illinois, Maryland, Pennsylvania ... November through March') conflict with 21's Minnesota Oct 1–Apr 30 framing. Restoration step specifics (electric 1–4 hours, gas 1–2 hours relight) are asserted without source.
- ai_slop: medium — formulaic process list, unsupported ranges, no original verified evidence; the only real citations are the CFPB/LIHEAP/DOE boilerplate shared with 21/26.
- visual_gaps: 5 visuals (fee chart, process, avoidance, timeline) — visually the richest page; the problem is textual.
- action: improve (or rewrite). Next: (1) either add a real tariff citation per row or strip the fee table to structure-only like 27; (2) align moratorium language with 21/can-utility-shut-off-service; (3) cite or remove the restore-timing specifics; (4) keep LIHEAP block but canonical-link to 21 for notice/protection rules.

---

### /blog/46-what-time-is-electricity-cheapest/ — What Time Is Electricity Cheapest?
- purpose/intent: quick-reference answer for TOU cheapest hours; then hands off depth to 08.
- quality: 8/10
- seo: 7/10
- weaknesses: thin by line count (80 lines) but earns its URL as the answer page; clean intent separation from 08 ('This page provides the quick-reference answer. For a full explanation... see Time-of-Use Electricity Rates Explained'); real 2026 examples (PG&E E-TOU-C off-peak $0.3676–0.3994 winter, ConEd off-peak supply 5.22¢, TXU Free Nights $0 up to 2,000 kWh); savings math worked ($45/mo summer shift on 200 kWh); product box is contextually relevant.
- ai_slop: low — the 'Note on Your Exact Hours: Do not assume the hours in the table above apply to you' disclaimer is honest, not slop.
- visual_gaps: has TOU clock + 24h price curve; good.
- action: keep. Next: add a state/zip lookup teaser if rate-plan hub grows; keep strong 08 handoff.

---

### /blog/49-demand-charges-electricity-bill-explained/ — How to Review a Demand Charge on an Electricity Bill
- purpose/intent: demand charge verification (kW vs kWh, interval, ratchet) — mostly commercial.
- quality: 7/10
- seo: 7/10
- weaknesses: real substance (Forest Service 30–70% of commercial bills; SRP 60-minute on-peak intervals; Stillwater 15-minute intervals + 65% ratchet + 80% power-factor correction; Hamilton OH kVA), but Sources list shows the same DOE URL twice (items 1 and 2 are identical energy.gov links) — sloppy citation hygiene; audience is narrow (residential searchers may not have a demand line); FAQ answers are procedural rather than example-driven.
- ai_slop: low — 'kW is the rate of use in a single interval, kWh is energy accumulated over time' is crisp.
- visual_gaps: has kW-vs-kWh strip + 15-min curve; good visuals.
- action: improve. Next: fix duplicate source; add a worked dollar example with a named tariff; add a residential-vs-commercial 'does this apply to me' gate near the top.

---

### /blog/12-how-to-read-your-gas-bill/ — How to Read Your Gas Bill
- purpose/intent: gas bill walkthrough; line items, therm/CCF conversion, seasonal comparison.
- quality: 8/10
- seo: 7/10
- weaknesses: line-item walkthrough table + worked 64-therm check + 1.037 conversion are strong; seasonality block ('January runs about 19% of the annual total versus about 2.4% in July') and the Columbia Gas SCO worked example ($2.7250 + $2.25 = $4.975/Mcf, billed $0.4975/Ccf) are duplicated nearly verbatim on gas-delivery-charge-vs-supply-charge — the clearest cannibalization pair in the cluster; off-season price trap note ('May 2026 averaged $19.83/Mcf') is a sharp original insight; overlaps mcf-vs-ccf-vs-therms and 07-gas-bill-too-high (both outside shard) but reconciling-guides section explicitly bridges them.
- ai_slop: low — worked examples carry the page; some table cells are generic ('Your utility's tariff or rate schedule').
- visual_gaps: has annotated gas bill anatomy; one diagram per major concept would help (conversion chain).
- action: improve/merge-target. Next: absorb gas-delivery-charge-vs-supply-charge into a deep-dive section (preserve its correction note), redirect gas-delivery slug; keep therm/CCF content split cleanly from mcf-vs-ccf-vs-therms.

---

### /blog/gas-delivery-charge-vs-supply-charge/ — Gas Delivery Charge vs Supply Charge Explained
- purpose/intent: gas two-bucket delivery/supply explanation + shopping guidance.
- quality: 8/10
- seo: 7/10
- weaknesses: strong content buried under a cannibalized URL — the SCO worked example and EIA Jan 19%/Jul 2.4% paragraph are near-identical to 12; the most valuable asset is the explicit correction note ('this guide previously used Columbia Gas of Ohio's $3.25 per Mcf added to NYMEX figure as a delivery example... miscategorized... corrected') — a rare trust-building artifact that must be preserved if merged; 'Bottom Line' sums up well ('The supply charge is the molecule; the delivery charge is the pipes').
- ai_slop: low — but the page's core teaching is redundant with 12 unless it differentiates harder.
- visual_gaps: no visual on this page (0 {{< visual >}}), the only major page in the cluster without one.
- action: merge -> /blog/12-how-to-read-your-gas-bill/. Next: fold the two-category table + correction note + shopping guidance into 12 as a 'Delivery vs Supply Deep-Dive' section; 301 the gas-delivery URL; keep 24 as the electricity canonical and cross-link.

---

## CLUSTER OVERLAP MAP

Pairs with >40% topical overlap (shared query space = gas/electric bill charges, delivery vs supply, fixed charges, estimates, shutoff/assistance):

1. 12-how-to-read-your-gas-bill ↔ gas-delivery-charge-vs-supply-charge — overlap ~70%. Shared query space: 'gas delivery charge vs supply charge', 'gas bill charges'. Identical SCO worked example ($2.7250+$2.25=$4.975/Mcf, $0.4975/Ccf), identical EIA seasonality sentence family (Jan ~19% / Jul ~2.4%), same supply/delivery framing and ConEd quotes. **Stronger: 12** (broader read-the-bill intent). **Merge direction: gas-delivery → 12** (absorb two-category table + correction note + shop-supply section; redirect slug; gas-delivery page currently has no visual so nothing lost).
2. 24-delivery-charge-vs-supply-charge ↔ gas-delivery-charge-vs-supply-charge — overlap ~50% conceptually. Shared query space: 'delivery vs supply charge'. Different fuel, different shopping rules; cross-linked both ways already. **Stronger: 24** (more verified data + visuals). **Merge direction: none** — keep both as fuel-specific canonicals; gas side consolidates into 12 per pair 1.
3. 17-what-is-customer-charge ↔ 22-minimum-bill — overlap ~45%. Shared query space: 'fixed monthly charge on utility bill', 'why is my bill the same when I don't use much'. FAQ pairs teach equality-vs-identity ('They can be equal without being the same thing'); PG&E March 2026 restructure fact repeated on 22/24. **Stronger: 17** (verified amounts table). **Merge direction: none** — distinct line items; canonicalize the PG&E restructure fact to 17 or 22 and link.
4. 18-fuel-adjustment ↔ 19-surcharges-and-riders — overlap ~45%. Shared query space: 'fuel adjustment', 'utility rider charge'. Mechanisms vs line-items taught symmetrically ('Adjacent, not identical: the rider is the commission-approved mechanism; the fuel adjustment charge is the line item it produces'). **Stronger: 19** (broader rider mechanism + 5 real riders). **Merge direction: none** — keep both; each FAQ explicitly routes the reader to the other; add one canonical statement on 04's table row.
5. 14-estimated-utility-bill ↔ 23-utility-billing-cycle — overlap ~40%. Shared query space: 'estimated vs actual meter reading'. 23 has an estimated-vs-actual table with the same trigger facts (locked gate/dog/weather) and true-up explanation; 14 has the force-actual-read workflow + TX rules. **Stronger: 14** (specialist depth). **Merge direction: partial** — keep both; trim 23's estimate section to summary + link to 14; dedup trigger lists.
6. 21-past-due-balance ↔ 28-reconnection-fee — overlap ~45%. Shared query space: 'utility shutoff', 'utility bill assistance', 'disconnection notice'. Both carry LIHEAP/CFPB block, payment-plan guidance, TX 10-day notice, winter-protection framing; 28's moratorium claims conflict with 21's verified MN rules. **Stronger: 21** (verified state law citations). **Merge direction: none** (prevent vs restore intent) — but 28 must cite 21 + can-utility-shut-off for protection rules and stop restating unsourced ranges.
7. 26-utility-deposit ↔ 27-utility-connection-fee — overlap ~40%. Shared query space: 'new utility service fees', 'utility setup charges'. Fee-router figure explicitly separates the three branches; FAQs distinguish deposit vs service-start charge. **Stronger: 27** (fee-router + published point examples). **Merge direction: none** — distinct line items; strengthen existing cross-links.
8. 04-hidden-fees ↔ 17/18/19/20/21/22/25/26/27/28 — hub-spoke architecture: overlap is deliberate (~40-60% against any spoke on the shared query space 'every charge on utility bill explained'). **Stronger: each spoke** (depth) with 04 as TOC. **Merge direction: none** — keep table summary-level; verify no spoke outranks the hub on its own keyword (17's title is the strongest for 'customer charge').
9. 46-what-time-is-electricity-cheapest ↔ 08-time-of-use-electricity (outside shard) — overlap ~40% conceptually. Shared query space: 'cheapest time to use electricity' vs 'time-of-use rates'. Intent separation is explicit: 46 = quick reference, 08 = mechanism. **Stronger: 08** (depth). **Merge direction: none** — keep 46 as answer page with strong handoff (already present).
10. 11-understanding-kwh-usage ↔ what-is-a-kilowatt-hour (outside shard) — overlap ~50% expected. Shared query space: 'kilowatt hour', 'kWh explained'. **Cross-shard lead for Commander**: dedup/redirect one before both compete.
11. 09-apartment-utilities-cost ↔ average-utility-bills-by-state-2026 (outside shard) — overlap ~40% on the 10-state table. Shared query space: 'average utility bills by state'. 09's table is a duplicate (page even links out to the 50-state page). **Cross-shard lead**: 09 should keep apartment-specific framing only and link the state page.
12. 49-demand-charges ↔ 24-delivery-charge-vs-supply-charge — overlap ~40%. Shared query space: 'demand charge on electric bill'. Demand sits inside the delivery bucket; both linked. **Stronger: 24** (breadth). **Merge direction: none** — keep 49 as specialist; existing related-reading covers it.
13. 20-utility-bill-proration ↔ 23-utility-billing-cycle — overlap ~40%. Shared query space: 'why is my utility bill prorated', 'billing period days'. Proration = period-length subset; both cover service dates. **Merge direction: none** — 23 links 20 for partial-periods already; keep.

**Merge candidates ranked:**
1. gas-delivery-charge-vs-supply-charge → merge into 12-how-to-read-your-gas-bill (highest duplication; preserve correction note; 301 redirect).
2. 28-utility-reconnection-fee — improve-not-merge: replace unsourced fee table with real tariff citations or structure-only; fix moratorium conflict.
3. 09-apartment-utilities-cost — improve: de-dup state table with average-utility-bills-by-state; add FAQ + visual; if not improved it risks noindex for thinness.
4. (Cross-shard) 11 vs what-is-a-kilowatt-hour; 09 vs average-utility-bills-by-state — Commander to route merge decisions site-wide.

**Templated repetition summary (whole-cluster):**
- 22/22 pages open with '## Quick Answer' + bold imperative claim; 14/22 H1s start 'How to Review/Verify a ...' — formulaic but each Quick Answer carries distinct verified content; not sentence-level slop.
- Repeated knowledge-base facts: EIA 18.34¢/kWh (≥5 shard pages: 10,11,14,24,46), EIA 899 kWh (4: 11,23,24,46), LIHEAP 6.7M + hotline (21,26,28 + others), PG&E March 2026 restructure (17,22,24), Consumers $8 System Access (17,24), SCO example (12,gas-delivery), CFPB 'Get help paying rent and bills' cited in 8/22 shard pages. These are same-source repeats, not word-for-word plagiarism — canonicalize, do not rewrite.
- ConEd is the most-cited source (13/22 shard pages); puc.texas.gov in 6. Heavy single-source dependence is a freshness risk if either changes.

**Cross-shard leads for Commander:**
- Verify EIA 18.34¢/kWh June 2026 + 899 kWh/month + 10,791 kWh/2022 against .squad/content-metrics.md (global fact, 9 whole-site files).
- 28's 'verified via state PUC dockets 2024–2026' claim cannot be checked from any URL on the page — fact-check before trusting the fee table.
- Demand/TOU/rate-plan cluster (08, 10, 46, 49, which-rate-plan, tiered-rates) needs a second-wave audit as one unit.
- Gas cluster overlap with mcf-vs-ccf-vs-therms and 07-gas-bill-too-high (outside shard) — route merge decision site-wide.
