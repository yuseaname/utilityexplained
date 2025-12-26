import { siteConfig } from "@/lib/site";
import posts, { getCategories } from "@/lib/posts";

export default function sitemap() {
  // High-priority pillar pages
  const pillarPages = [
    { path: "/electricity-explained", priority: 0.9, changefreq: "monthly" },
    { path: "/gas-explained", priority: 0.9, changefreq: "monthly" },
    { path: "/water-explained", priority: 0.9, changefreq: "monthly" },
    { path: "/heating-cooling-explained", priority: 0.9, changefreq: "monthly" },
    { path: "/utility-bills-costs-explained", priority: 0.9, changefreq: "monthly" },
    { path: "/utilities-glossary", priority: 0.8, changefreq: "monthly" }
  ];

  // Standard pages
  const pages = [
    { path: "", priority: 1.0, changefreq: "weekly" },
    { path: "/blog", priority: 0.9, changefreq: "daily" },
    { path: "/about", priority: 0.5, changefreq: "yearly" },
    { path: "/contact", priority: 0.5, changefreq: "yearly" },
    { path: "/privacy-policy", priority: 0.3, changefreq: "yearly" },
    { path: "/terms", priority: 0.3, changefreq: "yearly" },
    { path: "/disclaimer", priority: 0.3, changefreq: "yearly" }
  ];

  const pageEntries = [...pillarPages, ...pages].map((item) => ({
    url: `${siteConfig.url}${item.path}`,
    lastModified: new Date().toISOString(),
    priority: item.priority,
    changefreq: item.changefreq as "yearly" | "monthly" | "weekly" | "daily"
  }));

  const postEntries = posts.map((post) => ({
    url: `${siteConfig.url}/blog/${post.slug}`,
    lastModified: post.date,
    priority: 0.7,
    changefreq: "monthly" as const
  }));

  // Category pages
  const categories = getCategories();
  const categoryEntries = categories.map((c) => ({
    url: `${siteConfig.url}/blog/category/${encodeURIComponent(c)}`,
    lastModified: new Date().toISOString(),
    priority: 0.6,
    changefreq: "weekly" as const
  }));

  // Blog pagination pages (/blog/page/[n])
  const PER_PAGE = 9;
  const totalPages = Math.ceil(posts.length / PER_PAGE);
  const paginationEntries = Array.from({ length: Math.max(0, totalPages - 1) }).map((_, i) => ({
    url: `${siteConfig.url}/blog/page/${i + 2}`,
    lastModified: new Date().toISOString(),
    priority: 0.5,
    changefreq: "weekly" as const
  }));

  return [...pageEntries, ...postEntries, ...categoryEntries, ...paginationEntries];
}
