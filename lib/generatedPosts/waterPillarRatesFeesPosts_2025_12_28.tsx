import type { Post } from "@/lib/types";
import ContentImage from "@/components/ContentImage";

export const waterPillarRatesFeesPosts_2025_12_28: Post[] = [
  {
    slug: "tiered-water-rates-explained",
    title: "Tiered Water Rates Explained: How Tiers Work, Why Your Price Jumps, and How to Stay in a Lower Tier",
    description:
      "Tiered water rates can make bills jump even when usage barely changes. Learn how tiers work, where the thresholds are, and how to avoid a surprise jump.",
    category: "Water",
    keyword: "tiered water rates",
    date: "2025-12-28",
    readTime: "12 min read",
    image: {
      src: "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa",
      alt: "Water flowing from a city hydrant with sunlight"
    },
    relatedSlugs: [
      "what-is-ccf-on-a-water-bill",
      "why-is-my-water-bill-higher-in-summer",
      "average-water-usage-per-person",
      "how-to-read-a-water-meter",
      "drought-surcharge-on-water-bill-explained",
      "stormwater-fee-on-water-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: your price per unit jumps mid-bill",
        content: (
          <>
            <p className="lead">
              You did not double your water use, but the bill looks like you did.
              That is the usual experience with tiered rates. The unit price changes
              when you cross a threshold.
            </p>
            <p>
              This guide explains how tiers are structured, why they exist, and how
              to keep your usage inside the lower-cost blocks. If you want the
              basics first, start with <a href="/water-explained">water service explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#how-tiers-work">How tiered water rates work</a></li>
              <li><a href="#why-it-jumps">Why the total jumps faster than usage</a></li>
              <li><a href="#where-listed">Where tiers show up on the bill</a></li>
              <li><a href="#stay-lower">How to stay in a lower tier</a></li>
              <li><a href="#mistakes">Common mistakes</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              Tiered water rates charge a lower price for the first block of usage,
              then higher prices for additional blocks. Crossing a threshold can
              make the bill jump even if usage only rises slightly.
            </p>
          </>
        )
      },
      {
        id: "how-tiers-work",
        title: "How tiered water rates work",
        content: (
          <>
            <p>
              A tiered plan splits usage into blocks, each with its own price. For
              example, the first 4 CCF might be billed at one rate, the next 6 CCF
              at a higher rate, and anything beyond that at the highest rate.
            </p>
            <figure>
              <ContentImage
                src="https://images.unsplash.com/photo-1453738773917-9c3eff1db985"
                alt="Water tower against a clear sky"
              />
              <figcaption>Tiered rates reward lower usage and discourage waste.</figcaption>
            </figure>
            <table>
              <thead>
                <tr>
                  <th>Tier</th>
                  <th>Usage range</th>
                  <th>Example rate</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Tier 1</td>
                  <td>0 to 4 CCF</td>
                  <td>$2.50 per CCF</td>
                </tr>
                <tr>
                  <td>Tier 2</td>
                  <td>4 to 10 CCF</td>
                  <td>$4.00 per CCF</td>
                </tr>
                <tr>
                  <td>Tier 3</td>
                  <td>10+ CCF</td>
                  <td>$6.00 per CCF</td>
                </tr>
              </tbody>
            </table>
            <p>
              If you are not sure what a CCF is, use
              <a href="/blog/what-is-ccf-on-a-water-bill"> this CCF explainer</a>.
            </p>
          </>
        )
      },
      {
        id: "why-it-jumps",
        title: "Why the total jumps faster than usage",
        content: (
          <>
            <p>
              The jump happens when you move into a higher tier. The extra units
              are priced higher, so each additional CCF costs more than the ones
              before it.
            </p>
            <p>
              Another factor is billing cycle length. A longer cycle means more
              days of usage, which can push you into a higher tier even if your
              daily usage stays steady. If you see an unusual spike, compare usage
              per day in
              <a href="/blog/why-my-utility-bill-is-higher-with-same-usage"> this guide</a>.
            </p>
            <p>
              Summer outdoor use is the most common reason households cross tiers.
              If your bill jumps in warm months, see
              <a href="/blog/why-is-my-water-bill-higher-in-summer"> why summer bills rise</a>.
            </p>
          </>
        )
      },
      {
        id: "where-listed",
        title: "Where tiers show up on the bill",
        content: (
          <>
            <p>
              Most bills show a separate line for each tier, with its own usage
              amount and rate. Look for labels like:
            </p>
            <ul>
              <li>Tier 1 usage / Tier 2 usage</li>
              <li>Block 1 / Block 2</li>
              <li>Conservation rate tiers</li>
            </ul>
            <p>
              If the line items are confusing, compare your meter readings using
              <a href="/blog/how-to-read-a-water-meter"> the meter guide</a>.
            </p>
          </>
        )
      },
      {
        id: "stay-lower",
        title: "How to stay in a lower tier",
        content: (
          <>
            <p>
              Staying in a lower tier is usually about controlling outdoor use and
              finding leaks early. These steps help:
            </p>
            <ul>
              <li>Water lawns early to reduce evaporation</li>
              <li>Adjust irrigation after rain instead of running on a timer</li>
              <li>Check for toilet leaks with a simple dye test</li>
              <li>Track usage weekly during peak months</li>
            </ul>
            <figure>
              <ContentImage
                src="https://images.unsplash.com/photo-1469474968028-56623f02e42e"
                alt="Garden hose watering plants in sunlight"
              />
              <figcaption>Outdoor watering is the fastest way to cross a tier.</figcaption>
            </figure>
            <p>
              If you want a sense of typical usage for your household, use
              <a href="/blog/average-water-usage-per-person"> average usage ranges</a>.
            </p>
          </>
        )
      },
      {
        id: "mistakes",
        title: "Common mistakes",
        content: (
          <>
            <ul>
              <li>
                <strong>Assuming the higher rate applies to all usage.</strong> Only
                the usage inside that tier is billed at the higher price.
              </li>
              <li>
                <strong>Ignoring billing days.</strong> A longer cycle can push you
                into a higher tier without a daily usage change.
              </li>
              <li>
                <strong>Missing hidden leaks.</strong> Even a small toilet leak can
                add enough usage to cross a tier threshold.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What are tiered water rates?",
        answer:
          "Tiered rates charge a lower price for the first block of water use and higher prices for additional blocks."
      },
      {
        question: "Does the higher tier rate apply to all my water use?",
        answer:
          "No. Only the portion of usage within that tier is billed at the higher rate."
      },
      {
        question: "Why did my bill jump even though usage barely changed?",
        answer:
          "You likely crossed a tier threshold, which raises the price for the additional units."
      },
      {
        question: "How can I avoid hitting a higher tier?",
        answer:
          "Focus on outdoor watering, fix leaks quickly, and monitor usage during warm months."
      }
    ]
  },
  {
    slug: "drought-surcharge-on-water-bill-explained",
    title: "Drought Surcharge on a Water Bill Explained: What It Is, When It Appears, and How It Is Calculated",
    description:
      "Drought surcharges show up during water shortages to fund supply and conservation programs. Learn how they are calculated and how to reduce the impact.",
    category: "Water",
    keyword: "drought surcharge water bill",
    date: "2025-12-28",
    readTime: "12 min read",
    image: {
      src: "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
      alt: "Dry landscape with cracked soil and a distant horizon"
    },
    relatedSlugs: [
      "why-is-my-water-bill-higher-in-summer",
      "tiered-water-rates-explained",
      "average-water-usage-per-person",
      "water-service-charge-explained",
      "stormwater-fee-on-water-bill-explained",
      "sewer-averaging-water-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: a new drought charge appears on the bill",
        content: (
          <>
            <p className="lead">
              You open your bill and see a drought surcharge you did not have last
              season. It can feel like a penalty, but it usually funds supply
              protection and conservation efforts during shortages.
            </p>
            <p>
              This guide explains what the charge is, when it appears, and how to
              reduce its impact without guessing. For a bigger picture of how
              water bills are structured, start with
              <a href="/water-explained"> water service explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#why-exists">Why drought surcharges exist</a></li>
              <li><a href="#how-calculated">How drought surcharges are calculated</a></li>
              <li><a href="#where-listed">Where it shows up on the bill</a></li>
              <li><a href="#reduce-impact">How to reduce the impact</a></li>
              <li><a href="#mistakes">Common mistakes</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              A drought surcharge is a temporary charge used to cover the higher
              cost of water supply and conservation programs during droughts. It
              usually ends when drought conditions improve.
            </p>
          </>
        )
      },
      {
        id: "why-exists",
        title: "Why drought surcharges exist",
        content: (
          <>
            <p>
              Droughts reduce available water supplies and raise the cost of
              treating and delivering water. Utilities may need to buy water from
              alternate sources or invest in conservation programs, both of which
              cost more than normal operations.
            </p>
            <figure>
              <ContentImage
                src="https://images.unsplash.com/photo-1501785888041-af3ef285b470"
                alt="Dry hills and sparse vegetation under a bright sky"
              />
              <figcaption>Shortages raise the cost of supply and treatment.</figcaption>
            </figure>
            <p>
              The surcharge spreads those extra costs across customers rather than
              raising the base rate permanently.
            </p>
          </>
        )
      },
      {
        id: "how-calculated",
        title: "How drought surcharges are calculated",
        content: (
          <>
            <p>
              Utilities handle this in different ways, but the most common methods
              are:
            </p>
            <ul>
              <li>A flat monthly charge added to every bill</li>
              <li>A per-unit fee (per CCF or per 1,000 gallons)</li>
              <li>An extra percentage added to the water usage line</li>
            </ul>
            <p>
              Many drought plans also tighten outdoor watering rules. That means
              it is easier to cross a tier threshold if you keep the same habits.
              See <a href="/blog/tiered-water-rates-explained">tiered rates</a> if
              your bill uses tiers.
            </p>
          </>
        )
      },
      {
        id: "where-listed",
        title: "Where it shows up on the bill",
        content: (
          <>
            <p>
              Drought charges are often listed as separate line items. Look for
              labels like:
            </p>
            <ul>
              <li>Drought surcharge</li>
              <li>Water shortage fee</li>
              <li>Conservation charge</li>
            </ul>
            <p>
              If you see multiple new line items, compare them with
              <a href="/blog/water-service-charge-explained"> water service charges</a>
              so you can separate fixed fees from temporary ones.
            </p>
          </>
        )
      },
      {
        id: "reduce-impact",
        title: "How to reduce the impact",
        content: (
          <>
            <p>
              The best defense is lowering usage during drought months, especially
              outdoor use. Small changes can keep you under a higher tier and
              reduce the per-unit surcharge impact.
            </p>
            <ul>
              <li>Reduce lawn watering frequency and duration</li>
              <li>Fix toilet leaks and dripping faucets quickly</li>
              <li>Track your weekly usage to catch spikes early</li>
            </ul>
            <p>
              If you are unsure what normal usage looks like, start with
              <a href="/blog/average-water-usage-per-person"> average usage ranges</a>.
            </p>
          </>
        )
      },
      {
        id: "mistakes",
        title: "Common mistakes",
        content: (
          <>
            <ul>
              <li>
                <strong>Assuming it is permanent.</strong> Drought surcharges are
                typically temporary and are removed when conditions improve.
              </li>
              <li>
                <strong>Confusing it with stormwater fees.</strong> Stormwater fees
                are often based on property drainage, not drought conditions.
              </li>
              <li>
                <strong>Ignoring outdoor use rules.</strong> Violating restrictions
                can lead to extra penalties in some service areas.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What is a drought surcharge on a water bill?",
        answer:
          "It is a temporary charge used to cover higher supply and conservation costs during drought conditions."
      },
      {
        question: "Is a drought surcharge permanent?",
        answer:
          "Usually no. It is typically removed when drought conditions improve and costs normalize."
      },
      {
        question: "How is the drought surcharge calculated?",
        answer:
          "It may be a flat monthly fee, a per-unit charge, or a percentage added to usage charges."
      },
      {
        question: "How can I lower a drought surcharge?",
        answer:
          "Reduce water use during drought months, especially outdoor watering, and avoid crossing higher tiers."
      }
    ]
  },
  {
    slug: "stormwater-fee-on-water-bill-explained",
    title: "Stormwater Fee on Your Water Bill Explained: What It Pays For and How It Is Set",
    description:
      "Stormwater fees help fund drainage, flood prevention, and clean runoff programs. Learn how fees are calculated and why they appear on water bills.",
    category: "Water",
    keyword: "stormwater fee",
    date: "2025-12-28",
    readTime: "12 min read",
    image: {
      src: "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
      alt: "Rainwater flowing along a curb into a street drain"
    },
    relatedSlugs: [
      "water-service-charge-explained",
      "how-sewer-charges-work-on-your-water-bill",
      "sewer-averaging-water-bill-explained",
      "tiered-water-rates-explained",
      "drought-surcharge-on-water-bill-explained",
      "why-did-my-water-bill-suddenly-increase"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: a stormwater fee shows up on a water bill",
        content: (
          <>
            <p className="lead">
              You see a stormwater fee even though you did not use more water. That
              is because stormwater charges are usually about drainage and runoff,
              not household usage.
            </p>
            <p>
              This guide explains what stormwater fees fund, how they are set, and
              how to tell them apart from sewer charges. For the overall bill
              structure, start with <a href="/water-explained">water service explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#what-pays-for">What stormwater fees pay for</a></li>
              <li><a href="#how-set">How stormwater fees are set</a></li>
              <li><a href="#sewer-difference">Stormwater fees vs sewer charges</a></li>
              <li><a href="#reduce-impact">Ways to reduce the impact</a></li>
              <li><a href="#mistakes">Common mistakes</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              A stormwater fee funds drainage systems, flood prevention, and runoff
              cleanup. It is usually based on property characteristics, not water
              usage.
            </p>
          </>
        )
      },
      {
        id: "what-pays-for",
        title: "What stormwater fees pay for",
        content: (
          <>
            <p>
              Stormwater systems handle rain runoff from streets, roofs, parking
              lots, and other hard surfaces. Fees help pay for:
            </p>
            <ul>
              <li>Storm drains and collection pipes</li>
              <li>Flood control projects and retention ponds</li>
              <li>Street sweeping and debris removal</li>
              <li>Waterway cleanup and compliance programs</li>
            </ul>
            <figure>
              <ContentImage
                src="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429"
                alt="Stormwater flowing into a drain during rainfall"
              />
              <figcaption>Stormwater systems keep runoff from damaging roads and waterways.</figcaption>
            </figure>
          </>
        )
      },
      {
        id: "how-set",
        title: "How stormwater fees are set",
        content: (
          <>
            <p>
              Many utilities base the fee on property size or impervious surface
              area (roofs, driveways, patios). Common approaches include:
            </p>
            <ul>
              <li>A flat monthly fee for residential properties</li>
              <li>A fee tied to impervious area tiers</li>
              <li>Credits for approved drainage improvements</li>
            </ul>
            <p>
              Because it is based on property features, the fee does not change
              much when your water usage changes.
            </p>
          </>
        )
      },
      {
        id: "sewer-difference",
        title: "Stormwater fees vs sewer charges",
        content: (
          <>
            <p>
              Stormwater fees are different from sewer charges. Sewer charges fund
              wastewater treatment based on water usage, while stormwater fees fund
              runoff management based on property drainage.
            </p>
            <p>
              If you want to understand sewer charges, start with
              <a href="/blog/how-sewer-charges-work-on-your-water-bill"> how sewer charges work</a>
              and <a href="/blog/sewer-averaging-water-bill-explained"> sewer averaging</a>.
            </p>
          </>
        )
      },
      {
        id: "reduce-impact",
        title: "Ways to reduce the impact",
        content: (
          <>
            <p>
              Some utilities offer credits if you reduce runoff from your property.
              Common examples include rain gardens, permeable pavers, or rain
              barrels. Check local rules before making changes.
            </p>
            <p>
              If your bill also looks higher because of usage, compare with
              <a href="/blog/why-did-my-water-bill-suddenly-increase"> spike troubleshooting</a>
              so you can separate fixed fees from usage changes.
            </p>
          </>
        )
      },
      {
        id: "mistakes",
        title: "Common mistakes",
        content: (
          <>
            <ul>
              <li>
                <strong>Assuming stormwater fees are tied to usage.</strong> They
                are usually based on property drainage, not gallons used.
              </li>
              <li>
                <strong>Confusing stormwater and sewer charges.</strong> Sewer is
                wastewater treatment, stormwater is runoff control.
              </li>
              <li>
                <strong>Missing credit programs.</strong> Some utilities offer
                credits for runoff reductions, but you must apply.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What is a stormwater fee on a water bill?",
        answer:
          "It is a charge that funds drainage and runoff management systems, usually based on property characteristics."
      },
      {
        question: "Is a stormwater fee based on water usage?",
        answer:
          "Usually no. Many utilities set stormwater fees based on property size or impervious surface area."
      },
      {
        question: "Why do I pay stormwater if I already pay sewer?",
        answer:
          "Sewer charges fund wastewater treatment from indoor use. Stormwater fees fund runoff management from rain and streets."
      },
      {
        question: "Can I reduce my stormwater fee?",
        answer:
          "Some utilities offer credits for approved runoff reductions like rain gardens or permeable surfaces."
      }
    ]
  }
];
