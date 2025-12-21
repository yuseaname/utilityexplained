import Image from "next/image";

type ContentImageProps = {
  src: string;
  alt: string;
  width?: number;
  height?: number;
  className?: string;
};

const ContentImage = ({ src, alt, width = 1200, height = 800, className = "" }: ContentImageProps) => {
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      sizes="(max-width: 768px) 100vw, 800px"
      style={{ width: "100%", height: "auto", borderRadius: 12, margin: "1rem 0" }}
      className={className}
    />
  );
};

export default ContentImage;
