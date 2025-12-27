"use client";

import { useMemo, useState } from "react";
import PostCard from "@/components/PostCard";
import type { Post } from "@/lib/types";

type BlogSearchProps = {
  posts: Post[];
};

const BlogSearch = ({ posts }: BlogSearchProps) => {
  const [query, setQuery] = useState("");

  const filtered = useMemo(() => {
    const value = query.trim().toLowerCase();
    if (!value) return posts;
    return posts.filter((post) =>
      [post.title, post.description, post.keyword, post.category]
        .join(" ")
        .toLowerCase()
        .includes(value)
    );
  }, [posts, query]);

  return (
    <div className="blog-search">
      <label className="search-label" htmlFor="search">
        Search articles
      </label>
      <input
        id="search"
        className="search-input"
        placeholder="Search bills, meters, and seasonal costs"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <div className="post-grid">
        {filtered.map((post) => (
          <PostCard key={post.slug} post={post} trackingLabel="blog-search" />
        ))}
      </div>
      {filtered.length === 0 ? (
        <p className="empty-state">
          No matches yet. Try a simpler phrase like "water bill" or "kWh".
        </p>
      ) : null}
    </div>
  );
};

export default BlogSearch;
