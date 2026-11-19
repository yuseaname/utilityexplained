---
title: "Space Heater Keeps Tripping the Breaker? The Arithmetic and the Answer"
slug: "space-heater-keeps-tripping-breaker"
description: "Space heater tripping the breaker: a 1,500 W heater draws 12.5 amps — a 15-amp circuit's continuous limit before anything else plugs in. Here is what to do."
date: 2026-11-18
updated: 2026-11-18
author: "Home Energy Desk"
category: "Electricity"
categories: ["Electricity"]
tags: ["space heater", "breaker", "circuit", "electrical safety", "winter"]
keywords: ["space heater keeps tripping breaker", "space heater trips circuit", "1500 watt heater amps", "heater tripping breaker fix", "space heater breaker safety"]
image: "/images/articles/space-heater-keeps-tripping-breaker/space-heater-tripping-breaker_hero.webp"
image_alt: "Flat illustration of a portable space heater plugged into a wall outlet, with a home breaker panel nearby showing one switch flipped off."
hero_below_answer: true
sources:
  - https://www.cpsc.gov/s3fs-public/heaters.pdf
  - https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters
  - https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03
---

{{< jump-row "The arithmetic|#arithmetic" "Why it trips after a while|#time-delay" "Find what is sharing the circuit|#shared" "The never list|#never" "Cost-side note|#cost" >}}

## Quick Answer

**A 1,500-watt space heater on a standard 120-volt circuit draws 12.5 amps — which is more than a 15-amp breaker should carry continuously (its continuous rating is 80% of 15 amps, or 12) before a single other thing plugs in.** The breaker tripping is not a defect; it is the circuit doing exactly what it was designed to do. The fix is almost always to give the heater a circuit of its own — plug it straight into a wall outlet nothing else is using, keep it off extension cords and power strips (CPSC's explicit rule)[1][2], and move the load, not the protection: never install a bigger breaker to stop the tripping. If the heater trips a dedicated circuit immediately, or plugs and cords feel hot, the problem moves from usage to wiring — and that is an electrician.

## The arithmetic that explains everything {#arithmetic}

{{< visual src="/images/articles/space-heater-keeps-tripping-breaker/circuit-capacity.webp" alt="A capacity gauge bar filled almost to capacity by the heater load, with only a small margin remaining." wide="true" >}}


Amps are watts divided by volts. On a 120-volt circuit:

- 1,500 W heater on high → 1,500 ÷ 120 = **12.5 A**
- A 15-amp circuit's continuous-safe limit (80%) → **12 A**
- A 20-amp circuit's continuous-safe limit (80%) → **16 A**

So a full-power heater alone already exceeds the continuous limit of a 15-amp circuit — technically fine for short bursts, which is why the heater runs happily for a while, but with anything else drawing on the same circuit (a TV, a laptop charger, a lamp, a fridge on a shared kitchen circuit), the total crosses the line and the breaker opens. That "it works for twenty minutes then trips" pattern is the arithmetic plus the breaker's built-in time delay doing a slow accumulation of heat, not a mystery.

This is also why the wattage setting matters more than the brand: drop the heater to 750 W and it draws 6.25 A — comfortably inside a shared 15-amp circuit. The tradeoff is heat output, and the running cost of each setting is pure multiplication in [space heater running cost](/blog/space-heater-running-cost/).

## Why it trips after a while, not instantly {#time-delay}

Residential breakers are thermal-magnetic: a small, sustained overload heats a bimetal strip until it trips — deliberately, after minutes, because brief surges (a motor starting) are normal life. A heater at 13 amps on a 15-amp breaker might run 20 minutes before the strip warms enough to open. Two practical consequences: an outlet or plug that feels warm to the touch while the heater runs is the same accumulation happening in your wiring instead of the panel, and CPSC's guidance is to stop using that outlet and have it checked[1]; and repeated resets after trips keep stressing a circuit that has already told you it is at its limit.

## Finding what is sharing the circuit {#shared}

You do not need a circuit map to diagnose — the panel tells you:

1. Note which breaker flipped (the label — "Bedroom," "Kitchen small appl.," or famously, nothing legible).
2. Unplug everything else you can find on that zone's outlets.
3. Run the heater alone. Stable? Add devices back one at a time until the trip returns — the last addition is your co-tenant.

The usual silent partners: entertainment centers, computer setups, aquarium equipment, a second heater (two heaters on one circuit is a guaranteed trip), and anything with a compressor. Bathrooms and kitchens often have 20-amp circuits — a better home for a big heater — while bedrooms and living rooms are typically 15.

If the label is illegible or the zones make no sense, turning the tripped breaker off and testing which outlets went dead gives you the membership list the label never had.

## The never list {#never}

{{< visual src="/images/articles/space-heater-keeps-tripping-breaker/outlet-vs-strip.webp" alt="Correct versus wrong: a space heater plugged directly into a wall outlet with a check mark, versus the same heater on a power strip with a cross." wide="true" >}}


- **Never plug a space heater into an extension cord or power strip.** CPSC states it without qualification — plug directly into a wall outlet.[1][2] Strips and cords are not rated for a sustained 12-plus-amp load; the failure mode is heat where you cannot see it.
- **Never upsize the breaker.** A 20-amp breaker on 15-amp-rated wiring removes the protection that is tripping and leaves the wires to overheat instead. The breaker is the messenger; do not shoot it. If the circuit genuinely cannot serve the heater, an electrician can run a proper one.
- **Never keep resetting a breaker that keeps tripping.** Repeated trips under the same load mean overload or a developing fault; the third reset is where diagnosis should end and a professional begin.[1]
- **Never ignore a hot plug, cord, or outlet faceplate.** Discontinue use and have a qualified electrician check or replace the outlet.[1]
- **Never run the cord under a rug**, and keep the heater three feet from anything that burns.[1][2]

## The cost-side note {#cost}

Once the heater is safely on a circuit that holds it, the next question is usually the bill: at the {{< stat "electric_rate_jun2026" "raw" >}}¢ national average rate, eight hours a day of 1,500 W runs about $66 a month. The full math — per-hour cost by wattage, duty cycling, the state-rate spread — lives in [space heater running cost](/blog/space-heater-running-cost/), and the decision it feeds (heating one room versus the whole house) is [worked through here](/blog/cheaper-to-heat-one-room-vs-whole-house/). If a breaker-tripping heater has you shopping for a replacement, [what actually matters in an energy-efficient space heater](/blog/best-energy-efficient-space-heater/) avoids the marketing and ranks by the numbers that change the bill.

## FAQ

{{< faq "Can I just use a lower setting so it stops tripping?" >}}
Often, yes — 750 W draws 6.25 amps, which coexists with other loads on a 15-amp circuit. You trade heat output for electrical peace. If low still trips an otherwise-empty circuit, stop: the heater or the wiring is the problem, not the setting.
{{< /faq >}}

{{< faq "Is it dangerous when a space heater trips a breaker?" >}}
The trip itself is the safety system working. The dangerous version is what people do next: extension cords, power strips, repeated resets, or a bigger breaker — each moves the stress from the protected breaker onto wiring or cords that have no trip mechanism. CPSC attributes an average of 1,600 fires a year to portable heaters[2]; the usage rules above are the prevention.
{{< /faq >}}

{{< faq "Why does the bathroom outlet handle the heater better?" >}}
Many bathroom and kitchen circuits are 20-amp with heavier wiring — a 16-amp continuous capacity versus 12. The GFCI outlet there is about shock protection, not capacity, but the circuit's headroom is real. Check the panel label to confirm before assuming.
{{< /faq >}}

{{< faq "Do older heaters draw more power?" >}}
A resistive element draws its rated watts whether new or old — age does not inflate the draw. What age changes is cord and plug condition, tip-over switches, and safety certifications; a heater with a stiff, scorched, or damaged cord should be replaced, not nursed along.[1]
{{< /faq >}}

{{< faq "Will an electrician visit actually fix this?" >}}
Yes — and for the right reason. An electrician can identify the circuit layout, verify the breaker matches the wire, and if you genuinely need big heat in that room, run a dedicated circuit. That is the correct version of "making the breaker stop tripping": more capacity properly wired, never a bigger fuse on the same wire.
{{< /faq >}}

## Related Reading

- [Space heater running cost: the per-hour math](/blog/space-heater-running-cost/) — what the heater costs once it stays on
- [Best energy-efficient space heaters](/blog/best-energy-efficient-space-heater/) — if you are replacing the offender
- [Cheaper to heat one room or the whole house?](/blog/cheaper-to-heat-one-room-vs-whole-house/) — the strategic question behind zone heating
- [Electric blanket vs space heater cost](/blog/electric-blanket-vs-space-heater-cost/) — the ten-times-cheaper alternative for a bed
- [How to read your electric bill](/blog/how-to-read-your-electric-bill/) — find the rate that drives the cost math
- [Electricity explained](/electricity-explained/)

## Sources

1. [CPSC Publication 098: Reducing Fire Hazards for Portable Electric Heaters](https://www.cpsc.gov/s3fs-public/heaters.pdf) (retrieved 2026-11-18)
2. [CPSC: Keep Warm and Safe This Winter — generators, furnaces, and space heaters](https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters) (retrieved 2026-11-18)
3. [EIA Electric Power Monthly, Table 5.03](https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03) (retrieved 2026-09-06)
