import type { Post } from "@/lib/types";

export const electricityPillarTieredDemandSupplyPosts_2025_12_26: Post[] = [
  {
    slug: "tiered-electricity-rates-explained",
    title: "Tiered Electricity Rates Explained (Tier 1 vs Tier 2 on Your Bill)",
    description:
      "Tiered rates can make a small usage increase look like a big price jump. This guide explains how tiers work, where they show up, and why the total changes.",
    category: "Electricity",
    keyword: "tiered electricity rates explained",
    date: "2025-12-26",
    readTime: "14 min read",
    image: {
      src: "/images/utility-electricity.jpg",
      alt: "Home at dusk with lights on and power lines in the foreground"
    },
    relatedSlugs: [
      "electricity-explained",
      "what-is-a-kilowatt-hour",
      "electric-bill-breakdown-understanding-line-items",
      "time-of-use-electricity-rates",
      "why-is-my-electric-bill-so-high-this-month",
      "demand-charge-electric-bill-explained",
      "supply-vs-delivery-charges-electricity"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: you used a little more, but the price jumped a lot",
        content: (
          <>
            <p className="lead">
              If your electric bill suddenly jumped and you did not change much,
              tiered pricing is often the hidden reason. You cross a threshold,
              and the next block of electricity costs more. It feels like a penalty,
              but it is just how the rate is structured.
            </p>
            <p>
              This guide turns tiered rates into something you can see and predict.
              If you want the full electricity basics first, start with
              <a href="/electricity-explained"> Electricity Explained</a>.
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
              <li><a href="#quick-answer">The short answer</a></li>
              <li><a href="#how-tiered-works">How tiered rates work (simple example)</a></li>
              <li><a href="#where-on-bill">Where tiers show up on your bill</a></li>
              <li><a href="#why-jump">Why the total jumps even with small changes</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The short answer (what tiered really means)",
        content: (
          <>
            <p>
              <strong>Tiered electricity rates</strong> mean your price per kWh changes
              after you use a certain amount of electricity. The first block is
              cheaper, and the next block costs more.
            </p>
            <p>
              It is not that your whole bill switches to a higher price. Only the
              usage above the threshold moves into the higher tier.
            </p>
          </>
        )
      },
      {
        id: "how-tiered-works",
        title: "How tiered rates work (simple example)",
        content: (
          <>
            <p>
              Think of tiers like steps. The first step is the baseline. The next
              step is more expensive. Many utilities set a baseline for a month
              and then raise the price after you pass it.
            </p>
            <h3>Baseline allowance and thresholds</h3>
            <p>
              A common structure looks like this:
            </p>
            <ul>
              <li>Tier 1: first 500 kWh at a lower price</li>
              <li>Tier 2: everything above 500 kWh at a higher price</li>
            </ul>
            <p>
              If you used 520 kWh, only 20 kWh are billed at Tier 2. That is why
              understanding <a href="/blog/what-is-a-kilowatt-hour">what a kWh is</a>
              helps the numbers feel less random.
            </p>
            <h3>Why the next tier costs more</h3>
            <p>
              Utilities often price the extra block higher to reduce peak demand and
              encourage conservation. It is a pricing structure, not a personal
              judgment. Once you see the threshold, the bill feels predictable.
            </p>
          </>
        )
      },
      {
        id: "where-on-bill",
        title: "Where tiers show up on your bill",
        content: (
          <>
            <p>
              Most bills list usage charges in separate lines. You might see
              "Tier 1\" and \"Tier 2\" or \"Baseline\" and \"Over Baseline."
            </p>
            <p>
              If your bill has many lines, this walkthrough helps you find the
              right section:
              <a href="/blog/electric-bill-breakdown-understanding-line-items"> Electric bill breakdown</a>.
            </p>
          </>
        )
      },
      {
        id: "why-jump",
        title: "Why the total jumps even with small changes",
        content: (
          <>
            <p>
              Two small shifts can cause a big total change:
            </p>
            <ul>
              <li>You crossed the tier threshold by a small amount.</li>
              <li>Your billing cycle was longer, so you used more days.</li>
            </ul>
            <p>
              Ask yourself: did this bill have more days? If so, compare kWh per
              day, not total kWh. The checklist is in
              <a href="/blog/why-is-my-electric-bill-so-high-this-month"> this bill-spike guide</a>.
            </p>
            <p>
              Also note the difference between tiered rates and time-of-use pricing.
              Time-of-use is about <em>when</em> you use power, not how much.
              If you see peak and off-peak lines, read
              <a href="/blog/time-of-use-electricity-rates"> time-of-use electricity rates</a>.
            </p>
            <p>
              If your bill also lists a separate demand charge, that is a different
              concept. See
              <a href="/blog/demand-charge-electric-bill-explained"> demand charges explained</a>.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>"All my kWh are billed at the higher rate."</strong> No.
                Only the usage above the threshold is billed at the higher tier.
              </li>
              <li>
                <strong>"Tiered rates and time-of-use are the same."</strong> Tiered
                is based on total usage. Time-of-use is based on time of day.
              </li>
              <li>
                <strong>"Tiered rates mean the utility made a mistake."</strong>
                It is a common pricing structure, not an error.
              </li>
            </ul>
            <p>
              If you also see separate supply and delivery charges, that is another
              layer of the bill. This guide keeps them clear:
              <a href="/blog/supply-vs-delivery-charges-electricity"> supply vs delivery charges</a>.
            </p>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What are tiered electricity rates?",
        answer:
          "Tiered rates mean the price per kWh changes after you use a certain amount of electricity. The first block is cheaper, and the next block costs more."
      },
      {
        question: "Does a higher tier apply to my whole bill?",
        answer:
          "No. Only the usage above the tier threshold is billed at the higher price. The first block stays at the lower price."
      },
      {
        question: "Why did my bill jump when my usage barely changed?",
        answer:
          "Small increases can push you into a higher tier, and longer billing cycles add days of usage. Compare kWh per day to see the real change."
      },
      {
        question: "Where do tiers show up on an electric bill?",
        answer:
          "They usually appear as separate usage lines labeled Tier 1 and Tier 2, or Baseline and Over Baseline."
      },
      {
        question: "Are tiered rates the same as time-of-use rates?",
        answer:
          "No. Tiered rates depend on total usage. Time-of-use rates depend on when you use electricity."
      }
    ]
  },
  {
    slug: "demand-charge-electric-bill-explained",
    title: "Demand Charges on Electric Bills Explained (Why Your Peak Usage Matters)",
    description:
      "A demand charge is based on your highest short-term usage, not your monthly total. Learn how it is measured and where it appears on your bill.",
    category: "Electricity",
    keyword: "demand charge electric bill",
    date: "2025-12-26",
    readTime: "15 min read",
    image: {
      src: "/images/utility-electricity.jpg",
      alt: "Electric meter and utility equipment on a building exterior"
    },
    relatedSlugs: [
      "electricity-explained",
      "what-is-a-kilowatt-hour",
      "electric-bill-breakdown-understanding-line-items",
      "why-is-my-electric-bill-so-high-this-month",
      "tiered-electricity-rates-explained",
      "supply-vs-delivery-charges-electricity"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: your total is normal, but one line is huge",
        content: (
          <>
            <p className="lead">
              Some electric bills include a line called "demand charge" that feels
              wildly out of proportion. You did not double your monthly usage, but
              that line can still be large. The missing detail is that demand charges
              are about a short peak, not your whole month.
            </p>
            <p>
              This guide explains demand charges in plain English, and how to spot
              them on your bill. If you want the full electricity overview first,
              start with <a href="/electricity-explained">Electricity Explained</a>.
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
              <li><a href="#quick-answer">The short answer</a></li>
              <li><a href="#demand-vs-energy">Demand vs energy: kW vs kWh</a></li>
              <li><a href="#how-measured">How peak demand is measured</a></li>
              <li><a href="#where-on-bill">Where demand charges appear</a></li>
              <li><a href="#who-sees">Who usually sees demand charges</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The short answer (what a demand charge is)",
        content: (
          <>
            <p>
              A <strong>demand charge</strong> is a fee based on your highest short-term
              electricity use during the billing period. It is measured in kW
              (how fast you used power), not kWh (how much you used overall).
            </p>
            <p>
              One short spike can set your demand charge for the whole month.
            </p>
          </>
        )
      },
      {
        id: "demand-vs-energy",
        title: "Demand vs energy: kW vs kWh in plain English",
        content: (
          <>
            <p>
              This is the core confusion:
            </p>
            <ul>
              <li><strong>kW (kilowatt)</strong> is how fast you are using electricity.</li>
              <li><strong>kWh (kilowatt-hour)</strong> is how much you used over time.</li>
            </ul>
            <p>
              A demand charge uses kW. The rest of your bill uses kWh. If you need a
              refresher, this guide explains the difference:
              <a href="/blog/what-is-a-kilowatt-hour"> what a kWh is</a>.
            </p>
          </>
        )
      },
      {
        id: "how-measured",
        title: "How peak demand is measured",
        content: (
          <>
            <p>
              Utilities measure demand in short windows, often 15 to 60 minutes.
              They look for your highest average within one of those windows.
            </p>
            <h3>Why one short spike matters</h3>
            <p>
              If multiple high-power devices run at the same time, your peak can
              jump. That one interval can set the demand charge line for the month.
            </p>
            <p>
              It helps to ask: when do many large loads overlap? Heating, cooling,
              dryers, and electric vehicle charging are common overlap points.
            </p>
          </>
        )
      },
      {
        id: "where-on-bill",
        title: "Where demand charges appear on the bill",
        content: (
          <>
            <p>
              Demand charges usually show as a separate line, labeled "Demand"
              or "kW demand." The rate is often written as a price per kW.
            </p>
            <p>
              If your bill has many lines, this guide helps you find the right
              section:
              <a href="/blog/electric-bill-breakdown-understanding-line-items"> electric bill breakdown</a>.
            </p>
          </>
        )
      },
      {
        id: "who-sees",
        title: "Who usually sees demand charges (and who does not)",
        content: (
          <>
            <p>
              Demand charges are more common on commercial and industrial accounts.
              Some utilities also apply them to large residential loads or special
              rate plans. Many households never see them.
            </p>
            <p>
              If your bill does not list a demand line item, this article is mainly
              for reference. If it does, the concept matters.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>"Demand charges are based on my total usage."</strong> No.
                They are based on your highest short-term usage.
              </li>
              <li>
                <strong>"If I cut kWh, demand charges always fall."</strong> Not
                necessarily. A short spike can still set a high demand.
              </li>
              <li>
                <strong>"Demand charges mean a billing error."</strong> They are
                a standard rate component for some plans.
              </li>
            </ul>
            <p>
              If your bill also uses tiered pricing, that is a separate structure.
              See <a href="/blog/tiered-electricity-rates-explained">tiered rates explained</a>.
            </p>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What is a demand charge on an electric bill?",
        answer:
          "A demand charge is a fee based on your highest short-term electricity use (kW) during the billing period, not the total kWh for the month."
      },
      {
        question: "How is peak demand measured?",
        answer:
          "Utilities measure usage in short windows, often 15 to 60 minutes, and bill based on the highest average in one of those windows."
      },
      {
        question: "Why is my demand charge high if my total usage is normal?",
        answer:
          "A single short spike can set the demand charge for the month even if your overall kWh is average."
      },
      {
        question: "Do all residential customers have demand charges?",
        answer:
          "No. Many residential plans do not include demand charges. They are more common for commercial accounts or special rate plans."
      },
      {
        question: "Where do demand charges show on the bill?",
        answer:
          "They usually appear as a separate line labeled Demand or kW Demand, with a price per kW."
      }
    ]
  },
  {
    slug: "supply-vs-delivery-charges-electricity",
    title: "Supply vs Delivery Charges Explained (Generation vs Distribution on Electric Bills)",
    description:
      "Your electric bill usually has two main buckets: supply and delivery. This guide explains what each one covers and why both show up.",
    category: "Electricity",
    keyword: "supply vs delivery charges electricity",
    date: "2025-12-26",
    readTime: "14 min read",
    image: {
      src: "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
      alt: "Power lines stretching across an open landscape"
    },
    relatedSlugs: [
      "electricity-explained",
      "electric-bill-breakdown-understanding-line-items",
      "fixed-vs-variable-rate-electricity-plan",
      "what-is-a-kilowatt-hour",
      "why-is-my-electricity-bill-so-high-in-summer",
      "tiered-electricity-rates-explained",
      "demand-charge-electric-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: two big charges that sound the same",
        content: (
          <>
            <p className="lead">
              Many people open an electric bill and see two large sections:
              "Supply" and "Delivery." Both say electricity, so why are there two?
              That split is real, and it is one of the fastest ways to make a bill
              feel less confusing.
            </p>
            <p>
              This guide separates those two buckets in plain English. If you want
              the full electricity overview, start with
              <a href="/electricity-explained"> Electricity Explained</a>.
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
              <li><a href="#quick-answer">The short answer</a></li>
              <li><a href="#supply">Supply charges (generation)</a></li>
              <li><a href="#delivery">Delivery charges (grid and service)</a></li>
              <li><a href="#compare">How to compare bills month to month</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The short answer (two charges, two jobs)",
        content: (
          <>
            <p>
              <strong>Supply charges</strong> pay for the electricity itself, measured
              in kWh. <strong>Delivery charges</strong> pay for the grid that brings
              that electricity to your home, plus service and maintenance.
            </p>
            <p>
              Your bill splits them because they are different costs with different
              pricing rules.
            </p>
          </>
        )
      },
      {
        id: "supply",
        title: "Supply charges (what you are paying for)",
        content: (
          <>
            <p>
              Supply is the energy you used. It is usually priced per kWh.
              If the supply rate changes, the total can change even if your usage
              stays steady.
            </p>
            <h3>Who sets supply prices</h3>
            <p>
              In some areas, the utility sets the supply price. In others, you might
              see a separate supplier listed. Either way, the supply line is about
              the energy itself.
            </p>
            <p>
              If you see fixed vs variable pricing on the supply line, this overview
              helps explain it:
              <a href="/blog/fixed-vs-variable-rate-electricity-plan"> fixed vs variable rates</a>.
            </p>
          </>
        )
      },
      {
        id: "delivery",
        title: "Delivery charges (the grid and service cost)",
        content: (
          <>
            <p>
              Delivery covers the system that gets electricity to you:
              transmission lines, local distribution, meters, and service crews.
            </p>
            <h3>Transmission vs distribution</h3>
            <p>
              Transmission is the high-voltage network that moves power long distances.
              Distribution is the local network that brings it to your street and home.
            </p>
            <h3>Why delivery does not drop to zero</h3>
            <p>
              Even if usage is low, the grid still has to be available. That is why
              delivery charges often include fixed and variable parts.
            </p>
          </>
        )
      },
      {
        id: "compare",
        title: "How to compare bills month to month",
        content: (
          <>
            <p>
              Start with usage and days. Then compare supply rate and delivery totals
              separately. This keeps you from mixing two different drivers.
            </p>
            <ul>
              <li>Compare kWh used (and kWh per day).</li>
              <li>Check the supply rate per kWh.</li>
              <li>Compare delivery totals and any fixed fees.</li>
            </ul>
            <p>
              If you need a quick map of the line items, this guide helps:
              <a href="/blog/electric-bill-breakdown-understanding-line-items"> electric bill breakdown</a>.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>"Supply and delivery are the same thing."</strong> They are
                different costs: energy vs the grid.
              </li>
              <li>
                <strong>"Delivery should disappear if I use less."</strong> Delivery
                often includes fixed fees that do not scale with usage.
              </li>
              <li>
                <strong>"If supply changed, the utility made a mistake."</strong>
                Supply rates can change just like any price.
              </li>
            </ul>
            <p>
              If your bill also uses tiered pricing or demand charges, those are
              separate structures:
              <a href="/blog/tiered-electricity-rates-explained"> tiered rates</a> and
              <a href="/blog/demand-charge-electric-bill-explained"> demand charges</a>.
            </p>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What is the difference between supply and delivery charges?",
        answer:
          "Supply charges pay for the electricity you used. Delivery charges pay for the grid and service that bring that electricity to your home."
      },
      {
        question: "Why do I have two big charges on my electric bill?",
        answer:
          "Because the bill separates the cost of energy (supply) from the cost of delivering it (delivery). They are different parts of the system."
      },
      {
        question: "Can my supply charge change even if usage stays the same?",
        answer:
          "Yes. If the supply rate changes, the total can change even if your kWh is steady."
      },
      {
        question: "Why do I still pay delivery charges when I use less?",
        answer:
          "Delivery includes fixed costs to keep the grid available, plus variable charges. The fixed portion does not drop to zero."
      },
      {
        question: "Where can I see supply and delivery on the bill?",
        answer:
          "They are usually listed as separate sections or line items labeled Supply and Delivery (or Generation and Distribution)."
      }
    ]
  }
];
