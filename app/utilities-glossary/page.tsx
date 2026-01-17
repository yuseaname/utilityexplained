import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import AdSlot from "@/components/AdSlot";
import Breadcrumbs from "@/components/Breadcrumbs";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Utilities Glossary: Common Terms Explained in Plain English",
  description:
    "Quick definitions for electricity, gas, water, and heating terms like kWh, therm, AFUE, SEER, CCF, and more--all explained in plain English.",
  alternates: {
    canonical: `${siteConfig.url}/utilities-glossary`
  },
  robots: {
    index: true,
    follow: true,
    "max-image-preview": "large",
    "max-snippet": -1
  }
};

export default function UtilitiesGlossaryPage() {
  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: "Utilities Glossary: Common Terms Explained in Plain English",
    description:
      "Quick definitions for electricity, gas, water, and heating terms like kWh, therm, AFUE, SEER, CCF, and more--all explained in plain English.",
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
      "@id": `${siteConfig.url}/utilities-glossary`
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
        name: "Utilities Glossary",
        item: `${siteConfig.url}/utilities-glossary`
      }
    ]
  };

  return (
    <div className="container section">
      <Breadcrumbs
        items={[
          { label: "Home", href: "/" },
          { label: "Utilities Glossary" }
        ]}
      />
      <h1>Utilities Glossary</h1>
      <Image
        src="/images/slots/b99c99cccad8df1bcb6d6f8f/image.webp"
        alt="Utilities Glossary"
        width={1536}
        height={1024}
        className="article-hero"
        sizes="(max-width: 768px) 100vw, 900px"
        priority
        fetchPriority="high"
        data-slot-id="b99c99cccad8df1bcb6d6f8f"
      />
      
      <p className="intro-text">
        Utility bills and energy systems use specialized terms that can feel confusing. This glossary defines common utility terminology in plain English. Use this as a quick reference when reading bills, comparing plans, or learning about home energy systems.
      </p>

      <section>
        <h2>Electricity Terms</h2>
        
        <h3 id="afue">AFUE (Annual Fuel Utilization Efficiency)</h3>
        <p>
          A percentage that measures how efficiently a furnace or boiler converts fuel into heat. A 95% AFUE furnace converts 95% of fuel into usable heat, with only 5% lost through the exhaust. Higher AFUE means lower fuel costs. See more in our <Link href="/heating-cooling-explained">heating and cooling guide</Link>.
        </p>

        <h3 id="amps">Amps (Amperes)</h3>
        <Image
          src="/images/slots/11341d4cc665a970f6f245ab/image.webp"
          alt="Amps (Amperes)"
          width={1536}
          height={1024}
          sizes="(max-width: 768px) 100vw, 900px"
          loading="lazy"
          decoding="async"
          style={{ width: "100%", height: "auto", borderRadius: 12, margin: "1rem 0" }}
          data-slot-id="11341d4cc665a970f6f245ab"
        />
        <p>
          A unit measuring electrical current. Your home's electrical service is rated in amps--commonly 100, 150, or 200 amps. This determines how much power can flow at once.
        </p>

        <h3 id="baseload">Baseload</h3>
        <p>
          The minimum amount of electricity your home uses continuously, even when major appliances are off. This includes refrigerators, clocks, standby electronics, and other constant draws.
        </p>

        <h3 id="demand-charge">Demand charge</h3>
        <p>
          A fee based on the highest power usage (in kW) during a billing period. Common for commercial customers but rare for residential. Encourages spreading usage over time rather than peaking.
        </p>

        <h3 id="delivery-charge">Delivery charge (Distribution charge)</h3>
        <p>
          The fee for transporting electricity from power plants to your home. Covers infrastructure like power lines, transformers, and maintenance. Separate from the energy charge. Learn more in our <Link href="/electricity-explained">electricity guide</Link>.
        </p>

        <h3 id="energy-charge">Energy charge (Supply charge)</h3>
        <p>
          The cost of the electricity itself, usually listed as a price per kWh. This is the usage-based portion of your bill.
        </p>

        <h3 id="kilowatt">Kilowatt (kW)</h3>
        <p>
          A unit of power equal to 1,000 watts. Measures how fast electricity is being used at a moment in time. A 2 kW space heater uses 2,000 watts when running.
        </p>

        <h3 id="kilowatt-hour">Kilowatt-hour (kWh)</h3>
        <p>
          A unit of energy. One kWh equals using 1,000 watts for one hour. Your electric bill charges for total kWh used during the billing period. See detailed examples in our <Link href="/blog/what-is-a-kilowatt-hour">kWh explainer</Link>.
        </p>

        <h3 id="off-peak">Off-peak hours</h3>
        <p>
          Times when electricity demand is low, usually overnight and early morning. Some utilities offer lower rates during off-peak hours to encourage shifting usage.
        </p>

        <h3 id="peak-hours">Peak hours</h3>
        <p>
          Times when electricity demand is highest, typically late afternoon and early evening. Utilities may charge higher rates during peak hours.
        </p>

        <h3 id="phantom-load">Phantom load (Vampire power, Standby power)</h3>
        <p>
          Electricity used by devices that are plugged in but turned off or in standby mode. Examples include TVs, chargers, and microwaves with clocks.
        </p>

        <h3 id="power-factor">Power factor</h3>
        <p>
          A measure of how efficiently electrical power is used. Mostly relevant for industrial and commercial users. Residential customers rarely see power factor charges.
        </p>

        <h3 id="seer">SEER (Seasonal Energy Efficiency Ratio)</h3>
        <p>
          A rating for air conditioners and heat pumps in cooling mode. Higher SEER means better efficiency and lower operating costs. Modern units range from 13 to 25 SEER. Learn more in our <Link href="/heating-cooling-explained">HVAC guide</Link>.
        </p>

        <h3 id="time-of-use">Time-of-use (TOU) pricing</h3>
        <p>
          A rate structure where electricity costs more during peak hours and less during off-peak hours. Encourages shifting usage to cheaper times. See more in our <Link href="/blog/fixed-vs-variable-rate-electricity-plan">rate plan comparison</Link>.
        </p>

        <h3 id="watt">Watt (W)</h3>
        <p>
          A unit of power. Measures how fast electricity is being used at a moment. A 60-watt light bulb uses 60 watts when on.
        </p>
      </section>

      <AdSlot label="Mid-page ad" />

      <section>
        <h2>Natural Gas Terms</h2>

        <h3 id="btu">BTU (British Thermal Unit)</h3>
        <p>
          A unit of heat energy. One BTU is the energy needed to raise one pound of water by one degree Fahrenheit. Natural gas energy content is measured in BTUs.
        </p>

        <h3 id="ccf">CCF (Hundred Cubic Feet)</h3>
        <p>
          A volume unit equal to 100 cubic feet of gas. Some utilities bill in CCF and convert to therms using a factor based on the gas's energy content.
        </p>

        <h3 id="commodity-charge">Commodity charge</h3>
        <p>
          Another term for the supply charge--the cost of the natural gas itself, separate from delivery fees.
        </p>

        <h3 id="conversion-factor">Conversion factor</h3>
        <p>
          A number used to convert gas volume (CCF) into energy (therms). Accounts for slight variations in gas energy content.
        </p>

        <h3 id="customer-charge">Customer charge (Base charge)</h3>
        <p>
          A fixed monthly fee you pay regardless of usage. Covers meter reading, billing, and service infrastructure.
        </p>

        <h3 id="mcf">MCF (Thousand Cubic Feet)</h3>
        <p>
          A volume unit equal to 1,000 cubic feet of gas. Less common for residential billing but used in some regions.
        </p>

        <h3 id="therm">Therm</h3>
        <p>
          A unit of heat energy equal to 100,000 BTUs. Natural gas bills usually charge per therm. See detailed examples in our <Link href="/blog/how-to-read-your-gas-bill-therms-explained">gas bill guide</Link>.
        </p>
      </section>

      <section>
        <h2>Water & Sewer Terms</h2>

        <h3 id="ccf-water">CCF (Hundred Cubic Feet)</h3>
        <p>
          A volume unit used for water billing. One CCF equals 100 cubic feet, or about 748 gallons.
        </p>

        <h3 id="cubic-foot">Cubic foot</h3>
        <p>
          A volume unit. One cubic foot of water equals 7.48 gallons. Some water meters measure in cubic feet.
        </p>

        <h3 id="gallon">Gallon</h3>
        <p>
          A volume unit. Most water usage is measured in gallons or converted from cubic feet. One gallon equals 0.1337 cubic feet.
        </p>

        <h3 id="kgal">kgal (Thousand Gallons)</h3>
        <p>
          A volume unit equal to 1,000 gallons. Some water utilities use kgal as the billing unit.
        </p>

        <h3 id="meter-reading">Meter reading</h3>
        <p>
          The number displayed on your water, gas, or electric meter showing cumulative usage. The difference between two readings is your usage for that period.
        </p>

        <h3 id="estimated-reading">Estimated reading</h3>
        <p>
          A usage estimate when the utility cannot access the meter. The next actual reading corrects the estimate.
        </p>

        <h3 id="sewer-charge">Sewer charge (Wastewater charge)</h3>
        <p>
          The cost of treating wastewater. Often calculated as a percentage of water usage or a per-unit charge. Learn more in our <Link href="/water-explained">water service guide</Link>.
        </p>

        <h3 id="tiered-pricing">Tiered pricing (Block pricing)</h3>
        <p>
          A rate structure where the price per unit increases as you use more. Encourages conservation by making higher usage more expensive.
        </p>

        <h3 id="winter-average">Winter average</h3>
        <p>
          A method some utilities use to calculate sewer charges. They average winter water usage (when outdoor use is minimal) and apply that to sewer billing year-round.
        </p>
      </section>

      <section>
        <h2>Heating & Cooling Terms</h2>

        <h3 id="central-air">Central air conditioning (Central AC)</h3>
        <p>
          A system that cools air at a central unit and distributes it through ducts. Serves the whole home.
        </p>

        <h3 id="cop">COP (Coefficient of Performance)</h3>
        <p>
          A ratio measuring heat pump efficiency. COP is heat delivered divided by electricity used. A COP of 3 means the system delivers 3 units of heat for every 1 unit of electricity.
        </p>

        <h3 id="ductless">Ductless mini-split</h3>
        <p>
          A heating and cooling system with an outdoor compressor and one or more indoor air handlers. Does not require ductwork. Can provide both heating and cooling.
        </p>

        <h3 id="furnace">Furnace</h3>
        <p>
          A heating system that burns fuel (gas, oil) or uses electricity to heat air, which is then distributed through ducts.
        </p>

        <h3 id="heat-pump">Heat pump</h3>
        <p>
          A system that moves heat rather than creates it. In summer, it cools like an air conditioner. In winter, it extracts heat from outdoor air and moves it indoors. More efficient than electric resistance heat. See our <Link href="/heating-cooling-explained">heating and cooling comparison</Link>.
        </p>

        <h3 id="hspf">HSPF (Heating Seasonal Performance Factor)</h3>
        <p>
          A rating for heat pumps in heating mode. Higher HSPF means better efficiency and lower electricity costs.
        </p>

        <h3 id="hvac">HVAC</h3>
        <p>
          Heating, Ventilation, and Air Conditioning. Refers to the systems that heat, cool, and circulate air in your home.
        </p>

        <h3 id="resistance-heat">Resistance heat (Electric resistance heat)</h3>
        <p>
          A heating method that converts electricity directly into heat. Nearly 100% efficient at the point of use, but often more expensive to operate than gas or heat pumps because electricity is usually more costly per unit of energy.
        </p>

        <h3 id="thermostat">Thermostat</h3>
        <p>
          A device that controls your HVAC system by sensing indoor temperature and turning heating or cooling on or off to maintain your set temperature.
        </p>

        <h3 id="programmable-thermostat">Programmable thermostat</h3>
        <p>
          A thermostat that lets you set schedules for different temperatures at different times of day. Reduces heating and cooling when you are away or asleep.
        </p>

        <h3 id="smart-thermostat">Smart thermostat</h3>
        <p>
          A thermostat that learns your habits, adjusts automatically, and can be controlled remotely via smartphone app. Often eligible for utility rebates.
        </p>
      </section>

      <section>
        <h2>General Utility Terms</h2>

        <h3 id="auto-pay">Auto-pay</h3>
        <p>
          Automatic bill payment from a bank account or credit card. Prevents late fees but requires maintaining adequate account balance.
        </p>

        <h3 id="budget-billing">Budget billing (Level payment plan)</h3>
        <p>
          A program that averages your annual usage and charges the same amount each month. Smooths out seasonal swings. The utility adjusts the amount periodically based on actual usage. Learn more in our <Link href="/utility-bills-costs-explained">billing guide</Link>.
        </p>

        <h3 id="billing-cycle">Billing cycle (Billing period)</h3>
        <p>
          The time span covered by a utility bill, usually 28 to 35 days. Compare bills by usage per day to account for varying cycle lengths.
        </p>

        <h3 id="deregulated-market">Deregulated market</h3>
        <p>
          A region where you can choose your energy supplier for the commodity portion of your bill. The delivery portion remains with your local utility.
        </p>

        <h3 id="fixed-rate">Fixed rate</h3>
        <p>
          A rate plan that locks in the price per unit for a set term, usually 6 to 24 months. Provides price stability. See our <Link href="/blog/fixed-vs-variable-rate-electricity-plan">rate comparison guide</Link>.
        </p>

        <h3 id="variable-rate">Variable rate</h3>
        <p>
          A rate plan where the price per unit changes each month based on market conditions. Can be cheaper in low-demand months but may spike during extreme weather.
        </p>

        <h3 id="late-fee">Late fee</h3>
        <p>
          A penalty charged when payment is received after the due date. Usually $5 to $25. Avoid by using auto-pay or setting payment reminders.
        </p>

        <h3 id="reconnection-fee">Reconnection fee</h3>
        <p>
          A fee charged to restore service after disconnection for non-payment. Often $50 to $150.
        </p>

        <h3 id="deposit">Deposit</h3>
        <p>
          An upfront payment required by some utilities for new customers. Often refunded after a period of on-time payments. Amounts vary based on credit and location.
        </p>
      </section>

      <section>
        <h2>How to use this glossary</h2>
        <p>
          Bookmark this page for quick reference when reading utility bills or comparing energy plans. For detailed explanations and real-world examples, visit our full guides:
        </p>
        <ul>
          <li><Link href="/electricity-explained">Electricity Explained</Link></li>
          <li><Link href="/gas-explained">Natural Gas Explained</Link></li>
          <li><Link href="/water-explained">Water Service Explained</Link></li>
          <li><Link href="/heating-cooling-explained">Heating & Cooling Explained</Link></li>
          <li><Link href="/utility-bills-costs-explained">Utility Bills & Costs Explained</Link></li>
        </ul>
        <p>
          If you have questions about a specific term or topic, explore our <Link href="/blog">full article library</Link> for in-depth explanations and practical advice.
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
