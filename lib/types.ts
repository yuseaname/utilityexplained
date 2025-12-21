import type { ReactNode } from "react";

export type FAQItem = {
  question: string;
  answer: string;
};

export type PostSection = {
  id: string;
  title: string;
  content: ReactNode;
};

export type Post = {
  slug: string;
  title: string;
  description: string;
  category: string;
  keyword: string;
  date: string;
  readTime: string;
  image: {
    src: string;
    alt: string;
  };
  sections: PostSection[];
  faqs: FAQItem[];
  relatedSlugs: string[];
};
