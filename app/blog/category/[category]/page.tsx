import type { Metadata } from "next";
import PostCard from "@/components/PostCard";
import Breadcrumbs from "@/components/Breadcrumbs";
import posts, { getPostsByCategory } from "@/lib/posts";
import { siteConfig } from "@/lib/site";

export const dynamicParams = false;

export function generateStaticParams() {
  const categories = Array.from(new Set(posts.map((p) => p.category)));
  return categories.map((category) => ({ category }));
}

export const generateMetadata = async ({ params }: { params: { category: string } }): Promise<Metadata> => {
  const title = `${params.category} Articles`;
  return {
    title,
    description: `Guides and explainers about ${params.category.toLowerCase()}.`,
    alternates: {
      canonical: `${siteConfig.url}/blog/category/${encodeURIComponent(params.category)}`
    }
  };
};

export default function CategoryPage({ params }: { params: { category: string } }) {
  const items = getPostsByCategory(params.category);
  return (
    <div className="container">
      <Breadcrumbs items={[{ label: "Home", href: "/" }, { label: "Blog", href: "/blog" }, { label: params.category }]} />
      <section className="section">
        <h1>{params.category}</h1>
        <p>
          Browse clear, plain-English guides focused on {params.category.toLowerCase()}.
          Each article breaks down utility terms, charges, and cost drivers so you can
          make sense of real bills faster.
        </p>
        <div className="post-grid">
          {items.map((post) => (
            <PostCard key={post.slug} post={post} trackingLabel="blog-category" />
          ))}
        </div>
      </section>
    </div>
  );
}
