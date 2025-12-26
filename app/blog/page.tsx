import type { Metadata } from "next";
import Link from "next/link";
import BlogSearch from "@/components/BlogSearch";
import Pagination from "@/components/Pagination";
import { getCategories } from "@/lib/posts";
import posts from "@/lib/posts";
import { siteConfig } from "@/lib/site";

export const metadata: Metadata = {
  title: "Utility Bill Guides",
  description:
    "Browse practical, plain-English articles about electricity, gas, and water bills.",
  alternates: {
    canonical: `${siteConfig.url}/blog`
  }
};

const PER_PAGE = 9;

export default function BlogPage() {
  const categories = getCategories();
  const totalPages = Math.ceil(posts.length / PER_PAGE);
  const firstPage = posts.slice(0, PER_PAGE);

  return (
    <div className="container">
      <section className="blog-hero">
        <h1>Utility explainers and adulting guides</h1>
        <p>
          Search by question or browse by topic. Every guide is written to be clear,
          neutral, and helpful for first-time renters and homeowners.
        </p>
        <div className="category-row">
          {categories.map((category) => (
            <Link
              key={category}
              href={`/blog/category/${encodeURIComponent(category)}`}
              className="category-badge"
              style={{ textDecoration: "none" }}
            >
              {category}
            </Link>
          ))}
        </div>
      </section>
      <BlogSearch posts={firstPage} />
      <Pagination basePath="/blog/page" current={1} totalPages={totalPages} />
    </div>
  );
}
