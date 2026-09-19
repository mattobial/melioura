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
