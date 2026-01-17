import type { Metadata } from "next";
import Image from "next/image";
import AdSlot from "@/components/AdSlot";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "About",
  description: "Learn why Utility Explained exists and how we build guides.",
  alternates: {
    canonical: `${siteConfig.url}/about`
  }
};

export default function AboutPage() {
  return (
    <div className="container section">
      <h1>About Utility Explained</h1>
      <Image
        src="/images/slots/459c72fec1184e770c59ccec/image.webp"
        alt="About Utility Explained"
        width={1536}
        height={1024}
        className="article-hero"
        sizes="(max-width: 768px) 100vw, 900px"
        priority
        fetchPriority="high"
        data-slot-id="459c72fec1184e770c59ccec"
      />
      <p>
        We started Utility Explained because utility bills shouldn't require a
        translator. If you've ever stared at a bill wondering what you're actually
        paying for, you're in the right place.
      </p>
      <p>
        This site is for renters, first-time homeowners, and anyone who wants to
        understand electricity, gas, and water costs without the jargon.
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
