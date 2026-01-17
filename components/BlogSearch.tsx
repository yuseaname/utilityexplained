"use client";

import { useMemo, useState } from "react";
import PostCard from "@/components/PostCard";
import type { Post } from "@/lib/types";

type BlogSearchProps = {
  initialPosts: Post[];
  allPosts: Post[];
  categories: string[];
};

const BlogSearch = ({ initialPosts, allPosts, categories }: BlogSearchProps) => {
  const [query, setQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("");

  const filtered = useMemo(() => {
    const value = query.trim().toLowerCase();
    const basePosts = value || activeCategory ? allPosts : initialPosts;
    return basePosts.filter((post) => {
      if (activeCategory && post.category !== activeCategory) return false;
      if (!value) return true;
      return [post.title, post.description, post.keyword, post.category]
        .join(" ")
        .toLowerCase()
        .includes(value);
    });
  }, [allPosts, initialPosts, query, activeCategory]);

  return (
    <div className="blog-search">
      <div className="category-row">
        <button
          onClick={() => setActiveCategory("")}
          className={`category-badge${!activeCategory ? " category-badge--active" : ""}`}
          aria-current={!activeCategory ? "page" : undefined}
        >
          All Topics
        </button>
        {categories.map((category) => (
          <button
            key={category}
            onClick={() => setActiveCategory(category)}
            className={`category-badge${activeCategory === category ? " category-badge--active" : ""}`}
            aria-current={activeCategory === category ? "page" : undefined}
          >
            {category}
          </button>
        ))}
      </div>
      {activeCategory ? (
        <div className="active-filter">
          <span>Topic: {activeCategory}</span>
          <button onClick={() => setActiveCategory("")} className="active-filter__clear">
            Clear
          </button>
        </div>
      ) : null}
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
