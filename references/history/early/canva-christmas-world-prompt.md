# Prompt — "Christmas Around the World" Canva deck (4-subagent build)

> Copy everything below into a new task. It is written for one **main agent** plus **4 subagents**, running on the user's own Chrome (Claude in Chrome), where Canva is already logged in with a **Premium** account.

---

## 0. Goal

Build a brand-new 12-slide Canva presentation (1920 × 1080) called **"Christmas Around the World – Deck"**.

- **Language:** all deck content is in **English**. Report back to the user in **Indonesian**.
- **Reference (mood only):** https://www.canva.com/templates/EAG2U8db99Y/ ("Red and Green Playful Merry Christmas Presentation" by ENIGMA STUDIO).
  - Use it for direction only. Do not make it identical: build everything from a blank design.

### Variables (change before running if needed)

| Variable | Default |
|---|---|
| Topic | Christmas traditions around the world |
| Slides | 12 (3 per subagent) |
| Handle / site | `@yourhandle` · `www.yourwebsite.com` |
| Canva account | Premium, so Pro elements are allowed |

---

## 1. Hard rules (all agents)

1. **No templates.**
   - Never click "Use this template" / "Gunakan template ini" on the reference.
   - Never duplicate or copy any page or element from it.
2. **Assets come from Canva Elements only** (Elemen → Grafis / Stiker / Bentuk / Bingkai).
   - Pro elements are allowed.
   - Photos only if no graphic fits.
3. **No Canva AI.** Do not use any of these:
   - Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand
   - "Tanya Canva", "AI Canva", or "Buat Animasi"
4. **Never act outward without the user's OK.**
   - Never share, publish, download, or change sharing or access settings.
   - Never log in for the user or change account settings.
5. **No brand logos.**
   - For example, the KFC fact on slide 8 is text only, with no logo art.
   - No trademarked characters.
6. **Stay in your lane.**
   - Each subagent edits only its own pages.
   - Never add, delete, or reorder pages.
   - Never click "Ubah semua" (Change all) in the color panel. It recolors every page.
7. **Facts must stay as written in §6.** If you shorten copy, don't change its meaning.

---

## 2. What to borrow vs. what must differ

| Borrow (the mood) | Must differ (our own identity) |
|---|---|
| Warm, playful, kid-friendly Christmas feel | **No** peeking-Santa cover, no snowman trio, no Santa-holding-gift poses |
| Cute watercolor illustration style | **No** hanging-bauble border along the top edge |
| Light background, red titles, green accents | **No** gift-box clusters in the bottom corners |
| Generous white space, one hero illustration per slide | **No** chunky slab-serif titles. We use a rounded sans. |
| A 2×2 card idea for a facts slide | Our facts slide uses **4 tilted postcards in a row**, not a 2×2 green grid |
| | Our story is a **world tour**: passport-stamp tags, a dashed travel path, a globe hero |

---

## 3. Design system

**Canvas:** 1920 × 1080.

**Margins:**
- Left and right: 120.
- Top and bottom: 96.
- Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Snow | `#FFFBF5` | Main background |
| Cream | `#FBEFD9` | Panels and cards |
| Holly Red | `#D7263D` | Titles and accents |
| Evergreen | `#1F5C46` | Dark backgrounds and cards |
| Butter Gold | `#F6C453` | Stars, pills, highlights |
| Candy Pink | `#F7B7B2` | Soft blobs and circles behind heroes |
| Ink | `#2B2B2B` | Body text |

### Fonts

Primary fonts:
- **Fredoka** for headings.
- **Nunito** for body text and labels.

If a font isn't available:
- **Baloo 2** for headings.
- **Quicksand** for body text.

Do not add any other font.

### Type scale

| Style | Spec |
|---|---|
| Display (cover, closing) | Fredoka Bold 140–160 |
| Slide title | Fredoka Bold 76–88, line spacing 1.0 |
| Card title | Fredoka SemiBold 36–40 |
| Stop tag / eyebrow | Nunito ExtraBold 22, UPPERCASE, letter spacing 200 |
| Body | Nunito Regular 26–28. Never below 22. Line spacing 1.4. |
| Bullets | Body style, prefixed with a gold "✦" or a small gold star element |

### Recurring motifs

Use these on every content slide so the 4 agents' work matches:
1. **Stop tag.** A rounded rectangle (radius 999, i.e. pill shape), Butter Gold fill, Ink text: `STOP 01 · GERMANY`.
2. **Dashed travel path.** A curved or straight dashed line in Holly Red, 4 px, near the title or between items.
3. **Sparkles.** 2–4 small gold star sparkles per slide, 24–60 px.
4. **Did-you-know card.** Cream card, radius 32, a 4 px Holly Red left accent bar, the title "Did you know?" in Fredoka 32 Holly Red, and one sentence in body style.

### Illustration style

Use **cute watercolor Christmas** illustrations: soft edges, warm palette, no harsh outlines.

The main agent picks **1–2 anchor creators** in Phase 0. Subagents prefer those creators so the style stays consistent: click the creator name on any element to browse their collection.

---

## 4. Orchestration

### Phase 0: main agent only (setup, about 10 min)

1. `tabs_context_mcp` → open https://www.canva.com.
   - The user is already logged in. Don't log in.
2. Create the design: Buat desain → Presentasi (16:9), 1920 × 1080.
   - Rename it to **Christmas Around the World – Deck**.
3. Press Ctrl+Enter to reach **12 pages**, then set each page background:

   | Slide | Background |
   |---|---|
   | 1 | Snow |
   | 2 | Evergreen |
   | 3 | Snow |
   | 4 | Snow |
   | 5 | Snow |
   | 6 | Evergreen |
   | 7 | Cream |
   | 8 | Snow |
   | 9 | Butter Gold |
   | 10 | Cream |
   | 11 | Snow |
   | 12 | Holly Red |

4. Search Elemen for "watercolor christmas globe" and "cute watercolor christmas" (Grafis tab).
   - Choose 1–2 anchor creators with big, consistent collections.
   - Write their names into the subagent briefs.
5. Copy the design's edit URL into every brief.
6. **Pilot wave:** launch Subagents A and B first.
   - If both report a working screenshot after their first slide, launch C and D.
   - If a subagent's screenshots time out, its background tab is being throttled. Run the rest in waves of 2 instead of 4.

### Phase 1: 4 subagents in parallel

Each subagent receives §1, §2, §3, its own slides from §6, and this common brief:

> **Common brief.**
>
> You are one of 4 builders on a shared Canva design.
>
> **Setup:**
> - Open your own Chrome tab with `<EDIT URL>`.
> - Go to your pages using the page strip at the bottom. Edit **only** slides `<X–Y>`.
>
> **Canva UI is in Indonesian:**
> - Elemen = Elements; Teks = Text.
> - Posisi = Position panel (Lebar / Tinggi / X / Y fields); Lapisan = Layers.
> - Rasio lock = aspect lock.
> - Avoid Tanya Canva, AI Canva, Bagikan, Unduh, and "Ubah semua".
>
> **Working method:**
> - Shortcuts: T text, R rectangle, C circle, L line, Ctrl+D duplicate, Ctrl+G group, Ctrl+Shift+L/C/R align.
> - Edit text: double-click → Ctrl+A → type → Esc.
> - Lock the aspect ratio before resizing any graphic.
> - Place everything with exact numbers in the Position panel.
> - Batch many clicks per browser call.
> - Before searching assets, apply nothing that filters out Pro. Pro is fine.
>
> **Check each slide:** after finishing it, take a zoom screenshot of the page and fix any overlap, clipping, or off-margin item.
>
> **When done, report:**
> - per slide: done / issues
> - each asset: search keyword + creator name
> - anything you could not match from the spec

**Assignment:**

| Subagent | Slides |
|---|---|
| A | 1–3 (Cover, Quote, Route) |
| B | 4–6 (Germany, Mexico, Philippines) |
| C | 7–9 (Sweden, Japan, Australia) |
| D | 10–12 (Fun facts, Try at home, Closing) |

### Phase 2: main agent (QA + report)

Run the QA checklist in §7, fix what's off, then send the report in §8.

---

## 5. Layout reference

Coordinates are in px on the 1920 × 1080 page. "Hero" means the main illustration. Every slide uses a **different layout**, and none repeats a reference layout.

---

## 6. Slide-by-slide spec

### Subagent A

#### Slide 1: Cover (bg Snow)

**Text, left column (X 120, width 860):**
- Gold pill tag at Y 170: `A FESTIVE WORLD TOUR`
- Title, Fredoka Bold 150, Holly Red, 3 lines starting at Y 230:
  > Christmas
  > Around the
  > World
- Subtitle, Nunito 30, Ink, width 700, at Y 760:
  > How six countries celebrate the most wonderful time of the year.
- Evergreen pill with Snow text at Y 880: `@yourhandle`

**Visuals:**
- Hero: a large watercolor Christmas globe or snow globe, about 760 wide, at X 1060, Y 170, with a Candy Pink circle (820) behind it.
- A dashed travel path curving from the end of the title toward the globe, with a tiny plane or sleigh on it.
- Gold sparkles.

**Asset keywords:** "watercolor christmas globe", "snow globe watercolor", "watercolor airplane cute", "gold star sparkle".

#### Slide 2: Quote (bg Evergreen)

- Centered quote, Fredoka Medium 64, Snow, width 1400, Y about 330:
  > "I will honour Christmas in my heart, and try to keep it all the year."
- Attribution, Nunito ExtraBold 22, Butter Gold, letter spacing 200, at Y 700:
  > — CHARLES DICKENS, A CHRISTMAS CAROL (1843)
- Decor:
  - Watercolor holly sprigs at the top-left and bottom-right corners, about 360 wide, partly off-canvas.
  - 3–4 gold sparkles.
  - A faint large wreath ring behind the quote, at 25 % transparency.

**Asset keywords:** "watercolor holly sprig", "watercolor christmas wreath", "gold sparkle".

#### Slide 3: Our Festive Route (bg Snow)

**Header:**
- Title, top-left at X 120, Y 110: **Our Festive Route**
- Subtitle, Nunito 26, at Y 210:
  > Six stops, six ways to celebrate.
- Top-right: a short dashed path with a small plane, plus a small globe.

**Grid:** 6 passport-stamp cards, 3 × 2.
- Card size: 520 × 260.
- X positions: 120, 700, 1280. Y positions: 360, 680.
- Style: Cream fill, radius 28, Holly Red **dashed** 3 px border.
- Each card holds a stop tag pill, a country name (Fredoka 40, Holly Red), one line of body text (Nunito 24), and a small watercolor icon (about 110) at the top-right corner.

| Stop | Country | One line |
|---|---|---|
| 01 | Germany | Christmas markets & Advent calendars |
| 02 | Mexico | Las Posadas, nine nights of celebration |
| 03 | Philippines | Parol lanterns & dawn Masses |
| 04 | Sweden | St. Lucia Day, a festival of light |
| 05 | Japan | Christmas cake & a famous fried-chicken dinner |
| 06 | Australia | A sunny Christmas at the beach |

### Subagent B

#### Slide 4: Germany (bg Snow) — Layout A: hero in an arch

- **Left:** a Cream arch shape, 640 × 820, at X 120, Y 160. The hero sits inside it: a watercolor Christmas market stall or Advent calendar, about 560 wide.
- **Right column, X 860, width 940:**
  - Stop tag at Y 170: `STOP 01 · GERMANY`
  - Title at Y 220, 2 lines: **Christmas Markets & Advent Calendars**
  - Bullets at Y 460:
    - ✦ Christmas markets (Weihnachtsmärkte) fill town squares with wooden stalls, lights, and warm drinks.
    - ✦ Dresden's Striezelmarkt is one of the oldest, first held in 1434.
    - ✦ Advent calendars began in 19th-century Germany as a way to count down to Christmas.
  - Did-you-know card, 940 × 150, at Y 800:
    > Many families open one little door every day from December 1 to 24.

**Asset keywords:** "watercolor christmas market", "watercolor advent calendar", "watercolor gingerbread heart".

#### Slide 5: Mexico (bg Snow) — Layout B: hero in a big circle on the right

- **Left column, X 120, width 860:**
  - Stop tag: `STOP 02 · MEXICO`
  - Title: **Las Posadas**
  - Bullets:
    - ✦ Nine nights of celebration, from December 16 to 24.
    - ✦ Each night, neighbors reenact Mary and Joseph's search for a place to stay.
    - ✦ Evenings end with songs, tamales, warm ponche, and a star-shaped piñata.
  - Did-you-know card:
    > "Posada" means "inn" or "lodging" in Spanish.
- **Right:** a Candy Pink circle (720) at X 1080, Y 180. The hero overlaps it: a star piñata, about 600, plus small papel-picado bunting.

**Asset keywords:** "watercolor star pinata", "papel picado", "watercolor tamales".

#### Slide 6: Philippines (bg Evergreen) — Layout C: dark slide with a glowing hero

Text uses Snow; the title and stop tag use Butter Gold.

- **Left column, X 120, width 820:**
  - Stop tag: `STOP 03 · PHILIPPINES`
  - Title: **Parol Lanterns & Simbang Gabi**
  - Bullets:
    - ✦ The season starts as early as September, one of the longest in the world.
    - ✦ Star-shaped parol lanterns glow in windows to recall the Star of Bethlehem.
    - ✦ Simbang Gabi is a series of nine dawn Masses from December 16 to 24.
  - Did-you-know card: Cream card with Ink text:
    > San Fernando, Pampanga, is famous for its Giant Lantern Festival.
- **Right:** a large parol / star lantern illustration, about 680, at X 1080, Y 160, with a soft gold glow behind it (a Butter Gold circle at 30 % transparency) and sparkles.

**Asset keywords:** "parol lantern", "star lantern watercolor", "christmas star lantern".

### Subagent C

#### Slide 7: Sweden (bg Cream) — Layout D: centered title, two columns

- **Top:**
  - Stop tag, centered, at Y 120: `STOP 04 · SWEDEN`
  - Title, centered, at Y 170: **St. Lucia Day — December 13**
- **Left column:** a Snow circle (560) at X 160, Y 360, with a St. Lucia girl (white gown, candle crown) inside it.
- **Right column, X 820, width 980:**
  - Bullets at Y 380:
    - ✦ A girl in a white gown and a crown of candles leads a procession of singers.
    - ✦ Families share saffron buns called lussekatter with coffee or glögg.
    - ✦ The festival brings light to one of the darkest times of the year.
  - A small saffron-bun illustration, about 160, beside the bullets.
  - Did-you-know card at Y 800:
    > Under the old Julian calendar, December 13 fell close to the winter solstice.

**Asset keywords:** "saint lucia illustration", "lussekatter", "saffron bun watercolor", "candle crown".

#### Slide 8: Japan (bg Snow) — Layout E: split screen

- **Left half (0–960):** a Holly Red panel holding:
  - Stop tag: `STOP 05 · JAPAN` (Butter Gold pill)
  - Title, Snow: **Christmas Cake & Fried Chicken**
  - Bullets, Snow:
    - ✦ Christmas Eve is often a romantic evening for couples rather than a family holiday.
    - ✦ A strawberry sponge "Christmas cake" is the classic dessert.
    - ✦ Since a 1974 ad campaign, many families pre-order a KFC Christmas dinner.
- **Right half:**
  - A strawberry shortcake hero, about 620, at X 1100, Y 170.
  - A small fried-chicken bucket, about 260, with **no logo**.
  - Did-you-know card, 760 wide, at X 1060, Y 820:
    > Christmas isn't a national holiday in Japan, so most people still work on December 25.

**Asset keywords:** "watercolor strawberry shortcake", "fried chicken bucket illustration", "japanese christmas illustration".

#### Slide 9: Australia (bg Butter Gold) — Layout F: full-bleed sunny scene

- **Text, top-left, width 900:** Ink text with a Holly Red title.
  - Stop tag: `STOP 06 · AUSTRALIA` (Snow pill)
  - Title: **A Sunny Christmas Down Under**
  - Bullets:
    - ✦ December is summer, so many families head to the beach or a backyard barbecue.
    - ✦ Seafood like prawns, and pavlova for dessert, often star on the menu.
    - ✦ Carols by Candlelight in Melbourne has gathered crowds since 1938.
- **Hero, bottom-right:** about 820 wide, partly bleeding off the edge. Use a beach Christmas scene, e.g. Santa surfing or a decorated palm tree.
- Did-you-know card, bottom-left:
  > In Australian folk songs, Santa's sleigh is pulled by six white kangaroos.

**Asset keywords:** "watercolor santa surfing", "beach christmas watercolor", "watercolor pavlova", "christmas palm tree".

### Subagent D

#### Slide 10: More Merry Facts (bg Cream)

- Title, top-left: **More Merry Facts**
- Subtitle:
  > Four quick stops we couldn't skip.
- **4 postcards** in one row. Each card:
  - 380 × 560 at Y 300, X positions 120, 560, 1000, 1440.
  - Rotations: −3°, 2°, −2°, 3°.
  - Snow fill, radius 24, with a soft shadow (Efek → Bayangan, subtle).
  - Contents: a small watercolor icon (about 150) at the top, a country name (Fredoka 36, Holly Red), and the fact (Nunito 22–24).

| Country | Fact |
|---|---|
| Iceland | Jólabókaflóð, the "Christmas book flood": books are given on Christmas Eve and read that night. |
| Italy | La Befana, a kind old woman on a broomstick, brings gifts on January 6. |
| Ukraine | Spider-web ornaments recall a folk tale of a spider that decorated a poor family's tree. |
| Ethiopia | Ganna is celebrated on January 7, following the Ethiopian Orthodox calendar. |

**Asset keywords:** "watercolor book stack christmas", "cute witch broom", "spider web ornament" (fallback: "watercolor silver ornament"), "watercolor candles".

#### Slide 11: Bring a Tradition Home (bg Snow)

- Title, centered: **Bring a Tradition Home**
- **3 steps** horizontally, centers at X 400, 960, 1520, Y 420 to 900.
- Each step has:
  - a Butter Gold circle (140) with a number 1 / 2 / 3 in Fredoka 64
  - an illustration of about 220 above or beside it
  - a card title in Fredoka 38, Holly Red
  - body text in Nunito 24, width 460, centered
- A dashed travel path connects the 3 circles.

| # | Card title | Body |
|---|---|---|
| 1 | Bake Lussekatter | Twist saffron dough into S-shapes and top with raisins. (Sweden) |
| 2 | Craft a Paper Parol | Fold colored paper into a star lantern for your window. (Philippines) |
| 3 | Host a Book-Swap Night | Wrap a favorite book, swap, and read together with cocoa. (Iceland) |

**Asset keywords:** "saffron bun", "paper star lantern", "watercolor books cocoa".

#### Slide 12: Closing (bg Holly Red)

- **Centered text:**
  - Fredoka Bold 150, Snow, at Y 300: **Merry Christmas**
  - Fredoka SemiBold 72, Butter Gold, at Y 480: **& Happy Holidays!**
  - Nunito 30, Snow, at Y 620:
    > Thanks for traveling with us.
  - Snow pill, Holly Red text, Nunito 24, at Y 720: `www.yourwebsite.com  •  @yourhandle`
- **Decor:**
  - A watercolor string of lights across the top edge.
  - A small sleigh or plane flying over a mini globe, bottom-right.
  - Gold sparkles.

**Asset keywords:** "watercolor christmas lights garland", "watercolor sleigh", "watercolor globe small".

---

## 7. QA checklist (main agent, Phase 2)

- [ ] 12 pages, in order, and titles match §6.
- [ ] Only Fredoka and Nunito (or the stated fallbacks). Sizes follow §3. Body text is ≥ 22 px everywhere.
- [ ] Colors only from §3. Stop tags, sparkles, and did-you-know cards look identical across all slides.
- [ ] No overlap, clipping, or text touching illustrations. Everything sits inside the margins except intentional bleeds.
- [ ] Illustration style is consistent, with anchor creators used where possible.
- [ ] None of the "must differ" items from §2 appear.
- [ ] No Canva AI used. No brand logos.
- [ ] Facts unchanged from §6. US-English spelling, except inside the Dickens quote, which keeps "honour".
- [ ] Nothing shared, downloaded, or published. Sharing settings untouched.
- [ ] Optional, only if time allows: subtle Fade/Rise animation on titles and a Dissolve transition. No AI animation.

## 8. Final report to the user (in Indonesian)

1. The edit link.
2. One line per slide.
3. Assets per slide: keyword + creator, marking which are Pro.
4. What was deliberately done differently from the reference (§2).
5. Any spec item not achieved, plus total build time and the waves used (4 at once, or 2 + 2).
