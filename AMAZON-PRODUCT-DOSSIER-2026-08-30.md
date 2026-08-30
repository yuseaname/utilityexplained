# AMAZON-PRODUCT-DOSSIER — utilityexplained.com — 2026-08-30

- **Prepared by:** Lieutenant (SQ-062). Research artifact for affiliate-content strategy — NOT marketing copy. Amazon availability labels are carried verbatim from wave-1 workers; UNVERIFIED = not evidenced this run, never proof of absence.
- **Ground truth:** evidence-brief sections A-F (Commander-verified 2026-08-30), carried through unchanged. Wave-1 results read in full: 02-tracer.json (45-entry HVAC/envelope) · 01-prospector-r2.json (electric) · 01-prospector.json + 02-prospector-2.json (keyword sets) · 05-executor.json (gaps + cannibalization) · 01-mason.json + brief E3 (water) · 06-scout.json + 04-twin_q.json (machinery/keyword context).
- **Reconciliation:** mason's 14-of-16 UNVERIFIED water rows are superseded for the leak-slot anchors by Commander triple-verification (brief E3); tracer/prospector UNVERIFIED labels carry verbatim even where brands are repo-wired (brief B); prospector's Amazon evidence was a geo-localized (MXN) search view — therefore price BANDS only, exact prices never printed.
- **Hard law (enforced below):** price BANDS only · ASINs only when evidence-backed (§7.4) · savings framed as mechanism, zero promised %/$ · safety devices ALERT, never prevent · every product row shows availability + install class + renter flag.
- **Site infrastructure (brief A/B):** Hugo, 85 articles; `{{< product-box asin=... name=... label=... description=... >}}` on 25 articles plus inline `{{< amazon asin=... text=... >}}`; Associates tag centralized (litwd-20), rel=sponsored nofollow, Rybbit per-ASIN click events, disclosure shortcode. Audience: homeowners AND renters — renter flags are first-class per brief F.

## 1. Executive summary

1. This dossier catalogs Amazon-available products that help U.S. households reduce, monitor, understand, and manage electricity, heating/cooling, gas, and water costs — taxonomy §2, catalog §3, keywords §4, pipeline §5, Commander top-5 stress-test §6, guardrails §7.
2. Strongest availability + purchase intent: plug-in watt meters (P3 P4400 ~9.7K stars ~400+/mo; generic 8.5K-star Best Seller; prospector evidence 2026-08-30) · point water-leak sensors (GoveeLife 5-pack triple-verified live: $59.98 In Stock) · air-sealing consumables (tracer CONFIRMED across the category) · window insulation kits (3M/Duck CONFIRMED).
3. Highest-ticket anchors: whole-home energy monitors (~$100-200, panel install, renters excluded) and whole-home water monitors (Flume 2 ~$199; Moen Flo $559 live) — both land on products the site already wires (Emporia in 6 files, Govee in 5, Flo in 3 — executor grep).
4. Distinctive open SERPs: thermal curtains (Reddit + brand blogs only, no review mill) · humidity/dehumidifier cost questions (OPEN) · water-leak upgrade/insurance/water-bill angle (head saturated, angle uncovered) · MERV question space (forums; zero site coverage).
5. Cannibalization fences (executor, Commander-verified): kill-a-watt how-to and leak-detector roundup are HIGH fragmentation zones — enter only via the sharply angled pieces in §5-§6, never as generic roundups.
6. Renters are first-class: renter-clean paths exist for electric (plug meter, monitoring smart plug), envelope (shrink kits, sweeps, weighted stoppers, hang-on curtains), and water (Govee stick-on; Flume with meter access).
7. Honesty spine: monitors measure — user behavior saves; humidity devices are comfort-framed and climate-dependent; every circulating figure is labeled study-/manufacturer-/EPA-reported (§7.1); gas/CO detectors alert, never prevent (§7.2).
8. Pipeline: 10 article angles staged for the Sept-Nov pre-winter window from brief D's 16 deduplicated winnable targets; the Commander's 5 ranked slots are stress-tested in §6 without reordering.
9. Biggest operational risk: availability decay — Amazon search endpoints were 503-limited on 2026-08-30 while direct product pages (/gp/aw/d/ASIN) stayed fetchable (mason-verified fallback); the §7.3 checklist makes publish-time verification mandatory.
10. Recommended uncorrelated checks before any publish: dsv4/qwen wing seats re-derive price bands against live listings and re-confirm leak-slot stock states — Lieutenant (GLM) is never the sole verifier of this synthesis (§7.5).

## 2. Master product taxonomy (utility × purpose)

| Utility ↓ / Purpose → | DIRECT SAVINGS & MEASUREMENT | AWARENESS | COMFORT | MAINTENANCE | EFFICIENCY |
|---|---|---|---|---|---|
| **Electric** | Whole-home CT monitors (Emporia Vue 3 / Refoss EM16P / Eyedro) · plug-in meters (P3 Kill A Watt) · monitoring smart plugs (Kasa KP115 / Tapo P110M / Emporia) | In-app usage reports (monitors; ecobee energy reports) · smart-meter education tie-ins | Portable power stations (outage cost-avoidance ONLY — never pays-for-itself) | — | EV pass-through monitoring (Poniie PN2500) · scheduled kill of phantom loads |
| **Heating/cooling** | Envelope measurement: IR thermometers · FLIR-class phone thermal | Hygrometers (temperature + RH awareness) | Smart/programmable thermostats (ecobee / Nest / Amazon budget / Honeywell) · humidifiers (winter dry air) | Pleated furnace filters MERV 8-13 (1-3 month cycle) | Air-sealing (sweeps, weatherstrip, rope caulk, outlet gaskets, attic covers, chimney plugs) · window kits + thermal curtains · ceiling fans (reverse mode) · thermostat lock guards (landlord) |
| **Gas** | — (no metering product; meter-read education is site-native) | NG/propane detectors · CO detectors (distinct devices — §7.2) | Thermostat scheduling on gas furnaces (long-tail only) | Pro-led combustion upkeep (not an Amazon product slot) | Gas-heat-specific thermostat angle (zero site coverage — open slot) |
| **Water** | Whole-home flow monitors + shutoff (Flume 2, Moen Flo) · low-flow showerheads + faucet aerators | Point leak sensors (Govee class) · meter leak-indicator education (art. 06 tie-in) | Spray-comfort low-flow selection (no per-gallon promises) | Toilet-leak test / dye tablets (UNVERIFIED) | Water-heater blankets · pipe foam · smart irrigation (head SATURATED — footnote only) |

Purpose-axis definitions: DIRECT = measures or cuts metered usage · AWARENESS = detects/visualizes cost drivers or hazards · COMFORT = changes felt conditions, no savings promised · MAINTENANCE = recurring protective replacement · EFFICIENCY = reduces load passively or via control.

## 3. Product catalog by category

Install classes: PLUG-IN · BATTERY-PLACE (plug/hang/lay/strap) · STICK-ON/TAPE · SCREW-ON · TOOL-DIY (hand tools) · PANEL (electrical) · PRO (trade). Every row carries its wave-1 availability label verbatim · install class · renter flag. Band = price band only.

### 3.1 Plug-in watt meters — electric · DIRECT SAVINGS & MEASUREMENT

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| P3 Kill A Watt P4400 (B00009MDBU, repo-wired ×7 files) | $15-30 | Appliance-level kWh mystery → metered socket reads live watts + cumulative kWh | PLUG-IN · YES | CONFIRMED — live Amazon search fetch 2026-08-30 (~9.7K stars, ~400+/mo) |
| P3 P4460-class (kWh-cost projection variant) | $25-40 (band not captured — verify at publish) | kWh → projected dollars → programmable utility rate × measured kWh | PLUG-IN · YES | UNVERIFIED this run (live keyword p4400 vs p4460 — verify ASIN at publish) |
| Generic Upgraded Watt Meter class | $15-30 (MXN-converted band) | Same metered-socket mechanism at impulse price | PLUG-IN · YES | CONFIRMED — 2026-08-30 (8.5K stars, category Best Seller) — secondary link only |
| Poniie PN2500 (Level-1 pass-through with energy monitor) | $150-200 | See what EV charging adds → pass-through kWh metering during an L1 session | PLUG-IN · YES (garage outlet) | CONFIRMED — live search fetch 2026-08-30 (252 stars) |

- Problem/seasonality: phantom loads, refrigerator draw, which-appliance-costs-most; steady year-round, summer AC-anxiety bump, slight Oct-Nov heater-check uptick (prospector).
- Affiliate potential: lowest AOV in the dossier but clearest measured purchase intent; P4400 primary + monitoring plugs as basket augment; renters are the entire funnel; feeds slots #1 and #5.
- Limitations: 120 V plug loads only (no hardwired/240 V, no whole-home view); duplicate-listing trap on generics — lead with branded P3; accuracy skepticism is real search intent (is a kill a watt meter accurate).

### 3.2 Whole-home energy monitors — electric · DIRECT SAVINGS & MEASUREMENT

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Emporia Vue 3 (B0C7B1LKDW, repo-wired ×6 files) | $100-170 | Whole-home + per-circuit visibility → CT clamps on mains + up to 16 circuits; livestream app, usage reports; solar-ready | PANEL (DIY-electrical or electrician) · NO — renters excluded, classify honestly | CONFIRMED — live search fetch 2026-08-30 (858 stars, 1K+/mo) |
| Refoss EM16P (16-circuit) | $100-150 | Same CT mechanism at lower price → multi-channel split + app reports | PANEL · NO | CONFIRMED — 2026-08-30 (175 stars) |
| Eyedro (class) | $100-200 | Budget whole-home → CT clamps + wifi module + cloud plans | PANEL · NO | CONFIRMED — 2026-08-30 (121 stars) |
| Sense (brand) | n/a (never invent) | ML load disaggregation — must be discussed in the slot #1/#2 articles | PANEL · NO | UNVERIFIED on Amazon (sold via sense.com, 2026-08-30) |

- Problem/seasonality: why-is-my-bill-high diagnosis, vampire hunting, solar/net-metering visibility; evergreen with Jan-resolution + Jun-Aug spikes.
- Affiliate potential: highest-price electric anchor; Emporia pre-wired across 6 articles (03, 05, how-do-smart-meters, 11, ev-charging, gadgets); Sense's non-Amazon status printed as a caveat, not buried.
- Limitations/pro-needs: line-voltage panel work — electrician-recommended note mandatory; needs neutral + CT slot space; renters route to §3.1/§3.3.

### 3.3 Energy-monitoring smart plugs — electric · DIRECT SAVINGS & MEASUREMENT

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Kasa KP115 (B08LN3C7WK, repo-wired) | band n/c (verify at publish) | Per-device kWh + scheduled standby kill → metering chip reports to app; schedules cut idle draw | PLUG-IN · YES | UNVERIFIED this run (listing not captured; inventory pre-validated by live site wiring, brief B) |
| Tapo P110M (B0DKGBP38V, repo-wired) | band n/c (verify) | Same mechanism; Matter-class ecosystem fit | PLUG-IN · YES | UNVERIFIED this run (repo-wired) |
| Emporia smart plug (B0CLVV7X7Y, repo-wired) | band n/c (verify) | Same; co-sells with Vue ecosystem dashboards | PLUG-IN · YES | UNVERIFIED this run (repo-wired) |

- Differentiation fence: NOT a general smart-plug roundup (excluded, brief F) — only energy-monitoring-capable plugs, answering which-smart-plug-measures-energy-usage.
- Affiliate potential: mid-band impulse AOV; bridges §3.1 and §3.2; ties into existing 50-best-smart-plugs and phantom-power articles.
- Limitations: metering accuracy varies by model; the window-AC question must answer compressor-surge honestly; cheapest generics drift.

### 3.4 Smart & programmable thermostats — heating/cooling · COMFORT (+ monitoring angle)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| ecobee Smart Thermostat Premium (B09XXS48P8, repo-wired) | $150-250 | Schedule + occupancy setbacks → remote sensors, eco+ pre-conditioning; energy reports = the monitoring angle | TOOL-DIY (C-wire; power off) · PARTIAL — leases may forbid swaps; keep + reinstall original | UNVERIFIED this run (brand ASIN repo-wired; verify live at publish) |
| Google Nest Learning (B0D5BBYRJM, repo-wired) | $180-280 | Learns schedule → auto-setbacks, app/voice, energy history | TOOL-DIY (C-wire or Power Connector) · PARTIAL (same) | UNVERIFIED this run (repo-wired) |
| Amazon Smart Thermostat (budget anchor) | $60-100 | Schedules + Alexa Hunches at entry price → same setback mechanism | TOOL-DIY (C-wire req.) · PARTIAL | UNVERIFIED this run |
| Honeywell T9/T10 | $130-200 | Room-sensor balancing → occupied-room priority | TOOL-DIY · PARTIAL | UNVERIFIED this run |
| 7-day programmable + lock guard $10-20 (LANDLORD angle) | $30-60 | Occupancy-only runtime → weekly schedule, no app; guard limits tenant setpoint drift | TOOL-DIY · YES if lease allows; guard = landlord-installed | UNVERIFIED this run |

- Competition law: head SATURATED (Wirecutter + brand pages) — long-tail only (how much can a smart thermostat save per month / without c wire / work with my furnace).
- Affiliate potential: existing Nest/ecobee article cross-links; budget anchor + lock-guard is the differentiated landlord/rental angle; bi-modal Oct-Nov + Jul seasonality.
- Limitations: C-wire, HVAC-compatibility, and lease caveats mandatory on every renter mention; no per-month dollar promises (§7.1).

### 3.5 Furnace filters (MERV tiers) — heating/cooling · MAINTENANCE

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| MERV 8 pleated multipack (Filtrete 1085 / Nordic Pure class) | $15-40 (multipack) | Airflow protection at low restriction → blower runs against a clean filter | BATTERY-PLACE (drop-in) · YES (tenant-replaceable where lease assigns filters) | UNVERIFIED this run (staple brands — verify live) |
| MERV 11/13 high-capture (Filtrete 1900/2200, Nordic Pure class) | $25-60 | Allergen capture + recurring replacement → same drop-in, subscribe-and-save fit | BATTERY-PLACE · YES | UNVERIFIED this run |
| Cheap fiberglass / wrong-size (anti-recommendation row) | $10-25 | The problem row for the guide → honest capture-vs-restriction contrast | — | n/a (educational counterpoint) |

- Zero site coverage today (executor) — the cleanest structural gap in the inventory; recurring 1-3 month cadence fits subscribe-and-save.
- Affiliate potential: commodity margins but recurring baskets + evergreen question traffic (does a clogged furnace filter increase electric bill); winter-peak replacement cadence.
- Limitations: SIZE is the critical failure point (top returns complaint); high-MERV static-pressure caveat ties to art. 13 (ac short-cycling) — never recommend blind MERV 13.

### 3.6 Air-sealing & draft-proofing — heating/cooling · EFFICIENCY (all CONFIRMED — cheapest entries, renter-perfect)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| M-D Caulk Cord Weatherseal 71510 (rope caulk) | $8-15 | Small-gap drafts at sash/trim → press-in soft rope seals stationary joints | STICK-ON/TAPE · YES | CONFIRMED — tracer search fetch 2026-08-30 |
| M-D Cinch slide-on door bottom, 36in 2pk | $15-30 | Under-door infiltration → U-channel slides on, vinyl fin sweeps threshold | TOOL-DIY (trim to length) · PARTIAL (door alteration) | CONFIRMED — 2026-08-30 |
| Holikme under-door draft stopper (B07MSM6G9R, Commander-confirmed ASIN) | $8-15 | Bottom-gap drafts/noise/dust → adhesive sweep seals door-to-floor gap | STICK-ON · YES | CONFIRMED — tracer + Commander SERP 2026-08-30 |
| Gorilla Grip / NABOWAN weighted draft stoppers | $15-25 | Larger gaps, zero install → weighted snake blocks airflow | BATTERY-PLACE (lay in place) · YES | CONFIRMED — 2026-08-30 |
| Outlet insulation gaskets 50-pk (Tondiamo / Wakhow class) | $5-15 | Wall-cavity leakage at outlets → foam pad behind plate slows air exchange | TOOL-DIY (screwdriver; breaker off) · YES | CONFIRMED — 2026-08-30 |
| DGSL / Miloo attic-hatch covers (R-13-15.6 class) + chimney flue plugs $12-60 | $25-60 | Stack-effect loss at hatch / unused flue → insulated tent or sized flue plug | TOOL-DIY · NO (hatch), PARTIAL (flue, removable) | CONFIRMED — 2026-08-30 (flue plug: MUST remove before any fire) |
- Tracer's strongest category overall: cheap, renter-perfect, huge unit counts, everything CONFIRMED; funnel base for slot #5.
- Affiliate potential: whole-house multi-unit baskets (windows + doors + outlets + hatch); Amazon's own listing ranks #1 organic for best door draft stopper (CONTESTED-SOFT per brief D) — content must out-teach the marketplace, not out-list it.
- Limitations: gap-size fit matters; adhesive durability on high-wear exterior doors; attic covers need landlord buy-in; flue-plug remove-before-fire warning is mandatory copy (§7.2).

### 3.7 Window insulation & thermal curtains — heating/cooling · EFFICIENCY (slot #2 category)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| 3M Indoor Window Insulator Kit (2141W-6; 2/5/6-window packs) | $10-35 | Cold glass + condensation → shrink film + hair-dryer tension creates a dead-air layer | STICK-ON · YES | CONFIRMED — live search fetch 2026-08-30 |
| 3M Outdoor Patio Door Kit (7ft x 9.3ft) | $20-40 | Sliding-door glass loss → same dead-air mechanism, larger sheet | STICK-ON · PARTIAL (exterior may need landlord OK) | CONFIRMED — 2026-08-30 |
| Duck MAX Strength kit (5/10-window) | $10-30 | Budget shrink-film alternative → same mechanism | STICK-ON · YES | CONFIRMED — 2026-08-30 |
| Thermal/blackout curtains (NICETOWN / Deconovo class) | $20-50 | Winter window heat loss + summer solar gain → multi-layer lining traps still air; blackout a secondary benefit | BATTERY-PLACE (rod hang) · YES | UNVERIFIED brand listings this run (tracer budget) — category Commander-SERP-confirmed top-selling on Amazon, 2026-08-30 |
| Insulated window blanket cover (LSGCQ class) | $15-30 | Hung fabric barrier over glass → insulating layer without any adhesive | BATTERY-PLACE · YES | CONFIRMED — appeared in 3M fetch, 2026-08-30 |

- Study/manufacturer-reported figures (LABEL, never promise; §7.1): thermal curtains up to 25-40% of window heat loss — study-reported · window film up to 35% — manufacturer-reported.
- Affiliate potential / seasonality: SERP genuinely open (Reddit + brand blogs only, Commander-verified); publish Oct-Nov, peak Oct-Feb, minor summer solar-gain tail; baskets with §3.6 sweeps.
- Limitations: kits are one-season honesty (tape residue; remove before opening window); curtains must fully overlap (fit beats claims); brand ASINs gate publication (Dissent D-2, §6).

### 3.8 DIY audit tools — cross-utility · AWARENESS

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| FLIR ONE Pro (B072J49BX7, repo-wired in art. 47) / FLIR ONE Edge class | $200-330 | Find cold spots / missing insulation → phone-attach IR map of walls, windows, ducts | BATTERY-PLACE (phone attach) · YES | UNVERIFIED this run (repo-wired) |
| Etekcity-class laser IR thermometer | $15-50 | Spot-check surfaces before/after fixes → non-contact temperature reads | BATTERY-PLACE · YES | UNVERIFIED this run |

- Overlap fence: existing art. 47 (check-energy-leaks-home-diy) owns the audit walkthrough — cross-link, never duplicate (brief E2).
- Affiliate potential: winter temp-differential seasonality; IR gun = cheap audit-bucket conversion inside slot #5; FLIR = serious-DIYer upsell.
- Limitations: IR is visualization, not a savings calculator; emissivity caveat on readings; phone-compatibility note.

### 3.9 Humidity instruments & machines — heating/cooling · COMFORT (climate-dependent honesty REQUIRED)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| ThermoPro TP50 / Govee-class hygrometer | $10-25 | Know indoor RH/temp → guides humidify-dehumidify decisions and setpoint comfort | BATTERY-PLACE · YES | CONFIRMED-staple (brief E2, 2026-08-30); exact ASIN verify at publish |
| Cool-mist humidifier (Levoit Classic 300S class) | $30-80 | Winter dry air at lower setpoints → raises RH so lower thermostats stay comfortable | BATTERY-PLACE · YES | UNVERIFIED this run |
| Dehumidifier (hOmeLabs / Frigidaire 35-50 pint; mini $40-70) | $150-300 (full size) | Latent load on AC → removes moisture so AC dehumidifies less; comfort framing ONLY | BATTERY-PLACE (drain/bucket) · YES (portable) | UNVERIFIED this run |

- Honesty law (brief F): pros are split — the answer is climate-dependent (humid + mild = likely help; very hot or right-sized AC = questionable). The honest treatment IS the differentiation; running-cost transparency without dollar promises.
- Affiliate potential / seasonality: OPEN question space (Reddit + HVAC blogs only); hygrometer = evergreen tuning accessory; dehumidifier peaks humid-summer, humidifier winter.
- Limitations: the dehumidifier's own kWh partially offsets; comfort varies by person/climate; never promise AC savings.

### 3.10 Gas & CO safety devices — gas · AWARENESS (framing law §7.2 — ALERT, never prevent)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Natural gas / propane detector (Kidde / Honeywell / NGP-3 class, plug-in) | $20-40 | Detect unburned gas buildup near appliances → sensor alarm at elevated concentration | BATTERY-PLACE (plug-in) · YES | UNVERIFIED this run (staple brands — verify live) |
| Standalone CO detector (Kidde Nighthawk class) | $20-40 | CO awareness → electrochemical sensor alarm | BATTERY-PLACE · YES | UNVERIFIED this run |
| Combo smoke + CO (Kidde / First Alert class, 10-yr sealed) | $25-60 | Two-hazard alarm coverage → smoke + CO in one unit; some hardwire = TOOL-DIY | BATTERY-PLACE · YES (battery forms; coordinate landlord on required units) | UNVERIFIED this run |

- Mandatory copy elements: detectors ALERT, never PREVENT · suspected gas leak → leave the area and call the gas utility/professional from outside · CO detectors do NOT detect natural gas (distinct devices, distinct education).
- Affiliate potential: low AOV, high trust signal inside the gas-bill cluster (07); evergreen; natural pairing in any gas-heat article.
- Limitations: placement matters (near gas appliances; follow manufacturer height/placement for NG vs propane); test-schedule and false-alarm honesty.

### 3.11 Whole-home water monitors & shutoff — water · DIRECT SAVINGS & MEASUREMENT (slot #4 anchor)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Flume 2 (B08DX6MP8X, Commander-confirmed) | ~$199 (vs $269 direct) | Hidden use + slow leaks → straps onto the existing meter, no pipe cutting, app flow breakdowns | BATTERY-PLACE (strap-on) · PARTIAL — YES for renters with accessible meter | CONFIRMED — Commander SERP 2026-08-30; Amazon cheaper than direct |
| Moen Flo 900-001 (triple-verified B00C03D01Q) | $559 (live 2026-08-30) | Catastrophic-leak protection + awareness → inline valve cuts the main on leak/pressure anomalies | PRO (plumber cuts into main line) · NO — owner property | CONFIRMED — mason live fetch + Commander SERP + repo (sold by Amazon.com) |
| Moen variants (1in B081HT5LD6 · point detector 920-004 B0855BFQCZ · bundle B08B1FG41F) | band n/c (verify at publish) | Fit and step-down options for the same system | same | CONFIRMED (Commander, 2026-08-30; verify live) |

- Problem/seasonality: surprise water bills (44/06 tie-ins), insurance-discount angle (do smart shutoff valves lower home insurance — long-tail uncovered), travel/rental protection; evergreen with a fall insurance-renewal angle.
- Affiliate potential: HIGHEST EPC band in the dossier (packet fact); both products already wired site-wide; the upgrade narrative powers slot #4.
- Limitations: Flo = pipe-cut (plumber for most owners); Flume needs meter compatibility (lock/lid issues); renter honesty varies by building meter setup.

### 3.12 Point-of-use water leak sensors — water · AWARENESS (mason's accepted strongest water subcategory)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| GoveeLife Water Leak Detector 1s 5-pack (triple-confirmed B0DQLFC3Q6) | $59.98 listed (live 2026-08-30) | Catch drips at water heater, toilet, sump early → stick-disc sensors alarm to phone at low cost | SCREW/STICK · YES | CONFIRMED — mason product-page fetch + repo wiring + Commander SERP, 2026-08-30 |
| YoLink point sensor (class) | band n/c (verify) | Long-range hub-and-sensor mesh for detached spaces → same alarm-first mechanism | SCREW/PLACE · YES | UNVERIFIED — exact ASIN not captured (verify at publish) |
| Point-sensor field (First Alert L1 · D-Link SW-A11KT · Eufy · SwitchBot · X-Sense · Kidde) | band n/c (verify each) | Competing alarm-first ecosystems; Commander-SERP landscape (PCMag/Wirecutter/CNET picks) | SCREW/PLACE · YES | UNVERIFIED individually this run |

- Problem/seasonality: the water-heater drip found at $60 instead of the floor found at thousands; evergreen with a winter freeze-panic bump.
- Affiliate potential: low price → high conversion; feeds the §5 upgrade-path article (Govee now → Flo/Flume later); renter-perfect; already wired in 44/06/gadgets.
- Limitations: alarm-only (local beeps; some need hub/wifi); battery checks; whole-home shutoff covers what point sensors cannot see — that contrast IS the slot #4 article.

### 3.13 Low-flow fixture retrofits — water · DIRECT SAVINGS (SCREW-ON, renter-restore note)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Niagara Earth massage showerhead, 1.25 GPM (N2912CH class) | band n/c (verify) | Hot-water volume cost → flow restriction cuts heated gallons per shower | SCREW-ON · YES | CONFIRMED — Commander SERP 2026-08-30; ASIN verify at publish |
| High Sierra Half Dome, 1.5-1.8 GPM | band n/c (verify) | Low flow with pressure feel → nozzle engineering reduces flow, keeps spray | SCREW-ON · YES | CONFIRMED — same basis |
| Kohler Forté, 1.75 GPM | band n/c (verify) | Mainstream-brand entry → moderate restriction | SCREW-ON · YES | CONFIRMED — same basis |
| Faucet aerator multipacks (male/female threads) | band n/c (verify) | Cheapest heated-water cut → thread-on flow reducers per tap | SCREW-ON · YES | CONFIRMED staple category — ASINs at publish |

- EPA label law: WaterSense = at least 20% less water under the EPA program definition (EPA program claim — label as such, never as a bill promise).
- Affiliate potential / seasonality: runner-up only (MED cannibal with art. 44, which already wires aerators); evergreen with summer water-bill anxiety; the savings-MATH angle is unowned per brief D.
- Limitations: low-flow-vs-low-pressure complaints must be answered by model choice; renters unscrew originals — keep-and-restore note; per-year dollar math stays illustrative-mechanism, never promised (§7.1).

### 3.14 Water-heater blanket & pipe insulation — water/gas · EFFICIENCY (LOW cannibalization — executor)

| Product | Band | Problem → mechanism | Install · Renter | Amazon availability |
|---|---|---|---|---|
| Water heater insulation blanket (40-80 gal fit kits) | band n/c (verify at publish) | Standby heat loss from the tank → wraps the tank jacket (electric simplest; gas needs placement cautions) | TOOL-DIY (wrap + tape) · PARTIAL — landlord item in practice | CONFIRMED category-level — live Amazon Best Seller category, Commander SERP 2026-08-30; ASINs at publish |
| Pre-slit self-sealing pipe foam, 3/4in multipack | band n/c (verify) | Distribution losses on exposed runs → slip-on foam halves per pipe section | STICK/SLIP-ON · YES | CONFIRMED category-level — same basis, 2026-08-30 |

- Site gap is clean: only 2 list-item mentions sitewide (executor) — LOW cannibalization; pairs with anchors how-to-lower-electric, 44, 48, 07, 30.
- Affiliate potential / seasonality: cheap multi-item basket beside the MERV piece; Oct-Nov publish peak; evergreen standby-loss education.
- Limitations: gas water heaters — follow manufacturer placement cautions (top/vent clearance); R-value honesty; small-ticket AOV.

### 3.15 Footnote-only candidates (NOT primary slots; verify before any use)

| Candidate | Band | Status / why footnote |
|---|---|---|
| Smart sprinkler controllers (Rachio 3 / Orbit B-hyve) | band n/c | Head SATURATED (CR + CNET + Wirecutter + Wired); current ASINs UNVERIFIED — runner-up long-tail only, Mar-Jun window |
| Smart vents (Flair $150-400 · Keen $80-120/vent) | $80-400 | MIXED field evidence; Keen vendor status uncertain (tracer caution) — footnote only |
| ENERGY STAR / DC-motor ceiling fans (Hunter / Honeywell / Minka) | $150-400 | Install often pro (PARTIAL renter); comfort mechanism framing; UNVERIFIED this run |
| Portable power stations | band n/c | Outage cost-avoidance framing ONLY (never pays-for-itself); UNVERIFIED this run |
| Recirculation pumps · pressure gauges · toilet repair kits · dye tablets | band n/c | Mason UNVERIFIED rows; toilet-leak education already on site (is-your-toilet-running-leak-test) — link, do not build product pages blind |

## 4. Keyword opportunities (competition classes = Commander-verified 2026-08-30 SERPs, brief D — no upgrades taken on worker inference)

| Domain | Informational | Commercial | Long-tail questions | Competition class (verified) |
|---|---|---|---|---|
| energy-monitor | how a whole-home energy monitor works (CT clamp) · how much electricity does my house use | best whole home energy monitor · emporia vue vs sense | do home energy monitors save money · is emporia vue worth it without solar · can a monitor detect energy vampires | head CONTESTED (brand + Wirecutter); long-tail OPEN |
| watt-meter | how to use a kill a watt meter · how to measure appliance power consumption | kill a watt vs smart plug energy monitor · p4400 vs p4460 | how many watts does my refrigerator use · is a kill a watt meter accurate · what appliance uses the most electricity | UNVERIFIED (likely CONTESTED; Amazon-saturated products) |
| smart-plug (energy-monitoring only) | how do smart plugs with energy monitoring work | best smart plug with energy monitoring | which smart plug measures energy usage · can a smart plug measure a window AC watts | head CONTESTED (direct SERP unverified; Wirecutter in category) |
| thermostat | what is a c wire for a thermostat | best smart thermostat without c wire | how much can a smart thermostat save per month · does a smart thermostat pay for itself · will it work with my furnace | head SATURATED (Wirecutter + brand pages) — long-tail only |
| thermal-curtain | do thermal curtains work · what makes curtains thermal | best thermal curtains for winter · insulated vs thermal curtains | do thermal curtains really save on heating bills · thermal curtains for sliding glass doors worth it | CONTESTED-OPEN (Reddit + brand blogs; NO review mill observed) |
| weatherstrip | how to weatherstrip a door · how to stop a draft under the door | best door draft stopper | does a draft stopper actually work · what weatherstripping is best for a front door | CONTESTED-SOFT (#1 organic = Amazon listing B07MSM6G9R + NY Strategist + one blog) |
| window-film/kit | how do window insulation kits work | best window insulation kit for winter | will window film lower my electric bill in summer · do window films pay for themselves in one winter | CONTESTED (Bob Vila, EcoWatch, CR; 3M/Duck/Frost King dominate) |
| leak-detector | why use a whole home leak detector vs point sensors | flume vs moen flo smart water shutoff · best wifi water leak sensor with shutoff | when should I upgrade from a point leak sensor to whole home · do smart shutoffs lower home insurance · how much water does a slow drip waste per month | head SATURATED (PCMag + Wirecutter + CNET + CR); bill/upgrade angle UNCOVERED |
| low-flow | what does gpm mean in a showerhead | best low flow showerhead · best 1.5 gpm high pressure showerhead | how much money does a low flow showerhead save per year · will a low flow showerhead reduce my water heater bill | CONTESTED (general roundups; nobody owns savings math) |
| furnace-filter / MERV | why does a dirty filter raise my heating bill | best merv 13 furnace filter · merv 13 vs merv 8 | does a clogged furnace filter increase electric bill · how often should I change my furnace filter to save energy | head CONTESTED (Wirecutter + CR); forums own the questions |
| humidity / dehumidifier | why does high humidity make ac work harder · what humidity level should my home be | best dehumidifier for whole home (soft) | do dehumidifiers help with cooling costs in summer · how much does a dehumidifier cost to run per month · will one let me set my thermostat higher | OPEN (Reddit + HVAC blogs only) |
| irrigation | what is evapotranspiration in smart sprinklers | best wifi sprinkler controller for water savings | how much does a smart sprinkler controller save on my water bill · will it pay for itself in one season | head SATURATED (CR + CNET + Wirecutter + Wired) — long-tail runner-up only |

- No search volumes exist anywhere in wave-1 — keyword priority above is qualitative and question-led per evidence quality; do not invent volumes downstream.
- The Commander-ordered 16-target winnable pool (brief D) maps 1:1 into §5's pipeline; watt-meter and smart-plug classes remain UNVERIFIED and must be SERP-checked before building under them.

## 5. Article pipeline (10 angles; internal-link targets from brief C)

| # | Working title | Primary keyword | Reader question | Intent | Hook / differentiation | Internal links (brief C) | Window |
|---|---|---|---|---|---|---|---|
| 1 | Do Home Energy Monitors Save Money? | do home energy monitors save money | Will buying a monitor cut my bill? | informational w/ commercial close | Monitors measure, behavior saves — honest mechanism piece; Emporia wired, Sense open | 03, 05, how-do-smart-meters, ev-charging, gadgets, 11 | evergreen; Jan + Jun-Aug peaks |
| 2 | Emporia Vue 3 vs Sense: an Impartial Comparison | emporia vue vs sense | Which monitor should I actually buy? | commercial comparison | Brand SERP lacks impartial answer; Sense-not-on-Amazon caveat printed up front | 03, 05, gadgets, how-do-smart-meters, 11 | evergreen |
| 3 | Do Thermal Curtains Really Save on Heating Bills? | do thermal curtains really save on heating bills | Is the curtain upgrade worth it — and does it do anything? | informational | SERP = Reddit + brand blogs only; hang-technique section; all figures labeled study-reported (§7.1) | 07, 44, 05, gadgets | publish Oct-Nov; peak Oct-Feb |
| 4 | What MERV Rating Do I Need? (And Does a Clogged Filter Raise My Bill?) | what merv rating do i need | Which filter for my system — and how often? | informational | Zero site coverage; static-pressure honesty ties art. 13; subscribe-and-save multipacks | 47, how-to-lower-electric-bill-complete-guide, 13, ac-running-but-not-cooling | publish Oct-Nov; evergreen S&S |
| 5 | Point Sensors vs Whole-Home Water Protection: When to Upgrade | when should I upgrade from a point leak sensor to whole home | I have Govee sensors — when do I need Flo or Flume? | informational + comparison | Insurance + surprise-water-bill angle avoids the saturated head; products already wired | 44, 06, gadgets, why-did-my-water-bill-suddenly-increase, is-your-toilet-running-leak-test | evergreen (fall insurance angle) |
| 6 | How to Find and Seal the 10 Draftiest Spots in Your Home | how to stop a draft under the door (draft-stopper cluster) | Where is my house losing air — and what exactly do I buy? | how-to w/ purchase basket | Room-by-room audit → product basket; renter-perfect; IR-gun step cross-links 47 without duplicating it | 07, 47, 05, 06 | publish Sept-Oct; winter peak |
| 7 | Which Smart Plug Measures Energy Usage? | which smart plug measures energy usage | Which plug shows watts, not just on/off? | commercial, differentiator fence | NOT a general roundup (F-ruled); KP115 / P110M / Emporia-plug monitoring angle only | 50, phantom-power-draw-explained, gadgets, 42 | evergreen; Nov-Dec setup + summer |
| 8 | How Many Watts Does My Refrigerator Use? (Measuring Big Appliances) | how many watts does my refrigerator use | What are my fridge, space heater, or EV charger actually costing? | informational | Kill A Watt as the measurement path; kWh math built from the site's own education, no invented dollars | how-to-lower-electric-bill-complete-guide, 03, 11, gadgets | evergreen |
| 9 | Do Dehumidifiers Help With Cooling Costs? (The Climate-Dependent Answer) | do dehumidifiers help with cooling costs in summer | Will a dehumidifier lower my summer bill? | informational | Climate-dependent honesty IS the differentiator (brief F); running-cost math + latent-load explainer | 30, 03, gadgets, 44 | publish Apr-Jun; humid-season peak |
| 10 | Do Window Insulation Kits Pay Off in One Winter? | best window insulation kit for winter / will window film lower my electric bill in summer | Shrink kits vs films vs curtains — what is worth it? | info + commercial | Mechanism (dead-air layer) + one-season honesty; figure labels mandatory | 07, 05, 06, 44 | publish Oct-Nov |

- Runners-up (one line each, per Commander): low-flow showerhead savings math — MED cannibal with art. 44 (fold into 44 or the §4 long-tail later, never a standalone roundup) · dehumidifier-cost question — OPEN but comfort-framed (covered as #9's second half) · smart-thermostat monthly-savings long-tail — SATURATED head; FAQ material inside #4/#6 territory only.
- Seasonality spine: Sept-Oct = #6 and #4 prep · Oct-Nov = #3, #4, #10 publish · evergreen = #1, #2, #5, #7, #8 · Apr-Jun = #9 and the irrigation footnote.

## 6. THE COMMANDER'S RANKED TOP-5 (reproduced verbatim from the draft — stress-tested below, NOT reordered)

1. **Whole-home energy monitor guide — 'Do Home Energy Monitors Save Money?'** (+ Emporia-vs-Sense comparison with Sense-not-on-Amazon caveat; plug-monitor renter path; Emporia already wired across 6 articles).
2. **Thermal curtains — 'Do Thermal Curtains Really Work?'** (SERP open-ish: Reddit + brand blogs only; winter-timed publish Oct-Nov; NICETOWN/Deconovo confirmed best-sellers; study-reported figures labeled).
3. **Furnace filter MERV guide — 'What MERV Rating Do I Need?'** (zero site coverage; recurring subscribe-and-save; forum-weak question space; HVAC cluster cross-links).
4. **Water-leak upgrade path — 'Point Sensors vs Whole-Home: When to Upgrade'** (SATURATED head avoided via upgrade/insurance/water-bill angle; Govee + Flo + Flume verified ASINs; highest EPC band; already-wired products).
5. **Draft-proofing audit — 'How to Find and Seal the 10 Draftiest Spots'** (all products confirmed; cheapest entries; renter-perfect; 07/47 cross-links; winter-timed).

- Runners-up: low-flow showerhead savings math (MED cannibal w/ 44) · dehumidifier-cost question (OPEN but comfort-framed) · smart-thermostat monthly-savings long-tail (SATURATED head).

**Slot 1 — case FOR:** the savings-question frame is exactly the site's native format, the long-tail is open while Emporia sits pre-wired across 6 articles and Sense is an untouched brand slot, and the renter path (plug meter / monitoring plug) widens the audience beyond panel owners. **Biggest risk:** the title promises savings the device cannot promise — if the piece drifts toward implied % returns it violates savings law; and the Sense-not-on-Amazon caveat must be explicit or the comparison misleads.

**Slot 2 — case FOR:** the winter keyword is measurably open (Reddit + brand blogs only, Commander-verified), the products are cheap and enormously reviewed, and Oct-Nov timing aligns with the gas-bill cluster (07). **Biggest risk:** the 25-40%-of-window-heat-loss class of figures is study/manufacturer-reported, never a bill promise — and brand listings were not individually search-CONFIRMED this wave (tracer UNVERIFIED at category level), so the piece is gated on publish-time ASIN verification.

**Slot 3 — case FOR:** MERV is the only double-verified structural zero on the site (executor grep + brief C), the recurring filter cadence fits subscribe-and-save economics, and the question-form SERP is forum-held — where an 85-article education site wins. **Biggest risk:** head terms are Wirecutter/CR property — chasing best-MERV-filter lists instead of the question space ranks nowhere and earns thin margins.

**Slot 4 — case FOR:** every anchor ASIN was triple-verified live (Govee B0DQLFC3Q6 $59.98 · Flo B00C03D01Q $559 · Flume B08DX6MP8X ~$199), the angle dodges a PCMag/Wirecutter/CNET/CR-saturated head, and it carries the dossier's highest EPC band. **Biggest risk:** the executor matrix marks leak-detector content as a HIGH cannibalization zone (44, 06, gadgets, why-did-my-water-bill, is-your-toilet) — drift into a general roundup would fragment the site's own water cluster.

**Slot 5 — case FOR:** every draft-audit product was search-CONFIRMED by tracer (plus Holikme B07MSM6G9R by Commander), entries are the cheapest in the catalog, the checklist format is renter-perfect, and the 07/47 cross-links feed both the HVAC cluster and the MERV piece. **Biggest risk:** per-unit value is tiny — if the article never merchandises audit tools (IR gun / FLIR) or baskets the whole house, traffic will not monetize; Amazon's own listing also ranks #1 on the head term, so the piece must out-teach the marketplace.

**Lieutenant dissent (conditions, not a reorder — the ranking stands):**
- **D-1 (slot 4):** the slot survives ONLY as the upgrade-path piece, published with link re-pointing in art. 44/06 toward it; a best-water-leak-detector roundup is prohibited by the cannibalization matrix, full stop.
- **D-2 (slot 2):** supported on the Commander's category-level SERP confirmation, but NICETOWN/Deconovo brand listings remain UNVERIFIED this run (tracer budget) — publish is gated on live product-page verification per §7.3, and every heat-loss figure stays labeled study-reported.
- **D-3 (slot 1):** the piece must open with the honest mechanism (a monitor tells you where; you make it save) or it violates §7.1. No dissent on rank — this is a framing requirement, not a placement dispute.

## 7. Editorial guardrails

### 7.1 Savings-claim law
- NEVER print a promised % or $ saving for any product or category. Cost help is always framed as mechanism: airflow reduced, latent load lifted, standby draws scheduled off, heated gallons reduced, dead-air layer added.
- Circulating research figures are allowed only with their label attached, verbatim: thermal curtains up to 25-40% of window heat loss — study-reported · window film up to 35% — manufacturer-reported · WaterSense at-least-20%-less-water — EPA program definition · any thermostat / dehumidifier / monitor dollar figure — manufacturer-reported or omitted.
- Monitor pieces carry the plain-language truth: a monitor guarantees measurement, not savings; the article's job is the behavior bridge.
- Dehumidifier honesty is mandatory (brief F): climate-dependent answer (humid + mild = likely help; very hot or right-sized AC = questionable) — and the device's own kWh draw is disclosed.
- Outage/backup gear: cost-avoidance framing ONLY (food kept cold, medical gear alive) — never pays-for-itself math.

### 7.2 Safety-device framing law
- Gas and CO detectors ALERT, never PREVENT. Copy never implies leak prevention or protection from harm — only detection + response.
- Suspected gas leak: leave the area immediately and call the gas utility / professional from outside, per utility guidance. This instruction appears wherever gas detectors do.
- CO detectors do not detect natural gas; gas detectors do not detect CO. Where a page touches both, keep the device education distinct — never conflate the two devices.
- Chimney flue plugs carry a mandatory remove-before-any-fire warning at every mention.
- Panel work (whole-home monitors) and thermostat swaps carry line-voltage / C-wire / power-off cautions; ELECTRICIAN-RECOMMENDED for anyone uncomfortable in the panel (prospector risk note).

### 7.3 Availability-verification-before-publish checklist (run per product, per page, at publish date)
1. Re-fetch the listing on publish day — CONFIRMED labels rot; a 2026-08-30 confirmation is not a 2026-10-15 fact.
2. Amazon search 503? Fetch https://www.amazon.com/gp/aw/d/ASIN directly — mason-verified fallback on 2026-08-30 (search endpoints 503'd; product pages served).
3. Buy-box sanity: sold/shipped by Amazon or the brand; flag official-store-only situations (Emporia L2 charger: official-store sale seen, Amazon UNVERIFIED — brief E1).
4. ASIN-to-copy match: pack size, color, model number — a 5-pack vs single mismatch is a content error, not a nitpick.
5. Price = band in copy, never an exact number; geo-localized research views (MXN trap) are sanity-checked, never printed.
6. Any UNVERIFIED → CONFIRMED promotion is logged in front-matter sources[] with URL + retrieved date, per site law (brief A).
7. Geo / Prime sanity check for the U.S. storefront before final ID insert.

### 7.4 Verify ASINs at publish time (evidence-backed inventory vs open verification list)

| ASIN | Product | Provenance (all evidence-backed; never invent) |
|---|---|---|
| B00009MDBU | Kill A Watt P4400 | repo-wired ×7 files (executor grep) + live search 2026-08-30 |
| B0C7B1LKDW | Emporia Vue 3 | repo-wired ×6 + live search 2026-08-30 |
| B0D5BBYRJM / B09XXS48P8 | Nest / ecobee Premium | repo-wired (live-listing verify pending) |
| B08LN3C7WK / B0DKGBP38V / B0CLVV7X7Y | Kasa KP115 / Tapo P110M / Emporia plug | repo-wired (live verify pending) |
| B09ZNN3JB7 / B072J49BX7 | Emporia EV charger / FLIR ONE Pro | repo-wired (EV charger availability UNVERIFIED — official-store sale seen) |
| B0DQLFC3Q6 | GoveeLife leak 5-pack | triple-verified live 2026-08-30 ($59.98 In Stock) |
| B00C03D01Q (+ variants B081HT5LD6 / B0855BFQCZ / B08B1FG41F) | Moen Flo 900-001 + variants | triple-verified live 2026-08-30 ($559) |
| B08DX6MP8X | Flume 2 | Commander SERP 2026-08-30 (~$199) |
| B07MSM6G9R | Holikme under-door draft stopper | Commander SERP 2026-08-30 |

Replace-the-marker-note: mason's guessed ASINs B07WC767JT (Flume 2) and B0771ZYV9L (Rachio 3) 404'd on 2026-08-30 — treated as void; correct ASINs likely exist but must be re-verified (mason evidence).

**Open verify-at-publish list (UNVERIFIED — do not ship IDs from memory):** Sense · thermostat live listings (ecobee / Nest / Amazon / Honeywell) · Kill A Watt P4460 · MERV multipack ASINs · NICETOWN / Deconovo curtain ASINs · humidifier / dehumidifier / hygrometer staples · gas / CO detector models · Poniie PN2500 (listing confirmed, ASIN not captured) · YoLink point sensor · Rachio 3 / B-hyve · low-flow ASINs (Niagara / High Sierra / Kohler) · blanket / pipe-foam ASINs · thermostat lock guards · smart-vent footnote items · smart-plug live listings (KP115 / P110M / Emporia plug).

### 7.5 Recommended uncorrelated checks (Lieutenant is GLM — never the sole verifier of this synthesis)
- Re-derive the §3 price bands against live listings (dsv4 / qwen wing seats qualify as uncorrelated).
- Re-run the leak-slot ASIN stock states and the thermal-curtain brand verification — the two publish gates for slots #2 and #4.
- SERP-check the still-UNVERIFIED competition classes (watt-meter; smart-plug head) before building §5 #7/#8.
- Confirm the article 44/06 link re-pointing plan (D-1) against the executor's anchor list before slot #4 ships.

---

## Appendix A. Winnable-target pool → pipeline map (16 Commander-ordered targets from brief D)

| # | Target keyword | Lands in |
|---|---|---|
| 1 | do whole home energy monitors save money | §5 #1 (slot 1) |
| 2 | do thermal curtains really save on heating bills | §5 #3 (slot 2) |
| 3 | how much can a smart thermostat save per month | runners-up — SATURATED-head FAQ only |
| 4 | which smart plug measures energy usage | §5 #7 |
| 5 | how many watts does my refrigerator use | §5 #8 |
| 6 | what appliance uses the most electricity in my home | §5 #8 (secondary) |
| 7 | is emporia vue worth it without solar | §5 #2 (slot 1 companion) |
| 8 | what type of weatherstripping is best for front door | §5 #6 (slot 5 cluster) |
| 9 | when should I upgrade from a point leak sensor to whole home | §5 #5 (slot 4) |
| 10 | do dehumidifiers help with cooling costs in summer | §5 #9 |
| 11 | does a clogged furnace filter increase electric bill | §5 #4 (slot 3) |
| 12 | will a smart sprinkler controller pay for itself in one season | footnote — irrigation runner-up, Mar-Jun only |
| 13 | how much money does a low flow showerhead save per year | runners-up — fold into art. 44 (MED cannibal) |
| 14 | will window film lower my electric bill in summer | §5 #10 |
| 15 | flume vs moen flo smart water shutoff | §5 #5 (comparison section) |
| 16 | how much does a dehumidifier cost to run per month | §5 #9 (second half) |

Coverage check: all 16 accounted for — 10 pipeline slots, 2 runner-up folds, 1 FAQ-only, 1 seasonal footnote, 2 absorbed as secondaries. No target dropped.

## Appendix B. Wave-1 provenance manifest (verification audit trail)

| Source file | Seat / status | What this dossier took from it |
|---|---|---|
| evidence-brief.md §A-F | Commander-verified ground truth | site infra (A), ASIN inventory (B), gaps + anchors (C), keyword + competition classes (D), product baselines (E), rulings (F) — carried unchanged |
| results/01-prospector-r2.json | prospector, complete | electric availability evidence (P4400, generic, Vue 3, Refoss, Eyedro, Poniie CONFIRMED; Sense / plugs / L2 UNVERIFIED), seasonality, risks |
| results/01-prospector.json | prospector, complete | energy/watt-meter/smart-plug/thermostat/curtain/weatherstrip keyword sets + verified thermostat class |
| results/02-prospector-2.json | prospector#2, partial | water-half keyword sets — competition UNVERIFIED (8/8 noisy searches); not upgraded by this dossier |
| results/02-tracer.json | tracer, complete | 24-entry envelope table (search-CONFIRMED air-sealing, window kits, outlet gaskets, attic covers, chimney plugs; UNVERIFIED thermostats, filters, detectors, fans, humid/dehumid, vents, audit tools), safety framing guidance |
| results/01-mason.json | mason, complete | 2 live water listings (Flo $559, Govee $59.98); 503/404 method notes → §7.3 fallback; 14 rows held UNVERIFIED |
| results/05-executor.json | executor, partial (salvaged) | gap analysis, cannibalization matrix, internal-link anchors — grepped and Commander-verified |
| results/06-scout.json | scout, partial | product-box/amazon shortcode machinery confirmation (support context only) |
| results/04-twin_q.json | twin_q, complete | SERP observations all tagged [INFERENCE] — used as context only, never as competition-class upgrades |

Water-side trio (Govee / Flo / Flume) rests on Commander triple-verification (brief E3), the strongest evidence base in the packet — every other product row remains at its wave-1 label.

---

*End of dossier — 2026-08-30. All availability labels carried verbatim from wave-1; zero invented prices, ASINs, volumes, or savings promises; Commander top-5 reproduced and stress-tested without reordering.*


