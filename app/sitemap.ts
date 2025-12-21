import { siteConfig } from "@/lib/site";
import posts, { getCategories } from "@/lib/posts";

export default function sitemap() {
  const pages = [
    "",
    "/blog",
    "/about",
    "/contact",
    "/privacy-policy",
    "/terms",
    "/disclaimer"
  ];

  const pageEntries = pages.map((path) => ({
    url: `${siteConfig.url}${path}`,
    lastModified: new Date().toISOString()
  }));

  const postEntries = posts.map((post) => ({
    url: `${siteConfig.url}/blog/${post.slug}`,
    lastModified: post.date
  }));

  // Category pages
  const categories = getCategories();
  const categoryEntries = categories.map((c) => ({
    url: `${siteConfig.url}/blog/category/${encodeURIComponent(c)}`,
    lastModified: new Date().toISOString()
  }));

  // Blog pagination pages (/blog/page/[n])
  const PER_PAGE = 9;
  const totalPages = Math.ceil(posts.length / PER_PAGE);
  const paginationEntries = Array.from({ length: Math.max(0, totalPages - 1) }).map((_, i) => ({
    url: `${siteConfig.url}/blog/page/${i + 2}`,
    lastModified: new Date().toISOString()
  }));

  return [...pageEntries, ...postEntries, ...categoryEntries, ...paginationEntries];
}
