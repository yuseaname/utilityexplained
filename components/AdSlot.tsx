"use client";

import type { ReactNode } from "react";
import { useEffect, useRef } from "react";

type AdSlotProps = {
  label?: string;
  className?: string;
  format?: "auto" | "rectangle" | "vertical" | "horizontal";
  slot?: string;
  responsive?: boolean;
  children?: ReactNode;
};

const AdSlot = ({ 
  label = "Advertisement", 
  className = "", 
  format = "auto",
  slot,
  responsive = true,
  children 
}: AdSlotProps) => {
  const adRef = useRef<HTMLModElement>(null);
  const adsEnabled = process.env.NEXT_PUBLIC_ADS_ENABLED === "true";
  const adClient = process.env.NEXT_PUBLIC_ADSENSE_CLIENT || "";

  useEffect(() => {
    if (adsEnabled && slot && typeof window !== "undefined") {
      try {
        // @ts-ignore
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      } catch (err) {
        console.error("AdSense error:", err);
      }
    }
  }, [adsEnabled, slot]);

  if (!adsEnabled || !slot) {
    return (
      <div className={`ad-slot ${className}`.trim()} aria-label={label}>
        <div className="ad-slot__label">{label}</div>
        <div className="ad-slot__box">Ad slot placeholder</div>
      </div>
    );
  }

  return (
    <div className={`ad-slot ${className}`.trim()} aria-label={label}>
      <div className="ad-slot__label">{label}</div>
      <ins
        ref={adRef}
        className="adsbygoogle"
        style={{ display: "block" }}
        data-ad-client={adClient}
        data-ad-slot={slot}
        data-ad-format={format}
        data-full-width-responsive={responsive ? "true" : "false"}
      />
    </div>
  );
};

export default AdSlot;
