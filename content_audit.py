import os
import re
import hashlib
import json
from collections import defaultdict

class Auditor:
    def __init__(self, root='.'):
        self.root = root
        self.articles = []
        self.categories = defaultdict(list)
        self.dupes = {}

    def scan(self):
        # Adapted for Next.js TSX structure
        exts = ['.tsx', '.md', '.mdx']
        for root, dirs, files in os.walk(self.root):
            # Skip node_modules, .git, .next
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '.next', 'out']]
            for f in files:
                if any(f.endswith(e) for e in exts):
                    self.analyze(os.path.join(root, f))

    def analyze(self, path):
        try:
            text = open(path, 'r', encoding='utf-8', errors='ignore').read()
        except Exception as e:
            print(f"Error reading {path}: {e}")
            return

        # Skip layout files and non-content files if possible, but for now scan all
        if 'layout.tsx' in path or 'd.ts' in path:
            return

        # Simple content hash (ignoring non-alphanumeric)
        clean = re.sub(r'[^a-z0-9]', '', text.lower())
        if not clean:
            return
        hashval = hashlib.md5(clean.encode()).hexdigest()

        # Extract Title
        title = self.extract_title(text) or os.path.basename(path)
        
        # Extract Category (heuristic based on folder name or content)
        category = self.extract_category(text, path) or 'Uncategorized'

        info = {
            'filepath': path,
            'title': title,
            'category': category,
            'content_hash': hashval,
            'word_count': len(text.split())
        }

        self.articles.append(info)
        self.categories[category].append(info)

    def extract_title(self, text):
        # Try to find title in metadata const
        m = re.search(r'title:\s*["\']([^"\']+)["\']', text)
        if m: return m.group(1)
        
        # Try to find H1 tag
        m = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
        if m: 
            # Remove any nested tags or braces
            clean_h1 = re.sub(r'<[^>]+>', '', m.group(1))
            clean_h1 = re.sub(r'{.*?}', '', clean_h1) 
            return clean_h1.strip()
            
        return None

    def extract_category(self, text, path):
        # Try to find category in object
        m = re.search(r'category:\s*["\']([^"\']+)["\']', text)
        if m: return m.group(1)

        # Fallback to parent folder name
        parent = os.path.basename(os.path.dirname(path))
        if parent not in ['app', 'pages', 'src', 'utilities']:
            return parent.capitalize()
        
        return None

    def dedupe(self):
        hmap = defaultdict(list)
        for a in self.articles:
            hmap[a['content_hash']].append(a)
        self.dupes = {k: v for k, v in hmap.items() if len(v) > 1}

    def export(self):
        out = {
            'articles': self.articles,
            'categories': self.categories,
            'duplicates': self.dupes
        }
        json.dump(out, open('audit.json', 'w'), indent=2)
        print(f"Saved audit.json with {len(self.articles)} articles.")

if __name__ == '__main__':
    # Set root to current directory
    A = Auditor('.')
    A.scan()
    A.dedupe()
    A.export()
