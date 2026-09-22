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

Four tiers. Only the `data-` attributes are the source of truth — the order
form's package rows, the order summary and the sticky bar all read from them.

| Tier | Price | Was | Per bottle | Saves |
|---|---|---|---|---|
| 1 Bottle | ₱1,460 | ₱1,990 | ₱1,460 | ₱530 |
| 2 Bottles | ₱2,590 | ₱3,980 | ₱1,295 | ₱1,390 |
| **3 Bottles** (Best Value) | **₱3,490** | ₱5,970 | ₱1,163 | ₱2,480 |
| 5 Bottles | ₱4,990 | ₱9,950 | ₱998 | ₱4,960 |

₱1,460 for one bottle is the figure you set. The rest step the per-bottle price
down (₱1,460 → ₱1,295 → ₱1,163 → ₱998) so each tier is visibly better value,
with the 5-pack breaking the ₱1,000 barrier. The ₱1,990 "was" price is a
placeholder SRP — set it to your real list price.

> **Check your margin.** I do not know your landed cost per bottle. The 5-pack
> sells each bottle at 68% of the single price, so confirm that still makes
> money before you run ads to it.

```html
<div class="plan" data-plan="3 Bottles" data-qty="3" data-price="3490" data-was="5970">
```
Update the visible text inside the card to match.

### 2. Testimonials — **important**
All six reviews are placeholders. Replace them with **real customer feedback**
before publishing. Invented reviews breach DTI rules and Facebook/TikTok ad
policy, and can get your ad account banned. The same goes for the "4.9 / 5"
rating in the hero.

The hosted copy in `public/` shows a visible "Sample reviews" badge and carries
`noindex` for exactly this reason. Both disappear once you swap in real reviews
and remove the badge from `build.py`.

### 6. Where orders go — WebCake → Pancake POS

**This is the one step that decides whether orders reach your POS.**

The form built into this page is a *fallback*. It cannot create orders in
Pancake by itself. For orders to land in `pos.pancake.biz`, the page must use
**WebCake's own Order Form element**, because that is what is wired to your
Pancake shop.

**Do this:**

1. In Pancake, create the product and add **one variant per tier**, named
   exactly as the page names them:
   `1 Bottle` · `2 Bottles` · `3 Bottles` · `5 Bottles`
   These strings come from `data-plan` in the pricing cards. Keeping them
   identical means the tier a customer picks maps cleanly to a POS variant,
   and your stock and reports stay correct.
2. Set each variant's price to the table above.
3. In WebCake, open the page and drop the **Order Form** element inside
   `<section id="order">`, then delete the `<form class="order-form"> ... </form>`
   block. **Keep `<section id="order">` itself** — every CTA on the page,
   including the sticky mobile bar, scrolls to that anchor.
4. Connect the WebCake page to your Pancake shop in WebCake's settings, and
   place one live test order to confirm it appears in the POS before spending
   on ads.

**If you keep the built-in form instead**, set your own endpoint:
```js
FORM_ENDPOINT: "https://script.google.com/macros/s/AKfy.../exec",
```
It POSTs JSON: `package, quantity, amount, name, phone, address, city,
province, note, payment, page, at`. Google Apps Script, Zapier or Make all
work, and you would then push those into Pancake yourself.

> ⚠️ If `FORM_ENDPOINT` is **blank**, the thank-you screen still appears but
> **the order goes nowhere**. That is test mode only.

---

## Page structure

Sections in order, following the proven Cash-on-Delivery funnel pattern:

1. Promo bar with countdown · sticky header
2. Hero — product, benefits, CTA
3. Trust strip (shipping · COD · quality · vegetarian)
4. **FDA Registered and Certified** ← add your real certificates here
5. Sleep banner (full-bleed photo + hook)
6. "Does This Sound Like You?" — six concern tiles
7. Comparison table: glycinate vs oxide vs citrate, plus specs
8. Six benefits
9. "However Your Day Ends" — lifestyle strip
10. "One Small Habit" — three dosage steps
11. Six testimonials
12. Brand creative
13. "Here's What Arrives" — packaging, before the price
14. **Pricing — four tiers** + limited-stock note + guarantee
15. **How Ordering Works** — four-step delivery timeline
16. FAQ
17. Order form with **selectable package rows** + reassurance row
18. **Closing CTA band**
19. Footer with compliance notice

### Patterns deliberately not copied

A reference page may show these; they are left out because they would require
inventing things you do not have:

| Pattern | Why not |
|---|---|
| Before/after photos | Would be fabricated, and implies a treatment claim the FDA does not allow for a food supplement |
| Doctor or founder endorsement | Needs a real, named person who agrees to it. Easy to add later — ask and I will build the section |
| "As seen on" media logos | Only legitimate if you have actually been featured |
| Live "someone just ordered" popups | Fabricated social proof |
| 60-day money-back guarantee | That is a policy decision, not a design one. The page says 7 days — change it if your policy differs |

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
