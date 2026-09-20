#!/usr/bin/env python3
"""Build the self-contained WebCake landing page.

Inlines the product photos as base64 data URIs so the HTML can be pasted
into a WebCake HTML/Embed block without uploading anything first.
Run:  python3 build.py
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "src" / "template.html"
ASSETS = ROOT / "assets"
OUT = ROOT / "melioura-landing.html"

html = TEMPLATE.read_text(encoding="utf-8")
for name in ("hero", "lifestyle", "sunrise", "cap",
             "capsules", "leaf", "flower", "stonetex"):
    f = ASSETS / f"{name}.jpg"
    if not f.exists():
        sys.exit(f"missing asset: {f}")
    uri = "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode()
    html = html.replace(f"__IMG_{name.upper()}__", uri)

OUT.write_text(html, encoding="utf-8")
print(f"built {OUT} ({len(html)/1024:.0f} KB)")

# Hosted copy (GitHub Pages / Netlify / any static host).
# Same page, plus: noindex while it is a draft, and a visible marker on the
# testimonials so the sample reviews are never shown as if they were real.
TAG = ('<span style="display:inline-block;background:#8A6A33;color:#FFF3E0;'
       'font-family:Jost,Arial,sans-serif;font-size:.68rem;font-weight:600;'
       'letter-spacing:.14em;text-transform:uppercase;padding:6px 16px;'
       'border-radius:999px;margin-bottom:18px">'
       '\u26a0 Sample \u2014 palitan ng totoong review</span>\n      ')
ANCHOR = '<p class="eyebrow">Mula sa Mga Gumagamit</p>'
hosted = html.replace('<meta name="viewport"',
                      '<meta name="robots" content="noindex, nofollow">\n<meta name="viewport"', 1)
assert hosted.count(ANCHOR) == 1
hosted = hosted.replace(ANCHOR, TAG + ANCHOR, 1)

PUB = ROOT / "public"
PUB.mkdir(exist_ok=True)
(PUB / "index.html").write_text(hosted, encoding="utf-8")
(PUB / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
print(f"built {PUB/'index.html'} ({len(hosted)/1024:.0f} KB)")
