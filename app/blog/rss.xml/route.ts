import { NextResponse } from "next/server";
import posts from "@/lib/posts";
import { siteConfig } from "@/lib/site";

export const revalidate = 3600; // 1 hour

export async function GET() {
  const items = posts
    .slice()
    .sort((a, b) => (a.date < b.date ? 1 : -1))
    .map((p) => {
      const url = `${siteConfig.url}/blog/${p.slug}`;
      return `
      <item>
        <title><![CDATA[${p.title}]]></title>
        <link>${url}</link>
        <guid isPermaLink="true">${url}</guid>
        <pubDate>${new Date(p.date).toUTCString()}</pubDate>
        <description><![CDATA[${p.description}]]></description>
      </item>`;
    })
    .join("\n");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
  <rss version="2.0">
    <channel>
      <title><![CDATA[${siteConfig.name} Blog]]></title>
      <link>${siteConfig.url}/blog</link>
      <description><![CDATA[Utility guides in plain English.]]></description>
      <language>en-us</language>
      ${items}
    </channel>
  </rss>`;

  return new NextResponse(xml, {
    status: 200,
    headers: {
      "Content-Type": "application/rss+xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600"
    }
  });
}
