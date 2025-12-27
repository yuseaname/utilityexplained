import type { Metadata } from "next";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Terms of Service",
  description: "Terms for using Utility Explained.",
  alternates: {
    canonical: `${siteConfig.url}/terms`
  }
};

export default function TermsPage() {
  return (
    <div className="container section">
      <h1>Terms of Service</h1>
      <p>
        Utility Explained provides informational content only. By using this
        site, you agree that the content is provided "as is" without warranties of
        any kind.
      </p>
      <h2>Use of content</h2>
      <p>
        You may read and share links to our content for personal, non-commercial
        purposes. You may not republish full articles without permission.
      </p>
      <h2>No professional advice</h2>
      <p>
        Content on this site is not legal, financial, or professional advice. For
        decisions about your utilities or housing, consult qualified professionals
        or your utility provider.
      </p>
      <h2>Changes</h2>
      <p>
        We may update these terms periodically. Continued use of the site means you
        accept any updates.
      </p>
      <p>Effective date: 2024-12-01</p>
    </div>
  );
}
