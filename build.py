#!/usr/bin/env python3
"""
Drain Flow site builder.

Assembles the multi-page static site from shared partials so that the header,
nav, and footer live in ONE place (_partials/) and every page inherits the same
branding. To add a page or change the nav, edit _partials/ and the _pages/*.html
bodies, then re-run:

    python3 build.py

Output HTML is written to the repo root (next to styles.css), ready for
GitHub Pages or Cloudflare Pages with no extra config (root directory served).
"""
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTIALS = ROOT / "_partials"
PAGES = ROOT / "_pages"

def slug_of(filename: str) -> str:
    """Turn 'home.md' -> 'home', 'index.md' -> 'index'."""
    return Path(filename).stem

DOMAIN = "https://drainflowpro.com"

# Ordered, human-readable sitemap entries (home first, then nav, then blog).
# out_name -> (path, change_freq). Automatically kept in sync with _pages/.
SITEMAP_ORDER = [
    ("index.html", "weekly"),
    ("services.html", "monthly"),
    ("blog.html", "weekly"),
    ("about.html", "monthly"),
    ("media.html", "monthly"),
    ("reviews.html", "monthly"),
    ("faq.html", "monthly"),
    ("contact.html", "monthly"),
    ("blog-never-down-drain.html", "yearly"),
    ("blog-no-dig.html", "yearly"),
    ("blog-sump-pump.html", "yearly"),
]

def build_page(src: Path, head: str, foot: str) -> None:
    """Wrap one page body with the shared head/foot, substituting meta."""
    body = src.read_text(encoding="utf-8")
    meta = re.search(r"\{\{ title: (.*?) \}\}\s*\{\{ desc: (.*?) \}\}", body, re.S)
    if not meta:
        raise ValueError(f"{src.name}: missing '{{{{ title: ... }}}}' and '{{{{ desc: ... }}}}' meta header")
    title = meta.group(1).strip()
    desc = meta.group(2).strip()
    page_html = body[meta.end():].lstrip("\n")

    out_name = "index.html" if src.stem == "home" else f"{src.stem}.html"
    can_on = f"{DOMAIN}/{out_name}" if out_name != "index.html" else f"{DOMAIN}/"

    # Auto-build FAQPage schema from the visible FAQ Q&A blocks (keeps them in lockstep).
    if out_name == "faq.html":
        faq_json = build_faq_schema(page_html)
        page_html = page_html.replace("<!-- AUTO:FAQ_JSON -->", faq_json)

    out = (head.replace("{{PAGE_TITLE}}", title)
                .replace("{{PAGE_DESC}}", desc)
                .replace("{{PAGE_TITLE_ESC}}", html.escape(title, quote=True))
                .replace("{{PAGE_DESC_ESC}}", html.escape(desc, quote=True))
                .replace("{{PAGE_CANON}}", can_on) + page_html + foot)
    out_path = ROOT / out_name
    out_path.write_text(out, encoding="utf-8")
    print(f"  wrote {out_name}  ({len(out)} bytes)")

def build_faq_schema(page_html: str) -> str:
    """Generate an https://schema.org/FAQPage JSON-LD block from visible
    <h2 class="faq-q"> / <p class="faq-a"> pairs, so the schema can never
    drift from the page content again."""
    items = re.findall(
        r'<h2 class="faq-q">(.*?)</h2>\s*<p class="faq-a">(.*?)</p>',
        page_html, re.S,
    )
    def plain(t):
        return re.sub(r"<[^>]+>", "", t).replace("&amp;", "&").strip()
    qas = []
    for q, a in items:
        qas.append({
            "@type": "Question",
            "name": plain(q),
            "acceptedAnswer": {"@type": "Answer", "text": plain(a)},
        })
    import json
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qas}
    return '<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=2) + '\n</script>'

def write_static_files() -> None:
    """Generate robots.txt + sitemap.xml from the canonical page set."""
    # robots.txt
    robots = "User-agent: *\nAllow: /\n\nSitemap: https://drainflowpro.com/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")

    # sitemap.xml
    entries = []
    for out_name, freq in SITEMAP_ORDER:
        if out_name != "index.html":
            url = f"{DOMAIN}/{out_name}"
            entries.append(f"  <url><loc>{url}</loc><changefreq>{freq}</changefreq></url>")
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{DOMAIN}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>\n"
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print("  wrote robots.txt + sitemap.xml")

def main() -> None:
    head = (PARTIALS / "head.html").read_text(encoding="utf-8")
    foot = (PARTIALS / "foot.html").read_text(encoding="utf-8")
    print("Building Drain Flow multi-page site...")
    for src in sorted(PAGES.glob("*.html")):
        build_page(src, head, foot)
    write_static_files()
    print("Done.")

if __name__ == "__main__":
    main()