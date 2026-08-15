#!/usr/bin/env python3
"""Utilityexplained affiliate expansion (2026-08-15).

Heater best-of page gets category-matched picks (mirrors its own table);
6 'why is my bill high / how to lower' pages get diagnostic + fix products.
All ASINs verified; reuses the site's curated family where possible.
Idempotent.
"""
import re

KILL = 'B00009MDBU'; KASA = 'B0D9B6MXGS'; GOVEE = 'B07QP153GT'
FLUME = 'B08DX6MP8X'; NEST = 'B0D5BBYRJM'; SIERRA = 'B001W2CEYA'

def box(asin, name, label, desc, btn="Check price on Amazon"):
    return ('{{< product-box asin="' + asin + '" name="' + name + '" label="' + label + '" description="' + desc + '" button="' + btn + '" >}}')

JOBS = {
    "content/blog/42-best-energy-efficient-space-heater.md": [
        box("B009P5BCNA", "Lasko 754200 Compact Ceramic Heater", "Home office pick (and the budget pick)",
            "The $25 answer for quick-session heat: 750W/1500W dual settings — the same 750W toggle this guide's math uses to halve heating cost. Small, quiet, and cheap enough to pay for itself in a single month of not touching the central thermostat."),
        box("B00G96S4Y8", "De'Longhi Dragon 4 Digital Oil-Filled Radiator", "Master bedroom pick",
            "Silent convection warmth that keeps radiating after the element cycles off — the oil-filled category this guide recommends for sleepers. Digital timer, no glowing element, no fan noise."),
        box("B002QZ11J6", "Dr Infrared Heater DR-968", "Drafty living room pick",
            "Heats people and furniture directly instead of the air — exactly the property that makes infrared the right call for drafty rooms. 5200 BTU dual-heating system covers spaces ceramic units can't."),
    ],
    "content/blog/03-why-is-my-electric-bill-so-high.md": [
        box(KILL, "P3 Kill A Watt P4400", "Find the culprit in an afternoon",
            "Plug in the fridge, the freezer, the entertainment center — this $30 meter shows each appliance's true monthly cost. Most 'mystery' high bills trace to one failing appliance; this finds it in an afternoon."),
    ],
    "content/blog/why-is-my-electric-bill-so-high-this-month.md": [
        box(KILL, "P3 Kill A Watt P4400", "The first diagnostic step",
            "Before assuming rate hikes, measure: a failing fridge compressor or ancient freezer can quietly add $30+/month. Plug-and-read — the fastest way to confirm whether usage or rates moved."),
    ],
    "content/blog/how-to-lower-electric-bill-without-solar.md": [
        box(KASA, "Kasa Matter Smart Plugs (2-pack, Energy Monitoring)", "Kill the phantom loads",
            "Standby drain from TVs, consoles, and chargers runs $50–150/year in typical homes. Schedule the entertainment center off overnight and watch per-device wattage in the app — the cheapest measurable win on this list."),
        box(KILL, "P3 Kill A Watt P4400", "Audit before you optimize",
            "Find which appliances actually deserve your attention before spending a dollar on fixes. One weekend, one meter, a ranked list of your home's real energy eaters."),
    ],
    "content/blog/44-how-to-lower-water-bill.md": [
        box(SIERRA, "High Sierra 1.5 GPM All-Metal Showerhead", "The fastest water-bill win",
            "A 2.5 GPM showerhead swapped for this 1.5 GPM WaterSense pick cuts ~1,800 gallons/year per daily showerer — with pressure that doesn't feel like a sacrifice. All-metal, no clogging nozzle."),
        box(GOVEE, "Govee Water Leak Detectors", "Stop silent leaks",
            "A running toilet can waste 6,000 gallons/month. $25 of sensors under sinks, behind toilets, and by the water heater catches leaks before they become line items."),
    ],
    "content/blog/06-water-bill-too-high.md": [
        box(GOVEE, "Govee Water Leak Detectors", "Localize the leak first",
            "High bill with no visible water? Place sensors at the usual suspects — toilet bases, under sinks, by the water heater and washer — and let the 100dB alarms point you to it."),
        box(FLUME, "Flume 2 Smart Water Monitor", "Watch usage in real time",
            "Straps onto your existing meter — no plumber. Hourly usage, leak alerts, and the data to prove whether your bill matches reality or the meter is wrong."),
    ],
    "content/blog/07-gas-bill-too-high.md": [
        box(NEST, "Google Nest Learning Thermostat (4th gen)", "The heating-bill autopilot",
            "Programs itself in a week — no schedule-building, which is where most programmable thermostats fail. Google's measured savings: ~12% on heating, ~15% on cooling. The single highest-impact device for gas heating bills."),
    ],
}

ANCHORS = ["## Related", "## Frequently Asked", "## FAQ", "## Conclusion", "## What to do next", "## Next steps"]
BOX_RE = re.compile(r"\{\{<\s*product-box", re.S)

changed, skipped = [], []
for path, boxes in JOBS.items():
    src = open(path).read()
    if BOX_RE.search(src):
        skipped.append(path); continue
    idx = min((i for i in (src.rfind(a) for a in ANCHORS) if i != -1), default=-1)
    if idx == -1:
        skipped.append(path + " (no anchor)"); continue
    src = src[:idx] + "\n\n".join(boxes) + "\n\n" + src[idx:]
    if "{{< affiliate-disclosure >}}" not in src:
        m = re.search(r"\A(?:\+\+\+.*?\+\+\+|---.*?---)\s*\n", src, re.S)
        if m:
            src = src[:m.end()] + "\n{{< affiliate-disclosure >}}\n" + src[m.end():]
    open(path, "w").write(src)
    changed.append(path)

print(f"changed={len(changed)} skipped={len(skipped)}")
for s in skipped: print("  SKIP " + s)
