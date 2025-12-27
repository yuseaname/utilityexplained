import type { Metadata } from "next";
import Image from "next/image";
import { notFound } from "next/navigation";
import AdSlot from "@/components/AdSlot";
import Breadcrumbs from "@/components/Breadcrumbs";
import FAQAccordion from "@/components/FAQAccordion";
import ReadingProgress from "@/components/ReadingProgress";
import RelatedPosts from "@/components/RelatedPosts";
import TableOfContents from "@/components/TableOfContents";
import SmartLinker from "@/components/SmartLinker";
import { siteConfig } from "@/lib/site";
import { formatDate } from "@/lib/utils";
import posts, { getNextReads, getPostBySlug, getRelatedPosts } from "@/lib/posts";
import Link from "next/link";

export const dynamicParams = false;

export async function generateStaticParams() {
  return posts.map((post) => ({ slug: post.slug }));
}

export const generateMetadata = async ({
  params
}: {
  params: { slug: string };
}): Promise<Metadata> => {
  const post = getPostBySlug(params.slug);
  if (!post) return {};

  return {
    title: post.title,
    description: post.description,
    alternates: {
      canonical: `${siteConfig.url}/blog/${post.slug}`
    },
    openGraph: {
      title: post.title,
      description: post.description,
      url: `${siteConfig.url}/blog/${post.slug}`,
      images: [
        {
          url: post.image.src,
          width: 1200,
          height: 630,
          alt: post.image.alt
        }
      ],
      type: "article"
    },
    twitter: {
      card: "summary_large_image",
      title: post.title,
      description: post.description,
      images: [post.image.src]
    }
  };
};

export default function BlogPostPage({ params }: { params: { slug: string } }) {
  const post = getPostBySlug(params.slug);
  if (!post) return notFound();

  const nextReads = getNextReads(post.slug);
  const related = nextReads.length === 0 ? getRelatedPosts(post.slug) : [];
  const all = posts.slice().sort((a, b) => (a.date < b.date ? 1 : -1));
  const idx = all.findIndex((p) => p.slug === post.slug);
  const prev = idx > 0 ? all[idx - 1] : null;
  const next = idx >= 0 && idx < all.length - 1 ? all[idx + 1] : null;

  const blogPostingLd = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: post.title,
    description: post.description,
    datePublished: post.date,
    dateModified: post.date,
    author: {
      "@type": "Organization",
      name: siteConfig.name
    },
    publisher: {
      "@type": "Organization",
      name: siteConfig.name
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `${siteConfig.url}/blog/${post.slug}`
    },
    image: [post.image.src]
  };

  const faqLd = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: post.faqs.map((faq) => ({
      "@type": "Question",
      name: faq.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: faq.answer
      }
    }))
  };

  const linkMap = [
    // Core metrics & units
    { phrase: "kwh", href: "/blog/what-is-a-kilowatt-hour" },
    { phrase: "kilowatt-hour", href: "/blog/what-is-a-kilowatt-hour" },
    { phrase: "kilowatt hours", href: "/blog/what-is-a-kilowatt-hour" },
    { phrase: "therm", href: "/blog/how-to-read-your-gas-bill-therms-explained" },
    { phrase: "therms", href: "/blog/how-to-read-your-gas-bill-therms-explained" },
    { phrase: "ccf", href: "/blog/what-is-ccf-on-a-water-bill" },
    { phrase: "gallon", href: "/water-explained" },
    
    // Rate & billing terms
    { phrase: "time-of-use", href: "/blog/time-of-use-electricity-rates" },
    { phrase: "time of use", href: "/blog/time-of-use-electricity-rates" },
    { phrase: "fixed rate", href: "/blog/fixed-vs-variable-rate-electricity-plan" },
    { phrase: "variable rate", href: "/blog/fixed-vs-variable-rate-electricity-plan" },
    { phrase: "tiered pricing", href: "/water-explained" },
    { phrase: "tiered water rates", href: "/blog/tiered-water-rates-explained" },
    { phrase: "tiered water pricing", href: "/blog/tiered-water-rates-explained" },
    { phrase: "tiered electric rates", href: "/blog/tiered-electricity-rates-explained" },
    { phrase: "demand charge", href: "/blog/demand-charge-electric-bill-explained" },
    { phrase: "demand charges", href: "/blog/demand-charge-electric-bill-explained" },
    { phrase: "budget billing", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "level pay", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "average billing", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "estimated bill", href: "/blog/estimated-utility-bill-explained" },
    { phrase: "estimated reading", href: "/blog/estimated-utility-bill-explained" },
    { phrase: "billing cycle", href: "/blog/utility-billing-cycle-explained" },
    { phrase: "billing days", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "kwh per day", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "fixed charge", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "customer charge", href: "/blog/what-is-customer-charge-on-utility-bill" },
    { phrase: "basic service charge", href: "/blog/what-is-customer-charge-on-utility-bill" },
    { phrase: "gas customer charge", href: "/blog/gas-customer-charge-explained" },
    { phrase: "fuel adjustment", href: "/blog/fuel-adjustment-charge-on-utility-bill-explained" },
    { phrase: "pga", href: "/blog/fuel-adjustment-charge-on-utility-bill-explained" },
    { phrase: "fca", href: "/blog/fuel-adjustment-charge-on-utility-bill-explained" },
    { phrase: "surcharge", href: "/blog/utility-bill-surcharges-and-riders-explained" },
    { phrase: "surcharges", href: "/blog/utility-bill-surcharges-and-riders-explained" },
    { phrase: "drought surcharge", href: "/blog/drought-surcharge-on-water-bill-explained" },
    { phrase: "rider", href: "/blog/utility-bill-surcharges-and-riders-explained" },
    { phrase: "riders", href: "/blog/utility-bill-surcharges-and-riders-explained" },
    { phrase: "franchise fee", href: "/blog/utility-bill-surcharges-and-riders-explained" },
    { phrase: "proration", href: "/blog/utility-bill-proration-explained" },
    { phrase: "prorated", href: "/blog/utility-bill-proration-explained" },
    { phrase: "past due", href: "/blog/past-due-balance-utility-bill-explained" },
    { phrase: "past-due", href: "/blog/past-due-balance-utility-bill-explained" },
    { phrase: "minimum bill", href: "/blog/minimum-bill-utility-bill-explained" },
    { phrase: "delivery charge", href: "/blog/delivery-charge-vs-supply-charge-utility-bill" },
    { phrase: "supply charge", href: "/blog/delivery-charge-vs-supply-charge-utility-bill" },
    { phrase: "gas delivery charge", href: "/blog/gas-delivery-charge-vs-supply-charge" },
    { phrase: "gas supply charge", href: "/blog/gas-delivery-charge-vs-supply-charge" },
    { phrase: "electricity delivery charge", href: "/blog/supply-vs-delivery-charges-electricity" },
    { phrase: "electric supply charge", href: "/blog/supply-vs-delivery-charges-electricity" },
    { phrase: "sewer charge", href: "/blog/how-sewer-charges-work-on-your-water-bill" },
    { phrase: "sewer charges", href: "/blog/how-sewer-charges-work-on-your-water-bill" },
    { phrase: "water service charge", href: "/blog/water-service-charge-explained" },
    
    // Systems & efficiency
    { phrase: "hvac", href: "/heating-cooling-explained" },
    { phrase: "heat pump", href: "/heating-cooling-explained" },
    { phrase: "ductless mini-split", href: "/blog/ductless-mini-split-vs-central-air" },
    { phrase: "variable speed", href: "/blog/single-stage-vs-two-stage-vs-variable-speed-hvac" },
    { phrase: "aux heat", href: "/blog/aux-heat-vs-emergency-heat-meaning" },
    { phrase: "emergency heat", href: "/blog/aux-heat-vs-emergency-heat-meaning" },
    { phrase: "afue", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    { phrase: "seer", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    { phrase: "hspf", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    
    // Troubleshooting & tasks
    { phrase: "water meter", href: "/blog/how-to-read-a-water-meter" },
    { phrase: "electric meter", href: "/blog/how-to-read-electric-meter" },
    { phrase: "gas meter", href: "/blog/how-to-read-gas-meter" },
    { phrase: "leak indicator", href: "/blog/water-meter-leak-indicator-explained" },
    { phrase: "toilet running", href: "/blog/is-your-toilet-running-leak-test" },
    { phrase: "leak detection", href: "/blog/why-did-my-water-bill-suddenly-increase" },
    { phrase: "high electric bill", href: "/blog/why-is-my-electric-bill-so-high-this-month" },
    
    // Comparisons & decisions
    { phrase: "gas vs electric", href: "/blog/gas-vs-electric-heating-cost-comparison" },
    { phrase: "average water usage", href: "/blog/average-water-usage-per-person" },
    { phrase: "stormwater fee", href: "/blog/stormwater-fee-on-water-bill-explained" },
    { phrase: "stormwater charge", href: "/blog/stormwater-fee-on-water-bill-explained" },
    
    // Pillar hubs
    { phrase: "electricity basics", href: "/electricity-explained" },
    { phrase: "gas basics", href: "/gas-explained" },
    { phrase: "water basics", href: "/water-explained" },
    { phrase: "utility bills", href: "/utility-bills-costs-explained" },
    { phrase: "utilities glossary", href: "/utilities-glossary" }
  ];

  const breadcrumbLd = {
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
        name: "Blog",
        item: `${siteConfig.url}/blog`
      },
      {
        "@type": "ListItem",
        position: 3,
        name: post.category,
        item: `${siteConfig.url}/blog/category/${encodeURIComponent(post.category)}`
      },
      {
        "@type": "ListItem",
        position: 4,
        name: post.title,
        item: `${siteConfig.url}/blog/${post.slug}`
      }
    ]
  };

  return (
    <div className="container">
      <ReadingProgress />
      <article className="article-layout">
        <div>
          <Breadcrumbs
            items={[
              { label: "Home", href: "/" },
              { label: "Blog", href: "/blog" },
              { label: post.category, href: `/blog/category/${encodeURIComponent(post.category)}` },
              { label: post.title }
            ]}
          />
          <header className="article-header">
            <p className="category-badge">{post.category}</p>
            <h1>{post.title}</h1>
            <p>{post.description}</p>
            <div className="article-meta">
              <span>{formatDate(post.date)}</span>
              <span>{post.readTime}</span>
              <span>Keyword: {post.keyword}</span>
            </div>
          </header>
          <div className="article-body">
            {/* Image source: Unsplash (see image src in post data). */}
            <Image
              src={post.image.src}
              alt={post.image.alt}
              width={1200}
              height={700}
              className="article-hero"
              sizes="(max-width: 768px) 100vw, 900px"
              priority
            />
            {post.sections.map((section, i) => (
              <section key={section.id} id={section.id}>
                <h2>{section.title}</h2>
                <SmartLinker map={linkMap}>{section.content}</SmartLinker>
                {i === 0 && <AdSlot label="In-article ad (top)" format="auto" slot={process.env.NEXT_PUBLIC_AD_SLOT_ARTICLE_TOP} responsive />}
                {i === Math.floor(post.sections.length / 2) && <AdSlot label="In-article ad (mid)" format="auto" slot={process.env.NEXT_PUBLIC_AD_SLOT_ARTICLE_MID} responsive />}
              </section>
            ))}
            <AdSlot label="After content ad" format="horizontal" slot={process.env.NEXT_PUBLIC_AD_SLOT_ARTICLE_BOTTOM} />
            <section>
              <h2>Frequently asked questions</h2>
              <FAQAccordion items={post.faqs} />
            </section>
            <nav className="post-nav" aria-label="Post">
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                {prev ? (
                  <Link href={`/blog/${prev.slug}`}>Prev: {prev.title}</Link>
                ) : <span />}
                {next ? (
                  <Link href={`/blog/${next.slug}`}>Next: {next.title}</Link>
                ) : <span />}
              </div>
            </nav>
          </div>
          <RelatedPosts
            posts={related}
            labeledPosts={nextReads}
            title={nextReads.length ? "Next read" : undefined}
          />
        </div>
        <TableOfContents sections={post.sections} />
      </article>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(blogPostingLd) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqLd) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbLd) }}
      />
    </div>
  );
}
