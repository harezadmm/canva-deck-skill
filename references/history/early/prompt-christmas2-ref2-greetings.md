# Prompt — "Season's Greetings 2026" year-end Christmas deck (Christmas 2 · Ref 2, fast pipeline)

> Copy everything below into a new task. One **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Season's Greetings 2026 – Year-End Celebration"**.

It is a warm, illustrated Christmas and year-end greeting deck for a team, class or community. It covers:
- an opening greeting
- the year's highlights
- thank-yous
- holiday plans: party details, Secret Santa, schedule
- wishes for 2027
- a closing message

### Requirements

- **Client brief — COLORFUL:**
  - The night-sky background is a stage for **bright, jewel-toned color**: multi-colored fairy lights, rainbow gift wraps, colorful scarves and hats on the characters, and colored panels.
  - Every slide shows **at least 4 palette colors**.
  - The deck must never look like "navy and gold only".
- **Language:** all deck content in **English**. Report to the user in **Indonesian**.
- **Year:** the celebration is in December 2026; wishes look ahead to **2027**.
- **Reference (mood only):** https://www.canva.com/templates/EAHU-rE15Mk/ ("Red and Gold Illustrated Merry Christmas Greeting Presentation").
  - Borrow the *mood*: cozy, glowing, magical night, cute 3D-style chibi characters, snow.
  - **Build from scratch.** Never click "Use this template", never copy its pages or elements.
- **Expected time:** about 35–45 minutes.

### Skills to load first (main agent)

- `anthropic-skills:pptx` for the skeleton.
- `elite-powerpoint-designer`: aim for a warm, premium greeting feel.
- `ppt-visual` for varied layouts.
- `presentation-design` for QA.

---

## 1. Hard rules (all agents)

1. **Built from scratch; all assets come from Canva Elements.** (Project rule.)
   - The code skeleton may contain only **text and plain layout shapes**: background, panels, pills, circles, lines.
   - All visuals come from Canva Elements: characters, houses, trees, snow, lights, frames, glows and sparkles. Pro elements are allowed.
2. **No Canva AI.**
   - Not allowed: Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva", "Buat Animasi".
   - Skip assets whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing, downloading, or changes to sharing, access or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** The clipboard is shared between agents.
6. **Copy is exact as written in §6.** Bracketed items like `[Highlight 1]` stay as visible placeholders for the client to fill in.
7. **No logos or trademarks.** No brand logos and no trademarked characters.

---

## 2. Borrow vs. must differ

| Borrow (the mood) | Must differ (our identity) |
|---|---|
| Cozy, glowing, magical Christmas night | Background is a **midnight-blue winter sky gradient**, not deep red |
| Cute 3D-style chibi characters | Cast is **penguins, a fox, a polar bear cub and a small owl**. **No** snowman pair, no panda, no bunnies, no mouse, no chibi kids in parkas |
| Glowing title text | Titles are in an **elegant serif** with a soft gold glow, not a casual script |
| Snowy scenery | **No** snow-ground strip with blue pines and houses on every slide. Scenery appears only in **framed windows / arch panels** and on 3 "scene" slides |
| Warm light | Recurring **glowing lantern / fairy-light garland** motif instead of a campfire. **No** campfire on the cover or closing slide |
| Centered title with two text columns | Content in **frosted-glass panels** (semi-transparent white cards) with icons |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins 120 left/right, 96 top/bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Midnight | `#0F1B3D` | Background gradient top |
| Night Blue | `#1F3A6B` | Background gradient bottom |
| Frost | `#FFFFFF` at 12–16 % opacity | Frosted-glass panels |
| Warm Gold | `#F4B942` | Titles, glows, lanterns |
| Cranberry | `#C8233A` | Accent ribbons, pills |
| Snow | `#F7F9FC` | Body text on dark |
| Ice Blue | `#9CC7F0` | Secondary text, snowflakes |
| Berry Pink | `#FF5C8A` | Lights, gift wraps, scarves, panel tint |
| Teal Glow | `#2EC4B6` | Lights, ornaments, panel tint |
| Lilac | `#B39DFF` | Lights, ornaments, panel tint |
| Tangerine | `#FF9F43` | Lights, lanterns, panel tint |
| Mint | `#7BE0A0` | Ornaments, wreath accents, panel tint |

**Color rules (colorful brief):**
- **Fairy lights:** the lantern garland must be **multi-colored**, with bulbs in gold, pink, teal, lilac and tangerine. If the chosen element is single-color, recolor its bulbs where Canva allows. Otherwise pick a multi-color one.
- **Panels:** frosted panels alternate between plain Frost and **colored glass**: a Berry Pink, Teal Glow, Lilac, Tangerine or Mint tint at 22 % opacity, with a border in the same color at 50 %. Max 2 neighbouring panels in the same color.
- **Characters:** pick versions with **colorful outfits**, such as a pink scarf on the penguins, a teal hat on the fox, a lilac earmuff on the bear, and a tangerine scarf on the owl.
- **Glows:** behind every hero, add a soft radial glow in one accent color (not always gold), at 30 % opacity.
- **Sparkles:** mix gold, pink and teal.

Every slide uses the Midnight → Night Blue vertical gradient, except slides 7 and 11, which use a Cranberry → `#8E1B2C` gradient for a warm "chapter" feel.

### Fonts (max 2 families)

- **Titles:** Fraunces SemiBold. Fallback: Playfair Display.
  - Add a gold glow using Canva Efek → Cahaya / Glow (subtle, Warm Gold).
- **Body:** Nunito. Fallback: Lato.

| Style | Spec |
|---|---|
| Cover title | Fraunces 140–160, Warm Gold, glow |
| Slide title | Fraunces 72–84, Warm Gold, glow |
| Eyebrow | Nunito ExtraBold 22, UPPERCASE, letter spacing 250, Ice Blue |
| Panel title | Fraunces 36, Snow |
| Body | Nunito 26–28, Snow, line spacing 1.45. Never below 22 |

### Design rules (from elite-powerpoint-designer)

- One idea per slide. Max 6 lines of body text per panel. Max 4 font sizes per slide.
- Contrast ≥ 4.5:1: Snow or Gold on dark navy; no text on busy snow areas.
- Motion: titles Fade, panels Rise. Max 3 animated elements per slide. Transition: Dissolve is **not** used; use Fade for the whole deck.

### Recurring motifs (identical on every slide)

1. **Lantern garland:** a warm glowing fairy-light / lantern string draped across the top edge (Canva element, same one on every slide).
2. **Frosted-glass panel:** a White rectangle at 14 % opacity, radius 32, with a 2 px White border at 30 % opacity. Icons inside are gold line icons from Canva Elements.
3. **Falling snow:** a light snowflake/dot overlay (Canva element) at 40–60 % opacity, never over text.
4. **Gold sparkle cluster:** 2–3 per slide.
5. **Character hero:** one cast character per slide, in the same 3D/cute style throughout.

### Cast and illustration style

Cute **3D-style / soft-render chibi animals** in winter outfits (scarves, hats):
- a penguin duo
- a fox
- a polar bear cub
- a small owl

The asset scout must find **one creator or set** that has at least 3 of these in the same style, and use it everywhere. If a matching animal can't be found in that set, swap in another animal from the **same set** rather than mixing styles.

### Richness checklist (every slide)

- 1 character hero (at least 420 px).
- Lantern garland.
- Snow overlay.
- At least 1 framed scene or frosted panel.
- Gold sparkles.
- Text always inside a panel or on a clean area.
- **At least 4 palette colors clearly visible.**
- **A multi-colored garland.**
- **At least 1 colored glass panel or colored glow.**

---

## 4. Pipeline

### Phase 0A — main agent: skeleton .pptx (~5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU).
   - Convert px to EMU with `px * 9525`.
2. For every slide, create:
   - the gradient background (2-stop linear)
   - all text (exact copy, fonts, sizes, colors)
   - the frosted panels (white + transparency), pills and circles
3. For every visual, place a labeled placeholder rectangle at its exact position.
   - Fill: 20 % transparent Ice Blue.
   - Label example: `HERO: penguin duo waving 520w`.
4. Add the speaker notes from §7.
5. Save as `christmas2-greetings-skeleton.pptx`.

### Phase 0B — asset scout, in parallel (~10 min)

1. Search Canva Elements for every item listed in §6, plus:
   - the lantern garland
   - the snow overlay
   - one arch frame and one round window frame
   - a gold line-icon set
2. Write `christmas2-greetings-assets.md` with these columns:

| Slide | Item | Exact keyword | Creator | Result (row, col) | Pro/free |

3. Confirm that **one cast set** covers the penguins, fox, polar bear and owl. List the alternatives you found within that set.
4. Insert nothing into the design.

### Phase 0C — main agent: import (~3 min)

1. Upload the skeleton with the `file_upload` tool (Buat desain → Impor file, or the Unggahan panel). If upload fails, ask the user to drag the file in once.
2. Rename the design.
3. Check that the gradients and panel transparency survived the import.
4. If they didn't: re-apply them on one page, then copy only that page's background style per page. The main agent does this, not the builders.
5. **Fallback** if the import is broken: build slide 4 by hand as a kit page and duplicate it. Report which path was used.
6. Put the edit URL into each builder brief.

### Phase 1 — 4 builders in parallel (~20 min)

Each builder gets §1–3, its own slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`. For each slide:
> 1. Place decor first: garland, snow overlay, frames.
> 2. Place the hero character and icons, using the exact keyword and result from the asset sheet.
> 3. Add the gold glow effect to titles if the import dropped it.
> 4. Lock the aspect ratio and match each placeholder via Posisi, then delete the placeholders.
> 5. Run the richness checklist. Fix only overlap and clipping.
> 6. Take a zoom screenshot to check.
>
> The UI is in Indonesian. Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua". Never copy or paste. If screenshots time out twice, stop and report "BLOCKED".
>
> Report: per slide, done or issues; assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent: QA and report (~5 min)

---

## 5. Coordinates

All positions are px on the 1920 × 1080 page; (x, y) is the top-left corner.

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (scene slide, Midnight gradient)**
- Lantern garland across the top.
- Eyebrow, centered at y 200:
  > SEASON'S GREETINGS FROM ALL OF US
- Title, centered at y 250, Fraunces 150, Warm Gold with glow, 2 lines:
  > Merry Christmas
  > & Happy 2027
- Subtitle, centered at y 600, Nunito 30, Snow:
  > Celebrating a year of teamwork, kindness and good memories.
- Pill, centered at y 690, Cranberry, Snow text:
  > Your Team / Class Name
- Hero scene along the bottom (about 1500 wide, centered, y 700–1080):
  - snowy hills with a cozy glowing cabin;
  - the penguin duo on the left and the fox on the right, both waving;
  - small lanterns.
- Decoration: snow overlay and 3 gold sparkle clusters.

**Slide 2 — A Warm Hello (Midnight gradient)**
- Left: an arch-framed winter window, 620 × 780, at (120, 180). Inside it: a snowy night village with warm windows.
- Right column at x 840, width 960:
  - Eyebrow `OPENING MESSAGE`.
  - Title:
    > A Warm Hello
  - Frosted panel, 960 × 420, at y 420, containing:
    > As the year comes to a close, we want to pause and say thank you. Every challenge we faced and every win we celebrated, we did it together.
- Hero: the polar bear cub holding a mug (about 360), sitting at the bottom-right corner of the panel.

**Slide 3 — 2026 at a Glance (Midnight gradient)**
- Eyebrow `OUR YEAR`. Title, centered:
  > 2026 at a Glance
- Four frosted panels in a row, each 400 × 460, at y 360, x 120 / 560 / 1000 / 1440. Each panel has:
  - a gold line icon (about 96) at the top: star, rocket, heart, trophy;
  - a big number placeholder in Fraunces 72, Warm Gold: `[00]`;
  - a label in Nunito 26, Snow.
- Each panel is **colored glass** in a different color, left to right: Berry Pink, Teal Glow, Lilac, Tangerine.

| Panel | Icon | Label |
|---|---|---|
| 1 | star | `[Projects completed]` |
| 2 | rocket | `[New members joined]` |
| 3 | heart | `[Events together]` |
| 4 | trophy | `[Milestones reached]` |

- Hero: the owl perched on the garland at the top-right (about 220).

### Builder B

**Slide 4 — Highlights of the Year (Midnight gradient)**
- Eyebrow `HIGHLIGHTS`. Title:
  > Moments We'll Remember
- Three round window frames (Canva elements), each 420, at y 330, centers x 400 / 960 / 1520, each with a gold rim. Inside each frame goes a cute winter scene from the cast set (skating, building a snow fort, decorating a tree). These are placeholders for the client's own photos.
- Captions under each frame, Nunito Bold 26, Snow:
  - `[Highlight 1]`
  - `[Highlight 2]`
  - `[Highlight 3]`
- A note at y 940, Nunito 22, Ice Blue:
  > Tip: replace these windows with your own photos.

**Slide 5 — Thank You, Team (Midnight gradient)**
- Left column at x 120, width 900:
  - Eyebrow `WITH GRATITUDE`. Title:
    > Thank You, Team
  - Frosted panel with 4 rows, each with a gold ✦:
    - ✦ For showing up, even on the hard days
    - ✦ For sharing ideas and helping each other
    - ✦ For the laughter in between the work
    - ✦ For making this year truly special
- Right: the penguin duo hugging, with a heart sparkle (about 620), at (1160, 260), on a soft gold radial glow (a Canva glow element).

**Slide 6 — Holiday Party Details (Midnight gradient)**
- Eyebrow `YOU'RE INVITED`. Title, centered:
  > Holiday Party
- Large frosted invitation card, 1200 × 560, centered at y 320. Inside, three info rows, each with a gold line icon:
  - 📅 `Date: [Friday, December 18, 2026]`
  - 🕖 `Time: [6:00 PM – 9:00 PM]`
  - 📍 `Place: [Venue name & address]`
  - Use Canva icons, not emoji.
- Under the card: a Cranberry ribbon pill:
  > Dress code: cozy sweaters & something red!
- Hero: the fox in a scarf holding a lantern (about 380), standing at the card's bottom-left corner.

### Builder C

**Slide 7 — Secret Santa (Cranberry gradient, chapter slide)**
- Eyebrow `LET'S PLAY`. Title in Warm Gold:
  > Secret Santa
- Left column: a frosted panel with numbered rules.
  1. Draw a name — keep it secret!
  2. Budget: `[Rp 100.000 / $10]`
  3. Wrap your gift and add a fun clue.
  4. Big reveal at the party!
- Right: the polar bear cub with a stack of wrapped gifts (about 600), at (1180, 240).
- Decoration: gold ribbon swirls, snow overlay, sparkles.

**Slide 8 — Holiday Schedule (Midnight gradient)**
- Eyebrow `MARK YOUR CALENDAR`. Title:
  > Holiday Schedule
- Horizontal timeline: a gold line from x 220 to x 1700 at y 560, with 4 gold glowing dots. Above each dot, a date in Fraunces 48, Warm Gold. Below each, a label in Nunito Bold 26, Snow (width 320):

| Date | Label |
|---|---|
| `[Dec 18]` | `Holiday Party` |
| `[Dec 24]` | `Last Day Before Break` |
| `[Dec 25 – Jan 1]` | `Holiday Break` |
| `[Jan 4]` | `Welcome Back!` |

- Hero: the owl flying with a tiny calendar (about 300), at the top-right.
- A note at y 900:
  > Dates are placeholders — update to your schedule.

**Slide 9 — Wishes for 2027 (scene slide, Midnight gradient)**
- Eyebrow `LOOKING AHEAD`. Title, centered:
  > Our Wishes for 2027
- Five glowing lanterns floating up (Canva elements, about 200 each), in a gentle arc across the slide at y 300–520. Each lantern is a **different color**: gold, pink, teal, lilac and tangerine. Each has a short wish below it in Nunito Bold 24, Snow:
  - `More laughter`
  - `Bigger dreams`
  - `Good health`
  - `New adventures`
  - `Stronger together`
- Hero along the bottom: the penguin duo and the fox releasing lanterns from a snowy hill (about 1200 wide).

### Builder D

**Slide 10 — A Message for You (Midnight gradient)**
- Centered quote in Fraunces Italic 60, Snow, width 1400, at y 300:
  > "May your days be merry and bright, and may the new year bring you everything your heart wishes for."
- Attribution, Nunito ExtraBold 22, Warm Gold, letter spacing 250:
  > — FROM ALL OF US
- Hero: the polar bear cub and the owl looking up at the stars (about 520), at the bottom-right.
- Decoration: large soft gold glow behind the quote (25 % opacity), snow overlay, sparkles.

**Slide 11 — Holiday Greetings Around Us (Cranberry gradient, chapter slide)**
- Title, centered:
  > Holiday Greetings
- Six pills in a 3 × 2 grid, each 520 × 140, at x 120 / 700 / 1280 and y 360 / 560.
- Each pill is colored glass in a different color: Berry Pink, Teal Glow, Lilac, Tangerine, Mint and Ice Blue.
- Each pill has a greeting in Fraunces 40, Snow, plus its language in Nunito 22, Warm Gold:

| Greeting | Language |
|---|---|
| `Merry Christmas` | English |
| `Selamat Natal` | Indonesian |
| `Feliz Navidad` | Spanish |
| `Joyeux Noël` | French |
| `Frohe Weihnachten` | German |
| `Buon Natale` | Italian |

- Hero: the fox holding a wreath (about 320), at the bottom-center.

**Slide 12 — Closing (scene slide, Midnight gradient)**
- Lantern garland at the top. Title, centered at y 260, Fraunces 160, Warm Gold with glow:
  > Thank You!
- Subtitle, centered at y 470, Nunito 32, Snow:
  > Wishing you a cozy Christmas and a wonderful 2027.
- Pill, centered at y 580, Cranberry, Snow text:
  > www.yourwebsite.com  •  @yourhandle
- Hero scene along the bottom (about 1600 wide): the whole cast — penguins, fox, polar bear, owl — gathered around a glowing Christmas tree in the snow. Small cabins sit far in the background.
- Decoration: snow overlay and 3 gold sparkle clusters.

---

## 7. Speaker notes

- Slides 3, 4, 6 and 8: `Replace bracketed placeholders with your real details.`
- Slide 7: `Adjust the budget and currency for your group.`

---

## 8. QA checklist (main agent, with `presentation-design`)

- [ ] 12 pages, in order; all placeholders deleted.
- [ ] Bracketed client placeholders are still visible and readable.
- [ ] Richness checklist passes on every slide. The garland, snow overlay and frosted panels look identical across slides.
- [ ] **Colorful check:**
  - Every slide shows at least 4 palette colors.
  - The garland is multi-colored.
  - Colored glass panels alternate.
  - Characters wear colorful outfits.
  - No slide reads as only navy and gold.
- [ ] One consistent cast style; none of the reference's characters (snowman pair, panda, bunnies, mouse, parka kids).
- [ ] Every visual comes from Canva Elements. No Canva AI assets.
- [ ] Fonts are Fraunces + Nunito only (or the fallbacks). Body text ≥ 22 px. Contrast ≥ 4.5:1. Title glow is subtle and consistent.
- [ ] None of the §2 "must differ" items appear: no red background on regular slides, no casual script, no repeated snow-ground strip, no campfire.
- [ ] No overlap, clipping or stray elements. Check the Lapisan panel on each page once.
- [ ] Nothing shared, downloaded or published.

## 9. Final report (Indonesian)

1. The edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately done differently from the reference.
5. Which path was used (import or kit page), the time per phase, and anything not achieved.
6. A list of the placeholders the client must fill in.
