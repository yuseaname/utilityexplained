#!/usr/bin/env python3
"""SQ-047 depth-pass packets: thin-content enhancement + natural affiliate wiring."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "SQ-047 depth pass: enhance thin/weak pages per audit prescriptions, weave natural affiliate links where the prescription calls for them."
BASE = f"{REPO}/.squad/SQ-046/data-baseline.md"
FACTS = [
    "Monetization state: 23 verified links / 8 pages live; tracking live (data-rybbit-event). Product ASINs verified: Nest B0D5BBYRJM, Kill A Watt B00009MDBU, Kasa KP115 B08LN3C7WK, Govee B0DQLFC3Q6, Moen Flo B00C03D01Q, Emporia Vue 3 B0C7B1LKDW, Emporia EV charger B09ZNN3JB7, ecobee B09XXS48P8 (compatibility claims need spec verification).",
    "House voice: plain-English, practical, no hype, no first-person testing claims. Shortcodes: {{< product-box asin=... name=... label=... description=... button=... >}} and {{< amazon asin=... text=... >}}; disclosure {{< affiliate-disclosure >}} near top of any monetized page.",
    "Canonical EIA/DOE numbers in the data baseline — use those; web-verify anything new (cite URL + date in frontmatter sources).",
]

def packet(role, mission, extra, writes, criteria):
    return {
        "role": role, "mission": mission, "parent_objective": PARENT,
        "context": extra, "known_facts": FACTS,
        "resources": {"roots": [REPO], "write_paths": writes, "notes": f"Data baseline: {BASE}"},
        "constraints": [
            "Depth means USEFUL density: tables, ranges, named examples — not padded prose. Every new factual claim sourced (baseline or web-verified with URL).",
            "Affiliate links ONLY where a product genuinely solves the section's problem; if none fits, add none and say so in findings.",
            "Match house markdown style; update frontmatter 'updated: 2026-08-28'; add frontmatter 'sources:' for any new web-verified facts.",
            "Chunk discipline: edit file by file, save after each.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch", "write_file", "edit_file"],
        "success_criteria": criteria,
    }

packets = {}

packets["operator"] = packet("operator",
    "DEEP ENHANCEMENT of 2 files. (1) content/blog/do-programmable-thermostats-cut-heating-bills.md — 262 words is too thin for a monetized page: add a savings-by-thermostat-type table (manual / programmable / smart learning, DOE setback data from baseline: 7-10F 8h -> up to 10%; Nest published 12%/15%), a 'which type fits you' decision list, and tighten the existing 2 product boxes' descriptions to the new savings context (keep the ASINs). (2) content/blog/04-hidden-fees-utility-bill.md — transform from 327w generic review into the fee HUB: add a table of 6-8 actual fees (customer charge, transmission rider, franchise fee, distribution surcharge, environmental rider, late fee, reconnect fee, minimum bill) with typical ranges and how to spot each on a bill — source ranges from the site's OWN sourced fee pages (read content/blog/17-, 18-, 19-, 22-, 24-, 25-, 27-, 28- first and synthesize; cite their sources) — then add a linked directory of those fee explainer pages (this page becomes the cluster's launching pad). No affiliate links on this page (definitional intent).",
    "Read each file's current state and the linked siblings before writing. The fees table must be consistent with the site's own fee pages — no invented ranges.",
    ["content/blog/do-programmable-thermostats-cut-heating-bills.md", "content/blog/04-hidden-fees-utility-bill.md"],
    ["Thermostat page: savings table + decision list + boxes recontextualized (600+ words).", "Fees page: 6-8 fee table with ranges + linked directory of fee pages (700+ words)."])

packets["mason"] = packet("mason",
    "DEPTH PASS on 4 files. (1) content/blog/05-how-to-lower-utility-bills.md: add the audit's prioritization matrix (8-10 improvements x cost-to-implement x typical monthly savings x payback — savings figures from baseline/DOE ranges already used sitewide; label estimates), then ONE Kill A Watt product-box in the baseline-measurement section + ONE inline Emporia Vue 3 link for whole-home baseline (both ASINs verified). Fix nothing else about the title. (2) content/blog/06-water-bill-too-high.md: add the 3-step quick-diagnosis list at top (bill compare -> meter test -> isolate), a typical-usage-by-household-size table (EPA WaterSense has per-person averages — web-verify and cite), and move the existing leak-guide link mention into step 2 where it belongs. Keep existing Sprint-1 product boxes as-is. (3) content/blog/16-budget-billing-level-pay-explained.md (311w): add how-utility-calculates-it mechanics, a worked 12-month example table (seasonal bills vs level-pay), pros/cons list, and 'questions to ask your utility' — cite 1-2 utility or regulator pages (web-verify). No affiliate fit (utility program) — add none. (4) content/blog/13-ac-short-cycling-causes-fixes.md (400w): expand each cause with its diagnostic tell + typical fix cost range, add a causes table with time-to-diagnose, and a 'call a tech vs DIY' decision list — cite DOE/ENERGY STAR HVAC pages where load-bearing. Thermostat-related cause may reference the smart thermostat pages via internal link only (Nest box already exists elsewhere; do not duplicate here).",
    "Every table earns its place. Ranges consistent with sitewide figures; web-verify and cite anything not in the baseline.",
    ["content/blog/05-how-to-lower-utility-bills.md", "content/blog/06-water-bill-too-high.md",
     "content/blog/16-budget-billing-level-pay-explained.md", "content/blog/13-ac-short-cycling-causes-fixes.md"],
    ["4 files enhanced per prescription with tables + cited sources.", "05 carries exactly one box + one inline link; 16 and 13 carry zero if no natural fit (state so)."])

packets["tracer"] = packet("tracer",
    "REAL-DATA TABLES + 2 PLACEMENTS across 5 files. (1) content/blog/08-time-of-use-electricity.md: add a table of 3 real utility TOU schedules (e.g. PG&E, Con Edison, a Texas REP) with peak/off-peak windows and prices — FETCH each utility's current tariff/TOU page, cite URL + retrieved date; add a load-shift example (dishwasher at peak vs off-peak on the fetched rates). Natural link: one Kasa KP115 inline (schedule the shift automatically — verified ASIN B08LN3C7WK). (2) content/blog/10-fixed-vs-variable-utility-rate.md: table comparing real fixed vs variable offers from 3 deregulated states (TX/PA/OH — fetch Power to Choose or PA Power Switch for actual current rates, cite + date); add break-even explanation. No affiliate fit (rate plans are utility-side). (3) content/blog/09-apartment-utilities-cost.md: state-utility-cost table for the 10 most populous states (EIA Table 5a or state pages — web-verify, cite), + first-apartment utility checklist. (4) content/blog/is-your-toilet-running-leak-test.md: after the dye-test instructions add the Govee sensor box (B0DQLFC3Q6) framed as 'dye finds today's leak; a sensor catches the one that starts next year' + disclosure shortcode near top if absent. (5) content/blog/single-stage-vs-two-stage-vs-variable-speed-hvac.md: add the ecobee Smart Thermostat Premium box (B09XXS48P8) at 'Questions to Ask Before Buying' — FIRST verify on ecobee.com that it supports multi-stage/variable-speed equipment and note the compatibility basis in the description (cite the spec page); one-line comparison to Nest Learning already sold on-site.",
    "Rates/tables must be fetched this run — never from memory. Each fetched figure carries utility-name + URL + date in the frontmatter sources.",
    ["content/blog/08-time-of-use-electricity.md", "content/blog/10-fixed-vs-variable-utility-rate.md",
     "content/blog/09-apartment-utilities-cost.md", "content/blog/is-your-toilet-running-leak-test.md",
     "content/blog/single-stage-vs-two-stage-vs-variable-speed-hvac.md"],
    ["3 real-data tables (TOU, fixed-vs-variable, state costs) with fetched citations.", "Toilet + HVAC placements live with verified compatibility; rate-plan pages stay link-free (state if you disagree and why)."])

out = Path(f"{REPO}/.squad/SQ-047/packets"); out.mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1)); print(f"wrote {name}.json")
