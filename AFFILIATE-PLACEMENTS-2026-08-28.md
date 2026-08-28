# Affiliate Placement Plan — Conversion Editor Edition

**Date:** 2026-08-28 · **Lens:** post-AdSense, pure affiliate conversion. Every placement must solve the reader's problem first; the click is a side effect of usefulness.
**Rules baked in:** verified ASINs only (all checked on amazon.com this session) · links via site shortcodes (auto-tagged `utexplained-20`, `rel="sponsored nofollow"`) · disclosure already renders sitewide near links · no fabricated testing — specs come from manufacturer/DOE/EPA published facts · **no placement on crisis-intent pages** (reconnection fees, shutoff/past-due) — monetizing those is a trust-killer.

**Product inventory (all verified):** Nest Learning 4th-gen `B0D5BBYRJM` · Kill A Watt P4400 `B00009MDBU` · Kasa KP115 `B08LN3C7WK` · Kasa KP125MP2 2-pack `B0BYGRLRS1` · Tapo P110M 2-pack `B0DKGBP38V` · Emporia smart plug `B0CLVV7X7Y` · Emporia Vue 3 whole-home monitor `B0C7B1LKDW` · **NEW:** Moen Flo 900-001 `B00C03D01Q` · ecobee Premium `B09XXS48P8` · Emporia L2 EV Charger `B09ZNN3JB7` · Govee water sensors — *ASIN unverified, verify before publish.*

---

## TIER 1 — Implement now (traffic × intent × zero current monetization)

### 1. `03-why-is-my-electric-bill-so-high` — 27 pv/wk, #10 traffic, diagnosis intent

**Placement:** new paragraph at the end of `## A Practical Diagnosis Sequence` (line ~52–60), where the reader has just been told to stop guessing and measure.
**Publish-ready copy:**

```markdown
The one tool that ends the guessing: a plug-in usage meter. Put it on the appliance
you suspect, leave it 24 hours, and read the kWh and projected cost off the screen.

{{< product-box asin="B00009MDBU" name="P3 Kill A Watt P4400 Electricity Usage Monitor" label="Diagnose before you spend" description="Displays watts, kWh, and projected annual cost for anything you plug into it. 0.2% accuracy, 120V/15A, UL listed (P3 International spec sheet). This is step one of the diagnosis sequence above — it tells you whether the problem is the fridge, the space heater, or nothing electrical at all." button="Check price on Amazon" >}}

Want the whole-house picture instead of one outlet at a time? A circuit-level monitor
shows which of your breakers is actually eating the budget:

{{< amazon asin="B0C7B1LKDW" text="See the Emporia Vue 3 whole-home energy monitor on Amazon" >}} — 16 circuit-level sensors, real-time app data.
```

**Anchor/CTA:** "Diagnose before you spend" label + benefit-anchored inline text ("whole-home energy monitor"), button matches site convention.
**Rationale:** the article's core promise is *stop guessing* — the meter IS the promise, hardware form. Diagnosis-intent readers convert to measurement tools at the highest rate in this niche (they've already accepted "I need data").
**Additions:** "Best for" line under the box pair — *Kill A Watt: one suspect appliance, $25-ish. Vue 3: whole-home, needs panel access.* Pros/cons not needed at one-glance depth; the pair IS the comparison.

### 2. `06-water-bill-too-high` — 45 pv/wk, #3 traffic site-wide, water diagnosis

**Placement:** end of `## 3. Look for a Safe, Verifiable Explanation` (line ~49–54) — the section that tells readers to prove the leak before assuming one.
**Publish-ready copy:**

```markdown
Proof beats suspicion — and a $30 sensor catches what a monthly bill only hints at.
Place a couple near the water heater, under sinks, and behind the toilet: they alarm
on contact and tell your phone, so a slow leak becomes a same-day fix instead of a
next-quarter bill surprise.

{{< product-box asin="[GOVEE-VERIFY]" name="Govee Water Leak Detectors (5-pack)" label="Catch it while it's small" description="Contact sensors that alarm at 100 dB and send phone alerts when they touch water. Place under the water heater, behind the washing machine, and under sinks — the three places slow leaks hide longest." button="Check price on Amazon" >}}

If the bill is repeating and you want the leak found whether or not it's near a sensor,
a whole-home monitor on the main line sees every drop:

{{< amazon asin="B00C03D01Q" text="See the Moen Flo Smart Water Monitor & automatic shutoff on Amazon" >}} — monitors flow, pressure, and temperature 24/7, detects drops-per-minute leaks, and can shut the main itself (Moen 900-001 spec).
```

**Anchor/CTA:** "Catch it while it's small" — problem-language, not product-language. Inline anchor carries the two benefits that matter: *detection* + *shutoff*.
**Rationale:** section says "verifiable explanation"; sensors ARE verification hardware. The two-tier offer (cheap sensors / premium monitor) matches two reader states — first scare vs. repeat problem — without pressure.
**Additions:** short "Which do you need?" line — *sensors if you want cheap insurance in known spots; Flo if a leak already cost you money once.* **⚠️ Verify Govee ASIN before publish — do not ship unverified.**

### 3. `water-meter-running-when-no-water-used` — 33 pv/wk, urgent diagnosis

**Placement:** end of `## If It's Inside: Find the Culprit` (after the toilet/then-check subsections, ~line 62+) — reader has just localized the leak indoors.
**Publish-ready copy:** same two-box pattern as #2, but reversed order (reader KNOWS it's inside — the monitor finds WHERE):

```markdown
The 10-minute test above tells you *that* you have a leak. These tell you *where* —
continuously, including when you're not home to watch the meter.

{{< product-box asin="[GOVEE-VERIFY]" name="Govee Water Leak Detectors (5-pack)" label="Localize the leak" description="Contact sensors with loud alarms and phone alerts. Stagger them along the suspect path — water heater, under sinks, toilet bases, washing machine box — and the first one to trip is your culprit zone." button="Check price on Amazon" >}}
```

**Rationale:** highest-urgency water page (meter literally spinning). Readers here have emotionally committed to finding it TODAY — the sensor is the next physical step of the article's own test procedure.
**Additions:** one-line tie-back — *"Step 3 shut your main valve to prove house-vs-line; sensors do that proof continuously."*

### 4. `water-meter-leak-indicator-explained` — 24 pv/wk, monitoring mindset

**Placement:** end of `## How to isolate "house leak" vs "line leak"` (line ~81–94).
**Copy:** Moen Flo box (B00C03D01Q) + "Which do you need?" line. Angle: *"The leak indicator is a once-a-month check at the meter. This does it every minute of every day, and closes the valve when it finds one."*
**Rationale:** this page's reader has already internalized meter-based monitoring — the premium monitor is the same mental model, upgraded. Highest-probability premium water placement on the site.

### 5. `ev-charging-impact-electric-bill` — low traffic, high AOV, zero internal competition

**Placement:** end of `## Home Equipment and Safety` (line ~45–48).
**Publish-ready copy:**

```markdown
If the math says home charging is your plan, the equipment decision is simple: a
Level 2 charger turns a 12-hour trickle into a 3–4 hour fill, and a WiFi-enabled one
lets you schedule charging into the off-peak window your rate plan rewards.

{{< product-box asin="B09ZNN3JB7" name="Emporia Level 2 EV Charger (48 Amp, J1772)" label="Charge in the cheap window" description="48A/240V hardwired charger, up to 46 miles of range per hour, WiFi scheduling from the app — set it to start at your off-peak rate and the cheap hours do the work (Emporia spec sheet). Works with every J1772 EV; Tesla via adapter." button="Check price on Amazon" >}}

Want the charging cost separated from the rest of the house on your bill? The same
brand makes the circuit-level monitor we use elsewhere on this site:
{{< amazon asin="B0C7B1LKDW" text="Emporia Vue 3 energy monitor — see EV charging as its own line" >}}.
```

**Rationale:** EV-curious readers are planners — they read a bill-math article before buying hardware. Charger AOV (~$400+) at Home-category commission beats a dozen plug sales; the page has no competing placement and never will.
**Additions:** note pairing with the article's own rate-plan section — *charger scheduling only pays if a ToU plan exists; section above tells you if yours does.*

## TIER 2 — Next sweep

### 6. `05-how-to-lower-utility-bills` — 22 pv/wk, cross-utility action hub
**Placement:** end of `## Establish a Baseline` (line ~29–40). One box (Kill A Watt) + one inline (Vue 3). Copy angle: "You cannot lower what you don't measure — the baseline section's own first sentence." Restraint is the play here: the page is a prioritization guide, not a product page.

### 7. `single-stage-vs-two-stage-vs-variable-speed-hvac` — equipment deciders
**Placement:** end of `## Questions to Ask Before Buying` (line ~44+). ecobee box `B09XXS48P8` — the natural pairing: variable-speed equipment only performs with a thermostat that modulates it. Copy angle: *"A variable-speed air handler paired with a single-stage thermostat is a savings engine running in first gear."* Note: check ecobee's multi-stage/heat-pump support claims against the current spec sheet before publishing the description — cite ecobee's published compatibility, not assumptions.
**Additions:** mini comparison line — *ecobee Premium: smart sensors + air quality; Nest Learning: auto-schedule learning.* Both already site-verified ASINs — a rare two-brand comparison we can run honestly.

### 8. `is-your-toilet-running-leak-test` — dye-test page
**Placement:** after the dye-test instructions (body before `## Sources`, ~line 120s). Govee sensor box only. Angle: *"Dye finds today's leak; a sensor behind the tank finds the one that starts next year."* Flapper kits: natural fit but weak economics + fit/compatibility friction — **skip; not worth the reader's risk of ordering the wrong flapper.**

### 9. `why-did-my-water-bill-suddenly-increase` — repeat of water family
One Govee box at end of `## Sudden Bill Increase Causes` (line ~244+). Only if #2 ships first — avoid double-monetizing near-identical water pages before consolidation decisions (audit P2 merges the water cluster).

## NOT A FIT — deliberately unmonetized (trust calls)

| Page | Why no |
|---|---|
| `28-utility-reconnection-fee`, `26-deposit`, `21-past-due`, `can-utility-shut-off-service` | Crisis/poverty intent. Selling gadgets to a reader facing shutoff burns the brand for one commission. |
| `23-billing-cycle`, `how-sewer-charges-work`, `what-is-ccf`, `gas-customer-charge` | Definitional. No product answers the question; a box here is decoration. |
| `how-to-read-gas-meter`, `how-to-read-electric-meter` | Manual skill; tools add nothing. |
| `net-metering-explained` | Solar decisions close with installers, not Amazon carts. |
| `16-budget-billing`, `15/higher-same-usage` twins | Utility-program questions; product-neutral. |
| `why-is-my-furnace-blowing-cold-air`, HVAC symptom pages | Repair intent → service tech. Wrong product at the wrong moment. |

## EXISTING placements — improvements

- `30-spike` (1 box): add Kasa KP115 inline after the Kill A Watt box — *"the meter finds the thief; the smart plug executes the fix on a schedule."* Diagnosis→action pair lifts both CTRs.
- Flagship (4 boxes): **frozen until P0 sourcing lands** — adding traffic to 249 unsourced dollar figures is conversion in reverse.
- `07-gas` (1 box): correct as-is. 3.6k words + one relevant box = restraint that reads as honesty.

## Implementation priority (impact-ordered)

1. **03-electric-bill-high** — top-10 traffic, zero monetization, perfect tool-fit
2. **06-water-bill-too-high** — #3 traffic; verify Govee ASIN first
3. **water-meter-running** — urgency peak of the water journey
4. **water-meter-leak-indicator** — premium water conversion
5. **ev-charging** — highest AOV, build-and-forget
6. 30-spike companion link (2-minute edit)
7. 05-lower-utility-bills · 8. HVAC stages/ecobee · 9. toilet-dye page · 10. sudden-increase (post-consolidation)

*Estimated lift model (labeled assumption, replace with measured EPC after 2 weeks): Tier 1 adds ~150 pv/wk of monetized surface at info-page CTR 3–6% → 5–9 extra clicks/wk at product-page EPC, with the EV charger and Moen Flo as the AOV outliers that make the tail fat.*
