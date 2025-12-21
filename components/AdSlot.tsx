import type { ReactNode } from "react";

type AdSlotProps = {
  label?: string;
  className?: string;
  children?: ReactNode;
};

const AdSlot = ({ label = "Advertisement", className = "", children }: AdSlotProps) => {
  const adsEnabled = process.env.NEXT_PUBLIC_ADS_ENABLED === "true";
  return (
    <div className={`ad-slot ${className}`.trim()} aria-label={label}>
      {/* AdSense placeholder: insert script and ad markup here when approved. */}
      <div className="ad-slot__label">{label}</div>
      {adsEnabled ? children : <div className="ad-slot__box">Ad slot placeholder</div>}
    </div>
  );
};

export default AdSlot;
