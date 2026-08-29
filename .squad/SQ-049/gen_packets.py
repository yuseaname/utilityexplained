#!/usr/bin/env python3
"""SQ-049 depth wave: 7 traffic-weak + 5 thin money pages (12 files, 3 seats)."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "SQ-049 depth wave: top traffic-weak pages + thin money pages to full strength."
BASE = f"{REPO}/.squad/SQ-046/data-baseline.md"
FACTS = [
    "Verified products/ASINs: Nest B0D5BBYRJM, Kill A Watt B00009MDBU, Kasa KP115 B08LN3C7WK, Kasa KP125MP2 B0BYGRLRS1, Tapo P110M B0DKGBP38V, Emporia plug B0CLVV7X7Y, Vue 3 B0C7B1LKDW, Govee B0DQLFC3Q6, Moen Flo B00C03D01Q, ecobee B09XXS48P8, Emporia charger B09ZNN3JB7.",
    "These pages already carry product boxes where noted — deepen the CONTENT around them; do not add more links unless a section genuinely begs for one. Disclosure shortcodes already in place.",
    "House voice: plain-English, tables over prose, no hype, no fabricated testing. Sources: baseline first, else web_fetch with URL+date.",
]

def packet(role, mission, extra, writes, criteria):
    return {
        "role": role, "mission": mission, "parent_objective": PARENT,
        "context": extra, "known_facts": FACTS,
        "resources": {"roots": [REPO], "write_paths": writes, "notes": f"Data baseline: {BASE}"},
        "constraints": [
            "Depth = tables, worked examples, ranges, named utilities/programs — not padded prose. 800+ body words per page when done.",
            "Every new factual claim sourced; frontmatter 'updated: 2026-08-28'; house markdown style.",
            "Chunk discipline: file by file, save after each.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch", "write_file", "edit_file"],
        "success_criteria": criteria,
    }

packets = {}

packets["mason"] = packet("mason",
    "FOUR FILES. (1) content/blog/28-utility-reconnection-fee-explained.md (483w, 34 pv/wk, #4 traffic — the site's most underweight high-traffic page): add what triggers disconnection by utility type, a typical-fee table with state/range examples (web-verify a few real utilities' fee schedules, cite), the restoration process step-by-step, and how to avoid the fee (payment arrangements, protection programs, LIHEAP mention). NO affiliate links (crisis intent). (2) content/blog/23-utility-billing-cycle-explained.md (512w): add why cycle lengths vary (meter-read schedules, weekend/holiday shifts), the long-vs-short-month bill math with a worked example, estimated-vs-actual read interaction, and how to check your cycle dates. (3) content/blog/how-sewer-charges-work-on-your-water-bill.md (523w, 1 source): add the three billing models (metered water-based / flat / ERU), a worked example each, winter averaging explained, and 2-3 cited utility examples (web_fetch real utility sewer-rate pages). (4) content/blog/44-how-to-lower-water-bill.md — TRANSFORMATION: today it is investigation content under a 'lower water bill' slug. Rebuild it as the genuine 'How to Lower Your Water Bill' ACTION page the site lacks: ranked actions by cost (free behaviors -> cheap fixes -> upgrades: leak repairs, Toilet flapper, low-flow fixtures WaterSense, efficient irrigation, full-load habits), savings ranges per action cited from EPA WaterSense pages (web_fetch, cite), a payback table, and ONE Govee sensor product-box (B0DQLFC3Q6, verified) in the catch-silent-leaks section. Diagnose-first readers: link to 06-water-bill-too-high and the CCF calculator at top. This page fills the audit's #1 journey gap — make it the definitive answer to 'how to lower your water bill'.",
    "28 is crisis-intent: help the reader avoid/resolve the fee; sell nothing. 44 is the opposite: pure action page, one product max.",
    ["content/blog/28-utility-reconnection-fee-explained.md", "content/blog/23-utility-billing-cycle-explained.md",
     "content/blog/how-sewer-charges-work-on-your-water-bill.md", "content/blog/44-how-to-lower-water-bill.md"],
    ["4 pages at 800+ words with cited tables/examples; 28 stays link-free; 44 delivers true lower-water-bill intent with one Govee box."])

packets["tracer"] = packet("tracer",
    "THREE DEFINITIONAL PAGES. (1) content/blog/11-understanding-kwh-usage.md (425w): add the appliance consumption table (top 10 household loads, typical kWh/yr — EIA RECS or DOE figures, verify + cite), the cost equation worked on the current national rate (baseline: 18.34 c/kWh mid-2026), what moves a bill more (rate vs usage), and a short reading-your-meter-to-kWh bridge (link how-to-read-electric-meter). One natural link: Kill A Watt inline (B00009MDBU) in a 'measure your own appliances' section. (2) content/blog/12-how-to-read-your-gas-bill.md (391w, 1 source): add a full line-item walkthrough table (customer charge, delivery, supply/therms, riders, taxes — synthesize from the site's own gas pages, cite their sources), the therm/CCF conversion worked example, and seasonal-usage context with a real EIA natural-gas price figure (verify + cite). No affiliate fit (definitional) — none. (3) content/blog/46-what-time-is-electricity-cheapest.md (352w): anchor it to real ToU windows (PG&E/ConEd/TXU schedules already fetched and cited on 08-time-of-use — reuse those cited figures, read that page first), add the cheapest-hours table by plan type, off-peak habit list, and ONE Kasa KP115 inline link (B08LN3C7WK) for automating the shift. Cross-link 08 and the rate-plan hub.",
    "46 must not duplicate 08's deep dive — 46 is the quick answer + hours table, 08 is the explainer. Link them, don't copy.",
    ["content/blog/11-understanding-kwh-usage.md", "content/blog/12-how-to-read-your-gas-bill.md",
     "content/blog/46-what-time-is-electricity-cheapest.md"],
    ["3 pages at 800+ words, cited; exactly one inline link each on 11 and 46; 12 stays link-free."])

packets["operator"] = packet("operator",
    "FIVE THIN MONEY PAGES — deepen the content AROUND the existing product boxes; add NO new boxes unless explicitly specified. (1) content/blog/gadgets-that-lower-utility-bills.md (342w, weakest money page): expand each gadget category with what-it-does / typical-cost-range / who-it's-for / realistic savings basis (manufacturer/DOE published only), a gadgets comparison table, and honest 'when it does NOT pay' notes — the boxes stay where they are. Target 900+. (2) content/blog/phantom-power-draw-explained.md (360w): add the standby-load table by device class (DOE/IEA standby-power figures — verify + cite), the measurement walkthrough, total-typical-home math, and the automate-it section around the existing boxes. (3) content/blog/single-stage-vs-two-stage-vs-variable-speed-hvac.md (414w): add comfort/humidity/dehumidification differences, a runtime-behavior comparison, compatibility-with-thermostats section (the ecobee box already there), and a 'which stage for which climate/home' decision table. (4) content/blog/50-best-smart-plugs-standby-power.md (444w): add the measurement-first workflow (meter -> plug -> automation), a smart-plug-features comparison table (monitoring, Matter, hub-free — spec-based, cite product pages), safety notes (15A limits for high-draw appliances), and 'what a plug can't fix'. Keep both existing boxes. (5) content/blog/ev-charging-impact-electric-bill.md (496w): add the level-1-vs-level-2 comparison table, real cost-per-mile math on current rates (baseline + one real ToU off-peak price from 08's cited schedules), battery-size-to-bill examples (3 common EV sizes), and the plan-check list around the existing charger box.",
    "Every table spec-cited. Savings claims only from manufacturer/DOE/ENERGY STAR published figures. The boxes anchor the pages — content earns them.",
    ["content/blog/gadgets-that-lower-utility-bills.md", "content/blog/phantom-power-draw-explained.md",
     "content/blog/single-stage-vs-two-stage-vs-variable-speed-hvac.md", "content/blog/50-best-smart-plugs-standby-power.md",
     "content/blog/ev-charging-impact-electric-bill.md"],
    ["5 money pages at 800+ (gadgets 900+) with cited comparison tables; no new boxes; every spec claim attributable."])

out = Path(f"{REPO}/.squad/SQ-049/packets"); out.mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1)); print(f"wrote {name}.json")
