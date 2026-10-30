# Prompt 4/5 — "Merry Christmas: Christmas Through the Senses" (colorful)

> Copy everything below into a new task.
> Team: **1 main agent**, **1 asset scout**, and **4 builder subagents**.

**FIRST:** read and follow every section of
`%USERPROFILE%\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\scratch-workspaces\dcdc6f97-14f9-43a0-812f-7b344eef061a\12aa8b61-941b-457d-8505-99fb0b2a7c89\scratch-2026-10-22-82e737\canva-shared-pipeline.md`.

That file holds:
- §A — hard rules
- §B — colorful brief
- §C — pipeline, builder brief, QA and report

Deck slug: `christmas-senses`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Merry Christmas – Christmas Through the Senses"**.

It is a joyful, illustrated deck that explores Christmas through what we see, hear, smell, taste, and feel.

**Reference (direction only):** https://www.canva.com/templates/EAG3pQhgyFQ/ ("Orange Brown Illustrated Spirit of Christmas").

- **Borrow these ideas:**
  - Bold, warm, glowing festive energy.
  - Big expressive titles.
  - Illustration-led slides.
  - Short text in rounded boxes.
- **Build from scratch.**

**Must also differ from the earlier Christmas decks in this project:**
- Eco Christmas
- Christmas Around the World
- Family Fun Guide
- Season's Greetings

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Glowing festive energy | **Jewel-tone palette** (emerald, magenta, royal blue, gold, tangerine) on a deep emerald / berry background. **Not** an orange-red gradient |
| Big expressive titles | Bold rounded titles in Paytone One, each word a different jewel color. **No** glowing cream hand-lettering |
| Illustration-led slides | **Layered paper-cut (papercraft) illustrations**, with stacked paper layers, soft shadows and scalloped edges. **No** 3D gingerbread mascots, **no** Santa sleigh, **no** reindeer pair, **no** elf |
| Text in rounded boxes | Text sits in **scalloped paper tags and ornament-shaped badges**, not red rounded boxes |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Deep Emerald | `#0F4C3A` | Background (odd slides) |
| Berry Night | `#5A1846` | Background (even slides) |
| Gold | `#F6C744` | Titles, stars |
| Magenta | `#E5387A` | Accent |
| Royal Blue | `#3D6DE0` | Accent |
| Tangerine | `#FF8F3F` | Accent |
| Mint Frost | `#9BE7C4` | Accent, snow |
| Cream Paper | `#FFF4E2` | Tags and cards |

**Color rules:**
- Each "sense" slide has its own accent color for its paper tags and its title highlight:
  - Sight: Royal Blue
  - Sound: Magenta
  - Scent: Tangerine
  - Taste: Gold
  - Touch: Mint
- Every slide has **paper-layer corners** (Canva layered paper-cut elements) in 3+ colors.

### Fonts

- **Titles:** Paytone One (fallback: Lilita One), 76–90.
  - Multi-color words: Gold, plus the slide's accent color.
- **Body:** Mulish (fallback: Nunito), 26–28.
  - Dark Ink `#2A1E2C` on Cream Paper tags.
  - Cream on dark backgrounds.
- **Eyebrow:** Mulish ExtraBold 22, letter spacing 200, Mint Frost.

### Recurring motifs

1. **Sense badge:** an ornament-shaped badge (Canva bauble shape) with a sense icon (eye / music note / nose / cookie / mitten) and the label `SENSE 01`–`SENSE 05`.
2. **Scalloped paper tags:** Cream Paper, radius 24, scalloped edge, colored string. These hold the text.
3. **Paper-cut corners:** layered hills, trees, or snowflakes in the slide's colors.
4. **Gold stars and snow dots:** 3–5 per slide.
5. **Footer:** a thin gold garland line and the page number.

**Transition:** Fade.

### Illustration style

- **One papercraft / paper-cut Christmas illustration set**: trees, houses, ornaments, candles, cookies, mugs, mittens, bells, kids, animals.
- The asset scout searches terms like:
  - "paper cut christmas"
  - "papercraft christmas tree"
  - "layered paper christmas"

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (Deep Emerald)**
- Eyebrow:
  > A FESTIVE JOURNEY FOR ALL FIVE SENSES
- Title at (120, 240), width 960, 2 lines. "Merry" in Gold, "Christmas!" in Magenta:
  > Merry
  > Christmas!
- Subtitle on a Cream Paper tag:
  > Christmas through what we see, hear, smell, taste and feel.
- Hero (~860), right side: a layered paper-cut winter village with a big glowing tree, colorful houses and a starry sky.
- Paper-cut snowflakes at the corners.

**Slide 2 — Welcome Quote (Berry Night)**
- Centered on a big scalloped Cream tag:
  > "Christmas is not a time nor a season, but a state of mind."
- Attribution, in Gold:
  > — CALVIN COOLIDGE
- Decor: paper-cut ornaments hanging from the top in 5 colors, plus paper-cut holly in two corners.

**Slide 3 — Five Senses Map (Deep Emerald)**
- Title: `Five Senses of Christmas`.
- A big paper-cut Christmas tree hero in the center (~600 tall).
- Five ornament badges hang on and around the tree, each a different accent color. Each has its icon and label:

  | Badge | Caption |
  |---|---|
  | `SIGHT` | Twinkling lights |
  | `SOUND` | Carols & bells |
  | `SCENT` | Pine & cinnamon |
  | `TASTE` | Cookies & cocoa |
  | `TOUCH` | Cozy & warm |

- Each badge has a short caption on a small Cream tag.

### Builder B

**Slide 4 — Sense 01: Sight (Berry Night, accent Royal Blue)**
- Sense badge: `SENSE 01 · SIGHT`.
- Title: `What We See`.
- Three Cream tags with icons:
  - `Twinkling Lights` — Strings of color on houses and trees.
  - `Decorated Trees` — Ornaments, garlands and a star on top.
  - `Snowy Windows` — Frosty patterns and glowing candles.
- Hero (~640): a paper-cut street with colorful lit houses and a tree.

**Slide 5 — Sense 02: Sound (Deep Emerald, accent Magenta)**
- Sense badge: `SENSE 02 · SOUND`.
- Title: `What We Hear`.
- Hero in the center (~560): paper-cut carolers singing, with floating music notes in 5 colors.
- Four tags around the hero:
  - `Christmas carols`
  - `Jingling bells`
  - `Crackling fireplace`
  - `Laughter at the table`

**Slide 6 — Sense 03: Scent (Berry Night, accent Tangerine)**
- Sense badge: `SENSE 03 · SCENT`.
- Title: `What We Smell`.
- Hero (~560, left): a paper-cut kitchen window with steam swirls rising from a tray of cookies.
- Right: four scent "bubbles" (circles in 4 colors), each with an icon and a label:
  - `Fresh pine`
  - `Cinnamon & ginger`
  - `Baking cookies`
  - `Orange & cloves`

### Builder C

**Slide 7 — Sense 04: Taste (Deep Emerald, accent Gold)**
- Sense badge: `SENSE 04 · TASTE`.
- Title: `What We Taste`.
- A 2 × 2 grid of Cream tags, each with an illustration (~150):
  - `Gingerbread Cookies` — Spiced, sweet and fun to decorate.
  - `Hot Cocoa` — Topped with marshmallows.
  - `Festive Dinner` — Shared with family and friends.
  - `Candy Canes` — Peppermint stripes of red and white.
- Paper-cut table runner along the bottom.

**Slide 8 — Sense 05: Touch (Berry Night, accent Mint)**
- Sense badge: `SENSE 05 · TOUCH`.
- Title: `What We Feel`.
- Hero (~620, right): a paper-cut cozy scene with a person in a knitted sweater and mittens holding a mug by a window.
- Left: three tags:
  - `Soft knitted sweaters and scarves`
  - `Cold snowflakes on warm cheeks`
  - `Crinkly wrapping paper and ribbons`

**Slide 9 — The Feeling Inside (Deep Emerald)**
- Title: `The Sixth Sense: Joy`.
- Centered hero (~520): a big paper-cut heart made of layered colors, with sparkles.
- Three ornament badges below, in different colors:
  - `Giving` — The joy of a gift chosen with love.
  - `Together` — Time with the people who matter.
  - `Kindness` — Small acts that warm someone's day.

### Builder D

**Slide 10 — Make Your Own Christmas Memory (Berry Night)**
- Title: `Create a Senses Memory Jar`.
- A paper-cut jar hero (~520) filled with colorful paper notes.
- Numbered steps on Cream tags:
  1. Find a clean jar and colorful paper.
  2. Each day, write one Christmas moment you saw, heard, smelled, tasted or felt.
  3. Fold the notes and drop them in.
  4. Read them together on New Year's Eve!

**Slide 11 — Gratitude Wall (Deep Emerald)**
- Title: `Thank You, Christmas, For…`
- Six paper-cut ornament shapes in 6 colors hanging from a garland across the slide. Each holds one word (Mulish ExtraBold 26):
  - `Family`
  - `Friends`
  - `Laughter`
  - `Warmth`
  - `Music`
  - `Hope`
- Paper-cut snowy hills along the bottom.

**Slide 12 — Merry Christmas (Berry Night)**
- Title centered, Paytone One 140, multi-color:
  > Merry Christmas!
- Subtitle:
  > May all your senses be filled with joy.
- Contact pill, Cream:
  > www.yourwebsite.com  •  @yourhandle
- Hero along the bottom (~1400 wide): a paper-cut village with a big tree, and stars over the hills.
- Paper-cut ornaments hang from the top. Gold stars.

## 4. Deck-specific QA

- [ ] All five sense slides use their own accent color and sense badge.
- [ ] Background alternates Emerald / Berry.
- [ ] Papercraft illustration style is consistent.
- [ ] Nothing from the reference: no orange-red gradient, no 3D gingerbread mascots, no sleigh, no reindeer, no elf.
- [ ] Nothing from earlier Christmas decks: no world-tour stop tags, no scrapbook polaroids, no navy night penguins.
- [ ] The Coolidge quote is attributed as written.
