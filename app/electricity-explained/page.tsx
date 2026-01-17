import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import AdSlot from "@/components/AdSlot";
import Breadcrumbs from "@/components/Breadcrumbs";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Electricity Explained: Complete Guide to Understanding Your Electric Service",
  description:
    "Learn everything about electricity bills, kWh usage, electric rates, delivery charges, and how your home electrical system works in plain English.",
  alternates: {
    canonical: `${siteConfig.url}/electricity-explained`
  },
  robots: {
    index: true,
    follow: true,
    "max-image-preview": "large",
    "max-snippet": -1
  }
};

export default function ElectricityExplainedPage() {
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: "Electricity Explained: Complete Guide to Understanding Your Electric Service",
    description: "Learn everything about electricity bills, kWh usage, electric rates, delivery charges, and how your home electrical system works in plain English.",
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
      "@id": `${siteConfig.url}/electricity-explained`
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
        name: "Electricity Explained",
        item: `${siteConfig.url}/electricity-explained`
      }
    ]
  };

  return (
    <div className="container section">
      <Breadcrumbs
        items={[
          { label: "Home", href: "/" },
          { label: "Electricity Explained" }
        ]}
      />
      <h1>Electricity Explained: Your Complete Guide</h1>
      
      <div className="hero-card">
        <Image
          src="/images/slots/c4b7cdc06ad74fbf2d969102/image.webp"
          alt="Electricity Explained: Your Complete Guide"
          width={1536}
          height={1024}
          className="hero-image"
          sizes="(max-width: 768px) 100vw, 800px"
          priority
          fetchPriority="high"
          data-slot-id="c4b7cdc06ad74fbf2d969102"
        />
      </div>

      <p className="intro-text">
        Electricity powers nearly everything in your home, yet electric bills can feel like a foreign language. This guide explains how electricity works, how it is measured, how you are billed, and what you can do to understand and manage your electric costs--all in plain English.
      </p>

      <section>
        <h2>What is electricity and how does it reach your home?</h2>
        <p>
          Electricity is the flow of electrical energy through wires. Power plants generate electricity using coal, natural gas, nuclear energy, or renewable sources like wind and solar. That electricity travels through high-voltage transmission lines to substations, then through distribution lines to your neighborhood, and finally through a service line to your home.
        </p>
        <p>
          Your home has a meter that measures how much electricity flows in. Everything you plug in or turn on uses some of that electricity. The utility company reads the meter monthly and bills you for what you used.
        </p>
        <p>
          Think of electricity like water flowing through pipes. The power plant is the water tower, the transmission lines are the main pipes, and your outlets are the taps. You only pay for what comes through your meter, just like you only pay for water that passes through your water meter.
        </p>
      </section>

      <section>
        <h2>How electricity is measured: watts, kilowatts, and kilowatt-hours</h2>
        <p>
          Electricity is measured in units that describe power and energy. <strong>Watts (W)</strong> measure how fast electricity is being used at a moment in time--like the speedometer in a car. A 100-watt light bulb uses 100 watts when it is on.
        </p>
        <p>
          <strong>Kilowatts (kW)</strong> are just 1,000 watts. It is easier to say "2 kilowatts" than "2,000 watts." Large appliances like air conditioners, electric dryers, and ovens often use multiple kilowatts when running.
        </p>
        <p>
          <strong>Kilowatt-hours (kWh)</strong> measure total energy used over time--like the odometer in a car. One kWh means using 1,000 watts for one hour. If you run a 1,000-watt space heater for one hour, you use 1 kWh. If you run a 100-watt bulb for 10 hours, that is also 1 kWh.
        </p>
        <p>
          Your electric bill charges you for kWh, not watts or kilowatts. The more kWh you use in a month, the higher your energy charge will be.
        </p>
        <p>
          To calculate kWh for any appliance, use this simple formula: (watts / 1,000) x hours used = kWh. For example, a 1,500-watt space heater running for 8 hours uses (1,500 / 1,000) x 8 = 12 kWh.
        </p>
      </section>

      <section>
        <h2>Understanding your electric bill</h2>
        <Image
          src="/images/slots/28ec758d5f555ff5430adbc4/image.webp"
          alt="Understanding your electric bill"
          width={1536}
          height={1024}
          sizes="(max-width: 768px) 100vw, 900px"
          loading="lazy"
          decoding="async"
          style={{ width: "100%", height: "auto", borderRadius: 12, margin: "1rem 0" }}
          data-slot-id="28ec758d5f555ff5430adbc4"
        />
        <p>
          Most electric bills have three main parts: the energy charge, the delivery charge, and fixed fees. Each part serves a different purpose.
        </p>
        <h3>Energy charge (supply charge)</h3>
        <p>
          This is the cost of the electricity itself. It is usually listed as a price per kWh. If your rate is $0.15 per kWh and you used 800 kWh, the energy charge is $120. Some areas let you choose your energy supplier, which can affect this rate.
        </p>
        <h3>Delivery charge (distribution charge)</h3>
        <Image
          src="/images/slots/01a8e8e113c3baa2c365dea7/image.webp"
          alt="Delivery charge (distribution charge)"
          width={1536}
          height={1024}
          sizes="(max-width: 768px) 100vw, 900px"
          loading="lazy"
          decoding="async"
          style={{ width: "100%", height: "auto", borderRadius: 12, margin: "1rem 0" }}
          data-slot-id="01a8e8e113c3baa2c365dea7"
        />
        <p>
          This covers the cost of maintaining the power lines, poles, transformers, and infrastructure that bring electricity to your home. Delivery charges may be a fixed fee, a per-kWh charge, or both. You pay this to your local utility even if you choose a different energy supplier.
        </p>
        <h3>Fixed fees and other charges</h3>
        <p>
          Many bills include a customer charge or basic service fee. This is a flat monthly fee that applies even if you use very little electricity. You may also see regulatory charges, taxes, or renewable energy surcharges. These are usually small but can add up.
        </p>
        <p>
          Understanding these parts helps you see where your money goes. The energy charge is based on usage, so reducing kWh lowers that part of the bill. The delivery and fixed charges usually do not change with usage.
        </p>
      </section>

      <section>
        <h2>Common rate structures: flat, tiered, and time-of-use</h2>
        <h3>Flat rate</h3>
        <p>
          You pay the same price per kWh no matter when you use electricity or how much you use. This is the simplest structure and makes budgeting straightforward.
        </p>
        <h3>Tiered pricing</h3>
        <p>
          The price per kWh increases as you use more electricity. For example, the first 500 kWh might cost $0.12 each, and any kWh above that might cost $0.16. Tiered pricing encourages conservation by making higher usage more expensive.
        </p>
        <h3>Time-of-use (TOU) pricing</h3>
        <p>
          The price per kWh changes based on the time of day or season. Peak hours (usually late afternoon and early evening) cost more because demand is higher. Off-peak hours (overnight and early morning) cost less. <Link href="/blog/time-of-use-electricity-rates">Time-of-Use plans</Link> reward you for shifting usage to cheaper times.
        </p>
        <p>
          If you are on a TOU plan, running dishwashers, laundry, or charging electric vehicles during off-peak hours can reduce costs.
        </p>
      </section>

      <section>
        <h2>What uses the most electricity in a typical home?</h2>
        <p>
          Heating and cooling are usually the biggest electricity users in homes that rely on electric systems. Air conditioning in summer and electric heat in winter can account for 40% to 60% of total usage.
        </p>
        <p>
          Water heating is next, often using 12% to 18% of electricity. Electric water heaters run throughout the day to keep water hot, which adds up over time.
        </p>
        <p>
          Appliances like refrigerators, washers, dryers, dishwashers, and ovens use electricity regularly. A refrigerator runs constantly, while a dryer uses a lot of power but only when running.
        </p>
        <p>
          Lighting, electronics, and small appliances usually account for a smaller share of the total, but they still matter--especially devices left on standby or used frequently.
        </p>
        <p>
          Knowing which devices use the most helps you prioritize where to focus conservation efforts.
        </p>
      </section>

      <section>
        <h2>Seasonal changes and why electric bills vary</h2>
        <p>
          Electric bills often rise in summer and winter due to heating and cooling demand. In summer, air conditioners work hard to keep homes cool, especially during heat waves. In winter, homes with electric heat see sharp increases as outdoor temperatures drop.
        </p>
        <p>
          Spring and fall are usually the lowest-usage months because you need less heating or cooling. Bills during these months can be a good baseline for non-climate-control usage.
        </p>
        <p>
          Billing cycles can also vary in length. A 35-day billing period will cost more than a 28-day period even if daily usage stays the same. Always compare kWh per day to see whether your actual usage changed.
        </p>
      </section>

      <section>
        <h2>How to reduce electricity usage without major investments</h2>
        <ul>
          <li>Set your thermostat a few degrees higher in summer or lower in winter.</li>
          <li>Turn off lights and electronics when not in use.</li>
          <li>Use power strips to eliminate standby power draw.</li>
          <li>Run dishwashers and laundry with full loads.</li>
          <li>Replace incandescent bulbs with LEDs.</li>
          <li>Clean or replace HVAC filters regularly.</li>
          <li>Use fans to feel cooler without lowering the AC temperature.</li>
          <li>Seal air leaks around doors and windows.</li>
          <li>Set water heaters to 120 degF if safe for your household.</li>
          <li>Unplug chargers and small appliances when not needed.</li>
        </ul>
        <p>
          Small changes add up. Reducing usage by 10% to 15% can make a noticeable difference on monthly bills.
        </p>
      </section>

      <section>
        <h2>Fixed vs. variable rate electricity plans</h2>
        <p>
          In some regions, you can choose your electricity supplier and pick between fixed-rate and variable-rate plans. Fixed-rate plans lock in the price per kWh for a set term, often 6 to 24 months. This provides price stability and makes budgeting easier.
        </p>
        <p>
          Variable-rate plans change each month based on market conditions. They can be cheaper during low-demand months but may spike during extreme weather or high-demand periods.
        </p>
        <p>
          If you prefer predictable bills, a fixed rate is usually the safer choice. If you are comfortable monitoring prices and can adjust usage, a variable rate might work.
        </p>
        <p>
          Always read the plan documents carefully. Look for early termination fees, minimum usage charges, and whether the rate is promotional.
        </p>
      </section>

      <section>
        <h2>Smart meters and real-time usage data</h2>
        <p>
          Many utilities have installed <Link href="/blog/how-do-smart-meters-work">smart meters</Link> that record electricity usage hourly or daily. Smart meters send usage data automatically, which eliminates the need for manual meter reading.
        </p>
        <p>
          If you have a smart meter, your utility may offer an online portal or app where you can see daily or hourly usage charts. This data helps you identify when usage is highest and which days had unusual spikes.
        </p>
        <p>
          Reviewing usage patterns can reveal habits like high evening usage or days when the AC ran longer than expected. That insight makes it easier to adjust behavior and reduce costs.
        </p>
      </section>

      <section>
        <h2>Common misconceptions about electricity</h2>
        <h3>Misconception: Leaving devices plugged in does not use electricity</h3>
        <p>
          Many devices draw standby power even when turned off. This is called phantom load or vampire power. Chargers, TVs, cable boxes, and microwaves often use small amounts of power continuously. Using power strips to cut power completely can reduce this waste.
        </p>
        <h3>Misconception: Turning lights on and off wastes more electricity than leaving them on</h3>
        <p>
          This is false for modern bulbs. Turning off lights when you leave a room always saves energy, especially with LEDs. The small surge when turning on a light is negligible compared to the energy used if left on for even a few minutes.
        </p>
        <h3>Misconception: Electric heat is always more expensive than gas heat</h3>
        <p>
          It depends on local rates and system efficiency. In regions with low electricity prices or mild winters, efficient heat pumps can compete with gas heating. In colder climates with high electric rates, gas is often cheaper.
        </p>
      </section>

      <AdSlot label="Mid-page ad" />

      <section>
        <h2>Related guides to deepen your understanding</h2>
        <p>
          Now that you understand the basics of electricity, explore these specific topics to answer common questions and manage your electric service more effectively:
        </p>
        <ul>
          <li>
            <Link href="/blog/how-do-smart-meters-work">
              How Do Smart Meters Work? (And Should You Trust Them?)
            </Link> -- Learn about accuracy, privacy, and how to read your new meter.
          </li>
          <li>
            <Link href="/blog/time-of-use-electricity-rates">
              What Are Time-of-Use Rates?
            </Link> -- Decide if switching to a peak/off-peak plan will save you money.
          </li>
          <li>
            <Link href="/blog/how-to-lower-electric-bill-without-solar">
              How to Lower Your Electric Bill Without Solar Panels
            </Link> -- 12 proven methods to reduce costs without major investments.
          </li>
          <li>
            <Link href="/blog/what-is-a-kilowatt-hour">
              What Is a Kilowatt-Hour (kWh)?
            </Link> -- Learn how to calculate kWh for appliances and estimate costs.
          </li>
          <li>
            <Link href="/blog/why-is-my-electricity-bill-so-high-in-winter">
              Why is my electricity bill so high in winter?
            </Link> -- Understand winter heating loads and how to reduce costs.
          </li>
          <li>
            <Link href="/blog/why-is-my-electricity-bill-so-high-in-summer">
              Why is my electricity bill so high in summer?
            </Link> -- See how air conditioning and heat gain affect summer usage.
          </li>
          
          <li>
            <Link href="/blog/why-is-my-electric-bill-so-high-this-month">
              Why is my electric bill so high this month?
            </Link> - Quick troubleshooting checklist for sudden spikes.
          </li>
          <li>
            <Link href="/blog/electric-bill-breakdown-understanding-line-items">
              Electric bill breakdown: understanding line items
            </Link> - Learn where each charge comes from.
          </li>
          <li>
            <Link href="/blog/supply-vs-delivery-charges-electricity">
              Supply vs delivery charges on electricity bills
            </Link> - See what you can control and what you cannot.
          </li>
          <li>
            <Link href="/blog/tiered-electricity-rates-explained">
              Tiered electricity rates explained
            </Link> - Understand how usage tiers change pricing.
          </li>
          <li>
            <Link href="/blog/demand-charge-electric-bill-explained">
              Demand charges on electric bills
            </Link> - Learn when demand charges apply and why.
          </li>
          <li>
            <Link href="/blog/how-to-read-electric-meter">
              How to read your electric meter
            </Link> - Check readings against your bill.
          </li>
        </ul>
      </section>

      <section>
        <h2>Frequently asked questions</h2>
        <h3>How much electricity does the average home use?</h3>
        <p>
          In the United States, a typical household uses about 800 to 1,000 kWh per month. This varies widely by climate, home size, and heating or cooling type.
        </p>
        <h3>Can I lower my electric bill without changing my habits?</h3>
        <p>
          Small equipment upgrades like LED bulbs, efficient power strips, and programmable thermostats can reduce usage without requiring major behavior changes. Sealing air leaks and improving insulation also help.
        </p>
        <h3>What is the difference between energy and delivery charges?</h3>
        <p>
          Energy charges pay for the electricity you used. Delivery charges pay for the infrastructure that brings electricity to your home. Both appear on your bill, but only the energy charge is tied directly to kWh usage.
        </p>
        <h3>Do smart meters increase my bill?</h3>
        <p>
          No. Smart meters measure usage more accurately, which can reveal waste you did not notice before. The meter itself does not change how much electricity you use.
        </p>
        <h3>Should I switch to a time-of-use plan?</h3>
        <p>
          If you can shift most usage to off-peak hours, a time-of-use plan can save money. If you are home during peak hours and cannot adjust usage, a flat-rate plan may be simpler.
        </p>
      </section>

      <section>
        <h2>Final thoughts</h2>
        <p>
          Electricity is a constant part of daily life, but understanding how it is measured, billed, and used gives you control over costs. Start by reading your bill carefully, tracking usage over a few months, and identifying the biggest loads in your home. Small, consistent changes often add up to meaningful savings without sacrificing comfort.
        </p>
        <p>
          If you are ready to explore other utilities, visit our guides on <Link href="/gas-explained">gas service</Link>, <Link href="/water-explained">water bills</Link>, or <Link href="/heating-cooling-explained">heating and cooling systems</Link>.
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
