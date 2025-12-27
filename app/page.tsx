import Image from "next/image";
import Link from "next/link";
import AdSlot from "@/components/AdSlot";
import PostCard from "@/components/PostCard";
import { siteConfig } from "@/lib/site";
import posts from "@/lib/posts";

export default function HomePage() {
  const featured = posts.slice(0, 3);

  const organizationLd = {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: siteConfig.name,
    url: siteConfig.url,
    description: siteConfig.description
  };

  return (
    <div>
      <section className="hero">
        <div className="container hero-grid">
          <div>
            <h1>Finally understand your utility bills--no jargon, no stress.</h1>
            <p>
              Utility bills can feel like a foreign language. We break down electricity,
              gas, and water costs so you can budget with confidence--not confusion.
            </p>
            <p>
              Learn what kWh, therms, and CCF actually mean. Predict seasonal spikes
              before they hit. Read your bills like you wrote them.
            </p>
            <div className="hero-actions">
              <Link className="button" href="/blog">
                Pick your first guide
              </Link>
            </div>
          </div>
          <div className="hero-card">
            {/* Image source: Unsplash (https://unsplash.com/photos/3PeSjpLVtLg) */}
            <Image
              src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
              alt="Person reviewing a utility bill"
              width={520}
              height={360}
              className="hero-image"
            />
            <h3>What this site covers</h3>
            <ul>
              <li>How to read electric, gas, and water bills</li>
              <li>Why seasonal costs change</li>
              <li>Budgeting tips for renters and new homeowners</li>
              <li>Plain-English definitions for utility terms</li>
            </ul>
          </div>
        </div>
      </section>

      <AdSlot label="Homepage mid-content ad" format="horizontal" slot={process.env.NEXT_PUBLIC_AD_SLOT_HOME_MID} />

      <section className="section">
        <div className="container">
          <h2>How it works</h2>
          <div className="post-grid">
            <div className="hero-card">
              <h3>1. Pick your utility</h3>
              <p>
                Start with electric, gas, or water--whichever bill is confusing you
                right now.
              </p>
            </div>
            <div className="hero-card">
              <h3>2. Read the plain-English guide</h3>
              <p>
                No rush, no tests. Just clear explanations of what each charge
                means and why it's there.
              </p>
            </div>
            <div className="hero-card">
              <h3>3. Budget with confidence</h3>
              <p>
                Know exactly what you're paying for. Predict seasonal spikes.
                Spot errors before they cost you.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>Popular explainers</h2>
          <div className="post-grid">
            {featured.map((post) => (
              <PostCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      </section>

      <AdSlot label="Homepage lower ad" format="horizontal" slot={process.env.NEXT_PUBLIC_AD_SLOT_HOME_BOTTOM} />

      <section className="section">
        <div className="container">
          <h2>Why readers come here first</h2>
          <div className="post-grid">
            <div className="hero-card">
              <h3>Neutral, practical explanations</h3>
              <p>
                We focus on clear definitions, cost breakdowns, and simple checks you
                can do at home. No sales pitches and no pressure.
              </p>
            </div>
            <div className="hero-card">
              <h3>Designed for first-timers</h3>
              <p>
                Whether you are moving out for the first time or comparing heating
                options, the guides start with the basics and build from there.
              </p>
            </div>
            <div className="hero-card">
              <h3>Updated for real bills</h3>
              <p>
                Articles use current utility bill layouts and explain how to read
                them in everyday language.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>Start here</h2>
          <p>
            New to utilities? Start with the basics on how kWh works or how to read
            a water meter, then explore related topics like seasonal spikes and
            budgeting.
          </p>
          <div className="post-grid">
            {posts.slice(3, 6).map((post) => (
              <PostCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      </section>

      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(organizationLd) }}
      />
    </div>
  );
}
