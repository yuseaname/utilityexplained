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
import posts, { getPostBySlug, getRelatedPosts } from "@/lib/posts";
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

  const related = getRelatedPosts(post.slug);
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
    { phrase: "therm", href: "/blog/how-to-read-your-gas-bill-therms-explained" },
    { phrase: "therms", href: "/blog/how-to-read-your-gas-bill-therms-explained" },
    { phrase: "ccf", href: "/blog/what-is-ccf-on-a-water-bill" },
    { phrase: "gallon", href: "/water-explained" },
    
    // Rate & billing terms
    { phrase: "time-of-use", href: "/utility-bills-costs-explained" },
    { phrase: "fixed rate", href: "/blog/fixed-vs-variable-rate-electricity-plan" },
    { phrase: "variable rate", href: "/blog/fixed-vs-variable-rate-electricity-plan" },
    { phrase: "tiered pricing", href: "/water-explained" },
    { phrase: "demand charge", href: "/utility-bills-costs-explained" },
    { phrase: "budget billing", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "level pay", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "average billing", href: "/blog/budget-billing-level-pay-explained" },
    { phrase: "estimated bill", href: "/blog/estimated-utility-bill-explained" },
    { phrase: "estimated reading", href: "/blog/estimated-utility-bill-explained" },
    { phrase: "billing days", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "fixed charge", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "customer charge", href: "/blog/why-my-utility-bill-is-higher-with-same-usage" },
    { phrase: "delivery charge", href: "/blog/gas-delivery-charge-vs-supply-charge" },
    { phrase: "supply charge", href: "/blog/gas-delivery-charge-vs-supply-charge" },
    
    // Systems & efficiency
    { phrase: "hvac", href: "/heating-cooling-explained" },
    { phrase: "heat pump", href: "/heating-cooling-explained" },
    { phrase: "aux heat", href: "/blog/aux-heat-vs-emergency-heat-meaning" },
    { phrase: "emergency heat", href: "/blog/aux-heat-vs-emergency-heat-meaning" },
    { phrase: "afue", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    { phrase: "seer", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    { phrase: "hspf", href: "/blog/afue-vs-seer-vs-hspf-vs-cop" },
    
    // Troubleshooting & tasks
    { phrase: "water meter", href: "/blog/how-to-read-a-water-meter" },
    { phrase: "leak detection", href: "/blog/why-did-my-water-bill-suddenly-increase" },
    { phrase: "high electric bill", href: "/blog/why-is-my-electric-bill-so-high-this-month" },
    
    // Comparisons & decisions
    { phrase: "gas vs electric", href: "/blog/gas-vs-electric-heating-cost-comparison" },
    { phrase: "average water usage", href: "/blog/average-water-usage-per-person" },
    
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
                  <Link href={`/blog/${prev.slug}`}>← {prev.title}</Link>
                ) : <span />}
                {next ? (
                  <Link href={`/blog/${next.slug}`}>{next.title} →</Link>
                ) : <span />}
              </div>
            </nav>
          </div>
          <RelatedPosts posts={related} />
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
