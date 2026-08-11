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
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTIALS = ROOT / "_partials"
PAGES = ROOT / "_pages"

def slug_of(filename: str) -> str:
    """Turn 'home.md' -> 'home', 'index.md' -> 'index'."""
    return Path(filename).stem

def build_page(src: Path, head: str, foot: str) -> None:
    """Wrap one page body with the shared head/foot, substituting meta."""
    body = src.read_text(encoding="utf-8")
    # Page body declares its own meta block at the very top: {{ title }} {{ desc }}
    meta = re.search(r"\{\{ title: (.*?) \}\}\s*\{\{ desc: (.*?) \}\}", body, re.S)
    if not meta:
        raise ValueError(f"{src.name}: missing '{{{{ title: ... }}}}' and '{{{{ desc: ... }}}}' meta header")
    title = meta.group(1).strip()
    desc = meta.group(2).strip()
    page_html = body[meta.end():].lstrip("\n")

    out = (head.replace("{{PAGE_TITLE}}", title)
                .replace("{{PAGE_DESC}}", desc) + page_html + foot)
    out_name = "index.html" if src.stem == "home" else f"{src.stem}.html"
    out_path = ROOT / out_name
    out_path.write_text(out, encoding="utf-8")
    print(f"  wrote {out_name}  ({len(out)} bytes)")

def main() -> None:
    head = (PARTIALS / "head.html").read_text(encoding="utf-8")
    foot = (PARTIALS / "foot.html").read_text(encoding="utf-8")
    print("Building Drain Flow multi-page site...")
    for src in sorted(PAGES.glob("*.html")):
        build_page(src, head, foot)
    print("Done.")

if __name__ == "__main__":
    main()