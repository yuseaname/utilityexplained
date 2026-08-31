# SQ-065 Wave 1 — Tracer: The "My Bill Went Up → Why? → What Do I Do?" Journey

**Seat:** tracer (deep thread trace)
**Date:** 2026-08-30
**Scope:** 14 assigned blog pages + examine-only links of `average-utility-bills-by-state-2026` and `04-hidden-fees-utility-bill` (no entries written for those two per packet).
**Ground truth used:** `.squad/content-metrics.md` (words/ilinks per page), `rg`-verified internal links from every page source.

---

## The Journey Thread (framed)

**Entry:** reader opens a high-bill diagnosis page -> **diagnose** (03, why-did, 30-spike, breakdown, complete-guide, rates-fees) -> **act** (dispute, shutoff, assistance) -> **plan** (budget, moving) -> **forward** (rate-plan/EV/solar).
**Termination:** a page with zero useful onward links (dead end), an external third-party (utility/PUC/LIHEAP), or the reader giving up. The journey ends early right now because every diagnosed "bill is wrong / too high" path splits without an edge into act/plan pages, and the two largest forward-looking pages are absolute dead ends.

---

## Page-by-Page Audit (14 entries)

### /blog/03-why-is-my-electric-bill-so-high/ — Why Is My Electric Bill So High? Find the Real Cause
- **Purpose/intent:** Informational diagnosis — the entry hub for "why is my bill high." Serves homeowners troubleshooting a spike; commercial intent light (Amazon products embedded).
- **Quality: 8/10 · SEO: 8/10** (1,490 words; 6 ilinks; 6 sources; FAQ; 2 tables; hero + 2 diagrams + 2 product boxes)
- **Weaknesses:** The "rate change / billing error" branch (Quick Answer items 3–4; diagnosis sequence item 2) has no link to **which-rate-plan-is-right-for-me**, **how-to-dispute-utility-bill**, or **can-utility-shut-off-service**. The text says "contact the utility... dispute process" but links none of the site's act pages. A reader who decides "this is a billing error" is left to search.
- **ai_slop:** none — specific EIA figures, DOE save citations, concrete diagnosis sequence.
- **visual_gaps:** None significant; flowchart + seesaw diagram already present.
- **action:** improve — add act-cluster forward links (dispute, shutoff, rate plan) at the "When to Contact the Utility" section.
- **onward links (observed):** 01-how-to-read-electric-bill, electric-bill-breakdown-understanding-line-items, do-home-energy-monitors-save-money, 42-best-energy-efficient-space-heater, ev-charging-impact-electric-bill, how-to-lower-electric-bill-complete-guide. **Reader still needs:** how-to-dispute-utility-bill, can-utility-shut-off-service, which-rate-plan-is-right-for-me.

### /blog/why-did-my-utility-bill-go-up-this-month/ — Why Did My Utility Bill Go Up This Month?
- **Purpose/intent:** Informational — month-over-month cause ranking. Serves homeowners with a sudden jump and "nothing changed."
- **Quality: 6/10 · SEO: 6/10** (1,145 words; 2 markdown ilinks + 6 HTML hrefs; 1 source; FAQ; HTML body with markup, only 1 markdown heading)
- **Weaknesses:** Body is HTML `<h2>`/`<p>`, so metrics show a nearly heading-less file; visually four `<ContentImage>` figures compensate in production but content density is modest. The ranked causes link to deep explainers (billing cycle, estimated bill, rates-fees) but the forward act layer is absent — no dispute, no shutoff, no rate-plan switch.
- **ai_slop:** none — concrete ranked list, per-cause confirm steps.
- **visual_gaps:** none — three diagrams present.
- **action:** improve — add dispute/shutoff edges when cause #2 (rate change) or an error suspicion appears.
- **onward links (observed):** 30-sudden-spike, tiered-water-rates (markdown), plus hrefs: utility-bills-costs-explained hub, 23-utility-billing-cycle, 14-estimated, 24-delivery-vs-supply, why-electric-bil-changes-month-to-month (alias of 03 — resoves, but a wrong-target smell), hub. **Reader stll needs:** how-to-dispute-utity-bil, which-rate-plan-is-right-for-me.

### /blog/30-sudden-spike-in-electricity-bil-no-usage/ — Sudden Spike in Electricity Bil, No Usage Change
- **Purpose/intent:** Informational troubleshooting — deepest diagnostic in the cluster: 10-cause table + 12-step investigation.
- **Quality: 9/10 · SEO: 8/10** (3,543 words; 11 ilinks; 4 sources; FAQ; product boxes)
- **Weaknesses:** Almost the model tracing page — every cause links to its expainer. Two gaps: (1) cause #4 "hidden fees / rider charges" mentions rider lines but does not link 04-hidden-fees-utity-bil; (2) after the formal-dispute path is named it links dispute, but no edge to can-utity-shut-off when the reader's account is in arrears afte a spike they refuse to pay.
- **ai_slop:** none — worked examples, dollar ranges, named mechanisms.
- **visual_gaps:** none meaningful — flowchart + bar chart + meter photo.
- **action:** keep (minor improve) — add 04-hidden-fees link in Step 1, and shutoff edge near the dispute path.
- **onward links (observed):** 18-fuel-adjustment, 03-why-is-my-electric-bil-so-high, aux-heat-vs-emergency-heat, electric-bil-breakdown, 01-how-to-read, 46-what-time, 49-demand-charges, 14-estimated, 50-smart-plugs, how-to-dispute, how-to-lower-electric-bil-complete-guide. **Reader stll needs:** 04-hidden-fees-utity-bil, can-utity-hut-off-service.

### /blog/electric-bil-breakdown-understanding-line-items/ — Electric Bil Breakdown: Every Charge Explained
- **Purpose/intent:** Informational categorical — every line item named, with deep-dive links.
- **Quality: 8/10 · SEO: 8/10** (2,394 words; 18 ilinks; 4 sources; 9 FAQs; category table + TOU image)
- **Weaknesses:** Excellent line-item hub. Escalation text links how-to-dispute (good — this is the one page that does complete the act edge). Missing: no link to complete-guide-understanding-utity-bil (the bigger hub) and no link to which-rate-plan in the TOU section (has 10-fixed-vs-variable but not the decision page).
- **ai_slop:** none — EIA price figures, ConEd labels, CPU estimated-read rule.
- **visual_gaps:** none — 4-numbers image, TOU chart, category map.
- **action:** keep (minor improve).
- **onward links (observed):** 03, 01-read-bil, what-is-a-kilowatt-hour, 23-biling-cycle, 17-customer-charge, 10-fixed-vs-variable, how-to-read-electric-meter, 04-hidden-fees, 24-delivery-vs-supply, 49-demand, how-to-dispute, 18-fuel, 19-surcharges, which-rate-plan, 01. **Reader still needs:** complete-guide-understanding-utility-bill.

### /blog/complete-guide-understanding-utility-bill/ — The Complete Guide to Understanding Your Utility Bill (Every Line Explained)
- **Purpose/intent:** The pillar hub — 5-step workflow, verified bill, charge map to every explainer.
- **Quality: 9/10 · SEO: 9/10** (1,768 words; 28 ilinks; 6 sources; 7 FAQs; 12 tables)
- **Weaknesses:** **The worst missing edges in the whole journey.** The page's "When to escalate safely" section (line 137–139) tells the reader to "Follow the provider's written billing-review process" without linking the site's own **how-to-dispute-utility-bill**. It is the site's most-linked authoritative page and it never routes a reader to dispute, shut-off, assistance, or rate-plan pages. A reader at the apex of the funnel who concludes "bill is wrong" is dropped.
- **ai_slop:** none — verified bill, named sources per line.
- **visual_gaps:** none — annotated sample bill + tables.
- **action:** improve — add act-cluster links from "When to escalate safely": dispute, shutoff, assistance, rate plan.
- **onward links (observed):** average-utility-bills, 01-read-bill, 17-customer-charge, 24-delivery-vs-supply, gas-delivery-vs-supply, 11-kwh, 12-gas-bil, what-is-cf, 19-surcharges, 25-taxes, 18-fuel, 49-demand, 08-TOU, iered-electricity, 14-estimated, 20-proration, 22-minimum, 21-paid-due, how-sewer, how-utity-rates, gas-side, iered-water* (not in body). **Reader stll needs:** how-to-dispute-utity-bil, can-utity-hut-off-service, utity-asistance-programs-LIHEAP, which-rate-plan-is-right-for-me.

### /blog/how-utity-rates-fees-usage-work-together/ — How Uility Rates, Fees, and Usage Work Together
- **Purpose/intent:** Educational model — the three-bucket explanation.
- **Quality: 5/10 · SEO: 5/10** (808 words; 1 markdown ilink + 8 HML hrefs; 1 source; FAQ; layered model images)
- **Weaknesses:** Thinnest and most structurally inconsistent page in the set: almost all body is HML, so the file has only one Markdown heading and markdown ilinks=1. Its HML hrefs do reach the correct expainers (TOU, iered, water-service, taxes, net-merering, why-did, hub), but the page provides no decision edge into which-rate-plan. For an 808-word educational model this is acceptable depth, but it is the cluster's weakest link target.
- **ai_slop:** none — clean layered model, misconception list.
- **visual_gaps:** none — 4 ContentImage diagrams.
- **action:** improve — convert HML to Markdown heading structure; link which-rate-plan from the rates section.
- **onward links (observed):** complete-guide-understanding-utility-bill (markdown), plus hrefs: net-metering-explained, utility-bills-costs-explained hub, tiered-electricity-rates, 08-TOU, water-service-charge, 25-taxes, why-did-my-utility-bill, why-electric-bill-changes (alias→03). **Reader still needs:** which-rate-plan-is-right-for-me.

### /blog/which-rate-plan-is-right-for-me/ — Which Rate Plan Is Right: Fixed vs Variable vs TOU
- **Purpose/intent:** Informational decision — match plan to usage pattern.
- **Quality: 7/10 · SEO: 8/10** (702 words; 17 ilinks; 3 sources; 2 tables; decision clock)
- **Weaknesses:** Short but decision-focused. The Decision List item #1 explicitly mentions "EV charging overnight" yet does not link **ev-harging-impact-electric-bill** — a clear missed edge. It links net-metering (good) but the net-metering page is a dead end (see below).
- **ai_slop:** none — PG&E tariff citation, EIA price, concrete decision questions.
- **visual_gaps:** none — decision clock visual.
- **action:** improve — add ev-charging link in Decision List #1, 08-TOU already linked.
- **onward links (observed):** 10-fixed-vs-variable, 49-demand, tiered-water, 08-TOU, 46-what-time, 22-minimum, net-metering-explained, 24-delivery-vs-supply, 11-kwh, 05-lower-utility. **Reader still needs:** ev-charging-impact-electric-bill.

### /blog/how-to-dispute-utility-bill/ — How to Dispute a Utility Bill
- **Purpose/intent:** Transactional/action — escalation ladder, template letter, evidence log, state PUCs.
- **Quality: 8/10 · SEO: 8/10** (2,557 words; 5 ilinks; 11 sources; FAQs; template; no box; placeholder=0)
- **Weaknesses:** The act spine is well-built (links estimated, past-due, deposit, complete-guide, shutoff). Gaps: (1) the "Payment Assistance While You Dispute" section names LIHEAP and links external liheap.org but does NOT link the internal **utility-assistance-programs-liheap** page; (2) no backlink to 03 / 30-spike for the diagnosis context; (3) while it mentions state PUCs it links external naruc/usa.gov only — acceptable, but an internal hub link to weatherization/assistance would keep the user on-site.
- **ai_slop:** none — CA/CPUC, TX/PUCT citations, scam warning, template letter.
- **visual_gap:** Minor — a step diagram would aid; currently text/table only.
- **action:** improve — link internal LIHEAP page from Payment Assistance section.
- **onward links (observed):** 21-past-due, 26-deposit, 14-estimated, complete-guide, can-utility-shut-off. **Reader still needs:** utility-assistance-programs-liheap.

### /blog/can-utility-shut-off-service/ — Can the Utility Shut Off Your Service? What to Know
- **Purpose/intent:** Action/crisis — shutoff process, protections, how to stop a shutoff.
- **Quality: 8/10 · SEO: 8/10** (3,102 words; 6 ilinks; 6 sources; FAQs; tables; 2 callout boxes)
- **Weaknesses:** Strong crisis page. The assistance edge to LIHEAP page is present. Gaps: the water-shutoff section is local-rule-only with no site resource (acceptable), and the reconnection section links deposit/reconnection fees (good). Missing edge: none critical; this is the best act-page in the cluster.
- **ai_slop:** none — Minnesota statutes, USAGov, NARUC citations.
- **visual_gap:** minor — no visual for the step table; the table suffices.
- **action:** keep.
- **onward links (observed):** 14-estimated, utility-assistance-programs-liheap, 28-reconnection-fee, 26-deposit, how-to-dispute. **Good act spine.**

### /blog/utility-assistance-programs-liheap/ — LIHEAP, Utility Assistance Programs, & More
- **Purpose/intent:** Action/plan — crisis assistance, LIHEAP/WAP, hardship programs.
- **Quality: 7/10 · SEO: 7/10** (1,057 words; 8 ilinks; 3 sources; 5 FAQs; 6 tables)
- **Weaknesses:** Good support hub. Its "Emergency: Facing Shut-off This Week" section (Day 1) does not link **can-utility-shut-off-service** even though the crisis page is the exact complement — a reader who is facing shutoff needs the protections page, yet the LIHEAP page only links budgeting/complete-guide cluster. Missing edge: LIHEAP → can-utility-shut-off-service.
- **ai_slop:** none — benefits.gov/liheap.org links, concrete Day-1 actions.
- **visual_gap:** Minor — no diagram of the application flow that the section describes.
- **action:** improve — add can-utility-shut-off link in the Emergency section.
- **onward links (observed):** complete-guide (x2), 01-read-bill, 05-lower, 16-budget-billing, 21-past-due, how-to-budget, how-utility-rates. **Reader still needs:** can-utility-shut-off-service.

### /blog/how-to-budget-for-utilities-in-your-first-apartment/ — How to Budget for Utilities in Your First Apartment
- **Purpose/intent:** Plan — first-apartment budgeting, deposits, setup.
- **Quality: 7/10 · SEO: 7/10** (1,217 words; 6 ilinks; 1 source; 4 FAQs; HTML body)
- **Weaknesses:** Solid plan page. Missing: (1) no link to **which-rate-plan** when discussing choosing plans; (2) no link to **utility-assistance** when the budget section discusses affordability concerns (text says "ask your provider about budget billing" but doesn't link internal assistance page); (3) HTML-heavy but acceptable.
- **ai_slop:** none — concrete budget ranges, deposit/credit check details.
- **visual_gap:** Minor — budget table would help; currently prose/HTML only.
- **action:** improve — add which-rate-plan and utility-assistance edges.
- **onward links (observed):** average-water-usage, 26-deposit, moving-utilities-checklist, why-did-my-utility-bill, 47-energy-leaks, 09-apartment-utilities-cost. **Reader still needs:** which-rate-plan, utility-assistance-programs-liheap.

### /blog/moving-utilities-checklist/ — Moving Utilities Checklist
- **Purpose/intent:** Plan/action — transfer/deposit/connection/meter reading on a move.
- **Quality: 8/10 · SEO: 8/10** (2,078 words; 8 ilinks; 4 sources; FAQs; checklist)
- **Weaknesses:** Strong planning page with the best act edges in the plan cluster (deposit, connection fee, proration, shutoff, budget, meter reads). Minor gap: the final-bill dispute paragraph mentions "shutoff dispute" (good) but could link the full dispute page directly.
- **ai_slop:** none — concrete timeline, deposit refund mechanics, photo evidence tip.
- **visual_gap:** Minor — printable checklist is text, would benefit from a visual timeline.
- **action:** keep.
- **onward links (observed):** 26-deposit, 27-connection-fee, 20-proration, can-utility-shut-off, how-to-budget, how-to-read-electric-meter, how-to-read-gas-meter, how-to-read-a-water-meter. Good.

### /blog/net-metering-explained/ — Net Metering: How Solar Affects Your Electric Bill
- **Purpose/intent:** Forward — solar export crediting, NEM 2.0 vs NEM 3.0, bill anatomy.
- **Quality: 6/10 · SEO: 4/10** (1,196 words; **0 internal links**; 4 sources; 6 FAQs; 2 tables)
- **Weaknesses:** **ABSOLUTE DEAD END.** `rg '\]\(/'` returns zero internal links; body contains zero `href="/..."` internal links — only external source URLs. Content is strong (SCE/CPUC citations, concrete 400kWh x 6c example) but the page points nowhere on-site. A reader who lands here from which-rate-plan or how-utility-rates is stranded; the TOU/battery strategy discussion that would naturally link 08-time-of-use, 46-what-time, and which-rate-plan is left as prose.
- **ai_slop:** none — SCE/CPUC citations, labeled illustrative math, FAQ distinctions.
- **visual_gap:** Significant — no diagram of import/export/settlement flow; no visual of a solar bill.
- **action:** improve/rewrite link layer — add internal links to which-rate-plan, 08-TOU, 46-what-time, electric-bill-breakdown, 49-demand; add an import/export diagram.
- **onward links (observed):** none. **Reader still needs:** which-rate-plan, 08-time-of-use, 46-what-time-is-electricity-cheapest, electric-bill-breakdown.

### /blog/ev-charging-impact-electric-bill/ — How EV Charging Can Affect Your Electric Bill
- **Purpose/intent:** Forward — EV charging cost math, TOU rate planning, charger hardware.
- **Quality: 7/10 · SEO: 4/10** (1,530 words; **0 internal links**; 4 sources; 0 FAQs; 9 tables; 1 box)
- **Weaknesses:** **ABSOLUTE DEAD END.** Zero internal links, same as net-metering. Content is excellent — level 1/2 comparison, cost/mile math, battery-size table, plan-check list — and 03 links to it, so it receives traffic, but sends readers nowhere. Its TOU discussion should link which-rate-plan, 08-TOU, 46-what-time, 49-demand (demand charges explicitly mentioned); the Emporia-powered monitoring text should link do-home-energy-monitors-save-money.
- **ai_slop:** none — EIA Table 5a, Georgia Power R-TOU-8 example, per-mile math with real models.
- **visual_gap:** Minor — comparison tables are strong; would benefit from a charging-curve/TOU-window chart.
- **action:** improve/rewrite link layer — add internal links to which-rate-plan, 08-TOU, 46-what-time, 49-demand, do-home-energy-monitors, electric-bill-breakdown.
- **onward links (observed):** none. **Reader still needs:** which-rate-plan, 46-what-time, 08-time-of-use, 49-demand, do-home-energy-monitors.

---

## PATHWAY MAP (Directed Graph of the Stressed Reader's Journey)

```text
                 +----------------------- DIAGNOSE ------------------------+
                 |                                                        |
  03-why-is-my-electric-bill-so-high <---- why-electric-bill-changes-month-to-month (alias->03)
    |  6 ilinks                                                           |
    +--> 01-how-to-read-electric-bill  OK                                |
    +--> electric-bill-breakdown  OK                                      |
    +--> do-home-energy-monitors  OK                                      |
    +--> 42-best-energy-efficient-space-heater  OK                       |
    +--> ev-charging-impact-electric-bill  ==> DEAD END (0 links) ==> X   |
    +--> how-to-lower-electric-bill-complete-guide  OK (act)             |
    |   MISSING: how-to-dispute | can-utility-shut-off | which-rate-plan  |
    |                                                                     |
    +--> why-did-my-utility-bill-go-up-this-month                        |
    |     +--> 30-sudden-spike  OK (deep diagnostic)                     |
    |     +--> hub / 23-billing-cycle / 14-estimated / 24-delivery OK     |
    |     +--> why-electric-bill-changes (alias->03) [wrong-target smell] |
    |     MISSING: how-to-dispute | which-rate-plan                       |
    |                                                                     |
    +--> 30-sudden-spike (deepest: 11 ilinks)                            |
    |     +--> 03 OK | breakdown OK | read-bill OK | estimated OK |       |
    |          demand OK | fuel OK | TOU-time OK | smart-plugs OK |        |
    |          aux-heat OK                                                |
    |     +--> how-to-dispute OK  ==> (act starts here)                 |
    |     +--> how-to-lower-complete OK                                  |
    |     MISSING: 04-hidden-fees | shutoff                               |
    |                                                                     |
    +--> electric-bill-breakdown (hub: 18 ilinks)                         |
    |     +--> dispute OK (good act edge) | hidden-fees OK | demand OK |  |
    |          rate-plan OK | fee deep dives OK                          |
    |     MISSING: complete-guide-understanding-utility-bill              |
    |                                                                     |
    +--> complete-guide-understanding-utility-bill (apex: 28 ilinks)     |
    |     +--> every line-item explainer OK                               |
    |     +--> average-utility-bills OK | sewer OK | gas OK              |
    |     +--> escalation section talks "billing-review process"         |
    |          NO LINK to dispute | shutoff | assistance <-- TOP MISSING  |
    |                                                                     |
    +--> how-utility-rates-fees-usage (model: 1 md link + 8 hrefs)       |
          +--> complete-guide OK | net-metering X -> DEAD END            |
          +--> tiered | TOU | water | taxes | why-did OK                 |
          MISSING: which-rate-plan decision page                         |

+---------------------------- ACT --------------------------------------+
 how-to-dispute-utility-bill (deep diagnosis hosted)
    +--> 14-estimated OK | 21-past-due OK | 26-deposit OK | complete-guide OK
    +--> can-utility-shutoff OK  ==> (good adjacent act)
    +--> LIHEAP text external only -- MISSING internal utility-assistance

 can-utility-shutoff OK (best act page)
    +--> 14-estimated OK | 28-reconnection OK | 26-deposit OK | dispute OK
    +--> utility-assistance-programs-LIHEAP OK

 utility-assistance-programs-LIHEAP
    +--> 01-read OK | complete-guide OK | 05-lower OK | 16-budget-billing OK |
    |    21-past-due OK | how-to-budget OK | rates-fees OK
    +--> Emergency section does NOT link can-utility-shutoff <-- gap

+---------------------------- PLAN -------------------------------------+
 how-to-budget (first-apartment)
    +--> average-water OK | 26-deposit OK | moving OK | why-did OK |
    |    47-leaks OK | 09-apart OK
    +--> MISSING: which-rate-plan | utility-assistance

 moving-checklist OK (good)
    +--> 26-deposit OK | 27-connection OK | 20-proration OK | shutoff OK |
         budget OK | 3 meter-read OK

+---------------------------- FORWARD ----------------------------------+
 which-rate-plan (decision: 17 ilinks)
    +--> 10-fixed-variable OK | 08-TOU OK | 46-time OK | 49-demand OK |
    |    net-metering OK | 24-delivery OK | 11-kWh OK | 05-lower OK
    +--> MISSING: ev-charging-impact (Decision List #1 mentions EV overnight)

 net-metering-explained (receives from which-rate-plan + rates-fees)
    +--> ZERO outbound -- ABSOLUTE DEAD END  X X

 ev-charging-impact-electric-bill (receives from 03)
    +--> ZERO outbound -- ABSOLUTE DEAD END  X X
```

(ASCII diagram intentionally simplified; see the canonical edge list below for every observed +/- missing edge.)

### Canonical edge list (observed, verified by rg)
| Source | Target | Kind |
|---|---|---|
| 03-high | 01-read | edge OK |
| 03-high | electric-bill-breakdown | edge OK |
| 03-high | do-home-energy-monitors | edge OK |
| 03-high | 42-space-heater | edge OK |
| 03-high | ev-charging | edge OK -> dead end |
| 03-high | how-to-lower-complete | edge OK |
| why-did | 30-sudden-spike | edge OK |
| why-did | tiered-water | edge OK |
| why-did | hub/23/14/24/rates-fees | edges OK (href) |
| 30-spike | 18-fuel / 03 / aux / breakdown / 01 / 46 / 49 / 14 / 50 | edges OK |
| 30-spike | how-to-dispute | edge OK |
| 30-spike | how-to-lower-complete | edge OK |
| breakdown | 03 / 01 / 23 / 17 / 24 / 49 / 18 / 19 / 04 / which-plan / dispute | edges OK |
| complete-guide | 20 line explainers incl average-utility | edges OK |
| complete-guide | how-to-dispute | **MISSING** |
| rates-fees | complete-guide (md) + 8 hrefs | edge OK |
| rates-fees | which-rate-plan | **MISSING** |
| which-plan | 10 / 08 / 46 / 49 / net-metering / 24 / 11 / 05 | edges OK |
| which-plan | ev-charging | **MISSING** |
| dispute | 14 / 21 / 26 / complete / shutoff | edges OK |
| dispute | utility-assistance-LIHEAP | **MISSING** (external liheap.org only) |
| shutoff | 14 / 28 / 26 / dispute / LIHEAP | edges OK |
| LIHEAP | 01 / 05 / 16 / 21 / complete / budget / rates-fees | edges OK |
| LIHEAP | can-utility-shutoff | **MISSING** |
| budget | 09 / 26 / 47 / average-water / moving / why-did | edges OK |
| budget | which-plan / LIHEAP | **MISSING** |
| moving | 20 / 26 / 27 / shutoff / budget / 3-meter | edges OK |
| net-metering | (none) | **DEAD END** |
| ev-charging | (none) | **DEAD END** |

### Dead ends (0 useful onward links)
1. **net-metering-explained** — 0 internal links, confirmed by rg.
2. **ev-charging-impact-electric-bill** — 0 internal links, confirmed by rg.

### Missing edges that should exist (endpoint -> endpoint + reader need)
1. **complete-guide-understanding-utility-bill -> how-to-dispute-utility-bill** — reader at the pillar hub concludes the bill is wrong; the escalation section says "review process" without a site link.
2. **03-why-is-my-electric-bill-so-high -> how-to-dispute / can-utility-shutoff / which-rate-plan** — diagnose branch "error/rate" has no act exit; stressed reader bounces.
3. **net-metering / ev-charging -> which-rate-plan, 08-TOU, 46-time, 49-demand** — two dead-end pages with rich TOU content and zero onward paths.
4. **which-rate-plan -> ev-charging** — Decision List #1 explicitly mentions EV charging overnight; no link to the EV cost page.
5. **dispute -> utility-assistance** — dispute's payment-assistance section says LIHEAP but links only external site; internal page exists.
6. **LIHEAP -> can-utility-shutoff** — emergency section (Day 1) missing the protections page.
7. **complete-guide -> can-utility-shutoff / utility-assistance** — pillar hub missing the crisis layer.

---

## Where the Journey Breaks (top 3 breakpoints)

1. **Two forward pages are absolute dead ends** — net-metering-explained and ev-charging each carry zero internal links. Any reader routed there from which-rate-plan or 03 exits the site (or bounces).
2. **The apex hub never hands off to act/plan** — complete-guide-understanding-utility-bill's escalation section references billing review without linking the dispute/protection pages, so the highest-authority page funnels no readers into the actionable layer.
3. **The diagnose cluster splits without an act exit** — 03 (and why-did) tell the reader "contact the utility / dispute," but do not link dispute, shutoff, assistance, or rate-plan pages; the stressed reader's "I want to fix this now" path stalls on a diagnosis page.

## Pages rated below 6/10
- **how-utility-rates-fees-usage-work-together** — Quality 5/10 (structural HTML/markdown mismatch, thin), SEO 5/10 (1 markdown ilink).

## 3 Highest-impact actions
1. **Link net-metering and ev-charging into the cluster** (which-plan, 08-TOU, 46-time, 49-demand, breakdown) — turns two content-rich dead ends into journey continuations and passes link equity.
2. **Add act-cluster edges from complete-guide and 03** (dispute, shutoff, assistance, rate-plan) — the single graph change that wires the diagnose->act->plan path the stressed reader needs.
3. **Add one missing edge pair at the action layer** — dispute->internal LIHEAP and LIHEAP->shutoff — closing the crisis loop that keeps distressed readers on-site.
