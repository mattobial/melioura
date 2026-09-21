# Melioura PH — Landing Page (WebCake)

High-converting English landing page for **Melioura Magnesium Glycinate**,
written for the Philippine Cash-on-Delivery market.

## What you deploy

`build.py` produces two versions:

| File | Size | Use it for |
|---|---|---|
| `melioura-landing.html` | ~487 KB (single file) | Paste into a WebCake HTML block |
| `public/index.html` | 79 KB + 306 KB images | Netlify / GitHub Pages — much faster on mobile data |

```bash
python3 build.py
```

### Pasting into WebCake
1. Create a new page in WebCake.
2. Add a full-width **HTML / Embed / Custom Code** block.
3. Paste the **entire contents** of `melioura-landing.html`.
4. Preview on a phone before publishing.

> If your WebCake plan does not allow `<script>` inside an HTML block, use
> WebCake's **native Order Form element** (see below) and delete the `<script>`
> at the end. The design still works — you only lose the countdown, the
> automatic order summary and the sticky bar.

---

## Before you publish — 6 things to replace

Search the file for **`REPLACE`** (Ctrl+F).

| # | What | Where |
|---|---|---|
| 1 | **Prices and packages** | `data-price` / `data-qty` / `data-was` in `<section id="buy">` |
| 2 | **Testimonials** | `<section class="sec sec--rev">` — all six are samples |
| 3 | **FDA LTO and CPN numbers** | footer |
| 4 | **Contact details** (number, email, FB page) | footer |
| 5 | **Dosage** | the "One Small Habit" section — match your actual label |
| 6 | **Where orders go** | `CONFIG.FORM_ENDPOINT` in the `<script>` |

### 1. Prices
Edit these only. The order form and the sticky bar follow them automatically:

```html
<div class="plan" data-plan="3 Bottles — Buy 2 Get 1 Free"
     data-qty="3" data-price="1980" data-was="4770">
```
Remember to update the visible text inside the card too.

### 2. Testimonials — **important**
All six reviews are placeholders. Replace them with **real customer feedback**
before publishing. Invented reviews breach DTI rules and Facebook/TikTok ad
policy, and can get your ad account banned. The same goes for the "4.9 / 5"
rating in the hero.

The hosted copy in `public/` shows a visible "Sample reviews" badge and carries
`noindex` for exactly this reason. Both disappear once you swap in real reviews
and remove the badge from `build.py`.

### 6. Where orders go
**Option A — WebCake native form (recommended).**
Replace the whole `<form class="order-form"> ... </form>` with your WebCake
Order Form element. Do not remove `<section id="order">` — every button on the
page points at it.

**Option B — your own endpoint.**
```js
FORM_ENDPOINT: "https://script.google.com/macros/s/AKfy.../exec",
```
Google Apps Script, Zapier or Make all work. It POSTs JSON:
`package, quantity, amount, name, phone, address, city, province, note, payment, page, at`.

> ⚠️ If `FORM_ENDPOINT` is **blank**, the thank-you screen still appears but
> **the order goes nowhere**. That is test mode only.

---

## Photos — where each one is used

**Eight real photographs, each used exactly once. Nothing repeats.**

| Photo | Where it appears | Why there |
|---|---|---|
| `product.webp` | Hero | Transparent background, so the bottle floats — no box, more premium |
| `bed.webp` | Sleep banner (full-bleed) | Still life, so headline text stays readable over it |
| `woman.webp` | "Why Glycinate" | She is holding the bottle, which shows its real size |
| `desk.webp` · `couple.webp` | "However Your Day Ends" strip | Two everyday moments, small and side by side |
| `night.webp` | "One Small Habit" | She is taking it in bed — matches the "before bed" instruction |
| `pack.webp` | "Here's What Arrives" | Bottle + box + capsules, answering the COD buyer before the price |
| `evening.webp` | After the testimonials | Finished creative whose line is "a calmer evening for a brighter tomorrow" |

The bottle count on the pricing cards is **drawn as SVG**, not a photo, so the
same image is never repeated across the three cards.

### Photos kept out of the page on purpose

| File | Why |
|---|---|
| `assets/brand.webp` | Daytime pilates creative. Same baked headline as `evening.webp` but a weaker match for a sleep-led page. Kept so you can swap it back in one line. |
| The desk creative (man + laptop) | Near-duplicate of `brand.webp` in concept and shares its tagline. Two creatives with competing baked headlines make the page read like an ad slideshow. |
| The brand board | A design sheet, not photography. On a sales page it reads like an internal brand guideline. |

> The creatives with **baked-in text** are sized for full-screen social feeds, so
> that text reads small at page width. They work hardest as the actual
> Facebook/TikTok ads that drive traffic to this page. `evening.webp` is the one
> exception on the page, because its message matches the sleep hook directly.

### ⚠️ Never remove `height:auto` from `<img>`
If an `<img>` has `width` and `height` attributes but no `height:auto` in CSS,
the browser uses the height attribute as the real height and the photo renders
**stretched**. There is a global `img{max-width:100%; height:auto}` rule to stop
this happening again.

### Swapping a photo
Drop a replacement into `assets/` keeping the same filename and run
`python3 build.py`. To serve them from the WebCake media library instead, point
the `--img-*` variables in `:root` at your CDN links.

---

## Hosting a public preview

`public/` is the deployable copy (`index.html`, `robots.txt`, `img/`).

**Netlify** (a site named `melioura-ph` already exists in the account):
```bash
npx netlify-cli deploy --prod --dir=public --site melioura-ph
```
Or drag the `public/` folder onto https://app.netlify.com/drop

**GitHub Pages** — `public/` is pushed. In Settings → Pages, pick branch
`claude/philippines-landing-page-jkuwk4` and folder `/public`.

> WebCake is still the real destination for the live selling page. The hosting
> above is only for previewing and sharing.

---

## Responsiveness — how it works

The page is **container-based**, not viewport-based. A `<div class="mlr">`
wrapper declares `container-type: inline-size`, and every size (`cqi` units,
`@container` queries, `auto-fit` grids) follows the width of the **block** it
sits in — not the browser window. That is why it looks right inside a narrow
WebCake column, on a tablet and on a phone.

Two things **not** to change:
1. The `<div class="mlr">` wrapper — the whole layout adapts through it.
2. The sticky CTA bar sits **outside** `.mlr`. Move it inside and it stops
   pinning to the bottom of the screen, because a size container becomes the
   containing block for `position: fixed`.

There is also JavaScript that restores `<meta name="viewport">` if a page
builder strips it — the most common cause of a page looking "not responsive".

Tested from **320px to 1920px**, and inside containers of
320/380/600/768/900/1100px — no horizontal scroll and no overflow.

---

## For developers

```
src/template.html      # source, with __IMG_*__ placeholders
assets/*.webp          # the six photographs
build.py               # produces both versions
melioura-landing.html  # single-file output → WebCake
public/                # hosted output → Netlify / GitHub Pages
```

## Compliance

The page carries **"No Approved Therapeutic Claims"** and the advice to consult
a doctor. Benefit copy is deliberately structure/function wording ("supports",
"helps with") rather than claims to treat disease. Do not upgrade it to disease
claims — that is the most common trigger for an FDA advisory and for ad
rejection in the Philippines.
