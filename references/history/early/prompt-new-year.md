# Prompt — "New Year's Eve 2027" Canva deck (fast pipeline, ~30–40 min)

> Copy everything below into a new task. One **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"New Year's Eve 2027 – Party Deck"**. It introduces a New Year's Eve party: welcome, the plan for the night, food, dress code, activities, traditions around the world, resolutions, the countdown, and a closing slide.

- **Language:** all deck content in **English**. Report to the user in **Indonesian**.
- **Year:** the party is on **December 31, 2026**, welcoming **2027**.
- **Reference (mood only):** https://www.canva.com/templates/EAG2zwZ4H5w/ ("Gold and Black Modern New Year's Party Celebration Presentation").
  - Borrow the *mood*: dark, glamorous, gold-on-dark, celebratory, party photography.
  - **Build from scratch.** Never click "Use this template", never copy its pages or elements.

### Skills to load first (main agent)

- `anthropic-skills:pptx` → to generate the .pptx skeleton.
- `elite-powerpoint-designer` → design rules (summarised in §3; closest to its "Financial Elite" style: dark + gold, serif, centered, subtle motion).
- `presentation-design` → for the QA pass in §8.

---

## 1. Hard rules (all agents)

1. Assets come from **Canva Elements only** (Elemen → Grafis / Stiker / Bentuk / Bingkai / Foto). Pro is allowed. Party photos may come from Elemen → Foto.
2. **No Canva AI:** no Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva", "Buat Animasi". Skip any asset whose creator is "Canva AI Elements Lab".
3. No sharing, publishing, downloading, or changes to sharing/access/account settings.
4. **Stay in your lane.** Builders edit only their own pages. Nobody but the main agent adds, deletes, or reorders pages. Never click "Ubah semua".
5. **No copy/paste between pages.** All agents share one clipboard. Insert assets fresh from the Elements panel.
6. Facts on slide 8 stay exactly as written in §6.
7. No alcohol brand logos or any brand marks on bottles or products.

---

## 2. Borrow vs. must differ

| Borrow (the mood) | Must differ (our identity) |
|---|---|
| Dark background, gold as the hero color | Background is **deep navy**, not pure black |
| Gold fireworks for celebration | Fireworks are **small accents only** (max 1–2 per slide), never a full-slide burst behind a centered title |
| Party photography | Photos sit in **arched / round gold-framed windows**, not tilted cream-bordered photo strips |
| Big year numerals on the cover | **No** inflated-balloon "2026" numerals and **no** script "New Year" over them. Our cover uses a large **art-deco serif "2027"** with a thin gold sunburst |
| Serif titles in gold | Accent color **blush pink** joins gold; recurring **art-deco** lines, arches and a clock motif |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins 120 left/right, 96 top/bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Midnight Navy | `#0E1A33` | Main background |
| Ink Navy | `#16264A` | Panels and cards |
| Champagne | `#E8C77A` | Titles, frames, lines, numerals |
| Deep Gold | `#B8913E` | Gradient partner / shadows of gold |
| Blush | `#F2B8B5` | Small labels, highlights |
| Ivory | `#FBF6EC` | Body text, light slides |

### Fonts (max 2 families)

- **Titles / numerals:** DM Serif Display (fallback: Playfair Display).
- **Body / labels:** Montserrat (fallback: Poppins).

| Style | Spec |
|---|---|
| Cover numerals | DM Serif Display 300–340, Champagne |
| Slide title | DM Serif Display 72–88, Champagne |
| Label / eyebrow | Montserrat SemiBold 22, UPPERCASE, letter spacing 300, Blush |
| Body | Montserrat Regular 28, Ivory, line spacing 1.5. Never below 24 |
| Big number (timeline, countdown) | DM Serif Display 64–96, Champagne |

### Design rules (from elite-powerpoint-designer)

- One idea per slide. Max 6 lines of body text. Max 4 font sizes per slide.
- Contrast ≥ 4.5:1 (Ivory/Champagne on navy; navy text only on Ivory).
- Subtle motion only: titles Fade in; transitions Fade for the whole deck. Max 3 animated elements per slide.

### Recurring motifs (identical on every slide)

1. **Eyebrow label** in Blush above each title.
2. **Art-deco divider:** thin Champagne line (2 px) 240 wide with a small diamond in the middle, under each title.
3. **Gold-framed window:** a photo or illustration inside an arch or circle frame (Elemen → Bingkai), with a 6 px Champagne outline.
4. **Corner deco:** thin Champagne art-deco corner lines in 2 opposite corners (one Canva element, mirrored), 20 % transparent.
5. **Spark accents:** 2–4 small gold stars/sparkles; at most 1 small firework burst per slide.

### Imagery style

Warm, slightly moody party photography (sparklers, champagne glasses without labels, confetti, people celebrating) **or** elegant gold line/foil illustrations. The asset scout picks 1–2 anchor creators and keeps photos color-consistent (warm gold light on dark).

---

## 4. Pipeline (why this is fast)

All text, colors, shapes and lines are generated in code; agents only place photos and illustrations.

### Phase 0A — main agent: skeleton .pptx (≈5 min)

1. Use python-pptx. Slide size **20 in × 11.25 in** (18288000 × 10287000 EMU) → Canva imports as 1920 × 1080. px → EMU = `px * 9525`.
2. For every slide in §6, create: background, all text (exact copy, font names, sizes, colors, letter spacing), panels, dividers with diamond, timeline lines and dots, number circles.
3. For each photo/illustration, place a **placeholder rectangle** at its exact position (20 % transparent Ivory, label like `PHOTO: sparklers, arch frame 640×820`). Builders delete it after placing the real asset.
4. Save as `new-year-skeleton.pptx`. Render one slide to PNG (LibreOffice, if available) to sanity-check.

### Phase 0B — asset scout subagent, in parallel (≈10 min)

Search Canva Elements for every photo, frame, illustration and deco element in §6. Write `new-year-assets.md`:

| Slide | Item | Exact search keyword | Creator | Result position (row, column) | Pro/free |

Also choose **one** arch frame, **one** circle frame and **one** art-deco corner element to be reused on every slide. Insert nothing into the design.

### Phase 0C — main agent: import (≈3 min)

1. In Canva: Buat desain → Impor file (or Unggahan) → upload `new-year-skeleton.pptx` with the `file_upload` tool. If that isn't possible, ask the user to drag the file into Canva once.
2. Rename the design **New Year's Eve 2027 – Party Deck**. Check 2–3 slides: fonts mapped (re-set any substituted font on the affected text boxes), letter spacing and the divider diamonds survived.
3. **Fallback if the import is badly broken:** build slide 4 by hand as a fully styled "kit page", duplicate it for every slide, then let builders swap the text. Report which path was used.
4. Put the edit URL into each builder brief.

### Phase 1 — 4 builder subagents in parallel (≈15 min)

Each builder gets §1, §2, §3, its slides in §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`. For each slide:
> 1. Insert the frame / photo / illustration listed in the asset sheet (exact keyword, listed result).
> 2. For framed photos: drop the frame first, then drag the photo into the frame.
> 3. Lock aspect ratio and match the placeholder's size and position via Posisi (Lebar/Tinggi/X/Y). Delete the placeholder.
> 4. Add the corner deco and sparkles as described. Fix only real problems (overlap, clipping, unreadable text).
> 5. Zoom-screenshot the slide to check.
>
> UI is in Indonesian. Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua". Never copy/paste. If your tab's screenshots time out twice, stop and report "BLOCKED".
> Report: per slide done/issues, assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent QA + report (≈5 min). See §8.

---

## 5. Coordinates

All positions are px on the 1920 × 1080 page (x, y = top-left corner).

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (bg Midnight Navy)**
- Thin Champagne sunburst (radiating lines, 20 % transparent) centered behind the numerals, ~1100 wide.
- Eyebrow centered at y 180: `NEW YEAR'S EVE CELEBRATION`.
- Numerals `2027`, DM Serif Display 320, Champagne, centered at y 260.
- Divider centered at y 640.
- Subtitle centered at y 680, Montserrat 32, Ivory: `Goodbye 2026 — hello to new beginnings.`
- Info line centered at y 760, Montserrat SemiBold 24, Blush, letter spacing 200: `DECEMBER 31, 2026  •  8:00 PM  •  YOUR VENUE NAME`.
- Corner deco top-left and bottom-right; one small firework burst top-right (~260); 3 sparkles.

**Slide 2 — Welcome (bg Midnight Navy)**
- Left: arch-framed photo 640 × 820 at (120, 130): friends celebrating with sparklers.
- Right column at x 860, width 940:
  - Eyebrow at y 240: `WELCOME, FRIENDS`.
  - Title at y 290, 2 lines: `One Night to Celebrate Everything`.
  - Divider at y 500.
  - Body at y 540: `Tonight we say thank you to the year behind us and raise a glass to the one ahead. Expect good food, great music, and a midnight to remember.`
- Corner deco bottom-right; 2 sparkles.

**Slide 3 — The Plan for Tonight (bg Midnight Navy)**
- Eyebrow `THE PLAN` and title `How the Night Unfolds`, centered at y 110 / 160.
- Horizontal timeline: Champagne line 2 px from x 220 to x 1700 at y 560, with 5 Champagne dots (28) at x 220 / 590 / 960 / 1330 / 1700.
- Above each dot: time (DM Serif Display 64, Champagne) at y 420. Below: label (Montserrat SemiBold 26, Ivory) at y 600, width 300, centered:
  - `8:00 PM` — `Welcome drinks`
  - `9:00 PM` — `Dinner buffet`
  - `10:30 PM` — `Games & photo booth`
  - `11:50 PM` — `Countdown gathering`
  - `12:00 AM` — `Fireworks & cheers`
- Small gold clock illustration (~160) top-right; corner deco bottom-left.

### Builder B

**Slide 4 — Food & Drinks (bg Midnight Navy)**
- Left column at x 120, width 820:
  - Eyebrow `ON THE MENU`, title `Food & Drinks`, divider.
  - Bullets (Champagne ◆ + Ivory body):
    - `◆ Grazing table with cheese, fruit and finger food`
    - `◆ Main buffet with something for every taste`
    - `◆ Midnight dessert bar`
    - `◆ Sparkling drinks and mocktails for everyone`
- Right: two circle-framed photos, 520 at (1180, 140) (party food / grazing table) and 400 at (1040, 600) (sparkling glasses, no labels).
- 2 sparkles.

**Slide 5 — Dress Code (bg Ink Navy)**
- Centered eyebrow `DRESS CODE` at y 200 and title `Black, Gold & Glitter` at y 250 (DM Serif Display 96).
- Divider centered at y 400.
- Body centered at y 440, width 1100: `Dress to shine — think sequins, velvet, metallic accents, or your sharpest black outfit.`
- Bottom row: three small round-framed illustrations or photos (260 each) at y 640, centers x 660 / 960 / 1260: sequin dress / bow tie / sparkly shoes, with labels below (Montserrat SemiBold 22, Blush): `SEQUINS`, `SHARP SUITS`, `METALLIC TOUCHES`.

**Slide 6 — Games & Activities (bg Midnight Navy)**
- Eyebrow `KEEP THE PARTY GOING`, title `Games & Activities`, left-aligned at x 120.
- Four Ink Navy cards 400 × 440 (radius 24, 2 px Champagne outline) at y 420, x 120 / 560 / 1000 / 1440. Each: gold line icon (~120), card title (DM Serif Display 36, Champagne), one line of body (Montserrat 24, Ivory):
  1. `Photo Booth` — `Props, glitter and instant memories.`
  2. `Resolution Jar` — `Write a wish, read them next year.`
  3. `Dance Floor` — `A playlist of the year's best hits.`
  4. `Countdown Quiz` — `Guess the biggest moments of 2026.`
- Corner deco top-right.

### Builder C

**Slide 7 — Section break (bg Ivory)**
- Big centered numeral `12:00`, DM Serif Display 260, Midnight Navy, at y 280.
- Eyebrow above in Deep Gold at y 220: `AROUND THE WORLD`.
- Subtitle centered at y 620, Montserrat 32, Midnight Navy: `How different countries welcome the new year`.
- Gold globe or world-map line illustration (~300) at the bottom-right; Champagne corner deco top-left.

**Slide 8 — Traditions Around the World (bg Midnight Navy)**
- Eyebrow `TRADITIONS`, title `New Year Around the World`, centered at y 110 / 160.
- Five round-framed items in a row (circle frames 240, Champagne outline) at y 340, centers x 280 / 620 / 960 / 1300 / 1640, each with a small photo or illustration inside. Below each: country (DM Serif Display 36, Champagne) and fact (Montserrat 22, Ivory, width 300, centered):
  1. `Spain` — `Eat 12 grapes at midnight, one for each chime of the clock.`
  2. `Japan` — `Temple bells ring 108 times on New Year's Eve.`
  3. `Brazil` — `Many people wear white for peace and good luck.`
  4. `Scotland` — `Hogmanay brings "first-footing", the first guest of the new year.`
  5. `Denmark` — `Friends smash old plates on doorsteps for good luck.`

**Slide 9 — Resolutions (bg Midnight Navy)**
- Right: arch-framed photo 640 × 820 at (1160, 130) (hands writing in a notebook / sparkler). The photo sits on the right this time, mirroring slide 2.
- Left column at x 120, width 920:
  - Eyebrow `FRESH START`, title `Our 2027 Resolutions`, divider.
  - Numbered list (DM Serif Display 48 Champagne numbers, Montserrat 28 Ivory text) at y 480, 4 rows 96 apart:
    - `01  Spend more time with the people we love`
    - `02  Learn one new skill`
    - `03  Move more, worry less`
    - `04  Say yes to new adventures`

### Builder D

**Slide 10 — The Countdown (bg Midnight Navy)**
- Eyebrow centered `THE FINAL SECONDS` at y 180.
- Five number circles (Ink Navy fill, 4 px Champagne outline, 200) in a row centered at y 360, centers x 560 / 760 / 960 / 1160 / 1360: `5`, `4`, `3`, `2`, `1` (DM Serif Display 96, Champagne).
- Big line centered at y 640, DM Serif Display 96, Champagne: `Happy New Year!`
- One firework burst (~360) top-right and one bottom-left (both small, 30 % transparent); confetti accents.

**Slide 11 — Thank You & Cheers (bg Midnight Navy)**
- Left: circle-framed photo 620 at (160, 230): champagne glasses clinking (no labels).
- Right column at x 900, width 900:
  - Eyebrow `FROM ALL OF US`, title `Thank You for Making 2026 Shine`, divider.
  - Body: `Here's to more laughter, more adventures, and more nights like this one.`
- 2 sparkles; corner deco bottom-right.

**Slide 12 — Closing (bg Midnight Navy)**
- Thin Champagne sunburst behind, as on the cover (same element, same size) — ties the deck together.
- Centered: eyebrow `SEE YOU NEXT YEAR` (y 220), `Cheers to 2027` DM Serif Display 140 Champagne (y 290), divider (y 520), contact line Montserrat 26 Ivory (y 580): `www.yourwebsite.com  •  @yourhandle`.
- Corner deco top-left and bottom-right; confetti along the top edge; 3 sparkles.

---

## 7. Speaker notes (main agent adds in the .pptx)

- Slide 3: `Times are placeholders — edit to match your event.`
- Slide 8: `Facts are general traditions; verify before presenting if needed.`

---

## 8. QA checklist (main agent, run with `presentation-design`)

- [ ] 12 pages in order; every placeholder rectangle deleted.
- [ ] Only DM Serif Display + Montserrat (or stated fallbacks); body ≥ 24 px; contrast ≥ 4.5:1.
- [ ] Colors only from §3. Eyebrows, dividers, frames and corner deco identical across slides.
- [ ] Frames: one arch style and one circle style used throughout, all with the Champagne outline.
- [ ] Photos color-consistent (warm gold light), no visible brand labels.
- [ ] None of the §2 "must differ" items: no balloon numerals, no tilted photo strips, no full-slide firework bursts behind titles.
- [ ] No overlap, clipping or stray elements (check each page's Lapisan list once).
- [ ] Nothing shared, downloaded or published.

## 9. Final report to the user (Indonesian)

1. Edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately different from the reference (§2).
5. Path used (pptx import or kit-page fallback), time per phase, and anything not achieved.
