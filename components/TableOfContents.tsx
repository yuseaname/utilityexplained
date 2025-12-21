import Link from "next/link";
import type { PostSection } from "@/lib/types";

type TableOfContentsProps = {
  sections: PostSection[];
};

const TableOfContents = ({ sections }: TableOfContentsProps) => {
  return (
    <aside className="toc">
      <p className="toc-title">On this page</p>
      <nav aria-label="Table of contents">
        {sections.map((section) => (
          <Link key={section.id} href={`#${section.id}`} className="toc-link">
            {section.title}
          </Link>
        ))}
      </nav>
    </aside>
  );
};

export default TableOfContents;
