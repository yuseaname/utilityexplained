# Hosting, Caching, and Security Headers

This site is built as a static export (`output: "export"`), so caching, compression, and
security headers must be set at the host/CDN layer.

## Caching and Compression (Safe Wins)
- Enable Brotli and Gzip compression for HTML, CSS, JS, SVG, and JSON.
- Cache static assets aggressively:
  - `/_next/static/*` and `/images/*`
  - `Cache-Control: public, max-age=31536000, immutable`
- Cache HTML with a shorter TTL if your host supports it (e.g., 5-10 minutes) or leave
  it uncached for instant updates.

## Security Headers (Start with Report-Only CSP)
Recommended baseline:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-site
```

Report-only CSP starter (adjust domains based on your real integrations):
```
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self' https://pagead2.googlesyndication.com https://app.rybbit.io; img-src 'self' https: data:; style-src 'self' 'unsafe-inline'; font-src 'self' https: data:; connect-src 'self' https://app.rybbit.io; frame-src https://googleads.g.doubleclick.net https://tpc.googlesyndication.com; report-uri /csp-report
```

After collecting CSP reports, tighten to an enforced CSP.

## Common Host Examples

### Vercel (`vercel.json`)
```
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains; preload" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()" },
        { "key": "Cross-Origin-Opener-Policy", "value": "same-origin" },
        { "key": "Cross-Origin-Resource-Policy", "value": "same-site" },
        { "key": "Content-Security-Policy-Report-Only", "value": "default-src 'self'; script-src 'self' https://pagead2.googlesyndication.com https://app.rybbit.io; img-src 'self' https: data:; style-src 'self' 'unsafe-inline'; font-src 'self' https: data:; connect-src 'self' https://app.rybbit.io; frame-src https://googleads.g.doubleclick.net https://tpc.googlesyndication.com; report-uri /csp-report" }
      ]
    },
    {
      "source": "/_next/static/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/images/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}
```

### Netlify (`public/_headers`)
```
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Resource-Policy: same-site
  Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self' https://pagead2.googlesyndication.com https://app.rybbit.io; img-src 'self' https: data:; style-src 'self' 'unsafe-inline'; font-src 'self' https: data:; connect-src 'self' https://app.rybbit.io; frame-src https://googleads.g.doubleclick.net https://tpc.googlesyndication.com; report-uri /csp-report

/_next/static/*
  Cache-Control: public, max-age=31536000, immutable

/images/*
  Cache-Control: public, max-age=31536000, immutable
```

### Cloudflare (Rules)
- Cache static paths with long TTL.
- Add the headers above via Transform Rules.
- Enable Brotli in the dashboard.
