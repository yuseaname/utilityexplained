#!/usr/bin/env python3
"""Set accurate editorial labels on the AI-generated SQ-058 artwork.

The illustration model supplies the visual story. This small finishing pass keeps
the reader-facing words exact, rather than accepting AI-generated pseudo-text.
"""

from __future__ import annotations

from pathlib import Path
from subprocess import run
from tempfile import NamedTemporaryFile


ROOT = Path(__file__).resolve().parents[1]
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# (relative image path, title, supporting line)
ART = [
    ("01-how-to-read-your-electric-bill/statement-ledger-hero.webp", "READ YOUR ELECTRIC BILL, LINE BY LINE", "Start with the fields that control the total."),
    ("01-how-to-read-your-electric-bill/statement-anatomy-labeled.webp", "FIND THESE FIELDS FIRST", "Billing period  •  amount due  •  kWh  •  meter status  •  rate plan"),
    ("01-how-to-read-your-electric-bill/one-kwh-explained.webp", "ONE kWh = 1,000 WATTS FOR ONE HOUR", "Power × time becomes the energy shown on your statement."),
    ("01-how-to-read-your-electric-bill/actual-vs-estimated-read.webp", "ACTUAL READ vs ESTIMATED READ", "An estimate can true-up after the next actual meter reading."),
    ("01-how-to-read-your-electric-bill/effective-rate-worked-example.webp", "EFFECTIVE RATE = CHARGES ÷ kWh", "$152.30 ÷ 893 kWh = $0.1705 per kWh in this worked example."),
    ("08-time-of-use-electricity/tou-house-dusk-hero.webp", "WHEN YOU USE POWER CAN CHANGE THE PRICE", "Your tariff’s clock—not a national schedule—sets the timing."),
    ("08-time-of-use-electricity/dishwasher-load-shift-savings.webp", "MOVE FLEXIBLE LOADS AFTER PEAK HOURS", "One dishwasher cycle can cost differently at different times."),
    ("08-time-of-use-electricity/tou-interval-worksheet.webp", "MATCH YOUR USAGE TO YOUR TARIFF'S CLOCK", "Group your interval kWh by the actual periods in your plan."),
    ("08-time-of-use-electricity/tou-safety-gate-checklist.webp", "CHECK THE PLAN BEFORE YOU AUTOMATE", "Keep safety loads and equipment instructions ahead of the schedule."),
    ("why-did-my-water-bill-suddenly-increase/leak-check-checklist.webp", "START WITH THE LEAK CHECKS", "Dye test  •  fittings  •  irrigation  •  timer"),
    ("why-did-my-water-bill-suddenly-increase/two-hour-meter-test.webp", "T0 → T+2 HOURS: ALL WATER OFF", "A moving meter can point to a leak."),
    ("why-did-my-water-bill-suddenly-increase/next-step-router.webp", "FOLLOW THE RESULT", "Meter moved: leak checks  •  clean meter: billing details  •  mismatch: dispute"),
    ("how-to-read-a-water-meter/meter-to-bill-units.webp", "METER READING → BILLING UNIT", "Confirm whether your statement uses gallons, cubic feet, CCF, or kgal."),
    ("how-to-read-a-water-meter/ccf-usage-bracket.webp", "TWO READS TELL THE STORY", "Later reading − earlier reading = use for the period."),
    ("tiered-electricity-rates-explained/tier-usage-bins-hero.webp", "ONLY THE OVERFLOW CROSSES THE THRESHOLD", "The first block keeps its own rate."),
    ("tiered-electricity-rates-explained/tier-boundary-step-line.webp", "THE RATE CHANGES AFTER THE THRESHOLD", "Only usage beyond the line moves into the next tier."),
    ("tiered-electricity-rates-explained/tier-worked-example-split.webp", "BASE USE + OVERFLOW = YOUR USAGE CHARGE", "A tiered bill is built in parts—not repriced all at once."),
    ("tiered-electricity-rates-explained/tier-line-anatomy.webp", "CHECK EACH TIER LINE", "Verify the block quantity, rate, and displayed amount against the tariff."),
    ("49-demand-charges-electricity-bill-explained/kw-vs-kwh-demand-strip.webp", "kWh = TOTAL ENERGY  •  kW = POWER AT ONCE", "Demand charges use the rate of draw during the utility’s interval."),
    ("49-demand-charges-electricity-bill-explained/demand-line-verify-anatomy.webp", "FIND THE DEMAND LINE", "Verify the kW, interval, rate, and whether demand is actual or billed."),
    ("21-past-due-balance-utility-bill-explained/disconnection-notice-to-deadline.webp", "YOUR NOTICE DATE CONTROLS", "Read the stated deadline and the rules that apply to your service."),
    ("26-utility-deposit-explained/state-deposit-cap-ruler.webp", "CHECK THE RULE THAT APPLIES TO YOUR ACCOUNT", "Deposit caps and protections depend on the state and utility tariff."),
    ("26-utility-deposit-explained/deposit-refund-timeline.webp", "PAY → ON-TIME RECORD → RETURN OR FINAL CREDIT", "Your tariff sets the review and refund clock."),
    ("how-to-read-electric-meter/electric-dial-meter-sequence.webp", "READ LEFT TO RIGHT • DIALS ALTERNATE", "When a pointer sits between two numbers, record the lower one."),
    ("how-to-read-electric-meter/two-readings-subtraction.webp", "LATER READING − EARLIER READING = USAGE", "Compare the same meter at two points in the billing period."),
    ("how-to-read-electric-meter/meter-vs-bill-check.webp", "COMPARE YOUR READING TO THE BILL'S READ", "A small difference can be timing—not an error."),
    ("27-utility-connection-fee-explained/27-utility-connection-fee-explained_hero_v2.webp", "GET THE WRITTEN SCHEDULE OF CHARGES", "Confirm the service-start item before opening the account."),
    ("27-utility-connection-fee-explained/fee-situation-router.webp", "NEW SERVICE • RECONNECT • DEPOSIT ONLY", "Start from the charge situation that matches your account."),
    ("27-utility-connection-fee-explained/service-start-fee-anatomy.webp", "ONE CHARGE ≠ FIVE", "Ask which service-start, deposit, visit, construction, or move-out item applies."),
]


def annotate(relative: str, title: str, subtitle: str) -> None:
    image = ROOT / "static/images/articles" / relative
    probe = run(["identify", "-format", "%w %h", str(image)], check=True, capture_output=True, text=True)
    width, height = map(int, probe.stdout.split())
    title_size = 30 if width >= 1500 else 25
    body_size = 19 if width >= 1500 else 16
    top_height = 92 if width >= 1500 else 78
    bottom_height = 62 if width >= 1500 else 54
    with NamedTemporaryFile(suffix=".webp", dir=image.parent, delete=False) as temporary:
        destination = Path(temporary.name)
    try:
        run([
            "magick", str(image),
            "-fill", "#fffcfaeb", "-draw", f"rectangle 0,0 {width},{top_height}",
            "-fill", "#0e201c", "-font", FONT_BOLD, "-gravity", "north", "-pointsize", str(title_size),
            "-annotate", "+0+19", title,
            "-fill", "#fffcfae8", "-draw", f"rectangle 0,{height - bottom_height} {width},{height}",
            "-fill", "#274a42", "-font", FONT_REGULAR, "-gravity", "south", "-pointsize", str(body_size),
            "-annotate", "+0+17", subtitle,
            "-strip", "-quality", "84", str(destination),
        ], check=True)
        destination.replace(image)
    finally:
        destination.unlink(missing_ok=True)


if __name__ == "__main__":
    for relative, title, subtitle in ART:
        annotate(relative, title, subtitle)
        print(relative)
