# Prompt 5/5: "Guess the Idiom! A Pixel Picture-Puzzle Game Night" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set7-christmas-gamenight\canva-shared-pipeline.md`.

That file holds:
- §A: hard rules
- §B: colorful brief and richness checklist
- §C: pipeline, builder brief, QA, and report
- §D: lessons learned from earlier runs

Deck slug: `game-night-guess-the-idiom`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Guess the Idiom! A Pixel Picture-Puzzle Game Night"**. It is a playable game deck:
- teams look at pixel picture clues and guess the English idiom and its meaning
- the deck has 6 puzzle slides and a lightning round
- the answer key is at the end

It works for classrooms, English clubs, and family game nights.

**Reference (direction only):** https://www.canva.com/templates/EAHBo9amLyI/ ("Black Red Pixel Guess the Meaning Game Presentation").

- **Borrow the idea:**
  - a "guess the meaning" game mechanic
  - pixel-art picture clues
  - a bold pixel display font
  - big question-mark moments
- **Build from scratch.** Do not copy any layout, illustration, or text from the reference.

**Must also differ from:**
- The earlier game-night decks in this project:
  - "Game Night: The Ultimate Quiz Party": night-time quiz show, Midnight background, A/B/C/D answer buttons
  - "Game Night: Family Trivia Showdown": board-game tabletop, tile path, pawns
  - "Host the Ultimate Game Night": sticker-bomb, die-cut stickers, ticket stubs
- The sibling deck in this set, set7-4 "Game Night Quest": daytime pixel world map, HUD hearts, XP bar, sky and meadow backgrounds.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Guess-the-meaning game | Answers are **not** on the puzzle slides. Teams write them down, and everything is revealed on an **Answer Key** slide at the end |
| Pixel clues | Clues sit inside a **retro handheld-console screen frame** (generic, no brand) with a colorful pixel "cartridge label" for each puzzle |
| Black and red | A **light "Pixel Candy Arcade" look**: lilac cream background with a faint pixel grid, and **6 bright candy colors**. Red appears only as a tiny accent |
| Big question marks | Pixel **speech bubbles** with "?" in palette colors |
| — | **No** black or dark backgrounds, **no** A/B/C/D answer buttons (lightning tiles are numbered ⚡1–⚡4), **no** world map, HUD hearts or XP bar (those belong to set7-4), **no** brand consoles, logos or famous game characters |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Lilac Cream | `#F4EEFF` | Main background |
| Pixel Grid | `#E3D8FF` | Faint 24 px grid lines on the background |
| Ink | `#231A3D` | Text, pixel outlines |
| Magenta Pop | `#FF3EA5` | Titles, Puzzle 5 |
| Cyan Byte | `#18C6E3` | Puzzle 1 |
| Lime Bit | `#7DDE45` | Puzzle 2 |
| Tangerine Bit | `#FF8B2C` | Puzzle 3 |
| Violet Bit | `#6C4BFF` | Puzzle 4 |
| Lemon Bit | `#FFE14D` | Puzzle 6, highlights, coins |

**Puzzle colors** (cartridge label, console frame, hint cards):

| Puzzle | Color |
|---|---|
| 1 | Cyan Byte |
| 2 | Lime Bit |
| 3 | Tangerine Bit |
| 4 | Violet Bit |
| 5 | Magenta Pop |
| 6 | Lemon Bit |

Every slide has pixel sparkles, pixel "?" bubbles, and small pixel coins in 3+ palette colors.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Pixelify Sans Bold | Silkscreen → Lilita One | 70–84 | Magenta Pop with an Ink 4 px offset shadow |
| Body | Outfit Medium | Nunito | 26–28 | Ink |
| Labels | Outfit Bold | Nunito ExtraBold | 22 | UPPERCASE, letter spacing 150, puzzle color |

### Recurring motifs

1. **Console screen:** a rounded handheld-console shape in the puzzle color, with a light screen area (`#FFFFFF`) that holds the pixel clue icons. It has a D-pad and two buttons drawn as simple shapes, and no brand.
2. **Cartridge label:** a pixel tab reading `PUZZLE 01`–`PUZZLE 06` (or `LIGHTNING`) above the screen.
3. **Hint cards:** two small cards, `HINT 1` and `HINT 2`, each with a coin icon and its point cost.
4. **Points chips:** `No hint: 3 pts` · `1 hint: 2 pts` · `2 hints: 1 pt`.
5. **Answer line:** a dashed write-in strip reading `Your guess: ______________`.
6. **Footer:** a pixel heart and the page number in an 8-bit counter box.

**Transition:** Circle wipe ("Sapuan lingkaran"). If it is not available, use Dissolve ("Larut").

### Illustration style

- **One** pixel-art set (flat colors, 8-bit / 16-bit look):
  - diverse pixel people, with expressive faces
  - clue objects: cake slice, ice cube, hammer, bean can, rain cloud, thermometer, moon, calendar, pig with wings, airplane, cat, bag, coin, feet, bed and hay bale
- The asset scout searches terms like:
  - "pixel art cake"
  - "pixel ice cube"
  - "pixel cloud rain"
  - "pixel pig"
  - "pixel moon"
  - "pixel people"
  - "game console pixel"
  - "pixel question mark"
- Clue objects come from **one** pixel set wherever possible.

## 3. Slide-by-slide spec

### Builder A

**Slide 1: Cover**
- Eyebrow: `PIXEL PUZZLE GAME NIGHT`
- Title at (120, 220), width 960:
  > Guess the Idiom!
- Pill (Cyan Byte, Ink text):
  > Picture clues. Big laughs. Clever minds.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~860, right): diverse pixel friends huddled around a giant handheld console, with pixel "?" bubbles and floating clue icons (cake, ice cube, moon).
- Decor: pixel sparkles, coins.

**Slide 2: What's an Idiom?**
- Title: `What's an Idiom?`
- Statement card (Violet Bit tint):
  > An idiom is a phrase that means something different from its words. "It's raining cats and dogs" doesn't mean pets are falling from the sky — it means it's raining very hard!
- Two small cards:
  - `Why play?` — Learn everyday English while laughing together.
  - `Who can play?` — Kids, teens and grown-ups, in teams of 2–4.
- Hero (~480): a funny pixel scene of rain with pixel cats and dogs holding umbrellas.

**Slide 3: How to Play**
- Title: `How to Play`
- Four numbered steps on pixel number blocks (each a different color):
  1. Look at the picture clue on the screen.
  2. Talk with your team and guess the idiom.
  3. Need help? Use a hint, but it costs points.
  4. Write your answer and its meaning. We reveal them at the end!
- Points chips row: `No hint: 3 pts` · `1 hint: 2 pts` · `2 hints: 1 pt`
- Hero (~420): a pixel team writing answers on a whiteboard.

### Builder B

All puzzle slides share these parts: cartridge label, console screen with the clue icons, Hint 1 and Hint 2 cards, and the answer line. **Answers are not shown on the slide**; put them in the speaker notes only.

**Slide 4: Puzzle 01** (Cyan Byte), layout: console left, hints right
- Label `PUZZLE 01` · Title `What's the Idiom?`
- Clue on screen: a slice of cake + a smiling face giving a thumbs up.
- `HINT 1` — Something very easy is like eating this.
- `HINT 2` — It starts with "A piece of …"
- Speaker note: **Answer:** A piece of cake = something very easy.

**Slide 5: Puzzle 02** (Lime Bit), layout: console right, hints left
- Label `PUZZLE 02` · Title `What's the Idiom?`
- Clue on screen: an ice cube + a hammer + two people waving shyly.
- `HINT 1` — You do this when you meet new people.
- `HINT 2` — It starts with "Break the …"
- Speaker note: **Answer:** Break the ice = to start a conversation and help people relax.

**Slide 6: Puzzle 03** (Tangerine Bit), layout: console centered, hints below in a row
- Label `PUZZLE 03` · Title `What's the Idiom?`
- Clue on screen: a tipped-over can with beans spilling out + a "shh" face.
- `HINT 1` — It's about secrets.
- `HINT 2` — It starts with "Spill the …"
- Speaker note: **Answer:** Spill the beans = to tell a secret.

### Builder C

**Slide 7: Puzzle 04** (Violet Bit), layout: console left, tilted −4°, hints stacked right
- Label `PUZZLE 04` · Title `What's the Idiom?`
- Clue on screen: a person standing under a small rain cloud, holding a thermometer.
- `HINT 1` — It's how you feel when you're a little sick.
- `HINT 2` — It starts with "Under the …"
- Speaker note: **Answer:** Under the weather = feeling a little sick.

**Slide 8: Puzzle 05** (Magenta Pop), layout: console right, hints in speech bubbles from a pixel character on the left
- Label `PUZZLE 05` · Title `What's the Idiom?`
- Clue on screen: a big blue moon + a calendar.
- `HINT 1` — It's about something that happens very rarely.
- `HINT 2` — It ends with "… in a blue moon."
- Speaker note: **Answer:** Once in a blue moon = very rarely.

**Slide 9: Puzzle 06** (Lemon Bit), layout: console centered and large, hints as two coins on either side
- Label `PUZZLE 06` · Title `What's the Idiom?`
- Clue on screen: a pig with little wings + an airplane.
- `HINT 1` — People say it about things that will never happen.
- `HINT 2` — It starts with "When pigs …"
- Speaker note: **Answer:** When pigs fly = something that will never happen.

### Builder D

**Slide 10: Lightning Round**
- Label `LIGHTNING` · Title `Lightning Round!`
- Pill (Lemon Bit, Ink text):
  > 30 seconds per clue · 2 pts each · no hints!
- Four clue tiles in a 2 × 2 grid, each a mini console screen in a different color, numbered ⚡1–⚡4:
  - `⚡1` — a cat peeking out of a bag
  - `⚡2` — a pile of coins + an arm + a leg
  - `⚡3` — two shivering feet with snowflakes
  - `⚡4` — a bed + a hay bale
- Each tile shows only the pixel icons; the bullet text above is for the builder.
- Speaker notes: answers as on Slide 11.

**Slide 11: Answer Key**
- Title: `Answer Key`
- Ten answer rows in two columns (5 + 5). Each row has a colored number chip, the idiom in bold, and its meaning:
  1. **A piece of cake** — Something very easy.
  2. **Break the ice** — To start a conversation and help people relax.
  3. **Spill the beans** — To tell a secret.
  4. **Under the weather** — Feeling a little sick.
  5. **Once in a blue moon** — Very rarely.
  6. **When pigs fly** — Something that will never happen.
  7. ⚡1 **Let the cat out of the bag** — To reveal a secret by accident.
  8. ⚡2 **Cost an arm and a leg** — To be very expensive.
  9. ⚡3 **Get cold feet** — To feel nervous before something big.
  10. ⚡4 **Hit the hay** — To go to bed.
- Body text may be 22 here (the minimum) to fit.
- Decor: a small pixel trophy, sparkles.

**Slide 12: High Score!**
- Title centered, Pixelify Sans Bold 130, Magenta Pop with an Ink shadow:
  > High Score!
- Subtitle:
  > Thanks for playing — now use your new idioms all week!
- Three contact pills (Magenta / Cyan / Lime, Ink text):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): a pixel crowd of diverse friends celebrating, with confetti, coins and clue icons flying.

## 4. Speaker notes

- **Slides 4–10:** The answers listed in §3 go in each slide's notes. Read them aloud only after all teams have written their guesses.
- **Slide 3:** Tip for teachers: ask teams to use each idiom in a sentence for 1 bonus point.

## 5. Deck-specific QA

- [ ] No answers appear on slides 4–10, only in the speaker notes and on Slide 11.
- [ ] Each puzzle slide uses its own puzzle color, and slides 4–9 each use a different layout.
- [ ] Lilac Cream background with the faint pixel grid on all 12 slides; no dark backgrounds.
- [ ] No A/B/C/D buttons; no world map, HUD hearts or XP bar; no brand consoles or look-alike game characters.
- [ ] Clue icons clearly show the objects listed in §3.
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier game-night decks (§0).
