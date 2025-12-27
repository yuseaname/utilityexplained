import PostCard from "@/components/PostCard";
import type { Post } from "@/lib/types";

type RelatedPostsProps = {
  posts?: Post[];
  labeledPosts?: { post: Post; label?: string }[];
  title?: string;
};

const RelatedPosts = ({ posts = [], labeledPosts, title }: RelatedPostsProps) => {
  const items =
    labeledPosts && labeledPosts.length > 0
      ? labeledPosts
      : posts.map((post) => ({ post }));
  if (items.length === 0) return null;
  const heading = title ?? (labeledPosts?.length ? "Next read" : "Related articles");
  return (
    <section className="related-posts">
      <h2>{heading}</h2>
      <div className="post-grid">
        {items.map(({ post, label }) => (
          <div key={post.slug}>
            {label ? <p className="related-label">{label}</p> : null}
            <PostCard post={post} />
          </div>
        ))}
      </div>
    </section>
  );
};

export default RelatedPosts;
