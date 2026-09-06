# Affiliate Monetization & Organic Content Strategy — utilityexplained.com

**Date:** 2026-09-06 · **Prepared for:** Utility Explained (US / Amazon.com, Associates tag `utexplained-20`)

**Inputs:** full site inventory (96 articles, 6 hubs, 36 affiliate articles, 68 product boxes, Sept-4 Rybbit snapshot), official Amazon Associates US rate table + program policies (fetched 2026-09-06), SERP landscape checks (2026-09-06), existing internal dossiers (AMAZON-PRODUCT-DOSSIER-2026-08-30, AFFILIATE-PLACEMENTS-2026-08-28, ENGAGEMENT-ROOT-CAUSE-2026-08-31).

**Stated assumptions (placeholders not filled in brief — resolved from repo):**
- Target country/program: United States / Amazon.com (hugo.toml `languageCode en-us`, `.com` links).
- Publisher's real experience: research-based editorial process, **no hands-on product testing claimed anywhere on site**; honest "unavailable" notes; methodology page exists. Strategy below preserves that honest posture — no invented testing.
- No price-range preference given; unit economics below use market price bands (never on-page prices).

---

## 1. Executive Summary

**The niche opportunity.** Utility Explained owns a genuinely differentiated position — "the bill translator" — in a niche where the monetizable moment is precisely the site's core traffic event: **bill shock**. The top pages (`why is my electric bill so high`, `water bill too high`, `sudden spike`, `how to lower your electric bill`) attract exactly the reader who buys measurement and mitigation products. The affiliate flywheel (crisis diagnostic → measure it → fix it) is already wired into 36 articles.

**The strongest monetization direction.** Not new "best X" head-term articles — the site's leverage is **diagnostic-to-product ladders inside existing traffic**, plus a once-in-a-cycle freshness event: **Sense exited consumer hardware on Dec 31, 2025**, and most competing "best home energy monitor" lists are stale. The site's `emporia-vue-3-vs-sense-comparison` article is sitting on a vacated SERP.

**Top 3 product categories to prioritize** (of 18 scored, §3):
1. **Energy-measurement devices** — plug-in watt meters (Kill A Watt P4460/P4456) + energy-monitoring smart plugs (Kasa KP125M / Tapo P110M / Shelly Plug US). Low price but perfect intent match, basket-building, and the natural first rung of every ladder. Requires immediate remediation: the most-placed ASIN (P4400, 7 files) was flagged unavailable Aug 31.
2. **Whole-home energy monitoring (post-Sense)** — Emporia Vue 3 (~$169–180) as the anchor; "Sense discontinued / alternatives" content; ~$5 commission per unit at 3%.
3. **Water-leak detection & smart water monitoring ladder** — Govee 5-pack (~$60) → Flume 2 (~$199–269) → Moen Flo (~$550–676). The water cluster is the site's strongest engagement cluster, the Flume-vs-Flo-vs-Phyn SERP is owned by small sites (winnable), and the top rung carries the highest commission per order on the site (~$16–20).

**Biggest risks and constraints** (see §9, §10):
- **Measurement gap:** zero `affiliate_click` events recorded; the affiliate program is currently unmeasurable. Tracking fix is prerequisite #1.
- **Google dependency not yet earned:** ~90%+ of traffic is Bing/DDG ecosystem; Google is ~6% because **no GSC sitemap has ever been submitted**. Mechanical fix, high urgency.
- **Commission ceiling:** nearly every product here sits in Home Improvement/Home/Tools at **3%**. Unit economics work only with volume or high-AOV rungs (Flo, Vue 3, dehumidifiers) — do not chase sub-$15 items as standalone targets.
- **Trust liabilities:** the flagship page carries a refuted "$200–450/mo stacked savings" claim (audit C4), and fictional AI-drafted author personas are an E-E-A-T exposure that must not be expanded.
- **P4400 availability decay** demonstrates single-ASIN fragility; every category needs a 2-deep product bench.

---

## 2. Niche and Audience Analysis

### Audience segments (from existing content + analytics)

| Segment | Need | Budget signal | Products they rationally buy | Fit |
|---|---|---|---|---|
| **Bill-shock diagnosticians** (largest, top pages) | "Why did my bill spike?" — attribution | $20–70 impulse-curable | Watt meter, smart plug w/ monitoring, leak sensors | ★★★★★ — already the site's reader |
| **First apartment / first-home budgeters** | Predict and cap utilities | $15–50 | Smart plugs, draft stoppers, window kits, hygrometer | ★★★★ |
| **Anxious water-bill owners** | Leak attribution + prevention | $60–600 (ladder) | Govee 5-pack → Flume 2 → Moen Flo | ★★★★★ — highest engagement cluster |
| **Rate-plan optimizers (TOU/solar/EV)** | Shift usage to cheap hours | $100–300 | Vue 3, smart plugs, smart thermostat, L2 charger | ★★★★ — growing, high AOV |
| **Comfort/cost balancers** | Humidity, drafts, HVAC efficiency | $15–250 | Dehumidifier, filters, weatherization, thermal curtains | ★★★★ — seasonal (fall/winter spike is imminent) |

### Buyer needs → content alignment
The buying trigger is almost always a bill event, not product curiosity. That means informational pages (already ranking) are the storefront; standalone product pages need the diagnostic frame ("what a watt meter can and can't tell you") rather than listicle framing.

### Competitive landscape (SERP checks, 2026-09-06)
- **Winnable by this site:** `Emporia Vue vs Sense` (Reddit/forums rank — and now stale), `how many watts does a refrigerator use` (already published; niche blogs rank, no majors), `Flume vs Moen Flo vs Phyn` (plumbers and small blogs rank), `EV charging at home cost` (utilities and calculators — a bill-math site wins on framing), dehumidifier **cost-to-run** angles (RTINGS/HouseFresh test humidity, none own the kWh-cost angle), Kill A Watt **alternatives/how-to-use** (brand pages own the product name itself).
- **Hard head terms (attack via modifiers only):** `best water leak detector` (Wirecutter/PCMag/CNET/CR), `best smart thermostat` (same + ENERGY STAR), `best smart plug` broadly.
- **Walled gardens — do not enter:** whole-house water filters (SpringWell/Aquasana DTC affiliate ecosystems pay 10%+ and own the SERP).

### Positioning opportunity
Differentiators nobody else combines: (1) bill-literacy first — every product framed as "what it does to your bill, mechanically, with math"; (2) honest sourcing labels (researched vs tested); (3) renters-as-first-class (competitors assume ownership); (4) freshness on the post-Sense landscape. The E-E-A-T weakness (no hands-on testing, fictional personas) is best countered by **transparent methodology and math**, not by faked experience.

---

## 3. Product-Category Opportunity Scorecard

Commission column = official standard rate for the likely category (official table, affiliate-program.amazon.com, fetched 2026-09-06). **Per-ASIN category assignment requires verification** in Earnings Reports — several are flagged.

| # | Category | Likely rate | Traffic pot. | Buyer intent | Monetization suit. | Competition realism | Content depth | Trust/experience fit | **Overall** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Plug-in watt meters (Kill A Watt P4460/P4456) | 3% (Home Improv.) | 6 | 8 | 6 | 8 | 7 | 9 | **8.0** |
| 2 | Energy-monitoring smart plugs (Kasa/Tapo/Shelly/Eve/Emporia) | 3% | 7 | 8 | 7 | 6 | 8 | 9 | **7.8** |
| 3 | Whole-home energy monitors (Vue 3; Sense exited) | 3% | 6 | 9 | 8 | 8* | 8 | 8 | **7.8** |
| 6 | Point water-leak sensors (Govee, YoLink) | 3% | 6 | 8 | 7 | 7 | 7 | 9 | **7.4** |
| 7 | Smart water monitors/shutoffs (Flume 2, Moen Flo, Phyn) | 3% (verify) | 5 | 9 | 8 | 8 | 7 | 7 | **7.3** |
| 8 | Dehumidifiers (basement) | 3% | 7 | 9 | 7 | 5 | 8 | 6 | **7.0** |
| 5 | Smart thermostats (Nest 4th gen, ecobee, Honeywell) | 3% | 8 | 9 | 7 | 4 | 7 | 7 | **6.7** |
| 11 | HVAC filters (FilterBuy/Filtrete) | 3% (some Kitchen 4.5% — verify) | 6 | 8 | 6 | 6 | 6 | 8 | **6.5** |
| 10 | Air-sealing/weatherization consumables (draft stoppers, 3M kits) | 3% | 5 | 7 | 6 | 8 | 6 | 9 | **6.5** |
| 4 | Smart power strips w/ per-outlet metering (Kasa HS300) | 3% | 4 | 7 | 6 | 6 | 5 | 8 | **6.0** |
| 13 | Level 2 EV chargers (Emporia, ChargePoint) | 3–4.5% **verify** | 5 | 9 | 7 | 6 | 6 | 6 | **6.0** |
| 9 | Hygrometers/indoor climate sensors (Govee) | 3–4% **verify** | 5 | 6 | 5 | 7 | 5 | 9 | **5.8** |
| 12 | Thermal cameras/leak detectors (FLIR ONE Pro) | 4% "All Other" **verify** | 4 | 8 | 6 | 8 | 6 | 7 | **5.8** |
| 18 | Thermal curtains/window treatments | 3% | 4 | 6 | 5 | 7 | 5 | 7 | **5.2** |
| 16 | Smart irrigation (Rachio, B-hyve) | 3% | 4 | 7 | 6 | 6 | 6 | 6 | **5.0** |
| 17 | CO/gas safety alarms | 3% | 4 | 7 | 4 | 6 | 4 | 5 | **4.2** |
| 14 | Portable power stations (EcoFlow/Anker) | 4% **verify** | 6 | 8 | 7 | 3 | 5 | 4 | **4.0** |
| 15 | Whole-house/under-sink water filters | 3% | 7 | 8 | 7 | 2 | 6 | 5 | **3.0** |

\* Post-Sense vacuum temporarily lowers effective competition — a freshness window, not a permanent moat.

**Realistic unit economics at current rates** (commission ≈ band × rate; illustrative only):

| Product | Band | Est. commission | Note |
|---|---|---|---|
| Moen Flo | $550–676 | ~$16.50–20 | Highest per-order on site; pro-install caveat |
| Vue 3 | $169–180 | ~$5.10–5.40 | Anchor product (9 files already) |
| Midea Cube dehumidifier | ~$210–250 | ~$6.30–7.50 | Cost-to-run angle unique |
| Flume 2 | $199–269 | ~$6.00–8.00 | Watch new $49.99/yr subscription tier in content |
| Emporia L2 charger | ~$300–400 | ~$9–18 (3–4.5%, verify) | EV cluster growing |
| Govee leak 5-pack | ~$60 | ~$1.80 | Volume + ladder entry |
| Kasa KP125M 2-pack | ~$40 | ~$1.20 | Basket-builder |
| Kill A Watt P4460 | ~$25–35 | ~$0.75–1.05 | Ladder entry only |

**Conclusion:** sub-$40 items are ladder rungs, never targets. Money is made on Vue 3 / dehumidifiers / Flume / Flo / chargers, with 24-hour-cookie cross-cart basket-building from the cheap rungs.

---

## 4. Top Recommended Product Opportunities

All angles assume **researched buying guides with clearly labeled sourcing** — no invented hands-on testing. "Testing" column states the honest posture required.

| Product (ASIN) | Category / rate | Target buyer | Band | Why buyers consider it | Safest content angle | Testing posture | Key verification |
|---|---|---|---|---|---|---|---|
| **Emporia Vue 3** (B0C7B1LKDW on site; B0C79PNK84 listed) | Home Improv. / 3% | Bill-shock diagnoser, TOU/solar household | $169–180 | Only mainstream whole-home monitor left post-Sense; 16 circuits + solar | Comparison pillar + "is it worth it" math (break-even vs bill savings) | Not feasible to test — manufacturer specs + aggregated owner reports, labeled | CTs not cross-gen compatible (Vue 2 owners pain point = article); flexible-CT version $279.99 |
| **Sense (any model)** | — | **Content target, not a sales target** — discontinued Dec 31, 2025 | n/a | Owners need migration advice; buyers need warning | "Sense discontinued: what owners should do + 2026 alternatives" | n/a | Support/app status per sense.com help notice; never present as buyable |
| **P3 Kill A Watt P4460 EZ 3-pack** (B07HM9S6ZR) + **P4456 Flex** (B0C4G7QVZT) | Home Improv. / 3% | First-time diagnoser | $25–60 | The canonical entry device; P4456 is P3's pushed upgrade (memory, CO2, cost calc) | "How to use a Kill A Watt to find what's costing you" + alternatives page | Optional genuine purchase later (~$30) — the only realistic hands-on lane | **P4400 (B00009MDBU) flagged unavailable 2026-08-31 — re-check or swap all 7 files** |
| **Kasa KP125M 2-pack** (B0BYGRLRS1) | Home / 3% | TOU optimizer, renter | ~$40 | Matter + energy monitoring + routines/schedules | Head-to-head accuracy/feature comparison vs Tapo/Shelly | Optional purchase + simple accuracy test vs P4460 (labeled, reproducible method) | TP-Link shifting launches to Tapo; Kasa/Tapo app consolidation |
| **Tapo P110M 2-pack** (B0DKGBP38V) | Home / 3% | Same | ~$40 | TP-Link's current-gen energy plug | Same comparison | Same | |
| **Shelly Plug US Gen3/Gen4** | Home/All Other — **verify** | Home-Assistant-adjacent reader | ~$45 | Local control, precise metering, HA favorite | "For advanced users" section of comparison; Gen4 just launched | Research only | Gen4 availability/pricing |
| **GoveeLife leak detector 5-pack** (B0DQLFC3Q6) | Home Improv. / 3% | Anxious water-bill owner | ~$60 | Cheapest credible prevention; loud alarm + low-battery alert | **Placement guide** (water heater, sump, AC pan, washer, toilet) — long-tail winnable | Optional purchase; placement advice is safety-relevant, keep conservative | Triple-verified per dossier; confirm still in stock at publish |
| **Flume 2** (B08DX6MP8X) | Home Improv. / 3% (verify) | Metered homeowner w/o shutoff need | $199–269 | Strap-on install, no plumber | "Flume vs Flo vs Phyn" pillar + rebate round-up (e.g., LADWP $24) | Research only; install complexity from owner reports, labeled | New $149 + $49.99/yr subscription tier — must be covered honestly |
| **Moen Flo** (B00C03D01Q) | Plumbing / 3% (verify) | High-stakes homeowner, insurance-discount seeker | $550–676 | Automatic shutoff; insurance premium discounts | Comparison pillar + "do you need auto-shutoff?" decision tree | Research only; **pro install required — never imply DIY** | Street price varies; insurance discount availability by carrier |
| **Phyn Plus 2nd gen** | Plumbing / 3% (verify) | Same, plumber-quote comparison shopper | $490–580 | Same class as Flo, different diagnostics | Comparison table row | Research only | |
| **Midea Cube dehumidifier** | Home/Kitchen — **verify 3 vs 4.5%** | Basement owner, musty + AC-load | ~$210–250 | Wirecutter-cited category leader; drain-hose + pump options | **Cost-to-run per kWh** angle (unique vs RTINGS) in existing dehumidifier article | Research only; running-cost math is the differentiator | Confirm current model + pump variant ASIN before placing |
| **Frigidaire FHDD5034W1** | Home / 3% | Same, brand-loyal | ~$200–280 | Retail availability, Wi-Fi model | Alternative row | Research only | FFAD5033W1 discontinued — don't cite old model |
| **Emporia L2 EV charger** (B09ZNN3JB7) | **Auto 4.5%? verify** | New EV owner on TOU | ~$300–400 | Energy-dashboard integration with Vue | EV-charging-cost page upgrade + charger payback math | Research only | Category/rate verification; Energy Star list |
| **Nest Learning 4th gen** (B0D5BBYRJM) / **ecobee Premium** (B09XXS48P8) | Home Improv. / 3% | Heat-pump/TOU household | $249–279 | Bill automation on rate plans | **Modifier long-tail only:** "ecobee vs Nest on a heat pump," "smart thermostats + TOU rates" | Research only; savings claims must be mechanism-framed, no % promises | Head term is Wirecutter/CR-owned — do not fight it |
| **FLIR ONE Pro** (B072J49BX7) | All Other / 4% (verify) | DIY energy auditor | ~$400–550 | See heat leaks visually | Support content inside existing DIY-audit article (already placed) | Research only | Phone-compatibility table accuracy |
| **FilterBuy MERV 8 / Filtrete MERV 13** (B00CK025GK / B00TUDHCEA) | Home Improv. 3% (verify) | HVAC owner, recurring buy | $40–80/yr | Subscription-like repeat purchases | Already placed in MERV guide; add "how often + size-finding" support | Research only | MERV health-claim boundary — comfort/equipment framing only |

**Products deliberately NOT recommended for placement:** whole-house water filters (walled SERP), portable power stations (trend + 4% can't offset competition), space heaters beyond the existing single mention (fire-safety claims + model churn), gas detectors as a push category (safety claims risk), Rachio/B-hyve for now (audience mismatch — revisit if water hub grows a summer lawn cluster).

---

## 5. Organic Keyword and Search-Intent Map

*Demand/difficulty are qualitative estimates from SERP composition (2026-09-06) — no keyword-tool data exists in the repo; volumes "require verification." Existing pages listed have implied intent alignment from analytics, not rank tracking (GSC not yet set up).* **Cluster A — Measure Your Usage (priority 1):**

| Keyword/topic | Intent | Funnel | Demand | Difficulty | Page | Action |
|---|---|---|---|---|---|---|
| kill a watt alternatives / electricity usage meter options | Commercial | Mid | Med | Low-Med | — | **New** |
| best smart plug with energy monitoring | Commercial | Mid | High | Med | `smart-plug-energy-monitoring-which-measures-usage` | Upgrade → head-to-head |
| kasa vs tapo / shelly plug energy monitoring accuracy | Commercial | Low-funnel | Low-Med | Low | same | New section |
| how to use a kill a watt meter | Informational | Mid | Med | Low | — | New (support) |
| electricity usage monitor for appliance | Commercial | Mid | Med | Med | covered inline | Consolidate via internal links |
| best home energy monitor 2026 | Commercial | Mid | Med | **Med (post-Sense vacuum)** | — | **New pillar** |
| sense energy monitor discontinued / sense alternatives | Commercial/Info | Mid | Med (rising) | **Low** | `emporia-vue-3-vs-sense-comparison` | **Update + new article** |
| emporia vue vs sense | Commercial | Low-funnel | Low | **Low (Reddit ranks)** | same | Refresh, add shutdown |
| emporia vue 3 review / is it worth it | Commercial | Low-funnel | Med | Med | — | New (research-based, labeled) |
| home energy monitor for time-of-use / solar | Commercial | Mid | Low | Low | `do-home-energy-monitors-save-money` | Extend section |

**Cluster B — Water Leak & Monitoring (priority 3):**

| Keyword/topic | Intent | Funnel | Demand | Difficulty | Page | Action |
|---|---|---|---|---|---|---|
| flume vs moen flo vs phyn | Commercial | Low-funnel | Low-Med | **Low (small sites rank)** | `point-sensor-vs-whole-home…` | **New pillar** |
| flume 2 review / worth it / subscription | Commercial | Low | Low-Med | Low | — | New |
| water leak detector placement / where to place | Informational | Mid | Low-Med | Low | — | New (Govee) |
| govee water leak detector (5-pack) | Transactional-adj. | Low | Med | Low | existing boxes | Placement guide feeds it |
| smart water shutoff do I need one | Informational | Mid | Low-Med | Low | — | New decision-tree |
| best water leak detector for water heater / sump pump / washing machine | Commercial | Mid | Low | Low-Med | — | New (modifier pages) |
| water monitor insurance discount | Informational | Mid | Low | Low | — | Section inside pillar |
| ~~best water leak detector~~ (head) | — | — | High | **High (majors)** | — | **Do not target head-on** |

**Cluster C — Bill Diagnostics → Fix (existing traffic, monetization upgrades):**

| Keyword/topic | Intent | Funnel | Demand | Difficulty | Page | Action |
|---|---|---|---|---|---|---|
| why is my electric bill so high | Informational | Top | High | Med | `03-…` (30 sess/7d) | Already AFF; add ladder CTA |
| how to lower your electric bill | Info→Commercial | Mid | High | Med | flagship (134 sess/7d) | **Fix C4 math, unfreeze boxes** |
| how many watts does a refrigerator use | Informational | Top | High | **Low-Med (no majors)** | published | Refresh seasonally |
| dehumidifier cost to run / electricity use | Informational | Mid | Med | Low | `do-dehumidifiers-help-cooling-costs` | **Add products + cost math** |
| ev charging cost per month / by state | Info→Commercial | Mid | Med | **Med (fragmented)** | `ev-charging-impact-electric-bill` | Upgrade w/ tables + charger |
| smart thermostat time-of-use savings | Commercial | Mid | Low | Low | `do-programmable-thermostats…` | New angle section |
| ecobee vs nest for heat pumps | Commercial | Low | Low-Med | Low-Med | — | New |
| moving utilities checklist | Informational | Top | Med | Low | 12 sess, 105s dwell | Email capture + light links |
| electric bill breakdown / charges explained | Informational | Top | Med | Med | 30 sess, weak dwell | Engagement fix first (per root-cause doc) |

**Seasonal (Sep–Feb peak — starts now):** draft-proofing, window insulation kits, thermal curtains, space-heater costs, "why is my heating bill so high." Existing articles cover most; priority is winter refresh + internal-link passes, not new builds.

---

## 6. Content Cluster Blueprint

### Cluster 1 — "Know What's Using Power" (electricity measurement) — hub: electricity-explained → lower-your-bills

```
PILLAR: Best Home Energy Monitor 2026 (Post-Sense) [NEW]
  ├─ Emporia Vue 3 vs Sense [EXISTING — refresh + shutdown banner]
  ├─ Sense Discontinued: Owner Guide + Alternatives [NEW]
  ├─ Emporia Vue 3: Is It Worth It? (bill-math review, researched) [NEW]
  ├─ Best Smart Plug With Energy Monitoring: Kasa vs Tapo vs Shelly [UPGRADE existing]
  ├─ How to Use a Kill A Watt (find your power hogs) [NEW — support]
  ├─ Kill A Watt Alternatives in 2026 [NEW — replaces dead P4400 landing]
  └─ Existing diagnostic spokes (03, 30-spike, 11-kWh, phantom-power, fridge-watts) link INTO pillar
```
Internal links: every "measure it" mention across ~15 existing articles links to the pillar; pillar links down to comparisons; spoke→hub links added (85–88% currently missing).

### Cluster 2 — "Water: Detect, Attribute, Prevent" — hub: water-explained

```
PILLAR: Flume vs Moen Flo vs Phyn (+ Govee) — Smart Water Monitoring [NEW]
  ├─ Point Sensor vs Whole-Home Monitor [EXISTING — link up]
  ├─ Where to Place Water Leak Sensors (Govee 5-pack placement) [NEW]
  ├─ Do You Need an Auto-Shutoff? (decision tree + insurance discounts) [NEW]
  └─ Diagnostic spokes (06-water-high, water-meter-running, leak-indicator, toilet-leak) link IN
```
This cluster converts the site's best engagement (water pages: 78–80% bounce, 100s+ dwell — best on site).

### Cluster 3 — "Winter Bill Control" (seasonal refresh of existing, Sep–Feb)

```
FLAGSHIP: How to Lower Your Electric Bill [FIX + unfreeze]
  ├─ Drafts/sealing (how-to-find-seal-drafts, Holikme) — refresh
  ├─ Window kits / thermal curtains — refresh, re-verify ASINs
  ├─ Dehumidifier costs + products [UPGRADE]
  ├─ Space heater TCO — refresh (existing, careful claims)
  └─ Thermostats: TOU/heat-pump modifier article [NEW]
```

### Cluster 4 — "EV & Time-of-Use" (growth bet) — hub: electricity-explained

```
PILLAR: What EV Charging Really Costs (state table + TOU math) [UPGRADE existing]
  ├─ L2 charger payback (Emporia charger) [section]
  └─ TOU plan chooser [EXISTING 08] — link both ways
```

**Article template standard (all new content):** Quick-answer box → mechanism/math (site's differentiator) → honest "what we did not test" note → products as *options in a decision frame*, never a ranked "best" without criteria → disclosure shortcode → sources footer. CTA placement: one box mid-article + one end-of-article; never in the quick answer.

---

## 7. 90-Day Roadmap

| Days | Priority actions | Owner* | Effort | Impact | Success metric |
|---|---|---|---|---|---|
| **1–7** | Submit sitemap in GSC (never done; Google = 6% of traffic) | Owner | L | **H** | GSC "Pages indexed" > 100; impressions baseline |
| 1–7 | Wire `affiliate_click` as GA4 key event; verify Rybbit event firing (0 events recorded to date) | Owner | L | **H** | Events visible; weekly click count exists |
| 1–7 | Fix flagship C3/C4 (savings arithmetic, frontmatter); unfreeze 4-box placement | Editor | M | H | Flagship publish; bounce ≤ GA4 ~29% held |
| 1–7 | ASIN re-verification sweep: P4400 (7 files!), Vue 3, Govee, dehumidifier candidates | Editor | M | H | No dead-ASIN boxes live |
| 1–7 | Add missing in-article disclosures (2 files: `11`, `46`) | Editor | L | M | 36/36 articles disclosure-complete |
| 1–7 | Sense shutdown banner on Vue-vs-Sense + noindex check on retired URLs | Editor | L | M | Banner live |
| **8–30** | Publish: Sense Discontinued/Alternatives; Best Home Energy Monitor 2026 pillar; Kill A Watt Alternatives; Smart-plug head-to-head upgrade | Editor | H | H | 4 pieces live, interlinked |
| 8–30 | Spoke→hub link pass on top-15 traffic pages; wire `lower-your-bills` hub (only 3 inbound) | Editor | M | M | Hub clicks in nav analytics |
| 8–30 | Dehumidifier product integration (Midea Cube / FHDD5034W1) with cost-to-run math | Editor | M | H | First boxes on that page |
| 8–30 | GSC weekly review: impressions by page → double down list | Owner | L | H | First Google-impression data |
| **31–60** | Flume vs Flo vs Phyn pillar; Govee placement guide; auto-shutoff decision tree | Editor | H | H | Water cluster complete |
| 31–60 | EV cost upgrade (state table, charger payback); TOU-thermostat angle article | Editor | M | M | Cluster 4 live |
| 31–60 | Winter refresh pass (drafts, window kits, curtains, gas-high) + seasonal internal links | Editor | M | M | Refresh dates updated pre-Nov |
| 31–60 | E-E-A-T decision: consolidate or clearly re-label fictional personas (C9); author pages get honest "research-based, AI-assisted, human-edited" treatment | Owner | M | M | Personas no longer overclaim |
| **61–90** | Expand by GSC data: impressions>position 8–20 pages get upgrades; new modifier pages (leak-detector-for-X series) | Editor | M | H | 3+ pages moved into top 10 |
| 61–90 | First outbound-click cohort analysis: which boxes/placements earn clicks → prune/expand | Owner | L | **H** | CTR per placement known |
| 61–90 | Optional: buy KP125M 2-pack + P4460 (~$70 total) for a labeled mini accuracy test | Owner | L | M | One honestly-tested comparison |
| 61–90 | AdSense: re-review status → re-add manual slots if approved (display complements 3% affiliate) | Owner | L | M | AdSense live or formally deprioritized |

\* Owner = requires AWS/Amazon Associates console, GSC, GA4, or purchase authority. Editor = content work executable in-repo.

**Standing weekly cadence:** GSC + Rybbit snapshot → top movers, affiliate clicks, dead-ASIN check (15 min). Every publish day: re-verify ASINs (dossier guardrail).

---

## 8. First 10 Articles / Page Updates (exact priority order)

| # | Action | Title | Primary keyword | Intent | Outline (H2s) | Monetization relevance |
|---|---|---|---|---|---|---|
| 1 | **UPDATE** | How to Lower Your Electric Bill (flagship) | how to lower your electric bill | Info→Comm | Fix $ math (C4) · keep ladder structure · unfreeze 4 boxes (Vue 3, P4460, KP125M, Nest) | Highest-traffic page (134 sess/7d); trust repair first |
| 2 | **NEW** | Sense Is Discontinued — What Owners and Buyers Should Do | sense energy monitor discontinued | Commercial/Info | What happened · app/firmware status · owner migration paths · 2026 alternatives (Vue 3, plugs, utility data) | Vacated SERP, low competition; feeds Vue 3 boxes |
| 3 | **UPDATE** | Emporia Vue 3 vs Sense | emporia vue vs sense | Commercial | Add shutdown verdict · "if you already own Sense" · Vue 3 as default · CT-compat warning | Existing page + rising query |
| 4 | **REMEDIATE** | Kill A Watt swap across 7 files + **NEW** "Kill A Watt Alternatives 2026" | kill a watt alternatives | Commercial | What P4400 was · P4460 vs P4456 Flex · smart-plug route · whole-home route | Fixes dead-ASIN exposure; ladder entry |
| 5 | **UPDATE** | Do Dehumidifiers Help Cooling Costs → add products + cost-to-run | dehumidifier electricity cost | Info→Comm | Keep mechanism · add running-cost tables (per kWh) · Midea Cube / Frigidaire / hOmeLabs as options · basement sizing | Open monetization slot; unique angle vs RTINGS |
| 6 | **NEW** | Best Home Energy Monitor 2026 (Post-Sense) | best home energy monitor | Commercial | Landscape post-Sense · Vue 3 deep section · utility-data route (free) · plug-level route · who needs what | Cluster-1 pillar; $5+ per conversion |
| 7 | **NEW** | Flume vs Moen Flo vs Phyn (+ when a $60 Govee 5-pack is enough) | flume vs moen flo | Commercial | Ladder framing · install requirements (Flo/Phyn pro) · subscriptions (Flume $49.99/yr) · insurance discounts · decision tree | Highest EPC band on site |
| 8 | **UPDATE** | Smart Plug Energy Monitoring article → Kasa vs Tapo vs Shelly head-to-head | best smart plug for energy monitoring | Commercial | Methodology (research-based, labeled) · accuracy expectations · Matter/HA ecosystems · per-use-case pick | Existing 3-box page upgraded to head-term competitor |
| 9 | **NEW** | Where to Place Water Leak Sensors (5-pack placement map) | water leak detector placement | Informational | Why placement > brand · 6 locations (WH, sump, AC pan, washer, fridge line, toilet) · Govee example · maintenance | Feeds 6 existing Govee placements; long-tail winnable |
| 10 | **UPDATE** | EV Charging Impact on Your Bill → state cost table + charger payback | ev charging cost | Info→Comm | State $/kWh table · TOU charging math · L2 charger payback (Emporia) · metering your charger (Vue 3/plug) | Growing cluster; possible 4.5% rate (verify) |

---

## 9. Compliance and Credibility Checklist

**Already in place (verified in repo — keep and protect):**
- ✅ Direct `amazon.com/dp/?tag=utexplained-20` links, `rel="sponsored nofollow noopener"` — no cloaking, no redirects (satisfies redirect/cloak policy).
- ✅ No prices, availability, star ratings, review counts, or review text on page; boxes say "Price & availability shown on Amazon.com." (satisfies Product Information/PA-API display rules without needing PA-API).
- ✅ Local illustrative images only — zero Amazon imagery.
- ✅ 4-layer disclosure: dedicated page + footer + in-article shortcode (50 files) + Terms.
- ✅ Price bands only in prose; no promised savings (mechanism framing per dossier guardrails).
- ✅ Deliberately unmonetized crisis pages (shutoff, past-due, deposit) — a trust asset; keep.

**Gaps / items requiring current verification ("Policy verification required"):**
- ⚠️ **Exact statement wording:** OA §5 specifies "As an Amazon Associate I earn from qualifying purchases." Site uses "…we earn from qualifying purchases." Widely accepted, but verify against the current OA text in Associates Central. 
- ⚠️ 2 affiliate articles missing the in-article disclosure (`11-understanding-kwh-usage`, `46-what-time-is-electricity-cheapest`) — fix in week 1.
- ⚠️ Per-ASIN commission categories (EV charger → Auto 4.5%? Shelly → All Other 4%? dehumidifier → Kitchen 4.5%?) — verify in Earnings Reports before relying on unit economics.
- ⚠️ April 2026 OA changes now in force: onsite "halo" earning removed, 180-day ship window, stricter original-content definition — re-read the changelog at next login.
- ⚠️ Never use "Amazon" in page titles in ways that imply endorsement; keep to descriptive use.
- ⚠️ E-E-A-T: author personas are fictional (disclosed as AI-drafted, audit C9). **Do not expand personas or add credentials.** Consolidate to a transparent editorial voice; label all content research-based/AI-assisted with human editing.
- ⚠️ Safety-adjacent products (CO alarms, leak shutoffs, gas): keep "alert, never guarantee prevention" framing; Flo/Phyn = pro install, always stated.
- ⚠️ Do not add price-tracking features, discount promises, or "deal" framing anywhere (banned + low-trust).
- ⚠️ Self-purchases/friends-and-family purchases for testing are fine to **own** but must never flow through your own affiliate links.

---

## 10. "Do Not Pursue" List

| Item | Reason |
|---|---|
| Whole-house / under-sink water filter SERPs | Owned by DTC affiliate ecosystems (SpringWell et al., 10%+ commissions); 3% can't compete; independence would be doubted |
| `best water leak detector` / `best smart thermostat` / `best smart plug` **head terms as titles** | Wirecutter/PCMag/CNET/CR-owned; win modifiers instead |
| Portable power stations as a category push | Trend + price-volatile + 4% can't offset competition; keep only as generator-article context |
| Space-heater "best of" expansion | Fire-safety claim exposure, model churn, seasonal fads |
| Gas-detector / CO-alarm push category | Safety claims risk exceeds ~$1–3 commission value; keep existing single placements only |
| Displaying prices, ratings, review counts, or Amazon images manually | Policy violation without PA-API; current clean setup is a moat — don't break it |
| Any "guaranteed X% savings" claims or urgency/deal CTAs | Refuted-savings defect (C4) shows the failure mode; FTC + trust |
| Invented hands-on testing / fabricated reviewer personas expansion | Core credibility boundary; already an E-E-A-T liability (C9) |
| Monetizing crisis pages (shutoff/past-due/deposit/assistance) | Deliberate trust calls in AFFILIATE-PLACEMENTS — reversing them breaks the site's promise |
| Amazon Onsite / Influencer program dependence | April 2026 removal of halo earning cut Onsite income ~25% community-wide; not a strategy for this site |
| Paid traffic, "deal" pop-ups, link shorteners, e-mail spam to drive affiliate clicks | Program violations + brand destruction |
| Smart irrigation, lawn care expansion (for now) | Audience mismatch with bill-diagnostics reader; revisit only if summer water cluster data supports it |

---

### Source notes
- Commission table & policies: affiliate-program.amazon.com — Standard Commission Income Rates topic; Program Policies; Operating Agreement §5; April 14, 2026 change summary (all fetched 2026-09-06). Per-ASIN categories flagged "requires verification" throughout.
- Sense exit: sense.com consumer blog + help article "Support For Sense Home Energy Monitors" (sales ended Dec 31, 2025).
- Product/pricing bands: manufacturer sites and PCMag/Wirecutter citations retrieved 2026-09-06 — bands only, verify ASINs on publish day per dossier guardrail.
- Internal: KPI_DASHBOARD.md, GROWTH_LOG.md (Entry 24), .rybbit-snapshot-2026-09-04, ENGAGEMENT-ROOT-CAUSE-2026-08-31.md, FULL-CONTENT-SEO-AUDIT-2026-08-30.md, AMAZON-PRODUCT-DOSSIER-2026-08-30.md.
- Keyword demand/difficulty: qualitative SERP-composition estimates — no volume data collected; verify with GSC (post-submission) before committing to Cluster-4 expansion.
