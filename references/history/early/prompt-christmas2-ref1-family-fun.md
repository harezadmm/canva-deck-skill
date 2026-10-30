# Prompt — "Merry & Bright: A Christmas Family Fun Guide" (Christmas 2 · Ref 1, fast pipeline)

> Copy everything below into a new task.
> Team: one **main agent**, one **asset scout**, and **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Merry & Bright – Christmas Family Fun Guide"**. It's a cheerful, illustrated guide to Christmas activities for families, classes and kids' groups.

- **Client brief: COLORFUL.**
  - The deck must feel bright, joyful and multi-colored, like a candy shop at Christmas.
  - Every slide shows **at least 4 palette colors**, plus colorful illustrations.
  - A slide is never just red-on-cream.
- **Language:** all deck content in **English**. Report to the user in **Indonesian**.
- **Reference (mood only):** https://www.canva.com/templates/EAG2U8db99Y/ ("Red and Green Playful Merry Christmas Presentation" by ENIGMA STUDIO).
  - Borrow the **mood**: warm, playful, kid-friendly, cute watercolor Christmas art, light background, red-and-green holiday palette.
  - **Build from scratch.** Never click "Use this template". Never copy its pages or elements.
- **Not a repeat:** this deck must also look different from the earlier "Christmas Around the World" deck, which used Fredoka, a world-tour theme, stop tags and a globe.
- **Expected time:** about 35–45 minutes.

### Skills to load first (main agent)

| Skill | Use |
|---|---|
| `anthropic-skills:pptx` | Skeleton .pptx |
| `elite-powerpoint-designer` | "Creative Bold" direction |
| `ppt-visual` | Varied layouts |
| `presentation-design` | QA |

---

## 1. Hard rules (all agents)

1. **Built from scratch; every asset comes from Canva Elements.** This is a project rule.
   - The code skeleton may contain **text and plain layout shapes only**: background color, cards, pills, circles, lines.
   - Every visual comes from Canva Elements (Elemen → Grafis / Stiker / Bentuk / Bingkai). That includes characters, objects, frames, washi tape, stripes, doodles and sparkles.
   - Pro elements are allowed.
2. **No Canva AI.** Don't use Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva" or "Buat Animasi". Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing or downloading. No changes to sharing, access or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** All agents share one clipboard. Insert every asset fresh from the Elements panel.
6. **Keep the copy and steps exact as written in §6.** In the cookie recipe, only the main agent may adjust quantities, and only to fix an obvious typo.
7. **No brands or trademarks.** No brand logos, and no trademarked characters or movie titles. Slide 7 lists film **genres**, not titles.
8. **Safety in crafts and cooking.** Show adult help with ovens and scissors. No open flames near kids.

---

## 2. Borrow vs. must differ

| Borrow (the mood) | Must differ (our identity) |
|---|---|
| Cute watercolor Christmas illustrations | **No** peeking-Santa cover, no snowman trio, no Santa-holding-gift poses |
| Light background, red + green | Background is **soft mint** with **candy-cane stripe** accents. Not plain cream with baubles. |
| Gifts and baubles as decoration | **No** hanging-bauble border along the top, **no** gift-box clusters in the corners |
| Chunky titles | Rounded bubbly titles (Lilita One), **not** slab serif |
| One hero illustration per slide | Our identity is a **scrapbook / activity-card** look: polaroid frames, washi tape, recipe cards, numbered activity stamps, checklists |
| — | **No** world-tour items from the earlier deck: no stop tags, no dashed travel path, no globe |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins: 120 left/right, 96 top/bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Mint Snow | `#EAF6F0` | Main background |
| Paper | `#FFFDF7` | Cards and polaroids |
| Candy Red | `#E23B3B` | Titles, stripes, stamps |
| Pine | `#1E7A55` | Secondary titles, ✓ marks |
| Gingerbread | `#C07A45` | Recipe slide accents, kraft labels |
| Twinkle Gold | `#F5B841` | Stars, highlights |
| Cocoa | `#3B2A25` | Body text |
| Frosting Pink | `#F78FB3` | Card fills (tint), stamps, decorations |
| Ice Blue | `#5BC0EB` | Card fills (tint), snowflakes, ribbons |
| Sprout Lime | `#8FD14F` | Card fills (tint), leaves, ✓ circles |
| Lilac | `#A98BF0` | Card fills (tint), sparkles, washi tape |

**Color rules (colorful brief):**
- **Activity stamps.** Each one gets its own color, cycling through Candy Red, Ice Blue, Sprout Lime, Frosting Pink, Lilac, Twinkle Gold, Pine and Gingerbread for NO. 01–08.
- **Cards.** Fills alternate between Paper and the 20 % tints of Pink / Blue / Lime / Lilac / Gold. Never use more than 2 neighbouring cards in the same tint.
- **Washi tape.** Mix patterns and colors: stripes, dots and gingham in pink, blue, lime and gold.
- **Illustrations.** Choose the most colorful version available: rainbow ornaments, multi-colored lights, colorful sweaters.
- **Background.** The page stays Mint Snow, but each slide adds 2–3 soft colored **blobs or confetti** behind the content in different tints.

### Fonts (max 2 families)

- **Titles:** Lilita One (fallback: Luckiest Guy).
- **Body:** Quicksand Bold/Medium (fallback: Nunito).

| Style | Spec |
|---|---|
| Cover title | Lilita One 130–150, Candy Red, with a Paper outline effect if available |
| Slide title | Lilita One 72–84, Candy Red |
| Activity stamp | Lilita One 28 inside a scalloped circle |
| Card title | Lilita One 34–38, Pine |
| Body | Quicksand Medium 26–28, Cocoa, line spacing 1.4. Never below 22 |
| Checklist | Quicksand Bold 26, with Pine ✓ |

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per card.
- Max 4 font sizes per slide.
- Contrast ≥ 4.5:1.
- Motion: titles Fade; cards Rise, staggered. Max 3 animated elements per slide.
- Transition: Push, used for the whole deck.

### Recurring motifs (identical on every slide)

1. **Activity stamp:** a scalloped circle (Canva element) in Candy Red, 150 px, with Paper text `NO. 01` … `NO. 08`. Placed at the top-left of each activity slide.
2. **Candy-cane stripe band:** a diagonal red-and-white stripe strip (Canva element), 40 px tall, along the top **or** bottom edge. Alternate between slides.
3. **Polaroid / recipe card:** a Paper card, radius 16, with a slight rotation (−3° to 3°) and **washi tape** (Canva element) on one or two corners.
4. **Checklist "What you need":** Pine ✓ bullets inside a Paper card with a Gingerbread kraft label on top.
5. **Sparkles:** 2–4 Twinkle Gold sparkles per slide.

### Illustration style

**Cute watercolor Christmas** illustrations: kids, elves, gingerbread figures, cozy objects. The asset scout picks **one anchor creator** with a large cute-watercolor Christmas set, and uses it for every hero.

### Richness checklist (every slide)

Every slide has all of the following:
- 1 hero illustration of at least 480 px
- 2–5 supporting objects
- at least 2 decorative layers (stripe band, washi tape, sparkles or snow dots)
- text inside cards, never a bare paragraph
- **at least 4 palette colors clearly visible**
- **at least 1 colored blob or confetti cluster**

---

## 4. Pipeline

### Phase 0A — main agent: skeleton .pptx (~5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU).
   - Convert px to EMU with `px * 9525`.
2. For each slide, add:
   - the background
   - all text (exact copy, font names, sizes, colors)
   - the plain Paper cards, their rotation, and the circles
3. Mark every visual with a labeled placeholder rectangle at its exact spot.
   - Fill: 20 % transparent Pine.
   - Label example: `HERO: kids baking cookies 640w`.
4. Add the speaker notes from §7.
5. Save as `christmas2-familyfun-skeleton.pptx`.

### Phase 0B — asset scout, in parallel with 0A (~10 min)

Search Canva Elements for every hero, object and decor item in §6. Write the results to `christmas2-familyfun-assets.md` with these columns:

| Slide | Item | Exact keyword | Creator | Result (row, col) | Pro/free |

Choose 1 hero creator, 1 washi-tape set, 1 stripe band element and 1 scalloped stamp shape. Insert nothing into the design.

### Phase 0C — main agent: import (~3 min)

1. Upload the skeleton with the `file_upload` tool (Buat desain → Impor file, or Unggahan). If that fails, ask the user to drag the file in once.
2. Rename the design.
3. Check fonts and card rotation on 2–3 slides.
4. **Fallback:** if the import is broken, build slide 4 by hand as a kit page and duplicate it. Report which path you used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builders in parallel (~20 min)

Each builder gets §1–3, its own slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`.
>
> 1. Place the decorative layers first: stripe band, washi tape, snow dots.
> 2. Then place the hero, the objects and the stamp, using the exact keywords and results from the asset sheet.
> 3. Lock the aspect ratio. Match each placeholder's size and position using Posisi. Delete the placeholders.
> 4. Run the richness checklist.
> 5. Fix overlap and clipping only.
> 6. Take a zoom screenshot of each slide.
>
> Rules:
> - The UI is in Indonesian.
> - Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua".
> - Never copy or paste.
> - If screenshots time out twice, stop and report "BLOCKED".
>
> Report per slide: done or issues, plus assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent QA + report (~5 min)

Follow §8 and §9.

---

## 5. Coordinates

All positions are px on the 1920 × 1080 page. (x, y) is the top-left corner.

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (bg Mint Snow)**
- Candy-cane stripe band along the top edge.
- Kraft label pill at (120, 200), Gingerbread fill, Paper text: `A FAMILY FUN GUIDE`.
- Title at (120, 260), width 900, Lilita One 140, 2 lines:
  > Merry &
  > Bright!
  - "Bright!" is in Pine.
- Subtitle at (120, 640), Quicksand 32, width 780:
  > 8 cozy Christmas activities to share with the people you love.
- Pill at (120, 780), Candy Red fill, Paper text: `@yourhandle`.
- Hero: a large polaroid card (760 × 700, rotated 3°) at (1040, 160). Inside it is a watercolor scene of kids decorating a Christmas tree together. Washi tape sits on the top two corners.
- Decor: 3 sparkles, snow dots, a small gingerbread figure peeking from behind the polaroid's bottom-left corner.

**Slide 2 — A Little Note (bg Paper)**
- Centered handwritten-feel card, Mint Snow fill, 1400 × 620, at (260, 200), with washi tape at the top center.
- Inside the card:
  - Lilita One 56, Candy Red, centered:
    > The best gifts aren't under the tree —
  - Quicksand Bold 40, Cocoa, centered:
    > they're the moments we make together.
- Below the card, at y 860, Quicksand 26, Pine, centered:
  > Pick one activity a day, or try them all in one big weekend!
- Decor: a watercolor holly sprig and a mug of cocoa on the left and right edges (~280 each), plus 3 sparkles.

**Slide 3 — Your Fun Menu (bg Mint Snow)**
- Title at (120, 110):
  > Your Fun Menu
- 8 mini-cards in a 4 × 2 grid.
  - Size 380 × 300.
  - x = 120 / 560 / 1000 / 1440; y = 300 / 640.
  - Each card is Paper with a small rotation and holds: a small watercolor icon (~120), the stamp number, and a title in Lilita One 30, Candy Red.

| No. | Title |
|---|---|
| 01 | Bake Gingerbread Cookies |
| 02 | Make Paper Ornaments |
| 03 | Cozy Movie Night |
| 04 | Carol Sing-Along |
| 05 | Gift-Wrapping Station |
| 06 | Kindness Advent |
| 07 | Christmas Charades |
| 08 | Letters of Wishes |

- Candy-cane stripe band along the bottom edge.

### Builder B

**Slide 4 — No. 01 Bake Gingerbread Cookies (bg Mint Snow)**
- Stamp `NO. 01` at (120, 96). Title at (300, 110):
  > Bake Gingerbread Cookies
- Left: recipe card, Paper, 820 × 700, at (120, 280), rotated −2°, with a kraft label `WHAT YOU NEED`. Checklist:
  - ✓ 3 cups flour
  - ✓ 1 tsp ginger & 1 tsp cinnamon
  - ✓ ½ cup butter, softened
  - ✓ ½ cup brown sugar
  - ✓ ½ cup honey or molasses
  - ✓ 1 egg
- Right: a second card, 760 × 460, at (1040, 520), with a kraft label `HOW TO`. Numbered steps:
  1. Mix butter, sugar, honey and egg.
  2. Stir in flour and spices to make a dough.
  3. Roll out, cut shapes, bake 8–10 min at 175 °C with an adult.
  4. Cool, then decorate with icing!
- Hero: watercolor kids baking with an adult (~600), top-right at (1180, 96).
- Decor: cookie cutters, a rolling pin, sparkles.

**Slide 5 — No. 02 Make Paper Ornaments (bg Paper)**
- Stamp `NO. 02` and title:
  > Make Paper Ornaments
- Layout: three step polaroids in a row.
  - Size 520 × 560; x = 120 / 700 / 1280; y = 300.
  - Rotations: −3° / 2° / −2°.
  - Washi tape on each.
  - Each has an illustration on top and a step caption below it (Quicksand Bold 26).

| Step | Caption |
|---|---|
| 1 | Cut stars and circles from colored paper. |
| 2 | Decorate with glitter, buttons or drawings. |
| 3 | Punch a hole, add ribbon, and hang them up! |

- Tip bubble at the bottom center, Twinkle Gold:
  > Tip: reuse old cards and wrapping paper.

**Slide 6 — No. 03 Cozy Movie Night (bg Cocoa, dark slide)**
- Stamp `NO. 03`. Title in Paper:
  > Cozy Movie Night
- Left column (Paper text):
  - Checklist `SET THE SCENE`:
    - ✓ Blankets & pillows fort
    - ✓ Hot cocoa with marshmallows
    - ✓ A big bowl of popcorn
    - ✓ Fairy lights on, big lights off
  - Card `PICK A GENRE` with 3 pills:
    - `Animated Classics`
    - `Feel-Good Family Films`
    - `Snowy Adventures`
- Right: hero watercolor scene of a family on a sofa under a blanket with a glowing screen (~760), at (1060, 220).
- Decor: string lights along the top, Twinkle Gold sparkles.

### Builder C

**Slide 7 — No. 04 Carol Sing-Along (bg Mint Snow)**
- Stamp `NO. 04`. Title:
  > Carol Sing-Along
- Center: hero of watercolor kids caroling with song sheets and a lantern (~720), at (600, 260), on a Paper circle (800).
- Left and right of the hero: two music-note cards, each 380 × 260.
  - Left card text:
    > Make a playlist of everyone's favorite carols.
  - Right card text:
    > Add jingle bells, shakers or pots and spoons!
- Decor: floating music notes (Canva elements) in Candy Red and Pine, sparkles, a stripe band along the bottom.

**Slide 8 — No. 05 Gift-Wrapping Station (bg Paper)**
- Stamp `NO. 05`. Title:
  > Gift-Wrapping Station
- Left: hero of a watercolor table with kraft paper, ribbons, twine and tags (~700), inside a polaroid at (120, 260), rotated −2°.
- Right column at x 900, checklist `WHAT YOU NEED`:
  - ✓ Kraft paper or old newspaper
  - ✓ Ribbon, twine or fabric scraps
  - ✓ Tape and safety scissors
  - ✓ Handmade gift tags
- Small card below:
  > Let each person design their own signature wrap!
- Decor: a pine sprig, sparkles, washi tape.

**Slide 9 — No. 06 Kindness Advent (bg Mint Snow)**
- Stamp `NO. 06`. Title:
  > Kindness Advent
- Subtitle:
  > One small kind act every day until Christmas.
- A 3 × 2 grid of "door" cards. Each is a Paper card with a little number tag (Twinkle Gold circle) and one act:

| # | Act |
|---|---|
| 1 | Write a thank-you note |
| 2 | Bake treats for a neighbor |
| 3 | Donate toys you've outgrown |
| 4 | Call a grandparent |
| 5 | Help clean up without being asked |
| 6 | Give someone a compliment |

- Hero: a watercolor kid holding a gift box out to someone (~420), bottom-right, partly overlapping the last card's corner without covering its text.

### Builder D

**Slide 10 — No. 07 Christmas Charades (bg Candy Red, dark slide)**
- Stamp `NO. 07` in a Paper stamp with Candy Red text. Title in Paper:
  > Christmas Charades
- Left: `HOW TO PLAY` card (Paper, Cocoa text):
  1. Write Christmas words on slips of paper.
  2. Take turns acting them out — no talking!
  3. Your team guesses before the timer ends.
- Right: 6 word cards, tilted like scattered slips (Paper, Lilita One 32, Candy Red):
  - `Reindeer`
  - `Snowball Fight`
  - `Decorating a Tree`
  - `Elf`
  - `Ice Skating`
  - `Unwrapping a Gift`
- Hero: watercolor kid acting out a reindeer with antler hands (~460).
- Decor: a sand timer, Twinkle Gold sparkles.

**Slide 11 — No. 08 Letters of Wishes (bg Paper)**
- Stamp `NO. 08`. Title:
  > Letters of Wishes
- Center: a big letter-paper card, 1100 × 660, at (410, 260), lined-paper look (Mint Snow with thin Pine lines), with an envelope (Canva element) peeking behind it. Text inside:
  - Quicksand Bold 30:
    > Dear Christmas,
  - Then:
    > This year I wish for… / I'm thankful for… / Next year I want to…
  - Signature line:
    > Love, ______
- Side note card:
  > Seal the letters and open them together next Christmas!
- Decor: a stamp-style postage sticker, a pencil, sparkles.

**Slide 12 — Closing (bg Mint Snow)**
- Candy-cane stripe bands along the top **and** the bottom.
- Centered at y 300, Lilita One 150:
  > Merry Christmas!
  - "Christmas!" is in Pine.
- Subtitle centered at y 500, Quicksand Bold 34, Cocoa:
  > Thanks for making memories with us.
- Pill centered at y 620, Candy Red fill, Paper text:
  > www.yourwebsite.com  •  @yourhandle
- Hero: a row of the deck's watercolor characters (kids, a gingerbread figure, an elf) waving along the bottom (~1300 wide), with snow dots and sparkles.

---

## 7. Speaker notes

| Slide | Note |
|---|---|
| 4 | Always have an adult handle the oven; check for allergies (wheat, egg, dairy). |
| 6 | Pick age-appropriate films for your group. |

---

## 8. QA checklist (main agent, with `presentation-design`)

- [ ] 12 pages in order; all placeholders deleted.
- [ ] Richness checklist passes on every slide.
- [ ] **Colorful check:** every slide shows at least 4 palette colors.
- [ ] Stamps NO. 01–08 each have a different color.
- [ ] Cards alternate tints; no slide is mostly red-on-cream.
- [ ] Activity stamps NO. 01–08 are consistent.
- [ ] Polaroids, washi tape and stripe bands are consistent.
- [ ] Every visual comes from Canva Elements. No Canva AI assets.
- [ ] The hero style is consistent: one anchor creator.
- [ ] Only Lilita One + Quicksand (or the fallbacks). Body text ≥ 22. Contrast ≥ 4.5:1.
- [ ] None of the §2 "must differ" items appear, and nothing from the earlier world-tour deck.
- [ ] No logos, no film titles.
- [ ] No overlap, clipping or stray elements (check Lapisan on each page once).
- [ ] Nothing shared, downloaded or published.

## 9. Final report (Indonesian)

1. Edit link.
2. One line per slide.
3. Assets per slide (keyword + creator + Pro/free).
4. Differences from the reference.
5. Path used (import or kit page), time per phase, and anything not achieved.
