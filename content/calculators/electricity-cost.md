---
title: "Electricity Cost Calculator: What Any Appliance Costs to Run"
description: "Calculate what any appliance costs per hour, day, and month. Enter watts and your rate — the math and the national average are both built in."
date: 2026-10-05
draft: false
layout: calculator
sources:
  - "U.S. Energy Information Administration, Electric Power Monthly Table 5.6.A (July 2026 data, released 2026-09-24)"
---


<p class="data-freshness" style="font-size:.85rem;color:#666;">Data through {{< stat "electric_rate_jul2026" "date" >}} · Source: U.S. EIA · Last refreshed October 2026</p>
<div class="calc-shell">
  <h2>Appliance electricity cost calculator</h2>
  <p class="calc-intro">Enter the appliance's wattage (check the label or manual), how many hours a day it runs, and your rate from your bill. Don't know your rate? The national average is pre-filled.</p>
  <div class="calc-grid">
    <label>Appliance wattage (W)
      <input id="calc-watts" type="number" inputmode="decimal" value="1500" min="1" max="15000">
    </label>
    <label>Hours used per day
      <input id="calc-hours" type="number" inputmode="decimal" value="3" min="0" max="24" step="0.5">
    </label>
    <label>Your rate ($ per kWh)
      <input id="calc-rate" type="number" inputmode="decimal" value="0.1831" min="0.01" max="2" step="0.001">
      <span class="calc-hint">U.S. residential average (EIA, {{< stat "electric_rate_jul2026" "date" >}}): {{< stat "electric_rate_jul2026" >}}. Find yours: total electric charges ÷ total kWh on your bill.</span>
    </label>
  </div>
  <button id="calc-go" class="calc-btn">Calculate cost</button>
  <div id="calc-out" class="calc-out" aria-live="polite"></div>
</div>

<script>
(function(){
  var W = document.getElementById('calc-watts'), H = document.getElementById('calc-hours'),
      R = document.getElementById('calc-rate'), GO = document.getElementById('calc-go'),
      OUT = document.getElementById('calc-out');
  function fmt(n){ return '$' + n.toFixed(2).replace(/\.00$/,''); }
  function calc(){
    var w = parseFloat(W.value)||0, h = parseFloat(H.value)||0, r = parseFloat(R.value)||0;
    if (w<=0||h<0||r<=0){ OUT.innerHTML = '<p class="calc-err">Enter wattage, hours, and a rate above zero.</p>'; return; }
    var kwhDay = (w*h)/1000, costDay = kwhDay*r, costMonth = costDay*30.44, costYear = costDay*365;
    OUT.innerHTML =
      '<p class="calc-verdict"><strong>' + fmt(costMonth) + ' per month</strong> (' + fmt(costDay) + '/day, ' + fmt(costYear) + '/year)</p>' +
      '<p class="calc-detail">That is ' + kwhDay.toFixed(2) + ' kWh/day — ' + (kwhDay*30.44).toFixed(0) + ' kWh/month at ' + r.toFixed(3) + ' $/kWh.</p>' +
      '<p class="calc-detail">For context: the average U.S. home uses about {{< stat "avg_monthly_kwh" "raw" >}} kWh a month (EIA).</p>';
  }
  GO.addEventListener('click', calc);
  [W,H,R].forEach(function(el){ el.addEventListener('keydown', function(e){ if(e.key==='Enter') calc(); }); });
  calc();
})();
</script>
