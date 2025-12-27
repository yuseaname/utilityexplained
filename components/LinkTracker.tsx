"use client";

import { useEffect } from "react";
import { trackEvent } from "@/lib/analytics";

const LinkTracker = () => {
  useEffect(() => {
    const handler = (event: MouseEvent) => {
      const target = event.target as HTMLElement | null;
      if (!target) return;

      const link = target.closest("a[data-track]") as HTMLAnchorElement | null;
      if (!link) return;

      trackEvent({
        event: "internal_link_click",
        label: link.dataset.trackLabel ?? "internal",
        value: link.dataset.trackValue,
        href: link.getAttribute("href") ?? undefined
      });
    };

    document.addEventListener("click", handler);
    return () => document.removeEventListener("click", handler);
  }, []);

  return null;
};

export default LinkTracker;
