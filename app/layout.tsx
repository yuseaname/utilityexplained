import type { Metadata } from "next";
import type { ReactNode } from "react";
import { Fraunces, IBM_Plex_Sans } from "next/font/google";
import Script from "next/script";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import SkipLink from "@/components/SkipLink";
import LinkTracker from "@/components/LinkTracker";
import { siteConfig } from "@/lib/site";

const headingFont = Fraunces({
  subsets: ["latin"],
  variable: "--font-heading",
  weight: ["400", "600", "700"]
});

const bodyFont = IBM_Plex_Sans({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600"]
});

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.url),
  title: {
    default: siteConfig.name,
    template: `%s | ${siteConfig.name}`
  },
  description: siteConfig.description,
  openGraph: {
    title: siteConfig.name,
    description: siteConfig.description,
    url: siteConfig.url,
    siteName: siteConfig.name,
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: "Utility Explained"
      }
    ],
    type: "website"
  },
  twitter: {
    card: "summary_large_image",
    title: siteConfig.name,
    description: siteConfig.description,
    images: [siteConfig.ogImage]
  }
};

export default function RootLayout({ children }: { children: ReactNode }) {
  const adClient = process.env.NEXT_PUBLIC_ADSENSE_CLIENT || "";
  const adsEnabled = process.env.NEXT_PUBLIC_ADS_ENABLED === "true";
  
  return (
    <html lang="en" className={`${headingFont.variable} ${bodyFont.variable}`}>
      <head>
        <Script
          src="https://app.rybbit.io/api/script.js"
          data-site-id="d5b63e065e9d"
          strategy="afterInteractive"
        />
        {adsEnabled && adClient && (
          <Script
            async
            src={`https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${adClient}`}
            crossOrigin="anonymous"
            strategy="afterInteractive"
          />
        )}
      </head>
      <body>
        <SkipLink />
        <LinkTracker />
        <Header />
        <main id="main-content">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
