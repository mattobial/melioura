#!/usr/bin/env python3
"""Build the Melioura landing page in two flavours.

  melioura-landing.html  - one self-contained file, photos inlined as base64.
                           This is what you paste into a WebCake HTML block.
  public/index.html      - same page, but referencing public/img/*.webp.
                           Much lighter on mobile data; use it for any host
                           that serves a folder (Netlify, GitHub Pages).

Run:  python3 build.py
"""
import base64
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "src" / "template.html"
ASSETS = ROOT / "assets"
SINGLE = ROOT / "melioura-landing.html"
PUBLIC = ROOT / "public"

# One photograph per section — see README for the mapping.
PHOTOS = ("product", "bed", "woman", "night", "desk", "couple", "pack", "evening")

template = TEMPLATE.read_text(encoding="utf-8")


def fill(html: str, src_for) -> str:
    """Replace __IMG_NAME__ (CSS url()) and __IMG_NAME_SRC__ (<img src>)."""
    for name in PHOTOS:
        f = ASSETS / f"{name}.webp"
        if not f.exists():
            sys.exit(f"missing asset: {f}")
        ref = src_for(name, f)
        html = html.replace(f"__IMG_{name.upper()}_SRC__", ref)
        html = html.replace(f"__IMG_{name.upper()}__", ref)
    if "__IMG_" in html:
        sys.exit("unresolved image placeholder remains")
    return html


def inline(_name, f):
    return "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode()


def external(name, _f):
    return f"img/{name}.webp"


# --- 1. Self-contained file for WebCake -------------------------------------
single = fill(template, inline)
SINGLE.write_text(single, encoding="utf-8")
print(f"built {SINGLE.name} ({len(single)/1024:.0f} KB, self-contained)")

# --- 2. Hosted copy ---------------------------------------------------------
# Same page plus: noindex while the content is still placeholder, and a visible
# marker on the testimonials so the sample reviews are never shown as genuine.
TAG = ('<span style="display:inline-block;background:#8A6A33;color:#FFF3E0;'
       'font-family:Jost,Arial,sans-serif;font-size:.68rem;font-weight:600;'
       'letter-spacing:.14em;text-transform:uppercase;padding:6px 16px;'
       'border-radius:999px;margin-bottom:18px">'
       '⚠ Sample reviews — replace with real ones</span>\n      ')
# Anchored on a class, not on copy, so rewording the page cannot silently
# drop this marker.
ANCHOR = '<div class="rev-top rv">'

hosted = fill(template, external)
hosted = hosted.replace('<meta name="viewport"',
                        '<meta name="robots" content="noindex, nofollow">\n<meta name="viewport"', 1)
if hosted.count(ANCHOR) != 1:
    sys.exit("testimonial anchor not found - cannot mark sample reviews")
hosted = hosted.replace(ANCHOR, TAG + ANCHOR, 1)

img_dir = PUBLIC / "img"
img_dir.mkdir(parents=True, exist_ok=True)
for name in PHOTOS:
    shutil.copy2(ASSETS / f"{name}.webp", img_dir / f"{name}.webp")

(PUBLIC / "index.html").write_text(hosted, encoding="utf-8")
(PUBLIC / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
img_kb = sum(f.stat().st_size for f in img_dir.iterdir()) / 1024
print(f"built public/index.html ({len(hosted)/1024:.0f} KB + {img_kb:.0f} KB images)")
