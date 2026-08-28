#!/usr/bin/env python3
"""SQ-046 Sprint 1 packets: sourcing (mason+operator) + placements (tracer)."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "SQ-046 Sprint 1: sourcing pass + Tier 1 placements + measurement rig, one verified deploy."
DATA = f"{REPO}/.squad/SQ-046/data-baseline.md"
PLAN = f"{REPO}/AFFILIATE-PLACEMENTS-2026-08-28.md"

FACTS = [
    "CANONICAL DATA (Commander-verified 2026-08-28, citations in data baseline — use THESE numbers, never invent): avg US residential electric bill $159.14/mo mid-2026 (EIA, FY2024: $142.26); avg rate 18.3-18.4 c/kWh mid-2026, 17.30 FY2025; avg usage ~899 kWh/mo (EIA FAQ).",
    "DOE verified: thermostat setback 7-10F for 8h/day saves up to 10% (energy.gov/save/home-upgrades). energy.gov bill-share figures: heating ~30% of utility bills, water heating ~20%, duct losses 20-30%.",
    "Site voice: plain-English, practical, no hype. NEVER claim testing/review/firsthand use.",
]

def packet(role, mission, extra, writes, criteria):
    return {
        "role": role, "mission": mission, "parent_objective": PARENT,
        "context": extra, "known_facts": FACTS,
        "resources": {"roots": [REPO], "write_paths": writes,
                      "notes": f"Canonical data with source URLs: {DATA}"},
        "constraints": [
            "Cite only the baseline's verified numbers/URLs, or verify a new number yourself via web_fetch (cite URL + date). Never fabricate or estimate silently.",
            "Match each file's existing markdown style exactly; no restructures beyond the specified task.",
            "Update the frontmatter 'updated:' field to 2026-08-28 on every file you touch.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch", "write_file", "edit_file"],
        "success_criteria": criteria,
    }

packets = {}

packets["mason"] = packet("mason",
    "SOURCING PASS on 5 files. (A) content/blog/07-gas-bill-too-high.md and content/blog/30-sudden-spike-in-electricity-bill-no-usage.md: add frontmatter 'sources:' with the relevant baseline URLs (EIA end-use, DOE); for the 5-8 most load-bearing claims in each body, add inline citation in the site's existing style (e.g. '(U.S. EIA, [year])' matching how other sourced pages do it — check 03-why-is-my-electric-bill-so-high for the house pattern); reconcile any number that contradicts the baseline. (B) Draft math fixes (stay drafts): content/blog/average-utility-bills-by-state-2026.md — fix the internal contradiction ($262 vs $430-500: pick ONE basket definition, state it explicitly in a 'How we calculate' note, make all figures consistent with it and with baseline EIA data); content/blog/2026-utility-cost-index-by-state.md — fix the Hawaii error (rate x usage must reconcile; Hawaii usage is the nation's LOWEST ~500-550 kWh/mo due to no heating — verify via EIA and cite); label the 50-state table's methodology and mark estimates as estimates.",
    "Read the data baseline FIRST. House citation pattern: read content/blog/03-why-is-my-electric-bill-so-high.md frontmatter+body before editing.",
    ["content/blog/07-gas-bill-too-high.md", "content/blog/30-sudden-spike-in-electricity-bill-no-usage.md",
     "content/blog/average-utility-bills-by-state-2026.md", "content/blog/2026-utility-cost-index-by-state.md",
     "content/blog/02-average-utility-costs-2026.md"],
    ["Both monetized pages carry frontmatter sources + inline citations on load-bearing claims; contradictions reconciled to baseline.",
     "Draft state pages: Hawaii math fixed with cited EIA figures; basket definition stated; table labeled as estimates where unsourced."])

packets["operator"] = packet("operator",
    "SOURCING PASS on the flagship: content/blog/how-to-lower-electric-bill-complete-guide.md. It carries ~249 dollar figures with zero sources and 15.7% of site pageviews. Mission: (1) frontmatter 'sources:' with the baseline URLs; (2) inline-cite the ~12-15 LOAD-BEARING claims (thermostat savings %, HVAC share, LED savings, water-heater 120F savings, air-sealing ranges, phantom-load estimates) using baseline numbers — where the page's figure differs from the verified baseline, CORRECT the figure to the baseline, do not bend the citation; (3) add a short 'About our numbers' note near the top stating ranges are typical US figures compiled from EIA/DOE data, individual results vary; (4) leave the article structure, product boxes, and internal links untouched. CHUNK DISCIPLINE: edit section by section, save after each — do not compose one giant final turn.",
    "This is the trust-debt payment for the whole site. Verify any new number via web_fetch; the baseline file has the verified set.",
    ["content/blog/how-to-lower-electric-bill-complete-guide.md"],
    ["Frontmatter sources added; 12-15 load-bearing claims inline-cited or corrected to baseline; 'About our numbers' note present; structure/boxes untouched."])

packets["tracer"] = packet("tracer",
    "TIER 1 PLACEMENTS: insert the publish-ready copy from the placement plan into 6 files, at the exact section anchors specified there. Plan file: " + PLAN + " (read it first — sections 'TIER 1' and 'EXISTING placements'). Corrections to the plan as you execute: (1) Govee ASIN is VERIFIED: B0DQLFC3Q6 (GoveeLife Upgraded Smart Water Leak Detector 1s, 5-pack with gateway, SMS/app/email alerts, 105 dB alarm — fix the plan's '100 dB' to '105 dB' in your inserted copy); (2) pages: 03-why-is-my-electric-bill-so-high (end of 'A Practical Diagnosis Sequence'), 06-water-bill-too-high (end of section 3), water-meter-running-when-no-water-used (end of 'If It's Inside: Find the Culprit'), water-meter-leak-indicator-explained (end of 'How to isolate'), ev-charging-impact-electric-bill (end of 'Home Equipment and Safety'), 30-sudden-spike (add the Kasa KP115 companion inline link right after the existing Kill A Watt product box, per the plan's 'EXISTING placements' item); (3) ensure each touched file has the affiliate-disclosure shortcode near top (30-spike already has it); (4) preserve each article's voice — read 200 words around each anchor before inserting.",
    "Mechanical insertion of pre-written copy at named anchors. If an anchor section reads awkwardly with the insertion, adjust the transition sentence — do not move sections.",
    ["content/blog/03-why-is-my-electric-bill-so-high.md", "content/blog/06-water-bill-too-high.md",
     "content/blog/water-meter-running-when-no-water-used.md", "content/blog/water-meter-leak-indicator-explained.md",
     "content/blog/ev-charging-impact-electric-bill.md", "content/blog/30-sudden-spike-in-electricity-bill-no-usage.md"],
    ["All 6 placements live at correct anchors with verified ASINs; disclosures present; voice preserved."])

out = Path(f"{REPO}/.squad/SQ-046/packets"); out.mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1)); print(f"wrote {name}.json")
