import type { Metadata } from "next";
import AdSlot from "@/components/AdSlot";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "About",
  description: "Learn why Utility Plain English exists and how we build guides.",
  alternates: {
    canonical: `${siteConfig.url}/about`
  }
};

export default function AboutPage() {
  return (
    <div className="container section">
      <h1>About Utility Plain English</h1>
      <p>
        Utility Plain English is an informational site built for renters, first-time
        homeowners, and anyone who wants to understand home utility bills without
        confusing jargon. Our goal is to explain electricity, gas, and water costs in
        a calm, practical way so you can make informed choices.
      </p>
      <p>
        We focus on clear definitions, simple examples, and real-world ranges instead
        of sales language. We do not sell products or services. If we ever mention a
        service or provider, it is strictly for educational context.
      </p>
      <p>
        We also prioritize AdSense compliance by keeping content neutral and factual,
        with transparent policies and easy navigation.
      </p>
      <AdSlot label="About page ad" />
    </div>
  );
}
