#!/usr/bin/env python3
"""SQ-044 wave-2 BUILDER packets — disjoint write_paths, revenue-focused."""
import json
from pathlib import Path

REPO = "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained"
PARENT = "P1 revenue implementation for utilityexplained.com Amazon Associates pivot (store ID utexplained-20). P0 compliance already shipped + verified in production."

RULES = [
    "PRODUCT-BOX DOCTRINE: use the existing {{< product-box asin=... name=... label=... description=... button=... >}} shortcode pattern exactly as in content/blog/07-gas-bill-too-high.md:318.",
    "Only products whose ASIN you verified on amazon.com via web_search/web_fetch THIS run (cite the Amazon URL in your findings). Reuse already-verified ASINs where they fit: B0D5BBYRJM (Nest Learning Thermostat 4th gen), B00009MDBU (P3 Kill A Watt P4400).",
    "Descriptions state what the product does + manufacturer/DOE/ENERGY STAR published facts ONLY. NO testing claims, NO 'we found', NO first-person experience, NO invented specs or prices.",
    "Every page you add a product box to must have {{< affiliate-disclosure >}} near the top (after frontmatter) if not already present.",
    "amazon_tag comes from hugo.toml (utexplained-20, already fixed) — NEVER hardcode tag or price in URLs or text.",
    "Match each page's existing markdown style, heading voice, and Quick Answer structure. Do not restructure the article — enhance it.",
]

def packet(role, mission, extra, writes, criteria, tools_extra=None):
    return {
        "role": role,
        "mission": mission,
        "parent_objective": PARENT,
        "context": extra,
        "known_facts": [
            "Production verified clean: tag=utexplained-20 on both live product pages; 'As an Amazon Associate, we earn from qualifying purchases' renders sitewide (shortcode + footer).",
            "Site: Hugo, product-box + affiliate-disclosure shortcodes ready; hugo.toml amazon_tag=utexplained-20.",
            "Amazon commission context (verified 2026-08-27): Home Improvement/Home/Tools ~3%, Kitchen ~4.5%.",
        ],
        "resources": {"roots": [REPO], "write_paths": writes},
        "constraints": RULES,
        "authorized_actions": ["read_file", "list_dir", "search", "run_command", "web_search", "web_fetch", "write_file", "edit_file"],
        "success_criteria": criteria,
    }

C = "Read content/blog/07-gas-bill-too-high.md FIRST as the compliant reference (disclosure at line 16, product box at 318). Read layouts/shortcodes/product-box.html to know the exact parameters. "

packets = {}

packets["mason"] = packet("mason",
    "Monetize 4 high-intent articles with honest product boxes: (1) content/blog/50-best-smart-plugs-standby-power.md — it is ALREADY the smart-plug product page but has zero links: add 2-3 product boxes for smart plugs WITH energy-monitoring capability (verify ASINs on amazon.com; e.g. Kasa/Tp-Link and a runner-up — confirm current models yourself), placed in/next to the existing product discussion; (2) content/blog/phantom-power-draw-explained.md — 1-2 boxes: smart plug with monitoring + the Kill A Watt meter (B00009MDBU) as the measurement tool; (3) content/blog/gadgets-that-lower-utility-bills.md — 2-3 boxes matching the gadgets the article already discusses (Nest thermostat B0D5BBYRJM fits; verify 1-2 more the article names); (4) content/blog/do-programmable-thermostats-cut-heating-bills.md — 1-2 boxes: Nest Learning (B0D5BBYRJM) + one basic programmable alternative (verify ASIN). Each description: honest 'what it does' + cited manufacturer/DOE fact from the article. Add the disclosure shortcode atop any file missing it.",
    C + "You own EXACTLY these 4 files — no other writes. Your 1M window: read all 4 articles fully so boxes land in the right sections.",
    ["/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/50-best-smart-plugs-standby-power.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/phantom-power-draw-explained.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/gadgets-that-lower-utility-bills.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/do-programmable-thermostats-cut-heating-bills.md"],
    ["4 files monetized with verified-ASIN product boxes in contextually correct sections.", "Per-box Amazon source URL cited in findings; no testing/fabricated claims; disclosures present."])

packets["operator"] = packet("operator",
    "Upgrade the #1 traffic + money page: content/blog/how-to-lower-electric-bill-complete-guide.md (123 sessions/wk, just un-drafted, ~2000w, '20+ ways' format). You own exactly this file. Mission: (1) monetization: add a compact 'Tools that pay for themselves' comparison section after the Quick Answer area with 2-3 product boxes — Nest Learning Thermostat (B0D5BBYRJM, already verified: manufacturer-claimed ~12% heating/~15% cooling savings), Kill A Watt (B00009MDBU), and one verified smart-plug-with-monitoring ASIN — each with an honest 'best for' framing tied to numbered steps in the guide; (2) engagement: convert the flat 20+-item list into scannable cost-tiered H3 groupings (free behaviors / under-$50 / big-ticket) WITHOUT rewriting the substance — reorder only where logic demands; add a 'Start here' decision line under Quick Answer; (3) add 3-5 contextual internal links to related guides (phantom-power-draw, 50-best-smart-plugs, do-programmable-thermostats, heat-pump-vs-gas-furnace-savings) inside relevant steps; (4) ensure {{< affiliate-disclosure >}} sits atop the article; (5) update the 'updated:' frontmatter date to 2026-08-28.",
    C + "This is the revenue flagship — the page must read BETTER, not just carry links. Chunk your edits (write in sections, not one giant composition).",
    ["/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/how-to-lower-electric-bill-complete-guide.md"],
    ["Page upgraded: comparison section + verified boxes + cost-tier structure + internal links + disclosure + fresh date.", "No fabricated claims; every product fact attributable to manufacturer/DOE or the article's own sourced numbers."])

packets["cartographer"] = packet("cartographer",
    "Engagement wiring on the top-traffic pages (bounce 91.3%, pages/session 1.10 — your job is the internal-link graph that fixes both). You own EXACTLY these 14 files: 30-sudden-spike-in-electricity-bill-no-usage, 06-water-bill-too-high, 28-utility-reconnection-fee-explained, water-meter-running-when-no-water-used, 07-gas-bill-too-high, 23-utility-billing-cycle-explained, how-sewer-charges-work-on-your-water-bill, 03-why-is-my-electric-bill-so-high, what-is-ccf-on-a-water-bill, water-meter-leak-indicator-explained, 05-how-to-lower-utility-bills, average-water-usage-per-person, electric-bill-breakdown-understanding-line-items, 01-how-to-read-your-electric-bill (all under content/blog/). For EACH: (1) add a short 'Next step' line at the END of the Quick Answer section pointing to the single most-logical next guide (diagnosis page -> action page, fee page -> bill-anatomy page — you built the graph, use it); (2) ensure at least 2 contextual in-body links to related guides where the text naturally mentions their topic (do not force); (3) add ONE 'Related guides' short list (2-3 links) after the FAQ/sources area if the template does not already render related posts reliably — check public rendering first via the built HTML. Match existing link markdown style exactly. Do NOT touch the complete-guide (another seat owns it) or restructure any content.",
    "You mapped this graph in wave 1 — now wire it. Links must feel editorial, not mechanical. Read each file's Quick Answer before choosing the next-step target.",
    ["/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/30-sudden-spike-in-electricity-bill-no-usage.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/06-water-bill-too-high.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/28-utility-reconnection-fee-explained.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/water-meter-running-when-no-water-used.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/07-gas-bill-too-high.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/23-utility-billing-cycle-explained.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/how-sewer-charges-work-on-your-water-bill.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/03-why-is-my-electric-bill-so-high.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/what-is-ccf-on-a-water-bill.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/water-meter-leak-indicator-explained.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/05-how-to-lower-utility-bills.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/average-water-usage-per-person.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/electric-bill-breakdown-understanding-line-items.md", "/home/msi-command/Desktop/projects/affiliate sites/utilityexplained/content/blog/01-how-to-read-your-electric-bill.md"],
    ["All 14 pages carry a Quick Answer next-step link + >=2 contextual internal links.", "No content restructuring; markdown style matches each file's conventions."])

out = Path(f"{REPO}/.squad/SQ-044/packets-wave2")
out.mkdir(parents=True, exist_ok=True)
for name, p in packets.items():
    (out / f"{name}.json").write_text(json.dumps(p, indent=1))
    print(f"wrote {name}.json")
