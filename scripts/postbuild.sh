#!/bin/bash
# Fix Next.js static export: directories need index.html for /blog/ to work
# Without this, Apache returns 403 on /blog/ (directory without index file)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="$SCRIPT_DIR/../out"

# Main blog directory — copy blog.html as index.html
if [ -f "$OUT_DIR/blog.html" ]; then
  cp "$OUT_DIR/blog.html" "$OUT_DIR/blog/index.html"
  echo "✅ blog/index.html created"
else
  echo "⚠️  blog.html not found"
fi

# Subdirectories — add redirect index
REDIRECT_HTML='<!DOCTYPE html><html><head><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=/blog"><script>window.location.href="/blog"</script></head><body><p>Redirecting to <a href="/blog">/blog</a>...</p></body></html>'

for subdir in page category; do
  if [ -d "$OUT_DIR/blog/$subdir" ]; then
    echo "$REDIRECT_HTML" > "$OUT_DIR/blog/$subdir/index.html"
    echo "✅ blog/$subdir/index.html created"
  fi
done

echo "postbuild done"
