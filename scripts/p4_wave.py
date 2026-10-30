import re, pathlib

B = pathlib.Path(__file__).resolve().parent.parent / "content" / "blog"

def h2s(txt):
    return [m.group(1) for m in re.finditer(r"^## (.+?)\s*(\{#[a-z0-9-]+\})?\s*$", txt, flags=re.M)]

def slug_id(h):
    h = re.sub(r"\{#[^}]+\}", "", h)
    s = h.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())

def edit(fname, ops):
    p = B / fname
    txt = p.read_text(encoding="utf-8")
    log = []
    for op in ops:
        if op[0] == "sub":
            old, new = op[1], op[2]
            if new in txt and old not in txt:
                log.append("skip"); continue
            assert old in txt, f"{fname}: MISS {old[:60]}"
            txt = txt.replace(old, new, 1); log.append("ok")
        elif op[0] == "jump":
            links = " ".join('"%s|#%s"' % (lab, slug_id(h)) for lab, h in op[1])
            jr = '{{< jump-row ' + links + ' >}}\n\n'
            d = txt.find("{{< affiliate-disclosure >}}")
            if "jump-row" in txt:
                log.append("jump-skip"); continue
            if d > 0:
                txt = txt[:d] + jr + txt[d:]
            else:
                hs = h2s(txt)
                m2 = re.search(r"^## " + re.escape(hs[1]) + r".*$", txt, flags=re.M)
                if not m2:
                    log.append("jump-fail"); continue
                txt = txt[:m2.start()] + jr + txt[m2.start():]
            log.append("jump")
        elif op[0] == "bump":
            txt = re.sub(r"^updated: ['\"]?\d{4}-\d{2}-\d{2}", "updated: 2026-10-30", txt, count=1, flags=re.M)
            log.append("bump")
    p.write_text(txt, encoding="utf-8")
    print(fname + ": " + ",".join(log))

R5 = "[Texas](/blog/average-utility-bills-in-texas/), [Florida](/blog/average-utility-bills-in-florida/), [California](/blog/average-utility-bills-in-california/), [New York](/blog/average-utility-bills-in-new-york/), and [Pennsylvania](/blog/average-utility-bills-in-pennsylvania/)"

FAQ = {}

FAQ["11-understanding-kwh-usage"] = '''## Frequently asked questions {#faq}

{{< faq "What is a kWh in plain terms?">}}

A kilowatt-hour is the energy a 1,000-watt appliance uses while running for one hour — a 100-watt bulb lit for ten hours, or a space heater on high for one. It is the unit your meter counts and your bill prices, which is why every cost question about electricity eventually reduces to kWh × your rate.

{{< /faq >}}

{{< faq "What does one kWh cost?">}}

Nationally, the 2026 residential average is about 18¢/kWh (EIA) — but the state spread is wide, from roughly 15¢ in Florida to nearly 30¢ in California. The same kWh can cost twice as much in one state as another, so your own bill's rate line is the only number that matters for your math. The [state-by-state guide](/blog/average-utility-bills-by-state-2026/) shows where yours sits.

{{< /faq >}}

{{< faq "How many kWh does a house use per day?">}}

The national household average is about 899 kWh a month — roughly 30 kWh a day — but the real spread runs from single digits in small apartments to 60+ in large homes with electric heat. Usage, not rate, is what moves most bills month to month; [how many kWh a house uses per day](/blog/how-many-kwh-does-a-house-use-per-day/) breaks down the drivers.

{{< /faq >}}

## Sources'''

FAQ["where-to-place-water-leak-sensors"] = '''## Frequently asked questions {#faq}

{{< faq "Where should water leak sensors be placed?">}}

By consequence, not convenience: under the water heater first (failure there is sudden and large), then behind the washing machine, under sinks with supply lines, behind the toilet, near the dishwasher, and at the sump or main line if you have one. The six placements in this guide are ranked by how much damage each location prevents, not by how easy it is to reach.

{{< /faq >}}

{{< faq "How many water sensors does a house need?">}}

A five-pack covers the standard risk points: water heater, washer, kitchen sink, bathroom(s), and one spare for the dishwasher or refrigerator line. The coverage section maps a five-pack room by room — more sensors help, but the first five capture most of the risk.

{{< /faq >}}

{{< faq "Do I need one under every sink?">}}

No — prioritize by what fails catastrophically. A slow under-sink drip is a towel problem; a burst washing-machine hose or water-heater tank is a claim. Cover the big-failure sources first, then add sinks with the leftover units.

{{< /faq >}}

## Sources'''

FAQ["best-dual-flush-conversion-kits"] = '''## Frequently asked questions {#faq}

{{< faq "Do dual-flush conversion kits actually save water?">}}

On an older toilet they can: the conversion turns a 3.5-gallon full flush into a dual 1.6/0.8 system, and the per-year math in this guide works the savings from your actual flush mix. On a toilet already at 1.6 GPF the savings shrink to the difference between 1.6 and the half-flush — real, but modest.

{{< /faq >}}

{{< faq "Will a conversion kit fit my toilet?">}}

Only if it passes the compatibility checklist: a standard two-piece tank, a 2-inch flush valve (most kits), and a fill valve the kit can clear. One-piece, pressure-assisted, and some 3-inch-valve toilets are the common no-go cases — the checklist catches them in about a minute.

{{< /faq >}}

{{< faq "Is converting better than replacing the toilet?">}}

Converting is the cheap, renter-friendly move when the toilet is compatible and works fine otherwise; replacing wins when the toilet is old enough that the flapper, fill valve, and flush valve are all on borrowed life anyway. The head-to-head section runs both paths against a single criterion: cost per gallon actually saved.

{{< /faq >}}

## Sources'''

FAQ["furnace-tune-up-cost-schedule"] = '''## Frequently asked questions {#faq}

{{< faq "How often should a furnace be tuned up?">}}

Once a year, before the heating season starts — the schedule this guide builds. Annual service keeps efficiency at spec and catches wear while it is still a part, not a no-heat emergency in January.

{{< /faq >}}

{{< faq "What does a furnace tune-up include?">}}

Burner and heat-exchanger inspection, combustion and safety checks, blower and venting verification, and the filter swap — the full list is in the what's-included section. Anything beyond that list is where the upsell section tells you to slow down.

{{< /faq >}}

{{< faq "Can I skip the tune-up and just replace the filter?">}}

The filter is the highest-leverage DIY item, but it does not replace the safety inspections — combustion and heat-exchanger checks are the part that protects you, not just the bill. Filter yourself, and put the inspection on an annual clock; the maintenance-vs-repair section draws the line.

{{< /faq >}}

## Sources'''

FAQ["stormwater-fee-explained"] = '''## Frequently asked questions {#faq}

{{< faq "What is a stormwater fee?">}}

A charge that funds the drainage system that handles rain runoff — storm sewers, detention, and pollution control. It appears on the water bill in many cities and on the property-tax bill in others; the three billing models section shows how your city likely does it.

{{< /faq >}}

{{< faq "Can I get my stormwater fee reduced?">}}

Sometimes: many cities run credit programs for permeable surfaces, rain barrels, or on-site detention that reduce the runoff your property sends to the system. The credits section lists what typically qualifies — reductions are usually percentage discounts, not waivers.

{{< /faq >}}

{{< faq "Do renters pay the stormwater fee?">}}

If the city bills it through the water bill and the lease puts utilities in the tenant's name, yes — the renters-vs-owners section breaks down who actually sees the line item and who pays it through rent.

{{< /faq >}}

## Sources'''

FAQ["how-sewer-charges-work-on-your-water-bill"] = '''## Frequently asked questions {#faq}

{{< faq "Why is my sewer charge higher than my water charge?">}}

Because sewer service is priced on the treatment side — the system has to build and run collection plus treatment, and in many cities those costs exceed the fresh-water side. The three billing models section shows how your city computes it: water usage, winter average, or a flat rate.

{{< /faq >}}

{{< faq "What is winter averaging for sewer bills?">}}

A method cities use so you are not billed sewer treatment for summer irrigation water that never enters the sewer: your sewer charge is set from your water usage during winter months, when essentially all household water goes down the drain. The winter-averaging section shows how the window is chosen and how it can work for or against you.

{{< /faq >}}

{{< faq "Can I lower my sewer charge?">}}

Only through the mechanism your city uses: if it is winter-averaged, keeping winter usage down locks in a lower year-round sewer charge; if it is usage-based, indoor conservation carries over directly. The questions-to-ask section gets you the answer from the utility in one call.

{{< /faq >}}

## Sources'''

# ---------- FAQ pages ----------
edit("11-understanding-kwh-usage.md", [
    ("bump",),
    ("jump", [("The definition","The Definition, in One Table"),("Top household loads","Top Household Loads: Typical Annual kWh"),("The cost equation","The Cost Equation: What 18.34¢/kWh Means for Your Bill"),("Measure your own","Measure Your Own Appliances")]),
    ("sub", "## What Moves Your Bill More: Rate or Usage?",
     "That national figure is an average, not a quote: residential rates in 2026 run from 14.99¢/kWh in Florida to 29.75¢/kWh in California, against the 18.16¢ national mean. The [state-by-state table](/blog/average-utility-bills-by-state-2026/) has the full spread, with detail pages for " + R5 + ". And to turn any rate into a dollar figure for your own appliances, the [electricity cost calculator](/calculators/electricity-cost/) does the watts × hours × rate math for you.\n\n## What Moves Your Bill More: Rate or Usage?"),
    ("sub", "## Sources", FAQ["11-understanding-kwh-usage"]),
])
edit("where-to-place-water-leak-sensors.md", [
    ("bump",),
    ("jump", [("The rule","The Rule Behind Every Placement"),("Six placements","The Six Placements, Ranked by Consequence"),("Wasted placements","The Two Placements That Waste a Sensor"),("Five-pack coverage","What a Five-Pack Actually Covers")]),
    ("sub", "## Sources", FAQ["where-to-place-water-leak-sensors"]),
])
edit("best-dual-flush-conversion-kits.md", [
    ("bump",),
    ("jump", [("What it is","First, What a Dual-Flush Conversion Kit Actually Is"),("Compatibility","The Compatibility Checklist: Will It Fit Your Toilet?"),("The pick","The Danco HydroRight HYR460 — the Pick"),("The math","The Math: 3.5 GPF Down to 1.6 / 0.8, Per Year")]),
    ("sub", "## Sources", FAQ["best-dual-flush-conversion-kits"]),
])
edit("furnace-tune-up-cost-schedule.md", [
    ("bump",),
    ("jump", [("What's included","What a Furnace Tune-Up Actually Includes"),("Fuel differences","Gas vs. Oil vs. Electric: Cost Differences"),("Plan worth it?","Is a Maintenance Plan Worth It?"),("The upsell","One Caution: Watch for the Upsell")]),
    ("sub", "## Maintenance vs. Repair: Knowing the Difference",
     'The one piece of a "tune-up" that is genuinely DIY is the filter swap — and it is the piece that most affects your gas bill all winter: a clogged filter makes the furnace run longer for the same heat, every cycle.\n\n{{< product-box asin="B0DKZCJYXP" name="Filtrete 20x25x1 MERV 8 Furnace Filters (6-pack)" label="The DIY half of the tune-up" description="A heating season of standard MERV 8 filters for a fraction of one service call. Check the size printed on your current filter\'s frame — this listing is 20x25x1 and carries other sizes. Everything else in a tune-up is technician work; the filter is yours." button="Check price on Amazon" >}}\n\n## Maintenance vs. Repair: Knowing the Difference'),
    ("sub", "## Sources", FAQ["furnace-tune-up-cost-schedule"]),
])
edit("stormwater-fee-explained.md", [
    ("bump",),
    ("jump", [("What it pays for","What a Stormwater Fee Pays For"),("How cities bill it","The Three Ways Cities Bill Stormwater"),("Reduce it?","Can You Reduce It? Credits, Rain Barrels, and Permeable Surfaces"),("Renters vs owners","Renters vs. Owners: Who Pays?")]),
    ("sub", "## Sources", FAQ["stormwater-fee-explained"]),
])
edit("how-sewer-charges-work-on-your-water-bill.md", [
    ("bump",),
    ("jump", [("Three billing models","The Three Sewer Billing Models"),("Winter averaging","Winter Averaging Explained"),("Real examples","Real Utility Examples"),("Questions to ask","Questions to Ask the Utility")]),
    ("sub", "## Sources", FAQ["how-sewer-charges-work-on-your-water-bill"]),
])

# ---------- jump-only pages ----------
edit("smart-plug-energy-monitoring-which-measures-usage.md", [
    ("bump",),
    ("jump", [("What monitoring means",'What "Energy Monitoring" Means on a Spec Sheet'),("The comparison","The Comparison: Which Plugs Actually Meter"),("Which fits you","Which One Fits Your Setup"),("Window AC","The Window AC Question, Answered Honestly")]),
])
edit("23-utility-billing-cycle-explained.md", [
    ("bump",),
    ("jump", [("Why lengths vary","Why Cycle Lengths Vary"),("The bill math","The Long-vs-Short-Month Bill Math"),("Estimates & true-ups","Estimated-vs-Actual Read Interaction"),("Check your dates","How to Check Your Cycle Dates")]),
])
edit("complete-guide-understanding-utility-bill.md", [
    ("jump", [("Read order","Read the statement in this order"),("National average","The national average, in context"),("The 5-step workflow","The 5-step workflow to understand any utility bill"),("Where charges are explained","Where each charge is explained")]),
])
edit("sense-energy-monitor-discontinued-alternatives.md", [
    ("jump", [("What happened","What Actually Happened"),("If you own one","If You Own a Sense: Keep It, With Two Caveats"),("The alternatives","If You Were About to Buy One: The Alternatives, by Budget"),("The money math","Does Any of This Change the Money Math?")]),
])
edit("01-how-to-read-your-electric-bill.md", [
    ("jump", [("Find these first","Find These Items First"),("What a kWh means","What a kWh Means"),("The charges","Understand the Charges on Your Statement"),("Effective rate","Calculate a Bill-Wide Effective Rate")]),
])
edit("18-fuel-adjustment-charge-on-utility-bill-explained.md", [
    ("bump",),
    ("jump", [("Identify the charge","Identify the Exact Charge"),("How it works","How the Clause Works"),("Compare bills","Compare Bills Before Drawing a Conclusion"),("What it is not","What a Fuel Adjustment Is Not")]),
    ("sub", "## What a Fuel Adjustment Is Not",
     "For scale when you compare: fuel-adjusted rates ride on top of a base rate that itself varies enormously by state — 14.99¢/kWh in Florida to 29.75¢/kWh in California in 2026. The [state-by-state table](/blog/average-utility-bills-by-state-2026/) gives the baseline, with detail pages for " + R5 + ", so you can tell a normal fuel-adjustment bump from a base-rate problem.\n\n## What a Fuel Adjustment Is Not"),
])
edit("28-utility-reconnection-fee-explained.md", [
    ("jump", [("Triggers","What Triggers Disconnection by Utility Type"),("Fee table","Typical Reconnection Fee Table by State and Utility"),("Terms in writing","Get the Restoration Terms in Writing"),("Avoid the fee","How to Avoid the Reconnection Fee")]),
])
edit("ccf-calculator.md", [
    ("jump", [("The conversion","The Conversion, By Hand"),("Per-person baseline","Why the Per-Person Baseline Matters More Than Any National Average"),("Catch the leak","Catch the Leak Before It Bills")]),
])
edit("emporia-vue-3-vs-sense-comparison.md", [
    ("jump", [("What each does","What Each Device Actually Does"),("Side by side","Side-by-Side Comparison"),("Install","Install: Both Need Panel Work"),("Which fits","Which One Fits Your Question")]),
])
edit("how-do-smart-meters-work.md", [
    ("jump", [("Smart vs analog","How smart meters are different from analog meters"),("How they measure","How smart meters measure and transmit usage"),("Accuracy","Are smart meters accurate?"),("Privacy","Privacy concerns (what utilities can and cannot see)")]),
])
edit("how-to-read-gas-meter.md", [
    ("bump",),
    ("jump", [("Why read it","Why Read Your Own Gas Meter"),("Meter types","Identify Your Meter Type"),("Dial meters","Read a Dial Gas Meter, Step by Step"),("CCF & therms","CCF, Therms, and the Conversion Factor")]),
    ("sub", "## Sources",
     "## Related Reading\n\n- [Why is my gas bill so high? 11 causes and fixes](/blog/07-gas-bill-too-high/) — what to do with the reading once you have it\n- [Average utility bills by state (2026)](/blog/average-utility-bills-by-state-2026/) — what gas actually costs where you live\n\n## Sources"),
])
edit("how-utility-rates-fees-usage-work-together.md", [
    ("bump",),
    ("jump", [("Layers","Think in layers: usage times rate, plus fixed charges"),("Rates","Rates: the price per unit (and why it changes)"),("Fees","Fees: the parts that do not depend on usage"),("The ripple","How one change ripples through the total")]),
    ("sub", "## How one change ripples through the total {#ripple}",
     "One concrete anchor for the rate layer: residential electric rates in 2026 run 14.99¢/kWh (Florida) to 29.75¢/kWh (California) against an 18.16¢ national average — the [state-by-state table](/blog/average-utility-bills-by-state-2026/) shows the spread, with detail pages for " + R5 + ".\n\n## How one change ripples through the total {#ripple}"),
])
edit("moving-utilities-checklist.md", [
    ("bump",),
    ("jump", [("The timeline","The Timeline: 4 Weeks Out → Moving Day"),("Turn-off vs transfer","Turn-Off vs. Transfer: Which Applies to You"),("Deposits & fees","Deposits, Connection Fees, and How to Avoid Paying Twice"),("The final bill","The Final Bill: Catching Old-Home Charges")]),
])
edit("water-bill-leak-adjustment-how-to-get-credit.md", [
    ("jump", [("What the policy says","What a leak-adjustment policy actually says"),("The math","The math: how the credit is sized"),("Evidence checklist","The evidence checklist (collect before you write)"),("If the answer is no","If the answer is no")]),
])
edit("water-meter-box-full-of-water.md", [
    ("jump", [("The 2-minute diagnostic","The 2-minute diagnostic: rain, refill, or leak"),("Why boxes collect water","Why meter boxes collect water even without a leak"),("The two leak cases","The two leak cases — and who owns each"),("The urgency ladder",'"Who do I call tonight?" — the urgency ladder')]),
])
edit("what-temperature-thermostat-winter.md", [
    ("jump", [("The two numbers","The Two Numbers That Matter"),("Why setback saves",'Why the Setback Saves (It\'s Not "Reheat Eats the Savings")'),("Heat pump exception","The Exception That Pays for a Smart Thermostat: Heat Pumps"),("The settings table","The Full Settings Table")]),
])
edit("water-meter-leak-indicator-explained.md", [
    ("jump", [("The 60-second test","The 60-second test: how to check the leak indicator"),("Why your bill jumped","Why your bill jumped (and how the leak indicator proves it)"),("What it is","What the leak indicator actually is"),("False alarms","Common false alarms (things that sip water)")]),
])
edit("what-is-ccf-on-a-water-bill.md", [
    ("jump", [("What CCF means","What does CCF mean on a water bill?"),("CCF vs gallons","CCF vs cubic feet vs gallons (and why bills use different units)"),("Quick conversions","Quick conversions you can memorize"),("Is your CCF normal?","Is your CCF normal? A 30-second check")]),
    ("sub", "## Sources",
     "## Related Reading\n\n- [CCF calculator: convert your bill to gallons](/blog/ccf-calculator/) — the arithmetic, done for you\n- [Water meter leak indicator explained](/blog/water-meter-leak-indicator-explained/) — the meter's built-in leak detector\n- [How to read a water meter](/blog/how-to-read-a-water-meter/) — the full meter walkthrough\n\n## Sources"),
])

# ---------- state pages: calculator links + new-york anchor fix ----------
for st in ["texas","florida","california","new-york","pennsylvania"]:
    edit(f"average-utility-bills-in-{st}.md", [
        ("sub", "For the ranked fix list — free first, then cheap, then big-ticket — start at [how to lower your electric bill: the complete guide](/blog/how-to-lower-electric-bill-complete-guide/).",
         "To turn your own numbers into a dollar figure, the [electricity cost calculator](/calculators/electricity-cost/) does the watts × hours × rate math with your rate pre-filled or your own. For the ranked fix list — free first, then cheap, then big-ticket — start at [how to lower your electric bill: the complete guide](/blog/how-to-lower-electric-bill-complete-guide/)."),
    ])

p = B / "average-utility-bills-in-new-york.md"
txt = p.read_text(encoding="utf-8")
txt = txt.replace("{#water-and-sewer-in-new york}", "{#water-and-sewer-in-new-york}")
txt = txt.replace("#water-and-sewer-in-new york", "#water-and-sewer-in-new-york")
p.write_text(txt, encoding="utf-8")
print("new-york anchor space fixed")

print("WAVE COMPLETE")
