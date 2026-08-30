---
title: "CCF Calculator: Water Bill Units to Gallons + Dollars"
slug: "ccf-calculator"
description: "Enter your CCF usage and rate to convert water-bill units to gallons, calculate tiered cost, and find your household's gallons-per-person-day baseline."
date: 2026-08-28
updated: 2026-08-28
author: "Margaret Harrington"
category: "Water"
categories: ["Water"]
tags: ["water bill", "CCF", "calculator", "water rates"]
keywords: ["ccf calculator", "water bill calculator", "ccf to gallons", "water usage calculation"]
image: "/images/articles/ccf-calculator/ccf-conversion-chain.webp"
image_alt: "A CCF conversion chain showing one CCF becoming 748 gallons and then a water-use cost calculation."
og_image: "/images/social/og-ccf-calculator.webp"
sources:
  - https://www.epa.gov/watersense/understanding-your-water-bill (retrieved 2026-08-29)
  - https://www.epa.gov/watersense/how-watersense-calculator-works (retrieved 2026-08-29)
---

{{< affiliate-disclosure >}}

## Quick Answer

**One CCF (centum cubic feet) is 100 cubic feet — about 748 gallons.** Enter your bill's usage below to convert it, price it under a flat or tiered rate, and get the gallons-per-person-day baseline that makes period-to-period comparison possible.

<div id="ccf-calc" style="max-width:34rem;border:1px solid #e2e8f0;border-radius:.5rem;padding:1.25rem;background:#f8fafc;">
  <p style="margin-top:0;font-weight:600;">Your water bill numbers</p>
  <label style="display:block;margin:.5rem 0;">Usage (CCF): <input id="ccf-in" type="number" min="0" step="0.1" value="8" style="width:6rem;padding:.25rem;"> CCF</label>
  <label style="display:block;margin:.5rem 0;">Rate structure:
    <select id="tier-mode" style="padding:.25rem;">
      <option value="flat">Flat rate</option>
      <option value="tier">Two-tier rate</option>
    </select>
  </label>
  <div id="flat-row">
    <label style="display:block;margin:.5rem 0;">Rate per CCF: $<input id="rate-flat" type="number" min="0" step="0.01" value="4.10" style="width:6rem;padding:.25rem;"></label>
  </div>
  <div id="tier-rows" style="display:none;">
    <label style="display:block;margin:.5rem 0;">Tier 1: first <input id="tier1-ccf" type="number" min="0" step="1" value="6" style="width:5rem;padding:.25rem;"> CCF at $<input id="tier1-rate" type="number" min="0" step="0.01" value="3.60" style="width:5rem;padding:.25rem;"></label>
    <label style="display:block;margin:.5rem 0;">Tier 2: beyond that at $<input id="tier2-rate" type="number" min="0" step="0.01" value="5.20" style="width:5rem;padding:.25rem;"></label>
  </div>
  <label style="display:block;margin:.5rem 0;">People in the household: <input id="people" type="number" min="1" step="1" value="3" style="width:5rem;padding:.25rem;"></label>
  <label style="display:block;margin:.5rem 0;">Billing days: <input id="days" type="number" min="1" step="1" value="30" style="width:5rem;padding:.25rem;"></label>
  <button id="ccf-go" type="button" style="margin-top:.75rem;padding:.5rem 1rem;border:none;border-radius:.375rem;background:#b45309;color:#fff;font-weight:600;cursor:pointer;">Calculate</button>
  <div id="ccf-out" style="margin-top:1rem;padding:.75rem;border-radius:.375rem;background:#fff;border:1px solid #e2e8f0;font-size:.95rem;"></div>
</div>

<script>
(function () {
  var GAL_PER_CCF = 748; /* 100 cubic feet x 7.48052 gal/cu ft, EPA convention */
  function val(id) { return parseFloat(document.getElementById(id).value) || 0; }
  function money(x) { return "$" + x.toFixed(2); }
  function calc() {
    var ccf = val("ccf-in"), mode = document.getElementById("tier-mode").value;
    document.getElementById("flat-row").style.display = mode === "flat" ? "block" : "none";
    document.getElementById("tier-rows").style.display = mode === "tier" ? "block" : "none";
    var cost, breakdown = "";
    if (mode === "flat") {
      cost = ccf * val("rate-flat");
      breakdown = money(val("rate-flat")) + " x " + ccf.toFixed(1) + " CCF";
    } else {
      var t1 = val("tier1-ccf"), r1 = val("tier1-rate"), r2 = val("tier2-rate");
      var q1 = Math.min(ccf, t1), q2 = Math.max(ccf - t1, 0);
      cost = q1 * r1 + q2 * r2;
      if (q2 > 0) {
        breakdown = "Tier 1: " + q1.toFixed(1) + " CCF x " + money(r1) + " = " + money(q1 * r1) +
          "<br>Tier 2: " + q2.toFixed(1) + " CCF x " + money(r2) + " = " + money(q2 * r2);
      } else {
        breakdown = "All usage in Tier 1: " + q1.toFixed(1) + " CCF x " + money(r1);
      }
    }
    var gal = ccf * GAL_PER_CCF;
    var gpd = gal / Math.max(val("days"), 1);
    var gppd = gpd / Math.max(val("people"), 1);
    document.getElementById("ccf-out").innerHTML =
      "<strong>" + gal.toLocaleString() + " gallons</strong> this period (" + ccf.toFixed(1) + " CCF x 748)<br>" +
      "<strong>Usage cost: " + money(cost) + "</strong><br><span style='color:#64748b;'>" + breakdown + "</span><br>" +
      "<strong>" + gpd.toFixed(0) + " gal/day</strong> household — " +
      "<strong>" + gppd.toFixed(0) + " gal/person/day</strong> baseline";
  }
  document.getElementById("ccf-go").addEventListener("click", calc);
  document.getElementById("tier-mode").addEventListener("change", calc);
  calc();
})();
</script>

{{< visual src="/images/articles/ccf-calculator/tier-math-staircase.webp" alt="Two-tier water-rate staircase showing a lower first tier, a higher second tier, and the usage threshold between them." wide="true" >}}

## The Conversion, By Hand

No JavaScript? The math is three lines:

| Step | Example (8 CCF, flat $4.10/CCF, 3 people, 30 days) |
|---|---|
| Gallons: CCF × 748 | 8 × 748 = **5,984 gallons** |
| Cost: CCF × rate | 8 × $4.10 = **$32.80** (usage portion) |
| Baseline: gallons ÷ days ÷ people | 5,984 ÷ 30 ÷ 3 = **~66 gal/person/day** |

Utilities round the conversion differently — some bill in gallons, some in CCF, a few in cubic feet or 1,000-gallon units. EPA WaterSense notes that rate structures and units vary by utility, so confirm which unit your bill uses before comparing bills. [What is CCF on a water bill?](/blog/what-is-ccf-on-a-water-bill/) walks through reading the unit off a real statement.

## Why the Per-Person Baseline Matters More Than Any National Average

A single number from your own bill beats a generic target: it reflects your household size, your climate, your fixtures, and your irrigation. Track the gallons-per-person-day figure across similar seasons — a jump that survives a billing-length correction is the cheapest early warning that something changed, from a new roommate to a silent toilet leak. See [how to calculate water use per person](/blog/average-water-usage-per-person/) for the full method and its caveats.

Tiered rates make the cost line bend: if your utility charges more per CCF past a threshold, the calculator's tier mode shows how much of your bill sits in the expensive tier — and [how tiered water rates work](/blog/tiered-water-rates-explained/) explains why cutting the top tier is worth more than cutting the first.

## Catch the Leak Before It Bills

Usage-based math only sees a leak after the meter has run. If your baseline keeps climbing with no explanation, a whole-home monitor watches the flow continuously and can close the valve on its own — {{< amazon asin="B00C03D01Q" text="see the Moen Flo Smart Water Monitor & automatic shutoff on Amazon" >}} (monitors flow, pressure, and temperature; detects drops-per-minute leaks; Moen 900-001 spec). For a lower-cost first step, [check your water meter's leak indicator](/blog/water-meter-leak-indicator-explained/).

## Sources

1. [U.S. EPA WaterSense: Understanding Your Water Bill](https://www.epa.gov/watersense/understanding-your-water-bill)
2. [U.S. EPA WaterSense: How the WaterSense Calculator Works](https://www.epa.gov/watersense/how-watersense-calculator-works)
