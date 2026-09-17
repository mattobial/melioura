# Melioura PH — Landing Page (WebCake)

High-converting Taglish landing page para sa **Melioura Magnesium Glycinate**,
ginawa para sa Philippine COD market.

## Ang ide-deploy mo

**`melioura-landing.html`** — isang file lang, self-contained. Naka-embed na ang
mga litrato (base64), walang external dependency maliban sa Google Fonts.

### Paano i-paste sa WebCake
1. Gumawa ng bagong page sa WebCake.
2. Maglagay ng **HTML / Embed / Custom Code** block na buong lapad (full width).
3. I-paste ang **buong laman** ng `melioura-landing.html`.
4. I-preview sa cellphone bago i-publish.

> Kung hindi pinapayagan ng WebCake plan mo ang `<script>` sa HTML block:
> gamitin ang **native Order Form element** ng WebCake (tingnan sa baba) at
> tanggalin ang `<script>` sa dulo. Gagana pa rin ang buong disenyo — ang
> mawawala lang ay ang countdown, ang auto-sync ng summary, at ang sticky bar.

---

## Bago mag-publish — 6 na bagay na dapat palitan

Hanapin mo lang ang salitang **`PALITAN`** sa file (Ctrl+F).

| # | Ano | Saan |
|---|-----|------|
| 1 | **Presyo at package** | `data-price` / `data-qty` / `data-was` sa `<section id="buy">` |
| 2 | **Mga testimonial** | `<section class="sec sec--rev">` — sample lang ang nandoon |
| 3 | **FDA LTO at CPN number** | footer |
| 4 | **Contact details** (number, email, FB page) | footer |
| 5 | **Dosage** | `<section class="sec sec--how">` — itugma sa aktuwal na label |
| 6 | **Saan pupunta ang order** | `CONFIG.FORM_ENDPOINT` sa `<script>` |

### 1. Presyo
Dito ka lang mag-e-edit. Sinusundan ito ng order form at ng sticky bar automatically:

```html
<div class="plan" data-plan="3 Bottles — Buy 2 Take 1"
     data-qty="3" data-price="1980" data-was="4770">
```
Huwag kalimutang i-update din ang nakikitang teksto sa loob ng card.

### 2. Testimonials — **mahalaga ito**
Placeholder lang ang anim na review sa file. Palitan mo ng **totoong feedback**
mula sa mga aktuwal na customer bago i-publish. Ang gawa-gawang review ay labag
sa DTI rules at sa patakaran ng Facebook/TikTok ads — pwedeng ma-ban ang ad
account mo. Ganoon din ang “4.9 / 5” na rating sa hero.

### 6. Saan pupunta ang order
**Option A — WebCake native form (inirerekomenda).**
Palitan ang buong `<form class="order-form"> ... </form>` ng Order Form element
ng WebCake. Huwag alisin ang `<section id="order">` — doon naka-turo lahat ng
buton sa page.

**Option B — sariling endpoint.**
```js
FORM_ENDPOINT: "https://script.google.com/macros/s/AKfy.../exec",
```
Pwedeng Google Apps Script, Zapier, o Make webhook. Nagpapadala ito ng JSON:
`package, quantity, amount, name, phone, address, city, province, note, payment, page, at`.

> ⚠️ Kapag **blangko** ang `FORM_ENDPOINT`, lalabas pa rin ang “salamat” screen
> pero **walang napupuntahan ang order**. Pang-test lang iyon.

---

## Facebook / TikTok Pixel
May naka-comment na tracking hooks sa dulo ng `<script>` (`fbq`, `ttq`, `gtag`).
I-uncomment mo lang kapag naka-install na ang pixel sa WebCake page settings.

## Iba pang setting
```js
COUNTDOWN_HOURS: 5,      // haba ng promo timer
DEFAULT_PLAN_INDEX: 1    // 0 = 1 bote, 1 = 3 bote, 2 = 5 bote
```

---

## Para sa mga developer

```
src/template.html   # source, may __IMG_*__ placeholders
assets/*.jpg        # product photos (cropped mula sa brand board)
build.py            # nag-i-inline ng assets bilang base64
melioura-landing.html  # output — ito ang i-pa-paste sa WebCake
```

```bash
python3 build.py
```

Kung i-a-upload mo ang mga litrato sa WebCake media library (mas mabilis
mag-load kaysa base64), palitan mo na lang ang apat na `--img-*` variables
sa `:root` ng CSS:

```css
--img-hero: url("https://cdn.webcake.co/.../hero.jpg");
```

## Responsiveness — paano ito gumagana

Ang page ay **container-based**, hindi viewport-based. May wrapper na
`<div class="mlr">` na may `container-type: inline-size`, at lahat ng sukat
(`cqi` units + `@container` queries + `auto-fit` grids) ay sumusunod sa lapad
ng **block** na kinalalagyan nito — hindi sa lapad ng browser window.

Ibig sabihin: tama ang itsura kahit ilagay mo sa makitid na column ng WebCake,
sa tablet, o sa cellphone. Kung viewport-based ito (gaya ng karaniwan), lalabas
na desktop layout ang page sa loob ng makitid na WebCake block.

Dalawang bagay na **huwag galawin**:
1. Ang `<div class="mlr">` wrapper — dito nakasalalay ang buong pag-adjust.
2. Ang sticky CTA bar na nasa **labas** ng `.mlr` — kapag inilipat mo sa loob,
   titigil itong dumikit sa ibaba ng screen (ang size container ay nagiging
   containing block ng `position:fixed`).

May JS din na nagbabalik ng `<meta name="viewport">` kung tinanggal ito ng
page builder — iyon ang pinakamadalas na dahilan ng "hindi responsive" na page.

Nasubukan mula **320px hanggang 1920px**, at sa loob ng mga container na
320/380/480/600/768/900/1100px — walang horizontal scroll at walang overflow.

## Compliance
Naka-lagay na sa page ang **“No Approved Therapeutic Claims”** at ang paalala
na kumonsulta sa doktor. Structure/function ang pananalita ng mga benepisyo
(“sumusuporta”, “tumutulong”) — hindi panggamot sa sakit. Huwag itong palitan
ng disease claims; iyon ang pinakamadalas na dahilan ng FDA advisory at ng
pagka-reject ng ads sa Pilipinas.
