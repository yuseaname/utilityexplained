#!/usr/bin/env python3
"""SQ-048 P2 wave: stale refresh + adjudicated removals + rate hub + CCF calculator."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "SQ-048 P2: stale-year refresh, adjudicated removals (alias-based), rate-plan hub, CCF calculator."
BASE = f"{REPO}/.squad/SQ-046/data-baseline.md"
FACTS = [
    "Commander adjudication (traffic 2026-08-27): NO merges into monetized or >5 pv/wk pages. Removals use draft:true + alias-on-target (the host ignores .htaccess; Hugo aliases are the working redirect).",
    "Verified products: Kill A Watt B00009MDBU, Kasa KP115 B08LN3C7WK, Govee B0DQLFC3Q6, Moen Flo B00C03D01Q, Emporia Vue 3 B0C7B1LKDW, Nest B0D5BBYRJM, ecobee B09XXS48P8, Emporia charger B09ZNN3JB7, plus site-standard shortcodes.",
    "House voice: plain-English, no hype, no fabricated testing. Sources cited with URL + date.",
]

def packet(role, mission, extra, writes, criteria):
    return {
        "role": role, "mission": mission, "parent_objective": PARENT,
        "context": extra, "known_facts": FACTS,
        "resources": {"roots": [REPO], "write_paths": writes, "notes": f"Data baseline: {BASE}"},
        "constraints": [
            "Every factual claim sourced (baseline or web_fetch with URL+date). House markdown style. updated: 2026-08-28 on touched files.",
            "Chunk discipline: file by file, save after each.",
        ],
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch", "write_file", "edit_file"],
        "success_criteria": criteria,
    }

packets = {}

packets["mason"] = packet("mason",
    "TWO JOBS. (A) STALE-YEAR REFRESH on 6 live pages: content/blog/03-why-is-my-electric-bill-so-high.md, 01-how-to-read-your-electric-bill.md, 11-understanding-kwh-usage.md, mcf-vs-ccf-vs-therms-on-gas-bill.md, 43-understand-natural-gas-bill-charges.md, 18-fuel-adjustment-charge-on-utility-bill-explained.md — find every year-dated stat (2020-2023 refs), refresh with current EIA/DOE figures (baseline first; web-verify anything else, cite URL+date in frontmatter sources). Do NOT restructure; refresh numbers only. (B) ADJUDICATED REMOVAL SWEEP — for each of these EXACT pages: set draft:true in frontmatter AND add its URL path to the aliases list of its named target: 41-how-to-read-electricity-bill.md -> target 01-how-to-read-your-electric-bill.md (add '/blog/41-how-to-read-electricity-bill/'); how-to-read-your-utility-bill.md -> target complete-guide-understanding-utility-bill.md (add '/blog/how-to-read-your-utility-bill/'); why-electric-bill-changes-month-to-month.md -> target 03-why-is-my-electric-bill-so-high.md; supply-vs-delivery-charges-electricity.md -> 24-delivery-charge-vs-supply-charge-utility-bill.md; gas-customer-charge-explained.md -> 17-what-is-customer-charge-on-utility-bill.md; fixed-vs-variable-rate-electricity-plan.md -> 10-fixed-vs-variable-utility-rate.md. THEN sweep the whole content/ tree for markdown links pointing at those six removed URLs and rewire each to its target (report every rewired file:line). DO NOT touch any page not named here.",
    "Removal = draft + alias + inbound-link rewiring. Nothing else dies. If a target lacks an aliases: frontmatter key, create it preserving existing entries.",
    ["content/blog/03-why-is-my-electric-bill-so-high.md", "content/blog/01-how-to-read-your-electric-bill.md",
     "content/blog/11-understanding-kwh-usage.md", "content/blog/mcf-vs-ccf-vs-therms-on-gas-bill.md",
     "content/blog/43-understand-natural-gas-bill-charges.md", "content/blog/18-fuel-adjustment-charge-on-utility-bill-explained.md",
     "content/blog/41-how-to-read-electricity-bill.md", "content/blog/how-to-read-your-utility-bill.md",
     "content/blog/why-electric-bill-changes-month-to-month.md", "content/blog/supply-vs-delivery-charges-electricity.md",
     "content/blog/gas-customer-charge-explained.md", "content/blog/fixed-vs-variable-rate-electricity-plan.md",
     "content/blog/complete-guide-understanding-utility-bill.md", "content/blog/24-delivery-charge-vs-supply-charge-utility-bill.md",
     "content/blog/17-what-is-customer-charge-on-utility-bill.md", "content/blog/10-fixed-vs-variable-utility-rate.md",
     "content/_index.md", "content/electricity-explained.md", "content/gas-explained.md",
     "content/water-explained.md", "content/heating-cooling-explained.md", "content/utility-bills-costs-explained.md"],
    ["6 pages refreshed with current cited figures.", "6 removals drafted + aliased + every inbound link rewired (file:line list)."])

packets["operator"] = packet("operator",
    "TWO NEW PAGES. (1) content/blog/which-rate-plan-is-right-for-me.md — the rate-plan hub the site lacks: title 'Which Rate Plan Is Right for Me? (Fixed vs Variable vs Time-of-Use)'; Quick Answer decision list by household profile (predictable usage -> fixed; flexible schedule -> ToU; deregulated-state shopper -> compare variable); a comparison table (rate stability / bill predictability / best-for / risk) built on the site's own rate pages' verified data (READ 08-time-of-use, 10-fixed-vs-variable, 11-kwh, 49-demand-charges, net-metering-explained, tiered pages first and synthesize — their fetched citations are current); a linked directory of all 8 rate pages; 'questions to ask your utility' checklist. Frontmatter: category Electricity or Bills & Fees, author David Chen, sources from the sibling pages, updated 2026-08-28. NO affiliate links (rate choice is utility-side) — but END with one honest bridge line linking to 05-lower-utility-bills. (2) content/blog/ccf-calculator.md — the site's first tool page: title 'CCF Calculator: Convert Your Water Bill Units to Gallons and Dollars'; a vanilla-JS calculator (inline <script> in the markdown — the site already runs inline scripts; keep it dependency-free) with inputs: CCF usage, rate per CCF (or per 1,000 gal), tier structure toggle (flat/tiered 2-tier); outputs: gallons (1 CCF = 748 gal), cost breakdown, comparison vs EPA-average household (~300 gal/day family of four — verify current EPA WaterSense figure and cite); worked example table below the tool for no-JS readers; short SEO text on what CCF means (link what-is-ccf page) and tiered rates (link tiered-water-rates). Add ONE natural placement: Moen Flo inline link in a 'catch leaks early' closing note (B00C03D01Q, verified) with affiliate-disclosure shortcode near top. Test the JS logic by reading it twice — arithmetic must be exactly right.",
    "New-page frontmatter must include slug, description, date 2026-08-28, author, categories, tags, image only if one exists on disk (else omit image field — do not reference nonexistent assets).",
    ["content/blog/which-rate-plan-is-right-for-me.md", "content/blog/ccf-calculator.md"],
    ["Rate hub live with comparison table + 8-page directory + checklist.", "CCF calculator with working dependency-free JS, no-JS fallback table, cited EPA figure, one Moen Flo inline link + disclosure."])

out = Path(f"{REPO}/.squad/SQ-048/packets"); out.mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1)); print(f"wrote {name}.json")
