import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import AdSlot from "@/components/AdSlot";
import Breadcrumbs from "@/components/Breadcrumbs";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Water Service Explained: Complete Guide to Understanding Water Bills",
  description:
    "Learn how water is measured, how water bills are structured, what drives water costs, and how to manage usage in plain English.",
  alternates: {
    canonical: `${siteConfig.url}/water-explained`
  },
  robots: {
    index: true,
    follow: true,
    "max-image-preview": "large",
    "max-snippet": -1
  }
};

export default function WaterExplainedPage() {
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: "Water Service Explained: Complete Guide to Understanding Water Bills",
    description:
      "Learn how water is measured, how water bills are structured, what drives water costs, and how to manage usage in plain English.",
    author: {
      "@type": "Organization",
      name: siteConfig.name
    },
    publisher: {
      "@type": "Organization",
      name: siteConfig.name
    },
    datePublished: "2024-12-01",
    dateModified: new Date().toISOString(),
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `${siteConfig.url}/water-explained`
    }
  };

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: [
      {
        "@type": "ListItem",
        position: 1,
        name: "Home",
        item: siteConfig.url
      },
      {
        "@type": "ListItem",
        position: 2,
        name: "Water Service Explained",
        item: `${siteConfig.url}/water-explained`
      }
    ]
  };

  return (
    <div className="container section">
      <Breadcrumbs
        items={[
          { label: "Home", href: "/" },
          { label: "Water Service Explained" }
        ]}
      />
      <h1>Water Service Explained: Your Complete Guide</h1>
      
      <div className="hero-card">
        <Image
          src="/images/utility-water.jpg"
          alt="Clean water flowing from a modern faucet"
          width={800}
          height={450}
          className="hero-image"
          sizes="(max-width: 768px) 100vw, 800px"
          priority
        />
      </div>

      <p className="intro-text">
        Water service brings fresh water to your home and removes wastewater through sewer systems. Water bills often include both water and sewer charges, plus fixed fees. This guide explains how water is measured, how you are billed, what drives usage, and how to detect problems--all in plain, straightforward language.
      </p>

      <section>
        <h2>How water service works</h2>
        <p>
          Your local water utility treats water from wells, rivers, or reservoirs to make it safe for drinking and household use. The water flows through underground pipes to your neighborhood, then through a service line to your home.
        </p>
        <p>
          A water meter measures how much water enters your home. Everything you use--showers, toilets, laundry, cooking, outdoor watering--passes through the meter. The utility reads the meter monthly or bi-monthly and bills you for what you used.
        </p>
        <p>
          Wastewater (sewage) leaves your home through a separate drain system and goes to a treatment plant. Most utilities charge for sewer service based on water usage, since what goes in usually comes back out. Some systems use a winter average to estimate sewer charges, which avoids charging for outdoor water that does not enter the sewer.
        </p>
      </section>

      <section>
        <h2>How water is measured: gallons, cubic feet, and CCF</h2>
        <p>
          Water is measured by volume. The most common units on residential bills are <strong>gallons</strong> or <strong>cubic feet</strong>. One cubic foot equals 7.48 gallons.
        </p>
        <p>
          Some utilities use <strong>CCF (hundred cubic feet)</strong> as the billing unit. One CCF equals 100 cubic feet, or 748 gallons. A few utilities use <strong>thousand gallons (kgal)</strong> instead.
        </p>
        <p>
          Your bill should state which unit is used. If you see a number like "6 CCF," that means you used 600 cubic feet, or about 4,488 gallons. If the bill lists gallons directly, the conversion is simpler.
        </p>
        <p>
          Knowing the unit helps you translate meter readings into bill charges and estimate the cost of specific activities like filling a pool or watering a lawn.
        </p>
      </section>

      <section>
        <h2>Understanding your water bill</h2>
        <p>
          Water bills typically include water charges, sewer charges, and fixed fees. Some bills also include stormwater or drainage fees.
        </p>
        <h3>Water charge</h3>
        <p>
          This is the cost of the water you used. It may be a flat rate per unit or a tiered rate that increases as you use more. For example, the first 5 CCF might cost $3 per CCF, and anything above that might cost $5 per CCF.
        </p>
        <h3>Sewer charge</h3>
        <p>
          This covers the cost of treating wastewater. It is often calculated as a percentage of water usage or as a flat rate per unit. Some utilities cap sewer charges or use a winter average to avoid charging for outdoor watering.
        </p>
        <h3>Fixed fees</h3>
        <p>
          Most bills include a base charge or meter fee that you pay even if you use very little water. This covers the cost of maintaining infrastructure, meter reading, and billing.
        </p>
        <h3>Stormwater and other charges</h3>
        <p>
          Some utilities charge for stormwater management based on property size or impervious surface area. These charges help fund drainage systems and flood prevention.
        </p>
      </section>

      <section>
        <h2>Tiered water pricing and conservation rates</h2>
        <p>
          Many utilities use tiered pricing to encourage conservation. Lower usage is billed at a lower rate per unit, and higher usage is billed at progressively higher rates.
        </p>
        <p>
          For example, the first 3 CCF might cost $2.50 per CCF, the next 7 CCF might cost $4 per CCF, and anything above 10 CCF might cost $6 per CCF. This structure rewards efficiency and discourages waste.
        </p>
        <p>
          If you are close to a tier threshold, small reductions in usage can keep you in a lower-cost tier and reduce the total bill.
        </p>
        <p>
          Some utilities also offer lifeline rates for low-income households or fixed-income seniors. Ask your utility about available programs.
        </p>
      </section>

      <section>
        <h2>What uses the most water in a typical home?</h2>
        <p>
          Toilets are usually the largest indoor water user, accounting for 20% to 30% of total household usage. Older toilets use 3.5 to 5 gallons per flush, while newer models use 1.28 gallons or less.
        </p>
        <p>
          Showers and baths account for 15% to 25% of indoor use. A standard showerhead uses about 2.5 gallons per minute, while low-flow models use 1.5 to 2 gallons per minute.
        </p>
        <p>
          Washing machines use 10% to 20% of indoor water. Older top-loading machines use more water than newer high-efficiency models.
        </p>
        <p>
          Faucets (kitchen and bathroom sinks) account for another 15% to 20%. Dishwashers use a smaller share, usually 5% to 10%, because they are efficient compared to hand washing.
        </p>
        <p>
          Outdoor watering can easily exceed all indoor use combined. Lawns, gardens, and irrigation systems can use thousands of gallons per month in warm, dry climates.
        </p>
      </section>

      <section>
        <h2>Seasonal changes and why water bills vary</h2>
        <p>
          Water bills often spike in summer due to outdoor watering. Lawns, gardens, and pools require significant water, especially during hot, dry weather.
        </p>
        <p>
          Winter bills are usually lower because outdoor use drops to zero in most climates. Comparing winter and summer usage helps you estimate how much water goes to outdoor activities.
        </p>
        <p>
          Billing cycles can also vary in length. A 60-day billing cycle will cost more than a 30-day cycle even if daily usage stays the same. Always compare usage per day to see whether actual consumption changed.
        </p>
        <p>
          Household changes like guests, new appliances, or lifestyle shifts can also affect usage. Tracking water use over several months helps you identify normal patterns and spot unusual spikes.
        </p>
      </section>

      <section>
        <h2>How to read your water meter</h2>
        <p>
          Most water meters are either dial meters or digital meters. Dial meters have a series of small dials that you read from left to right. If the hand is between two numbers, record the lower number.
        </p>
        <p>
          Digital meters display the reading directly, usually in cubic feet or gallons. Some meters cycle through multiple screens, so wait for the total usage screen.
        </p>
        <p>
          To verify your bill, compare the current meter reading to the previous reading listed on the bill. The difference is your usage. If the units do not match, use the conversion: 1 cubic foot = 7.48 gallons.
        </p>
        <p>
          Many meters have a leak indicator--a small triangle, dial, or flashing light that moves when water is flowing. If it moves when all water is turned off, you likely have a leak.
        </p>
      </section>

      <section>
        <h2>How to detect leaks and reduce waste</h2>
        <p>
          Leaks are a common cause of high water bills. Even small leaks can waste hundreds of gallons per month.
        </p>
        <h3>Toilet leak test</h3>
        <p>
          Add a few drops of food coloring to the toilet tank and wait 15 minutes without flushing. If color appears in the bowl, the flapper is leaking and should be replaced.
        </p>
        <h3>Meter leak test</h3>
        <p>
          Turn off all water in the home, then check the meter. If the leak indicator moves or the reading changes after an hour, water is flowing somewhere.
        </p>
        <h3>Common leak sources</h3>
        <ul>
          <li>Toilet flappers (most common indoor leak)</li>
          <li>Dripping faucets and showerheads</li>
          <li>Leaking washing machine hoses</li>
          <li>Broken sprinkler lines or irrigation valves</li>
          <li>Outdoor hose bibs left partially open</li>
        </ul>
        <p>
          Fixing leaks quickly can save thousands of gallons per month and significantly reduce your bill.
        </p>
      </section>

      <section>
        <h2>How to reduce water usage without major changes</h2>
        <ul>
          <li>Fix running toilets and dripping faucets immediately.</li>
          <li>Take shorter showers or install a low-flow showerhead.</li>
          <li>Run dishwashers and washing machines only with full loads.</li>
          <li>Turn off the faucet while brushing teeth or washing dishes.</li>
          <li>Use a broom instead of a hose to clean driveways and sidewalks.</li>
          <li>Water lawns early in the morning to reduce evaporation.</li>
          <li>Adjust irrigation schedules based on rainfall.</li>
          <li>Install rain sensors on automatic sprinkler systems.</li>
          <li>Use mulch around plants to retain soil moisture.</li>
          <li>Consider drought-tolerant landscaping in dry climates.</li>
        </ul>
        <p>
          Small changes add up. Reducing usage by 10% to 15% can lower monthly bills and help during droughts or water restrictions.
        </p>
      </section>

      <AdSlot label="Mid-page ad" />

      <section>
        <h2>Common misconceptions about water service</h2>
        <h3>Misconception: Running water while the dishwasher runs wastes more water</h3>
        <p>
          Dishwashers use a fixed amount of water per cycle regardless of what else is happening. Running a faucet at the same time does add to total usage, but the dishwasher itself uses the same amount either way.
        </p>
        <h3>Misconception: Low-flow fixtures sacrifice performance</h3>
        <p>
          Modern low-flow showerheads and faucets are designed to maintain pressure and comfort while using less water. Most users do not notice a difference in performance.
        </p>
        <h3>Misconception: Water meters are always accurate</h3>
        <p>
          Water meters are generally very accurate, but they can fail or slow down over time. If your usage seems unusually high, request a meter test from your utility. Some charge a fee if the meter is found to be accurate.
        </p>
      </section>

      <section>
        <h2>Estimated readings and bill corrections</h2>
        <p>
          Some utilities estimate usage if they cannot access the meter. The next actual reading corrects the estimate, which can cause a higher or lower bill.
        </p>
        <p>
          If your bill says "estimated," you can often submit your own meter reading online or by phone to get an accurate bill. Take a photo of the meter for your records.
        </p>
        <p>
          If you believe a bill is incorrect, compare the reading on the bill to your meter. If they do not match, contact the utility and request a review.
        </p>
      </section>

      <section>
        <h2>Related guides to deepen your understanding</h2>
        <p>
          Now that you understand the basics of water service, explore these specific topics to answer common questions and manage your water bills more effectively:
        </p>
        <ul>
          <li>
            <Link href="/blog/how-to-read-a-water-meter">
              How to read a water meter (and know if it is accurate)
            </Link> -- Step-by-step guide to reading and checking your meter.
          </li>
          <li>
            <Link href="/blog/why-did-my-water-bill-suddenly-increase">
              Why did my water bill suddenly increase?
            </Link> -- Understand common causes of spikes and how to troubleshoot.
          </li>
          
          <li>
            <Link href="/blog/what-is-ccf-on-a-water-bill">
              What is CCF on a water bill?
            </Link> - Convert cubic feet to gallons and costs.
          </li>
          <li>
            <Link href="/blog/water-meter-leak-indicator-explained">
              Water meter leak indicator explained
            </Link> - Spot continuous use before it spikes your bill.
          </li>
          <li>
            <Link href="/blog/is-your-toilet-running-leak-test">
              Is your toilet running? Simple leak test
            </Link> - A quick check that saves hundreds of gallons.
          </li>
          <li>
            <Link href="/blog/how-sewer-charges-work-on-your-water-bill">
              How sewer charges work on your water bill
            </Link> - Understand wastewater pricing and averages.
          </li>
          <li>
            <Link href="/blog/water-service-charge-explained">
              Water service charge explained
            </Link> - See why a fixed fee appears every month.
          </li>
          <li>
            <Link href="/blog/tiered-water-rates-explained">
              Tiered water rates explained
            </Link> - Learn how higher use raises the price per unit.
          </li>
          <li>
            <Link href="/blog/why-is-my-water-bill-higher-in-summer">
              Why is my water bill higher in summer?
            </Link> - Outdoor watering and seasonal drivers.
          </li>
        </ul>
      </section>

      <section>
        <h2>Frequently asked questions</h2>
        <h3>How much water does the average person use per day?</h3>
        <p>
          In the United States, a typical person uses 40 to 80 gallons per day for indoor activities. Outdoor watering can add significantly more.
        </p>
        <h3>Why is my sewer charge higher than my water charge?</h3>
        <p>
          Wastewater treatment is expensive. Many utilities charge more for sewer service because treatment plants require significant maintenance and energy.
        </p>
        <h3>Can I lower my water bill if I don't have a lawn?</h3>
        <p>
          Yes. Indoor conservation measures like fixing leaks, taking shorter showers, and running full loads in appliances can all reduce usage and lower your bill.
        </p>
        <h3>What is a winter average, and how does it affect my bill?</h3>
        <p>
          Some utilities calculate sewer charges based on winter water usage, when outdoor watering is minimal. This average is used year-round to avoid charging sewer fees for water that goes to lawns or pools.
        </p>
        <h3>Should I worry about a small drip from a faucet?</h3>
        <p>
          Yes. A slow drip can waste 10 to 20 gallons per day, which adds up to hundreds of gallons per month. Fixing drips is usually simple and inexpensive.
        </p>
      </section>

      <section>
        <h2>Final thoughts</h2>
        <p>
          Water service is essential for daily life, but understanding how it is measured and billed gives you control over costs. Start by reading your bill carefully, checking for leaks, and tracking usage over a few billing cycles. Small changes like fixing leaks and adjusting outdoor watering can reduce usage significantly without major effort or expense.
        </p>
        <p>
          For broader utility budgeting advice, visit our <Link href="/utility-bills-costs-explained">utility bills and costs guide</Link>. To compare water costs to other utilities, see our guides on <Link href="/electricity-explained">electricity</Link> and <Link href="/gas-explained">natural gas</Link>.
        </p>
      </section>

      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
      />
    </div>
  );
}
