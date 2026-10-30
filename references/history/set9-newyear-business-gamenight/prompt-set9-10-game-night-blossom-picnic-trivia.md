# Prompt set9-10 — "Blossom Hill Picnic Trivia: A Spring Game Night" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set9-newyear-business-gamenight\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `game-night-blossom-picnic-trivia`.

**Hard rules, repeated (details in §A):**
- Every visual comes from **Canva Elements** only (Pro is OK). The skeleton holds only text and plain layout shapes.
- **No Canva AI** of any kind.
- **No logos, brands or trademarked characters.**
- Nothing shared, published or downloaded. Never log in for the user. Never click "Use this template".

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Blossom Hill Picnic Trivia: A Spring Game Night"**. It is a ready-to-run trivia night for teams of 2–4:
- **Round 1, Quick Answer:** 4 questions, 1 point each.
- **Round 2, Pick a Paddle:** 2 multiple-choice questions, 2 points each. Teams hold up a color paddle instead of letters.
- **Round 3, Fill the Blanks:** 3 words with missing letters, 3 points each.
- **Speed Round:** 5 true-or-false statements, 1 point each.
- **Picnic Jackpot:** one bet-your-points final question.
- A scoreboard slide and a thank-you.

**All answers live only in the speaker notes**, never on the slides.

**Reference (direction only):** https://www.canva.com/templates/EAGwfllf4I0/ ("White Blue Retro 8-Bit Pixel Cozy Plant Tree Game Night Game Presentation").

- **Borrow the idea:**
  1. a **cozy spring landscape**: sky, clouds, rolling green hills and a blossoming tree;
  2. a **framed question panel** in the middle of every slide;
  3. three question types: answer the question, multiple choice, complete the word;
  4. a simple game flow: how to play, questions, answers, thank you.
- **Build from scratch.** Do not copy any page, layout, illustration or text from the reference. Never click "Use this template". **Do not use pixel art**: the reference is pixel, this deck is smooth flat vector.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Spring sky, hills and blossom tree | A **golden-hour pastel picnic**: peach-to-pink gradient sky, soft flat-vector hills, a pink cherry-blossom tree, **bunting flags** across the top and a **gingham picnic blanket** strip along the bottom. **Not** a blue pixel sky. |
| Framed question panel | **"Gingham-trim cards"**: Cream rounded cards with a 12 px gingham top border. **No** pixel windows, **no** black-and-white outlines. |
| Multiple choice | Answers are **four color paddles** (Pink / Yellow / Blue / Green) that teams hold up. **No** A/B/C/D letters or buttons. |
| Complete the word | Letters sit in **tiles** (Cream for given letters, dashed blossom-pink for blanks). |
| — | **No** pixel art, pixel fonts or 8-bit look (set7-4 "Game Night Quest" is a daytime pixel world map; set7-5 "Guess the Idiom!" is a pixel console). **No** sticker-bomb with suit confetti, spinner wheel or ticket stubs (set6-2). **No** night quiz-show stage (earlier "Ultimate Quiz Party"). **No** board-game tabletop, tile path or pawns (earlier "Family Trivia Showdown"). **No** Christmas or New Year decor. |
| — | Must also differ from the sibling game-night decks written in parallel (set9-7, set9-8) and from set9-9 "Tabletop Tournament" (saturated checker tiles, isometric toys). This deck's identity is **pastel golden-hour picnic + gingham + color paddles**. Do not add checker backgrounds, isometric toys, neon or dark backgrounds. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Golden Sky | `#FFE8CC` → `#FFD0DD` | Background: a 2-stop gradient, top to bottom, on every slide |
| Night Indigo | `#2B2A5C` | Text, titles, outlines |
| Blossom Pink | `#FF8FB8` | Accent, Pink paddle, blossoms |
| Sunbeam | `#FFD25E` | Accent, Yellow paddle, highlights |
| Sky Blue | `#7EC8F2` | Accent, Blue paddle |
| Matcha | `#7BC47F` | Accent, Green paddle, hills |
| Lilac | `#B9A2F5` | Accent, bunting, badges |
| Peach | `#FFB38A` | Accent, bunting, banners |
| Cream | `#FFF9F0` | Cards |
| Hill Green (deep) | `#4FB477` | Back hill layer |

**Color rules:**
- The four **paddle colors** are fixed: Pink = Blossom Pink, Yellow = Sunbeam, Blue = Sky Blue, Green = Matcha. Use them for the paddles, the team rows on slide 9 and the pills in the "How to Play" slide.
- Round colors (eyebrow chip, card gingham accent):

  | Part | Slides | Color |
  |---|---|---|
  | Welcome, how to play | 1–2 | Lilac |
  | Round 1 | 3 | Sunbeam |
  | Round 2 | 4–5 | Blossom Pink |
  | Round 3 | 6 | Matcha |
  | Speed Round | 7 | Sky Blue |
  | Jackpot | 8 | Peach |
  | Scoreboard, finale | 9–10 | Lilac |

- All text is **Night Indigo** (contrast ≥ 4.5:1 on every pastel and on Cream). No white text.
- Bunting flags rotate through Pink, Sunbeam, Sky, Matcha, Lilac and Peach, so **at least 4 palette colors** show on every slide.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Archivo Black | — (whitelist; re-set to Archivo Black if substituted) | 76–96 (Thank You 140) | Night Indigo |
| Body | Quicksand Bold | — | 26–28 (24 minimum inside narrow cards) | Night Indigo |
| Labels / chips / paddle names | Quicksand Bold | — | 24–28; eyebrow 22 UPPERCASE, letter spacing 200, in a tinted chip | Night Indigo |
| Question numbers / letter tiles | Archivo Black | — | 40–64 | Night Indigo |

Only these 2 families. Both are on the §D whitelist. Max 4 font sizes per slide.

### Recurring motifs

1. **Golden-hour sky and hills:** a soft gradient sky with 2–3 flat clouds, and **two or three layers of rolling hills** (Matcha and Hill Green) along the bottom of every slide.
2. **Blossom tree:** a pink cherry-blossom tree on one side of every slide (left or right alternating), partly cropped by the slide edge.
3. **Bunting flags:** a string of small triangle flags in six palette colors across the top edge of every slide.
4. **Gingham-trim cards:** Cream rounded cards (radius 28) with a 4 px Night Indigo outline and a 12 px **gingham top border** (white and the round color).
5. **Color paddles:** four rounded paddles on sticks in Pink, Yellow, Blue and Green. Used as the answer options on slides 4–5 and in small form elsewhere.
6. **Falling petals:** a few drifting blossom petals in two sizes around heroes and corners.
7. **Footer:** a gingham picnic-blanket strip (about 28 px high) along the very bottom, with the page number in a small blossom badge at the right.

**Transition:** Dissolve ("Larut"), applied to all pages. Fallback if missing: Slide ("Meluncur").

### Illustration style

- **One** flat, soft, rounded vector set: a picnic hill with diverse friends of all ages, a basket, a blanket, lemonade, kites, a cherry-blossom tree and cute animals.
- No photos, no pixel art, no realistic style.
- **One** consistent rounded icon set.

**Search terms for the asset scout** (Canva Elements, English keywords):
- `cherry blossom tree flat`, `sakura tree illustration`, `falling petals`, `rolling hills flat`, `sunset sky flat`, `fluffy clouds flat`
- `picnic blanket illustration`, `picnic basket flat`, `friends picnic flat illustration`, `family picnic hill`
- `lemonade pitcher`, `sandwich flat`, `kite illustration`, `bunting flags`, `gingham pattern`, `checkered tablecloth`
- `mount fuji flat`, `cute octopus flat`, `stopwatch flat`, `treasure chest gold coins`, `golden trophy flat`, `thinking kid lightbulb`
- `paddle sign hand`, `question mark balloon`, `host megaphone clipboard`, `cheering friends flat`
- Icons: `picnic basket icon`, `lemonade icon`, `kite icon`, `clock icon`, `trophy icon`, `lightbulb icon`, `megaphone icon`, `pencil icon`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (Golden Sky; title left, hero right; blossom tree on the right edge)
- Eyebrow chip (Lilac tint): `SPRING GAME NIGHT`
- Title at (120, 230), width 980, Archivo Black 96, 2 lines:
  > Blossom Hill / Picnic Trivia
- Pill (Blossom Pink):
  > Three rounds. One jackpot.
- Presenter line (on a Cream chip):
  > Presented by [Your Name] · [Organization]
- A row of three tinted circles (Sunbeam / Sky / Matcha) with icons: picnic basket, lemonade, kite.
- Hero, right (~800): a hill-top picnic scene under a cherry-blossom tree: a diverse group of friends on a gingham blanket with a basket, lemonade and a trophy.
- Decor: bunting flags across the top, soft clouds, falling petals, rolling hills at the bottom.

**Slide 2 — How to Play** (hero left, 3 stacked round cards right, scoring chips bottom)
- Eyebrow chip (Lilac tint): `HOW TO PLAY`
- Title: `How to Play`
- Hero, left (~520): a friendly host with a megaphone and clipboard standing beside a picnic basket.
- Three gingham-trim cards, stacked on the right, each with an icon and a header:
  - `Round 1 · Quick Answer` (Sunbeam) — Listen, write your answer on a slip, and hand it in. 1 point each.
  - `Round 2 · Pick a Paddle` (Blossom Pink) — Four answers, four colors. Hold up your team's paddle. 2 points each.
  - `Round 3 · Fill the Blanks` (Matcha) — Guess the missing letters to finish the word. 3 points each.
- Four paddle-colored pills in a row at the bottom (Pink / Yellow / Blue / Green), with a small paddle icon each:
  - `Speed Round: 1 point each`
  - `Jackpot: bet 1–5 points`
  - `Play in teams of 2–4`
  - `Best total wins`
- Decor: bunting, petals, hills, blossom tree on the left edge.

**Slide 3 — Round 1: Quick Answer** (2 × 2 question grid left, hero right)
- Eyebrow chip (Sunbeam tint): `ROUND 1 · 1 POINT EACH`
- Title: `Quick Answer`
- Four gingham-trim question cards in a 2 × 2 grid, each with a number badge (Sunbeam / Pink / Sky / Matcha) in Archivo Black:
  - `1` What do we call a baby kangaroo?
  - `2` Which is the largest planet in our solar system?
  - `3` How many legs does a honeybee have?
  - `4` Which ocean is the largest on Earth?
- Hint pill (Lilac tint, pencil icon) under the grid:
  > Write it down. No shouting out answers!
- Hero, right (~480): a curious kid with a big lightbulb and a magnifying glass on a blanket.
- Decor: bunting, petals, hills, blossom tree on the right edge.

### Builder B

**Slide 4 — Round 2: Pick a Paddle** (question card top center, 4 paddle tiles in a row, hero bottom)
- Eyebrow chip (Blossom Pink tint): `ROUND 2 · 2 POINTS EACH`
- Title (centered): `Pick a Paddle`
- Question card (centered, ~1500 wide, Archivo Black number badge `5`):
  > What is the capital city of Japan?
- Four tall paddle tiles in a row (each ~340 wide), each with a color name chip and the answer:
  - `PINK` — Kyoto
  - `YELLOW` — Osaka
  - `BLUE` — Tokyo
  - `GREEN` — Sapporo
- Hero, bottom (~1000): friends on the hill holding up colored paddles, with a flat snow-capped mountain and blossoms behind them.
- Decor: bunting, petals, two cloud layers, hills.

**Slide 5 — Round 2: Pick a Paddle, Part 2** (hero left, question and 4 answer pills right)
- Eyebrow chip (Blossom Pink tint): `ROUND 2 · 2 POINTS EACH`
- Title: `Pick a Paddle, Part 2`
- Hero, left (~560): a cute flat octopus with a friendly face waving, with bubbles.
- Question card (right, Archivo Black number badge `6`):
  > How many hearts does an octopus have?
- Four stacked answer pills (each with a small paddle icon in its color):
  - `PINK` — Two
  - `YELLOW` — Three
  - `BLUE` — Four
  - `GREEN` — Eight
- Decor: bunting, bubbles, petals, hills, blossom tree on the right edge.

**Slide 6 — Round 3: Fill the Blanks** (three word rows left, hero right)
- Eyebrow chip (Matcha tint): `ROUND 3 · 3 POINTS EACH`
- Title: `Fill the Blanks`
- Three gingham-trim word rows. Each row has a clue pill (Peach, Sky or Lilac) above a row of letter tiles (Archivo Black 64; given letters on Cream tiles, blanks as dashed Blossom Pink tiles):
  - Clue: `A sour-sweet picnic drink` — `L _ M _ N A D E`
  - Clue: `What a cherry tree grows in spring` — `B L _ S S _ M`
  - Clue: `It carries your picnic food` — `B A _ K _ T`
- Instruction chip (Sunbeam tint):
  > Each team writes the full word.
- Hero, right (~500): a big picnic basket packed with sandwiches, fruit and a lemonade bottle.
- Decor: bunting, petals, hills, blossom tree on the left edge.

### Builder C

**Slide 7 — Speed Round** (3 + 2 card grid, stopwatch hero in the sixth cell)
- Eyebrow chip (Sky tint): `SPEED ROUND · 1 POINT EACH`
- Title: `True or False?`
- Five gingham-trim statement cards (three on the top row, two on the bottom row), each with a number badge (Pink / Sunbeam / Matcha / Lilac / Peach) and two small paddle-style pills, `TRUE` and `FALSE`:
  - `1` Honey can last for years without spoiling.
  - `2` Sound travels faster than light.
  - `3` A group of crows is called a murder.
  - `4` Bananas grow on trees.
  - `5` The Great Wall of China can be seen from the Moon with the naked eye.
- Rule chip (Sky tint, clock icon):
  > Stand up for TRUE. Stay seated for FALSE.
- Hero, in the sixth cell (bottom right, ~500): a big flat stopwatch with small lightning sparkles.
- Decor: bunting, petals, hills, blossom tree on the right edge.

**Slide 8 — Picnic Jackpot** (center hero, bet-rules card left, question card right)
- Eyebrow chip (Peach tint): `FINAL ROUND`
- Title (centered): `Picnic Jackpot`
- Category chip (Lilac tint, centered under the title):
  > CATEGORY: AMAZING ANIMALS
- Left card `How to bet` (Peach gingham), with number badges:
  1. Choose your bet: 1 to 5 points.
  2. Write your bet and your answer on a slip.
  3. Right? Win your bet. Wrong? Lose it.
- Right card `The Jackpot Question` (Sunbeam gingham):
  > Which is the only mammal that can truly fly?
  Apply a single **Muncul (appear) animation on click** to this card only, so the host can collect bets first.
- Hero, center (~520): a treasure basket overflowing with gold coins and blossoms, with sparkles.
- Decor: bunting, petals, hills, blossom tree on the left edge.

**Slide 9 — Scoreboard** (table left, trophy right)
- Eyebrow chip (Lilac tint): `SCOREBOARD`
- Title: `Who's Winning?`
- Score table on a big Cream card with a gingham top border (plain shapes, ~1250 wide). Header row (Lilac cells): `Team` · `R1` · `R2` · `R3` · `Speed` · `Jackpot` · `Total`. A `Max` row (Cream cells): `Max` · `4` · `4` · `9` · `5` · `5` · `27`. Then four team rows with empty fill-in cells, each team name in its paddle color:
  - `Pink Team` (Blossom Pink)
  - `Yellow Team` (Sunbeam)
  - `Blue Team` (Sky Blue)
  - `Green Team` (Matcha)
- Footnote chip (Peach tint):
  > Add up the points after every round.
- Hero, right (~480): a golden trophy with a ribbon and a few blossom petals.
- Decor: bunting, petals, hills, blossom tree on the right edge.

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Archivo Black 140, centered, Night Indigo.
- Subtitle:
  > Thanks for playing — see you at the next picnic.
- Winner banner (Sunbeam, trophy icon):
  > And the winning team is… ____________
- Three contact pills (Blossom Pink / Sky Blue / Matcha), each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): the whole group cheering on the hill under the blossom tree, with a trophy, a basket and a kite.
- Decor: bunting, many falling petals, kites, hills.

## 4. Speaker notes

- Slide 2:
  > Hand out slips of paper and pens. Give each team a Pink, Yellow, Blue or Green paddle (colored paper on a stick works). Total points available: 27.
- Slide 3, add:
  > Answers. Q1: A joey. Q2: Jupiter. Q3: Six. Q4: The Pacific Ocean.
- Slide 4, add:
  > Answer: Tokyo (Blue paddle). Fun fact: Kyoto was the old imperial capital of Japan.
- Slide 5, add:
  > Answer: Three (Yellow paddle). Two hearts pump blood to the gills and one pumps it to the rest of the body.
- Slide 6, add:
  > Answers: LEMONADE (missing E and O), BLOSSOM (missing O and O), BASKET (missing S and E).
- Slide 7, add:
  > Answers. 1: True. 2: False (light is far faster). 3: True. 4: False (the banana is a giant herb, not a tree). 5: False (it can't be seen from the Moon with the naked eye).
- Slide 8, add:
  > Read the category, collect bets and answers on slips, then click to show the question. Answer: A bat.
- Slide 9, add:
  > Tally the points together. Maximums: Round 1 is 4, Round 2 is 4, Round 3 is 9, Speed Round is 5, Jackpot up to 5. Total 27.
- Slides 3–8:
  > Check the answers once more before you host, and swap in questions that fit your audience.

## 5. Deck-specific QA

- [ ] 10 pages in order; Dissolve ("Larut") on all pages (or the Slide fallback, reported).
- [ ] Every slide has the golden-hour gradient, bunting flags, rolling hills, a blossom tree and the gingham footer strip.
- [ ] Cards have the gingham top border; the four paddles are Pink, Yellow, Blue and Green.
- [ ] Only Archivo Black and Quicksand. All text is Night Indigo; contrast ≥ 4.5:1.
- [ ] At least 4 palette colors visible on every slide.
- [ ] Questions and word puzzles match §3 word for word. **No answers appear on any slide**; all answers are in the speaker notes.
- [ ] The slide 8 question card has a single on-click appear animation; no other animations beyond the limit of 3 per slide.
- [ ] No pixel art, no checker backgrounds, no isometric toys, no A/B/C/D letters, no photos, no logos.
- [ ] `[Your Name] · [Organization]` on slide 1; the three contact pills on slide 10.
