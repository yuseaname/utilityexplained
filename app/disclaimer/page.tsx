import type { Metadata } from "next";
import Image from "next/image";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Disclaimer",
  description: "Important information about the limits of our content.",
  alternates: {
    canonical: `${siteConfig.url}/disclaimer`
  }
};

export default function DisclaimerPage() {
  return (
    <div className="container section">
      <h1>Disclaimer</h1>
      <Image
        src="/images/slots/929597bfc8926e58a2b97cef/image.webp"
        alt="Disclaimer"
        width={1536}
        height={1024}
        className="article-hero"
        sizes="(max-width: 768px) 100vw, 900px"
        priority
        fetchPriority="high"
        data-slot-id="929597bfc8926e58a2b97cef"
      />
      <p>
        Utility Explained is an informational resource. We do not provide
        financial, legal, or professional advice. Use the information on this site
        for educational purposes only.
      </p>
      <p>
        Utility rates and policies vary by provider and location. Always verify
        details with your local utility or service provider before making decisions.
      </p>
      <p>
        We make reasonable efforts to keep content accurate, but we cannot guarantee
        it is complete or up to date. If you notice an error, contact us so we can
        review and improve the information.
      </p>
      <p>Effective date: 2024-12-01</p>
    </div>
  );
}
