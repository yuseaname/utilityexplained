/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    unoptimized: true,
    remotePatterns: [
      {
        protocol: "https",
        hostname: "images.unsplash.com"
      },
      {
        protocol: "https",
        hostname: "images.pexels.com"
      },
      { protocol: "https", hostname: "devinebi.com" },
      { protocol: "https", hostname: "www.visualcapitalist.com" },
      { protocol: "https", hostname: "assets.fixr.com" },
      { protocol: "https", hostname: "assets.solar.com" },
      { protocol: "https", hostname: "www.landlordsafetycertificate.co.uk" },
      { protocol: "https", hostname: "smartenergycc.org" }
    ]
  }
};

module.exports = nextConfig;
