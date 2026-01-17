import type { Metadata } from "next";
import Image from "next/image";
import Pagination from "@/components/Pagination";
import PostCard from "@/components/PostCard";
import { siteConfig } from "@/lib/site";
import posts from "@/lib/posts";

const PER_PAGE = 9;

export async function generateStaticParams() {
  const totalPages = Math.ceil(posts.length / PER_PAGE);
  return Array.from({ length: totalPages - 1 }).map((_, i) => ({ page: String(i + 2) }));
}

export const generateMetadata = async ({ params }: { params: { page: string } }): Promise<Metadata> => {
  const p = Number(params.page) || 1;
  return {
    title: `Blog - Page ${p}`,
    description: "Browse practical, plain-English utility guides by page.",
    alternates: {
      canonical: p === 1 ? `${siteConfig.url}/blog` : `${siteConfig.url}/blog/page/${p}`
    },
    robots: {
      index: p <= 3,  // Only index first 3 pages to avoid thin content
      follow: true,
      "max-image-preview": "large"
    }
  };
};

export default function BlogPaged({ params }: { params: { page: string } }) {
  const current = Math.max(1, Number(params.page) || 1);
  const totalPages = Math.ceil(posts.length / PER_PAGE);
  const start = (current - 1) * PER_PAGE;
  const paged = posts.slice(start, start + PER_PAGE);

  return (
    <div className="container">
      <section className="section">
        <h1>Blog</h1>
        <Image
          src="/images/slots/5ace06f076805659dc8872b7/image.webp"
          alt="Blog"
          width={1536}
          height={1024}
          className="article-hero"
          sizes="(max-width: 768px) 100vw, 900px"
          priority
          fetchPriority="high"
          data-slot-id="5ace06f076805659dc8872b7"
        />
        <div className="post-grid">
          {paged.map((post) => (
            <PostCard key={post.slug} post={post} trackingLabel="blog-page" />
          ))}
        </div>
        <Pagination basePath="/blog/page" current={current} totalPages={totalPages} />
      </section>
    </div>
  );
}
