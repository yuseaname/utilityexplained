import Image from "next/image";
import Link from "next/link";
import type { Post } from "@/lib/types";
import { formatDate } from "@/lib/utils";
import CategoryBadge from "@/components/CategoryBadge";

type PostCardProps = {
  post: Post;
};

const PostCard = ({ post }: PostCardProps) => {
  return (
    <article className="post-card">
      {/* Image source: Unsplash (see image src in post data). */}
      <Image
        src={post.image.src}
        alt={post.image.alt}
        width={800}
        height={500}
        className="post-card__image"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
      <div className="post-card__content">
        <CategoryBadge label={post.category} />
        <h3>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </h3>
        <p>{post.description}</p>
        <div className="post-card__meta">
          <span>{formatDate(post.date)}</span>
          <span>{post.readTime}</span>
        </div>
      </div>
    </article>
  );
};

export default PostCard;
