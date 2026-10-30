# Prompt 1/3 — "The Magic of Christmas: Symbols & Their Stories" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set6-christmas-gamenight-newyear\canva-shared-pipeline.md`.

That file holds:
- §A — hard rules
- §B — colorful brief and richness checklist
- §C — pipeline, builder brief, QA, and report

Deck slug: `christmas-symbols-storybook`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"The Magic of Christmas: Symbols & Their Stories"**. It is a dreamy, illustrated storybook deck that explains what the best-known Christmas symbols mean, for families, schools and community events.

**Reference (direction only):** https://www.canva.com/templates/EAGO7nLR8X8/ ("Beige and Red Dreamy Illustration Christmas Presentation").

- **Borrow the idea:**
  - a soft, dreamy, hand-illustrated Christmas mood
  - warm cream content areas
  - red as the title color
  - one large illustration per slide with calm white space
- **Build from scratch.** Do not copy any layout, illustration, or text from the reference.

**Must also differ from the earlier Christmas decks in this project:**
- Eco-Friendly Christmas
- Christmas Around the World (world-tour stop tags, dashed travel path, globe)
- Family Fun Guide (mint background, scrapbook polaroids, washi tape)
- Season's Greetings (midnight-blue sky, penguins, frosted-glass panels)
- Christmas Through the Senses (papercraft layers, emerald/berry, sense badges)

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Dreamy illustrated mood | The background is a **dreamy dusk gradient** (rose mist to periwinkle mist), **not** flat beige |
| Cream content areas | Content sits on **open storybook pages** and **chapter ribbons**, not plain beige boxes |
| Red titles | Red titles are joined by a **6-color pastel-bright accent set** (sage, butter, twilight blue, rose, lilac, peach), so every slide is colorful |
| One big illustration per slide | Illustrations are **whimsical storybook art** (soft grain, rounded shapes, glowing light). Every content slide is a **"chapter"** about one symbol |
| — | **No** Santa face cover, **no** reindeer pair, **no** red-and-beige only slides, **no** items from the earlier Christmas decks listed in §0 |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Rose Mist | `#FBE8F0` | Background gradient top |
| Periwinkle Mist | `#E6E8FF` | Background gradient bottom |
| Storybook Cream | `#FFF8EE` | Book pages, cards |
| Plum Ink | `#3A2348` | Body text |
| Cherry Red | `#E0384B` | Titles, ribbons |
| Sage Pine | `#4FA37A` | Accent, trees |
| Butter Star | `#FFC94A` | Stars, highlights |
| Twilight Blue | `#5B7CFA` | Accent |
| Rose | `#FF8FB1` | Accent |
| Lilac | `#A07BF0` | Accent |
| Peach | `#FFAE7A` | Accent |

**Color rules:**
- The background is a linear gradient, Rose Mist (top) → Periwinkle Mist (bottom), on every slide.
- Each chapter slide has its own **chapter color** for its ribbon, fun-fact bubble and icon badge:

  | Chapter | Symbol | Chapter color |
  |---|---|---|
  | 1 | Christmas Tree | Sage Pine |
  | 2 | The Star | Butter Star |
  | 3 | The Wreath | Rose |
  | 4 | Lights & Candles | Peach |
  | 5 | Stockings | Twilight Blue |
  | 6 | Bells & Candy Canes | Lilac (Bells) + Cherry Red (Candy Canes) |
  | 7 | Gifts | Cherry Red |

- Every slide has **star-dust trails** (dotted sparkle lines) and soft glowing dots in 3+ palette colors.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Chewy | Sniglet | 76–90 | Cherry Red |
| Body | Quicksand SemiBold | Nunito | 26–28 | Plum Ink |
| Eyebrow | Quicksand Bold | Nunito ExtraBold | 22 | UPPERCASE, letter spacing 200, chapter color |
| Chapter number | Chewy | Sniglet | 30 | Cream, inside the ribbon |

### Recurring motifs

1. **Open storybook page:** a large cream two-page book shape (Canva "open book" element, recolored) that holds the text on chapter slides.
2. **Chapter ribbon:** a ribbon banner in the chapter color with `CHAPTER 01`–`CHAPTER 07`.
3. **Icon badge:** a round badge in the chapter color holding the symbol icon, placed top-right.
4. **Star-dust trail:** a dotted, curving sparkle line connecting the hero to the text.
5. **Fun-fact bubble:** a cloud-shaped bubble in a 25 % tint of the chapter color.
6. **Footer:** a small butter-yellow star with the page number.

**Transition:** Dissolve.

### Illustration style

- **One** whimsical storybook Christmas set: soft grain texture, rounded shapes, gentle glow, diverse people and children, cozy homes, snowy villages, trees, stars, wreaths, candles, stockings, bells, candy canes, gifts.
- The asset scout searches terms like:
  - "whimsical christmas illustration"
  - "storybook christmas"
  - "dreamy christmas village"
  - "cozy christmas night"
- **One** soft, rounded icon set for the symbol badges.

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover**
- Eyebrow: `A CHRISTMAS STORYBOOK`
- Title at (120, 220), width 940, 2 lines:
  > The Magic of Christmas
- Subtitle on a Cherry Red ribbon:
  > Symbols & Their Stories
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~860, right side): an open storybook with a tiny snowy village, a glowing tree and a big star rising out of its pages, plus star-dust trails in 4 colors.
- Decor: glowing dots, small stars, snowflakes.

**Slide 2 — Once Upon a Christmas**
- Title: `Once Upon a Christmas…`
- Open storybook page with this text:
  > Every Christmas symbol carries a little story — of light, hope, giving and togetherness. Let's open the book and discover them, one chapter at a time.
- Hero (~560, left): a child reading a book under a blanket by a snowy window, with a sleepy cat and a warm lamp.
- Decor: star-dust trail from the window into the book.

**Slide 3 — Table of Contents**
- Title: `Our Chapters`
- Seven chapter ribbons in a 2-column list, each in its chapter color, with an icon and a page number:
  1. `The Christmas Tree`
  2. `The Star`
  3. `The Wreath`
  4. `Lights & Candles`
  5. `Stockings`
  6. `Bells & Candy Canes`
  7. `Gifts`
- Hero (~380, bottom right): a stack of colorful storybooks with a candle and a sprig of holly.

### Builder B

**Slide 4 — Chapter 1: The Christmas Tree** (Sage Pine)
- Ribbon `CHAPTER 01` · Eyebrow `LIFE & HOPE` · Title `The Christmas Tree`
- Storybook page, two short paragraphs:
  - **The story:** Evergreen trees stay green through the coldest winter, so people saw them as a sign that life and hope continue.
  - **What it means today:** A decorated tree is the heart of the home — a place where families gather.
- Fun-fact bubble:
  > Decorated Christmas trees became popular in Germany centuries ago, then spread around the world.
- Hero (~560): a family decorating a glowing tree together.

**Slide 5 — Chapter 2: The Star** (Butter Star)
- Ribbon `CHAPTER 02` · Eyebrow `GUIDANCE` · Title `The Star`
- Storybook page:
  - **The story:** The star on top of the tree recalls the Star of Bethlehem, which in the Nativity story guided the wise men.
  - **What it means today:** A shining reminder to follow hope and light.
- Fun-fact bubble:
  > Some families top their tree with an angel instead of a star.
- Hero (~560): a child on a parent's shoulders placing a big star on the tree, with sparkles.

**Slide 6 — Chapter 3: The Wreath** (Rose)
- Ribbon `CHAPTER 03` · Eyebrow `EVERLASTING LOVE` · Title `The Wreath`
- Storybook page:
  - **The story:** A wreath is a circle with no beginning and no end — a symbol of everlasting love and hope.
  - **What it means today:** Hung on the front door, it says "welcome" to everyone who visits.
- Fun-fact bubble:
  > An Advent wreath holds four candles — one is lit on each Sunday before Christmas.
- Hero (~520): a colorful front door with a big wreath, a red ribbon, and snow on the steps.

### Builder C

**Slide 7 — Chapter 4: Lights & Candles** (Peach)
- Ribbon `CHAPTER 04` · Eyebrow `LIGHT IN THE DARK` · Title `Lights & Candles`
- Storybook page:
  - **The story:** Christmas comes in the darkest time of the year for many places, so light became a symbol of joy and hope.
  - **What it means today:** Twinkling lights and candles make homes and streets glow with welcome.
- Fun-fact bubble:
  > Before electric lights, families placed small candles on their trees. Electric Christmas lights first appeared in the 1880s.
- Hero (~560): a snowy street of houses glowing with multicolor lights.

**Slide 8 — Chapter 5: Stockings** (Twilight Blue)
- Ribbon `CHAPTER 05` · Eyebrow `SURPRISE & GENEROSITY` · Title `Stockings`
- Storybook page:
  - **The story:** A popular legend says Saint Nicholas secretly dropped gold coins down a chimney, and they landed in stockings hung by the fire to dry.
  - **What it means today:** Little surprises that show someone is thinking of you.
- Hero (~540): colorful stockings hanging over a cozy fireplace, each a different color and pattern.

**Slide 9 — Chapter 6: Bells & Candy Canes** (two half-page chapters)
- Ribbon `CHAPTER 06` · Title `Bells & Candy Canes`
- Left half (Lilac), card `Bells`:
  > Bells ring out joyful news and call people together to celebrate.
- Right half (Cherry Red), card `Candy Canes`:
  > A popular legend says candy canes were shaped like a shepherd's crook. The red and white stripes came later.
- Center hero (~420): a golden bell tied with a ribbon next to a giant striped candy cane, with sparkles.

### Builder D

**Slide 10 — Chapter 7: Gifts** (Cherry Red)
- Ribbon `CHAPTER 07` · Eyebrow `KINDNESS` · Title `Gifts`
- Storybook page:
  - **The story:** Giving gifts recalls the gifts the wise men brought in the Nativity story.
  - **What it means today:** A gift chosen with love says, "You matter to me."
- Three small idea tags (Rose / Sage / Twilight Blue):
  - `Handmade cards`
  - `Baked treats`
  - `Time together`
- Hero (~520): kids happily wrapping colorful gifts at a table.

**Slide 11 — Write Your Own Chapter**
- Title: `Write Your Own Chapter`
- Four numbered steps on cream page cards, each number on a chapter-color circle:
  1. Choose a symbol that feels like your family's Christmas.
  2. Draw it on a paper ornament.
  3. Write one sentence about what it means to you.
  4. Hang it on the tree and share its story.
- Hero (~500): a family drawing ornaments at a kitchen table, with paper and colored pencils.

**Slide 12 — Merry Christmas**
- Title centered, Chewy 140, Cherry Red:
  > Merry Christmas!
- Subtitle:
  > May your story be full of light and love.
- Three contact pills (Sage / Rose / Twilight Blue):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400 wide): a storybook closing gently over a glowing snowy village, with star-dust rising into the sky.

## 4. Speaker notes

- **Slides 4–10:**
  > Legends and meanings vary between families, cultures and faiths. Present them as traditional stories.

## 5. Deck-specific QA

- [ ] Every chapter slide uses its own chapter color for ribbon, icon badge and fun-fact bubble.
- [ ] Background is the dusk gradient on all 12 slides; no flat beige.
- [ ] One storybook illustration style across the deck.
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier Christmas decks (§0).
