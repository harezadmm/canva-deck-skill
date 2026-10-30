# Prompt set9-8 — "Table Tournament Night: Roll, Stack and Win" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set9-newyear-business-gamenight\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `table-tournament`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Table Tournament Night: Roll, Stack and Win"**. It is a ready-to-run **party-game tournament playbook** for friends, family or a club.

- Four original mini-games, each with real, playable rules that use everyday items (a die, a deck of cards, stacking blocks, paper and pens).
- Teams collect tournament points in each game, then the top four teams meet in a final bracket.
- Flow:
  1. cover
  2. tonight's menu and scoring
  3. house rules
  4. Game 1 — Dice Duel
  5. Game 2 — Card Climb
  6. Game 3 — Tower Stack
  7. Game 4 — Party Bingo (a "find someone who" card)
  8. the Cup Bracket
  9. scoreboard and awards
  10. thank you
- All game names are **original**. **No** real brand-name games, logos or trademarked characters.

**Reference (direction only):** https://www.canva.com/templates/EAHV56kjR0U/ ("Colorful Bright Cute Illustrated Handdrawn Fun Playful Boardgames Game Night Presentation").

- **Borrow the idea:**
  1. a **warm, hand-drawn board-game mood**: dice, cards, blocks and bingo as the stars;
  2. rich, earthy solid backgrounds (forest green, brown, red);
  3. cream notebook-paper cards holding the text;
  4. a "what's in store" menu, a bingo slide, a stacking-game slide and a "thanks" slide.
- **Build from scratch.** Do **not** click "Use this template" and do **not** copy any layout, illustration or text from the reference. Do not copy its boardgame-title frame, its host-character intro or its money-and-chips card poster.

**Must also differ from the earlier game-night decks** (the main agent should check these files before building):
- `set6-christmas-gamenight-newyear\prompt-set6-2-game-night-host.md`
- `set7-christmas-gamenight\prompt-set7-4-game-night-pixel-quest.md`
- `set7-christmas-gamenight\prompt-set7-5-game-night-guess-the-idiom.md`
- Earlier decks named inside those files: "Game Night: The Ultimate Quiz Party" and "Game Night: Family Trivia Showdown" (board-game tabletop).
- The other set9 game-night decks (set9-7, set9-9, set9-10).

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Earthy forest / brown / red backgrounds | A **"Scrapbook Tournament"** concept: **solid earthy backgrounds with a faint grid-paper texture**, and every content block is a **cream notebook-paper card** (spiral holes on the top edge, a slight tilt, a washi-tape strip on one corner). |
| Hand-drawn game objects | Heroes are **scrapbook collages** of dice, cards, block towers and bingo balls on paper and tape. **No** table-top scene, **no** winding tile path, **no** pawns (Family Trivia), **no** fox host. |
| Chunky titles | **Chewy** titles in Cream, with a Mustard hand-drawn underline squiggle. **No** Titan One, **no** Luckiest Guy die-cut sticker titles (set6-2). |
| One game per slide | Each game gets a **game color** and a **hanging points tag**, and a **tournament scoring system** (3 / 2 / 1) plus a **bracket**. The deck is rules-driven, not a quiz. |
| Confetti squiggles | **Squiggle doodles** (spirals, zigzags, stars) in 6 colors, plus **paper clips**, **staples** and **washi tape**. **No** playing-card suit confetti (set6-2), **no** stitched banners (Family Trivia). |
| — | **No** pixel art or retro arcade (set7-4, set7-5). **No** night quiz stage, Midnight or black backgrounds, Bungee or A/B/C/D buttons (Quiz Party). **No** sticker-bomb die-cut, spinner wheel or ticket stubs (set6-2). **No** music / vinyl / 70s identity (set9-7). **No** real brands, logos or characters. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Forest | `#2E6B4B` | Background; white or Cream text allowed |
| Cocoa | `#5A2F1E` | Background; white or Cream text allowed |
| Brick | `#C23B33` | Background and accent; white or Cream text allowed |
| Cream Paper | `#FFF8E8` | Notebook cards, titles on dark backgrounds |
| Ink Brown | `#2B1810` | Text on paper cards |
| Mustard | `#F2B63D` | Game 1, highlights, underline squiggles; Ink text on it |
| Disco Pink | `#F58CB0` | Game 2; Ink text on it |
| Sky | `#8ED0EA` | Game 3; Ink text on it |
| Lime | `#9BD35A` | Game 4; Ink text on it |
| Peach | `#FFA36B` | Accent; Ink text on it |

**Backgrounds** rotate in this order, slide 1 → 10: Forest → Cocoa → Brick → Forest → Cocoa → Brick → Forest → Cocoa → Brick → Forest. Each has a faint grid-paper texture (lines about 6 % lighter, 48 px apart). No two consecutive slides share a background.

**Color rules:**
- Each game slide (4–7) uses its game color for the eyebrow chip, washi tape, the hanging points tag, step-number circles and the card header strip:

  | Slide | Game | Color |
  |---|---|---|
  | 4 | Dice Duel | Mustard |
  | 5 | Card Climb | Disco Pink |
  | 6 | Tower Stack | Sky |
  | 7 | Party Bingo | Lime |
  | 8 | Cup Bracket | Peach |
  | 9 | Scoreboard | Mustard and Lime |

- Slides 1–3, 8–10 rotate all five game colors across tape, tags and doodles, so **at least 4 accents** are visible on every slide.
- Titles are Cream on the dark backgrounds (contrast ≥ 4.5:1). Card text is Ink Brown on Cream Paper. Chips and tags use Ink Brown text on their pastel fills.
- Never put Cream text on a pastel, and never put pastel text on a dark background.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Chewy | — (whitelist; re-set to Chewy if substituted) | 76–96 (cover 110, Thank You 140), no pill or highlight behind it | Cream Paper |
| Body | Poppins Medium | — | 26–28 | Ink Brown on paper |
| Card headers / tags / labels | Poppins Bold | — | 24–26 | Ink Brown |
| Eyebrow | Poppins Bold | — | 22, UPPERCASE, letter spacing 200, inside a small game-color chip | Ink Brown |

Only these 2 families. Both are on the §D whitelist. Do **not** use Titan One, Luckiest Guy, Lilita One, Bungee or pixel fonts in this deck.

### Recurring motifs

1. **Notebook-paper card:** cream rounded card (radius 20) with a row of 8 spiral holes along the top edge, 3 px Ink Brown outline, a faint ruled-line texture and a tilt between −2° and 2°. A soft shadow underneath. Holds every text block.
2. **Washi tape:** a semi-transparent tape strip (stripes, dots or plain) in a game color, stuck diagonally across one corner of each card.
3. **Hanging points tag:** a luggage-style tag with a hole and a string, in the game color, hanging from the top-right corner of game slides (4–7). The tag text is Poppins Bold.
4. **Squiggle doodles:** hand-drawn spirals, zigzags, stars and little dots in 6 palette colors scattered around heroes and corners. Plus 1–2 paper clips or staples per slide.
5. **Die footer:** a small white rounded-square "die" holding the page number, bottom-right, with a pip dot in the game color.
6. **Mustard squiggle underline:** a short hand-drawn wavy line under every title.

**Transition:** Stack ("Tumpuk"), applied to all pages. Fallback: "Meluncur", then "Larut".

### Illustration style

- One flat, hand-drawn, chunky, friendly set with warm colors and visible paper-craft feel (thick rounded shapes, soft shading, a slightly wobbly outline).
- Game objects: dice (six-sided, with pips), a fan of playing cards (generic, no brand faces), stacking wooden blocks and a tower, bingo balls and a bingo card, a trophy, a stopwatch, a clipboard, paper and pens.
- Characters: diverse friends and families of all ages laughing, rolling dice, pulling blocks, cheering. A small cheerful "host" with a whistle may appear.
- Icons: one consistent set (bold rounded line icons filled with palette colors).
- **No** photos, **no** real logos or brands, **no** real people, **no** card-brand faces.

**Search terms for the asset scout** (Canva Elements, English keywords):
- `dice illustration hand drawn`, `rolling dice flat`, `playing cards fan illustration`, `wooden block tower illustration`, `stacking blocks game`, `bingo balls illustration`, `bingo card illustration`
- `board game night illustration`, `friends playing games flat`, `family game night illustration`, `people laughing around table flat`, `cheering people flat`
- `trophy illustration cute`, `podium flat`, `stopwatch illustration`, `clipboard illustration`, `pencil and paper doodle`
- `washi tape`, `paper clip illustration`, `staple illustration`, `notebook paper spiral`, `luggage tag illustration`, `price tag illustration`
- `squiggle doodle`, `hand drawn star doodle`, `spiral doodle`, `zigzag doodle`, `confetti squiggles`
- Icons: `dice icon`, `cards icon`, `blocks icon`, `bingo icon`, `trophy icon`, `clock icon`, `phone icon`, `mail icon`, `web icon`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (title left, hero right; background Forest)
- Eyebrow chip (Mustard fill, Ink text): `GAME NIGHT PLAYBOOK`
- Title at (110, 220), width 860, Chewy 110, 3 lines, Cream, with a Mustard squiggle underline under the last line:
  > Table / Tournament / Night
- Pill (Brick fill, Cream text, Poppins Bold 32):
  > Roll. Stack. Win.
- Presenter line (Poppins Medium 26, Cream):
  > Hosted by [Your Name] · [Organization]
- A row of three tinted circles (Mustard / Pink / Sky) with icons: dice, cards, blocks.
- Hero, right (~780): a scrapbook collage on a tilted notebook-paper sheet: a stack of dice, a fan of playing cards, a small block tower and a few bingo balls, held with washi tape and a paper clip, with two laughing friends peeking from behind.
- Decor: squiggle doodles in the top-left corner, washi tape on the hero sheet, a half-hidden paper clip at the bottom.
- Footer: die with `1`.

**Slide 2 — Tonight's Menu** (row of 4 cards, banner and hero below; background Cocoa)
- Eyebrow chip (Pink fill, Ink text): `TONIGHT'S MENU`
- Title (centered): `Four Games, One Champion`
- Mustard squiggle underline under the title.
- Four notebook cards in one row, each with a game-color header strip holding `GAME 1`–`GAME 4`, a hero icon (dice, cards, blocks, bingo ball), a name and a one-line tagline:
  - `GAME 1` Mustard — `Dice Duel` — Push your luck and bank your points.
  - `GAME 2` Pink — `Card Climb` — Guess higher or lower up the ladder.
  - `GAME 3` Sky — `Tower Stack` — Pull a block. Keep the tower standing.
  - `GAME 4` Lime — `Party Bingo` — Mingle and find someone who…
- Scoring banner, bottom left (Mustard fill, Ink text, trophy icon):
  > Tournament points per game: 1st place = 3 · 2nd place = 2 · everyone else = 1
- Final chip, under the banner (Cream card, Ink text):
  > After four games, the top four teams play the Cup Bracket.
- Hero, bottom right (~600 wide): a spread of dice, cards and a bingo ball on paper with a stopwatch, a cheering friend and doodles.
- Footer: die with `2`.

**Slide 3 — House Rules** (hero left, 5 sticky notes right; background Brick)
- Eyebrow chip (Sky fill, Ink text): `HOUSE RULES`
- Title (right column, x 760): `Play Fair, Have Fun`
- Mustard squiggle underline under the title.
- Hero, left (~520): a group of diverse friends high-fiving around a small table with dice and cards, in the scrapbook style.
- Five sticky-note cards (staggered, slightly tilted, each with a number circle and a tiny icon) in Mustard / Pink / Sky / Lime / Peach:
  1. `Cheer for every team, not just yours.`
  2. `The host's call is final.`
  3. `Keep it quick: 30 seconds per turn.`
  4. `Phones down, eyes up, snacks welcome.`
  5. `Winning is fun. Laughing is better.`
- Needs-chip, bottom (Cream, Ink text, clipboard icon):
  > You will need: a die, a deck of cards, stacking blocks, paper and pens
- Decor: washi tape on each note, squiggles, a paper clip on the top-left.
- Footer: die with `3`.

### Builder B

**Slide 4 — Game 1: Dice Duel** (rules card left, hero right; background Forest; theme Mustard)
- Eyebrow chip (Mustard): `GAME 1 · PUSH YOUR LUCK`
- Title: `Dice Duel`
- Mustard squiggle underline under the title.
- Hanging points tag (Mustard), top right:
  > Win = 3 points
- Notebook card `How to play` (Mustard header strip, spiral holes) with four numbered steps (Mustard circles):
  1. `Teams take turns rolling one die as many times as they like.`
  2. `Add up your rolls. Say "Bank!" to lock in your points.`
  3. `Roll a 1 and you lose that turn's points. Your turn ends.`
  4. `The first team to bank 30 points wins.`
- Example bubble (Cream, Ink text, lightbulb icon):
  > Example: roll 4, 6, 3 and bank = 13 points. Roll 4, 6, 1 = zero.
- Hero, right (~540): a huge hand-drawn die mid-roll with smaller dice, a pencil and a score pad, a friend cheering and a friend covering their eyes.
- Decor: washi tape (Mustard) on the card, squiggles, one paper clip.
- Footer: die with `4`.

**Slide 5 — Game 2: Card Climb** (ladder hero across the top, 2 × 2 steps below; background Cocoa; theme Pink)
- Eyebrow chip (Pink): `GAME 2 · HIGHER OR LOWER`
- Title: `Card Climb`
- Mustard squiggle underline under the title.
- Hanging points tag (Pink), top right:
  > Win = 3 points
- Hero, top (~1100 wide, y 150–500): a row of six playing cards rising like stair steps (the first face up, the rest face down), with a small friend climbing the steps, in the scrapbook style.
- Four step cards in a 2 × 2 grid (Pink header strips, numbered circles):
  1. `Shuffle a deck and lay out a ladder of six cards, face down.`
  2. `Flip the first card. Guess if the next card is higher or lower. Ace is high.`
  3. `Right guess: flip it and keep climbing. Wrong guess or a tie: your turn ends.`
  4. `Each team gets two turns. The team that climbs the most cards wins.`
- Tie chip (Cream, Ink text):
  > A tie? One sudden-death flip decides.
- Decor: washi tape (Pink), squiggles, a paper clip.
- Footer: die with `5`.

**Slide 6 — Game 3: Tower Stack** (tower hero center, 2 step cards each side; background Brick; theme Sky)
- Eyebrow chip (Sky): `GAME 3 · STEADY HANDS`
- Title (centered): `Tower Stack`
- Mustard squiggle underline under the title.
- Hanging points tag (Sky), top right:
  > Last team standing = 3 points
- Hero, center (~520 tall): a tall wooden block tower, slightly wobbly, with one block half-pulled and a hand reaching in, a stopwatch beside it and nervous friends watching.
- Four step cards, two on the left and two on the right (Sky header strips, numbered circles), with short connector lines to the tower:
  1. `Build the tower: stack the blocks three across, level by level.`
  2. `On your turn, pull one block with one hand from any level below the top.`
  3. `Place it on top. You have 30 seconds.`
  4. `If the tower falls on your turn, your team is out. The last team standing wins.`
- Decor: washi tape (Sky), squiggles, a paper clip.
- Footer: die with `6`.

### Builder C

**Slide 7 — Game 4: Party Bingo** (bingo card left, rules right; background Forest; theme Lime)
- Eyebrow chip (Lime): `GAME 4 · MINGLE`
- Title: `Party Bingo`
- Mustard squiggle underline under the title.
- Hanging points tag (Lime), top right:
  > First to Bingo = 3 points
- Bingo card, left (~1000 wide): a big notebook-paper card headed `Find someone who…` with a 4 × 4 grid of 16 squares, tinted in rotating Mustard / Pink / Sky / Lime / Peach, each with a short prompt (Poppins Medium 22–24):
  - Has a pet
  - Plays an instrument
  - Loves spicy food
  - Can whistle
  - Speaks two languages
  - Has a birthday this month
  - Is wearing green
  - Has traveled by plane
  - Likes pineapple on pizza
  - Can juggle
  - Has a sibling
  - Plays chess
  - Loves karaoke
  - Is left-handed
  - Has a nickname
  - Reads comics
- Rules card, right (Lime header strip, spiral holes):
  - `Walk around and ask a question. If the answer is "yes," that person signs the square.`
  - `One signature per person.`
  - `First to complete a row, column or diagonal shouts "Bingo!"`
- Hero, right bottom (~480): a cluster of bingo balls, a marker pen and a cheering friend shouting "Bingo!" in a speech bubble.
- Decor: washi tape (Lime), squiggles, a paper clip.
- Footer: die with `7`.

**Slide 8 — The Cup Bracket** (bracket center, rules chip and hero bottom; background Cocoa; theme Peach)
- Eyebrow chip (Peach): `THE FINAL FACE-OFF`
- Title (centered): `The Cup Bracket`
- Mustard squiggle underline under the title.
- Bracket diagram, center (about 1500 wide), built from paper cards joined by Ink Brown lines:
  - Left, top card pair: `SEMI-FINAL 1` — `#1 seed` vs `#4 seed`, each with a line `Team name: ______`.
  - Left, bottom card pair: `SEMI-FINAL 2` — `#2 seed` vs `#3 seed`, each with a line `Team name: ______`.
  - Right: a big `FINAL` paper card with two empty slots, and beside it a trophy with the label `CHAMPION`.
  - Pair cards use rotating Peach / Mustard / Sky / Pink headers; the final card uses a Mustard header.
- Rules chip, under the bracket (Mustard fill, Ink text, dice icon):
  > Seed the top four teams by tournament points. Every match is a quick Dice Duel to 15 points.
- Hero, bottom right (~500): two big dice facing each other like a face-off, with lightning doodles and two friends rooting on either side.
- Decor: washi tape, squiggles, one paper clip.
- Footer: die with `8`.

**Slide 9 — Scoreboard and Awards** (table left, awards and hero right; background Brick; theme Mustard and Lime)
- Eyebrow chip (Mustard): `SCOREBOARD`
- Title: `Points and Prizes`
- Mustard squiggle underline under the title.
- Scoreboard, left (~1100 wide): a notebook-paper card with a ruled table. Column header pills (Mustard / Pink / Sky / Lime / Peach): `Team` · `Dice Duel` · `Card Climb` · `Tower Stack` · `Party Bingo` · `Total`. Five rows with labels `Team 1` … `Team 5` and empty cells to fill in (a dash `—` in each).
- Reminder chip under the table (Cream, Ink text):
  > 1st = 3 points · 2nd = 2 points · everyone else = 1 point
- Three award cards, right (ribbon-shaped, tilted, each with an icon):
  - `Lucky Roller` — Best Dice Duel run (Mustard)
  - `Steady Hands` — Last tower standing (Sky)
  - `Best Sport` — Cheered the loudest (Lime)
- Hero, right (~480): a shiny cartoon trophy cup with confetti and a podium (1-2-3).
- Decor: washi tape, squiggles, paper clip.
- Footer: die with `9`.

**Slide 10 — Thank You** (centered, hero along the bottom; background Forest)
- Title: `Thank You!` in Chewy 140, Cream, centered, with a Mustard squiggle underline.
- Subtitle (Poppins Medium 30, Cream, centered):
  > Thanks for playing! Same table, same time next week?
- Prize chip (Mustard fill, Ink text, trophy icon):
  > The champions take home the Golden Dice!
- Three contact pills (Pink / Sky / Lime, Ink text), each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): diverse friends and a family cheering around a small table covered in dice, cards, blocks and bingo balls, with confetti squiggles flying.
- Decor: squiggle confetti in both top corners, washi tape strips, a paper clip.
- Footer: die with `10`.

## 4. Speaker notes

- Slide 1:
  > Welcome everyone. Explain that teams will play four short games, collect tournament points, and the top four teams will meet in a final bracket. Gather a die, a deck of cards, stacking blocks, paper and pens before you start.
- Slide 2:
  > Explain the scoring: 1st place = 3 tournament points, 2nd = 2, everyone else = 1. Write the points on the scoreboard (slide 9) after every game.
- Slide 3:
  > Read the five rules aloud. Pick one person as the timer and one as the scorekeeper.
- Slide 4:
  > Dice Duel: a quick game. Pass one die between teams. Remind players that rolling a 1 wipes out the points of that turn only; banked points are safe. For a shorter game, play to 20.
- Slide 5:
  > Card Climb: use a standard deck without jokers. Count each correct guess as one step climbed. Let teams shuffle for each other. Ace is high; the lowest card is 2.
- Slide 6:
  > Tower Stack: use any stacking blocks. Ask players to keep their other hand behind their back. Play on a stable, flat table. Stop the game if someone feels unsafe.
- Slide 7:
  > Party Bingo: hand out a copy of the card (print it, or let players copy it onto paper). Feel free to swap prompts to suit your group. Stop after 10 minutes if nobody has a Bingo.
- Slide 8:
  > Seed the teams from the scoreboard. Break ties with a single Dice Duel roll-off. Matches are Dice Duel to 15 points.
- Slide 9:
  > Add up each team's tournament points from the games. Hand out the three fun awards, then crown the champion from the bracket.
- Slide 10:
  > Thank everyone, hand over the prize, and invite the group to host the next tournament. Replace the contact details with your own.

## 5. Deck-specific QA

- [ ] 10 slides in order; Stack ("Tumpuk") on all pages (or the stated fallback).
- [ ] Every text block sits on a cream notebook-paper card, chip, tag or pill; no bare paragraph on the background.
- [ ] Every slide has washi tape, squiggle doodles, a paper clip or staple, the Mustard squiggle underline under the title, and the die footer.
- [ ] Game slides (4–7) each have the hanging points tag in the game color.
- [ ] Slide backgrounds rotate Forest → Cocoa → Brick; no two consecutive slides share one; no black or midnight backgrounds.
- [ ] Rules and prompts match §3 word for word (including all 16 bingo prompts and the dice example math: 4 + 6 + 3 = 13).
- [ ] At least 4 accent colors visible per slide.
- [ ] Only Chewy and Poppins.
- [ ] Placeholders `[Your Name] · [Organization]` on the cover; contact pills on slide 10.
- [ ] No photos, no real brand-name games, logos or characters, no card-brand faces.
- [ ] Nothing from the earlier decks' identities: pixel art, sticker-bomb stickers, suit confetti, spinner wheel, ticket stubs, night stage, board tabletop, tile path, pawns, fox host, stitched banners, A/B/C/D buttons, vinyl and 70s music (set9-7).
- [ ] Hero on every slide is at least 480 px; every slide has 3–6 supporting items and at least 2 decor layers.
