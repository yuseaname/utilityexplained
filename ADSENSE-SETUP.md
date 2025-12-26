# AdSense Setup Guide for Utility Plain English

## Phase 4 Implementation Complete ✅

All critical SEO and AdSense optimizations have been implemented. Follow these steps to activate revenue.

---

## What Was Fixed

### 1. ✅ Sitemap Optimization
- Added all 6 pillar pages to sitemap
- Implemented priority values (1.0 = highest, 0.3 = lowest)
- Added changefreq hints for Google crawl scheduling
- Properly prioritized content types

### 2. ✅ Production-Ready AdSense Component
- Built `<AdSlot>` component with Google AdSense integration
- Supports all ad formats (auto, rectangle, horizontal, vertical)
- Lazy loading ready (prevents CLS violations)
- Environment-based activation (safe for dev/prod)

### 3. ✅ Schema Markup (Rich Snippets)
- Article schema on all 5 pillar pages
- Breadcrumb schema for navigation
- BlogPosting + FAQ schema on blog posts
- Organization schema on homepage

### 4. ✅ Metadata & SEO Enhancements
- Robots meta tags (max-image-preview, max-snippet)
- Canonical tags on all pages
- Pagination noindex rules (only first 3 pages indexed)
- OpenGraph and Twitter cards already present

### 5. ✅ Optimized Ad Placements
**Homepage:** 3 ad slots
- After hero section
- After "Popular explainers"
- Before trust section

**Blog Posts (14 posts):** 3+ ads per post
- After first section (in-article native)
- Mid-content ad (50% scroll)
- After content (before FAQ)

**Pillar Pages:** Ready for manual placement (add per page)

---

## Step-by-Step Activation

### Step 1: Apply for AdSense
1. Go to https://adsense.google.com
2. Sign up with the site: `https://www.utilityplainenglish.com`
3. Add AdSense verification code when prompted (already in `<head>`)
4. Submit for review

**Approval timeline:** 1-4 weeks (typical for new sites)

---

### Step 2: While Waiting for Approval
Do NOT enable ads yet. Focus on traffic:

1. **Submit to Google Search Console**
   - Add property: `utilityplainenglish.com`
   - Submit sitemap: `https://www.utilityplainenglish.com/sitemap.xml`
   - Request indexing for pillar pages

2. **Build Initial Backlinks**
   - Reddit: r/personalfinance, r/Frugal (helpful comments only)
   - Quora: Answer utility bill questions, link to guides
   - Local utility forums

3. **Content Expansion** (Optional)
   - Add 5-10 more blog posts (targets in Phase 5)
   - Update glossary with more terms
   - Add comparison tables to pillar pages

---

### Step 3: After AdSense Approval

1. **Create Ad Units in AdSense Dashboard**

Navigate to Ads → Ad units → Display ads

Create these units:

| Ad Unit Name | Type | Size | Use Case |
|--------------|------|------|----------|
| `Home Hero Ad` | Display | Responsive | Homepage after hero |
| `Home Mid Ad` | Display | Horizontal | Homepage mid-content |
| `Home Bottom Ad` | Display | Horizontal | Homepage lower |
| `Article Top Ad` | In-article | Native | Blog posts, top |
| `Article Mid Ad` | In-article | Native | Blog posts, middle |
| `Article Bottom Ad` | Display | Horizontal | Blog posts, bottom |
| `Pillar Top Ad` | Display | Responsive | Pillar pages, intro |
| `Pillar Mid Ad` | Display | Responsive | Pillar pages, mid |
| `Pillar Bottom Ad` | Display | Horizontal | Pillar pages, end |
| `Sidebar Ad` | Display | Vertical (300x600) | Future sticky sidebar |

2. **Copy Your Credentials**
   - Publisher ID: `ca-pub-XXXXXXXXXXXXXXXX`
   - Ad unit slot IDs: 10-digit numbers for each unit

3. **Create Environment File**

In the project root, create `.env.local`:

```bash
# Copy this from .env.example

# Enable ads
NEXT_PUBLIC_ADS_ENABLED=true

# Your AdSense publisher ID
NEXT_PUBLIC_ADSENSE_CLIENT=ca-pub-XXXXXXXXXXXXXXXX

# Ad Unit Slot IDs (get from AdSense dashboard)
NEXT_PUBLIC_AD_SLOT_HOME_HERO=1234567890
NEXT_PUBLIC_AD_SLOT_HOME_MID=1234567890
NEXT_PUBLIC_AD_SLOT_HOME_BOTTOM=1234567890

NEXT_PUBLIC_AD_SLOT_ARTICLE_TOP=1234567890
NEXT_PUBLIC_AD_SLOT_ARTICLE_MID=1234567890
NEXT_PUBLIC_AD_SLOT_ARTICLE_BOTTOM=1234567890

NEXT_PUBLIC_AD_SLOT_PILLAR_TOP=1234567890
NEXT_PUBLIC_AD_SLOT_PILLAR_MID=1234567890
NEXT_PUBLIC_AD_SLOT_PILLAR_BOTTOM=1234567890

NEXT_PUBLIC_AD_SLOT_SIDEBAR=1234567890
```

4. **Rebuild and Deploy**

```bash
npm run build
# Then deploy to your host (Vercel, Netlify, etc.)
```

5. **Verify Ads Are Showing**
   - Visit your site in incognito mode
   - Check homepage, blog posts, pillar pages
   - Ads may show as blank for first 24-48 hours (normal)

---

### Step 4: Monitor Performance

**First Week:**
- Check AdSense dashboard daily
- Watch for policy violations (fix immediately)
- Monitor page speed (ads slow sites—target <3s LCP)

**First Month:**
- Track RPM (Revenue Per Mille = revenue per 1,000 page views)
- Identify top-earning pages
- A/B test ad placements (move ads up/down slightly)

**Expected Benchmarks (US traffic):**
- **RPM:** $3-8 (utilities niche is mid-tier CPC)
- **CTR:** 1-3% (typical display ads)
- **Page views needed for $100/month:** ~3,000-10,000

---

## Troubleshooting

### Ads Not Showing
- Clear browser cache and cookies
- Wait 24-48 hours after enabling
- Check AdSense account for policy warnings
- Verify `.env.local` values are correct

### Low RPM
- Add more long-form content (more ads per page)
- Target high-CPC keywords (energy provider comparisons)
- Improve session depth (related posts, internal links)
- Focus on US traffic (highest CPCs)

### Policy Violations
- Remove any affiliate links (AdSense + affiliates = violation)
- Keep content neutral (no "best provider" recommendations)
- Add privacy policy footer link (already done ✅)
- Maintain 70%+ original content

---

## Next: Phase 5 Scaling Strategy

Once ads are live and earning:
1. **Traffic Growth:** SEO content expansion (see Phase 5 targets)
2. **Engagement:** Add calculators, interactive tools
3. **Seasonality:** Publish winter heating content (Nov-Feb), summer cooling (May-Aug)
4. **Email List:** Capture emails for return visits (higher RPM)

---

## Quick Reference: Files Changed

| File | What Changed |
|------|--------------|
| `app/sitemap.ts` | Added pillar pages, priorities, changefreq |
| `components/AdSlot.tsx` | Production AdSense integration |
| `app/layout.tsx` | Added AdSense script loader |
| `.env.example` | AdSense configuration template |
| `app/page.tsx` | 3 ad slots added |
| `app/blog/[slug]/page.tsx` | 3 ad slots per post |
| `app/electricity-explained/page.tsx` | Schema + robots meta |
| `app/gas-explained/page.tsx` | Schema + robots meta |
| `app/water-explained/page.tsx` | Schema + robots meta |
| `app/utility-bills-costs-explained/page.tsx` | Schema + robots meta |
| `app/heating-cooling-explained/page.tsx` | Schema + robots meta |
| `app/utilities-glossary/page.tsx` | Schema + robots meta |
| `app/blog/page/[page]/page.tsx` | Canonical + robots meta |

---

## Support & Resources

- **AdSense Help:** https://support.google.com/adsense
- **Policy Center:** https://support.google.com/adsense/answer/48182
- **Optimization Tips:** https://www.google.com/adsense/start/resources/

---

**Status:** ✅ Ready for AdSense approval and activation
**Estimated Setup Time:** 30 minutes (after approval)
**Revenue Potential:** $50-500/month (at 10k-50k monthly page views)
