import json, re
from pathlib import Path

root = Path(r"c:\Users\yusea\Desktop\repo\utilities\utilities")
files = [root/"lib"/"posts.tsx"] + sorted((root/"lib"/"generatedPosts").glob("*.tsx"))

# Basic JS/TS string literal parser (supports ", ', ` with escapes)
def parse_js_string(s, i):
    q = s[i]
    if q not in ('"', "'", '`'):
        raise ValueError('Not at string start')
    i += 1
    out = []
    while i < len(s):
        ch = s[i]
        if ch == '\\':
            if i + 1 < len(s):
                out.append(s[i + 1])
                i += 2
                continue
            i += 1
            continue
        if ch == q:
            return ''.join(out), i + 1
        out.append(ch)
        i += 1
    raise ValueError('Unterminated string')


def find_field_value(src, field, start, end):
    m = re.search(rf"\b{re.escape(field)}\s*:\s*([\"'`])", src[start:end])
    if not m:
        return None
    qpos = start + m.start(1)
    try:
        val, _ = parse_js_string(src, qpos)
    except Exception:
        return None
    return val


inventory = []
seen = set()

for f in files:
    src = f.read_text(encoding="utf-8")
    slug_iter = list(re.finditer(r"\bslug\s*:\s*([\"'`])", src))
    for idx, m in enumerate(slug_iter):
        qpos = m.start(1)
        try:
            slug, after = parse_js_string(src, qpos)
        except Exception:
            continue

        next_start = slug_iter[idx + 1].start() if idx + 1 < len(slug_iter) else None
        window_end = next_start if next_start is not None else min(len(src), after + 20000)

        title = find_field_value(src, "title", after, window_end)
        category = find_field_value(src, "category", after, window_end)

        if title is None or category is None:
            continue

        key = (str(f), slug)
        if key in seen:
            continue
        seen.add(key)
        inventory.append({
            "slug": slug,
            "title": title,
            "currentCategory": category,
            "sourceFile": str(f.relative_to(root)).replace('\\\\', '/')
        })

counts = {}
for p in inventory:
    counts[p["currentCategory"]] = counts.get(p["currentCategory"], 0) + 1

result = {
    "posts": sorted(inventory, key=lambda x: (x["currentCategory"], x["slug"], x["sourceFile"])),
    "countsPerCurrentCategory": dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
}
print(json.dumps(result, indent=2, ensure_ascii=False))
