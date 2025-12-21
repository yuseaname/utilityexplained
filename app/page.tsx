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
            <h1>Home utilities explained in plain English.</h1>
            <p>
              Utility bills can feel overwhelming. We break down electricity, gas,
              and water costs with clear examples, real-world ranges, and calm
              guidance so you can budget with confidence.
            </p>
            <p>
              Explore seasonal spikes, compare heating options, and learn how to read
              your meters without jargon.
            </p>
            <div className="hero-actions">
              <Link className="button" href="/blog">
                Browse the guides
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

      <AdSlot label="In-content ad" />

      <section className="section">
        <div className="container">
          <h2>Why people trust Utility Plain English</h2>
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
