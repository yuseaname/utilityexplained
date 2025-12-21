import PostCard from "@/components/PostCard";
import type { Post } from "@/lib/types";

type RelatedPostsProps = {
  posts: Post[];
};

const RelatedPosts = ({ posts }: RelatedPostsProps) => {
  if (posts.length === 0) return null;
  return (
    <section className="related-posts">
      <h2>Related articles</h2>
      <div className="post-grid">
        {posts.map((post) => (
          <PostCard key={post.slug} post={post} />
        ))}
      </div>
    </section>
  );
};

export default RelatedPosts;
