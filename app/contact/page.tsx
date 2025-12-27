import type { Metadata } from "next";
import AdSlot from "@/components/AdSlot";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Contact",
  description: "Send a message or ask a utility bill question.",
  alternates: {
    canonical: `${siteConfig.url}/contact`
  }
};

export default function ContactPage() {
  const contactEmail = siteConfig.socials.email;

  return (
    <div className="container section">
      <h1>Contact</h1>
      <p>
        Have a question about a utility bill topic? Send a note and we will consider
        it for a future guide. This form is informational only and does not create a
        customer support relationship with any utility provider.
      </p>
      <p>
        Submitting the form opens your email app so you can send the message directly
        to {contactEmail}.
      </p>
      <div className="contact-card">
        <form action={`mailto:${contactEmail}`} method="post" encType="text/plain">
          <label>
            Name
            <input type="text" name="name" placeholder="Your name" />
          </label>
          <label>
            Email
            <input type="email" name="email" placeholder="you@example.com" />
          </label>
          <label>
            Topic
            <input type="text" name="topic" placeholder="e.g., high electric bill" />
          </label>
          <label>
            Message
            <textarea name="message" rows={6} placeholder="How can we help?" />
          </label>
          <button type="submit">Send your question</button>
        </form>
      </div>
      <AdSlot label="Contact page ad" />
    </div>
  );
}
