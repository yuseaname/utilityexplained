"use client";

import { useState } from "react";
import type { FAQItem } from "@/lib/types";

type FAQAccordionProps = {
  items: FAQItem[];
};

const FAQAccordion = ({ items }: FAQAccordionProps) => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <div className="faq">
      {items.map((item, index) => {
        const isOpen = openIndex === index;
        return (
          <div key={item.question} className="faq-item">
            <button
              className="faq-question"
              type="button"
              aria-expanded={isOpen}
              onClick={() => setOpenIndex(isOpen ? null : index)}
            >
              {item.question}
            </button>
            {isOpen ? <p className="faq-answer">{item.answer}</p> : null}
          </div>
        );
      })}
    </div>
  );
};

export default FAQAccordion;
