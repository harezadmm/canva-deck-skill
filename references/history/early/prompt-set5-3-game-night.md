# Prompt 3/5 — "Game Night: Family Trivia Showdown" (colorful)

> Copy everything below into a new task.
> Team: one **main agent**, one **asset scout**, and **four builder subagents**.

**FIRST:** read and follow every section of
`%USERPROFILE%\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\scratch-workspaces\dcdc6f97-14f9-43a0-812f-7b344eef061a\12aa8b61-941b-457d-8505-99fb0b2a7c89\scratch-2026-10-22-82e737\canva-shared-pipeline.md`.

That file holds:
- §A — hard rules
- §B — the colorful brief
- §C — the pipeline, builder brief, QA and report

Deck slug: `game-night-trivia`.

---

## 0. Goal

Build a playable 12-slide Canva quiz deck (1920 × 1080) called **"Game Night – Family Trivia Showdown"**.

**Reference (direction only):** https://www.canva.com/templates/EAGVsh1mGZg/ ("Hijau Ilustrasi Game Tema Alam").

- **Borrow the idea:**
  - the playful quiz flow: question slide, then answer slide
  - answer buttons
  - friendly illustrated characters
  - big chunky titles
- **Build from scratch.**
- **Not a repeat:** this deck must also look different from the earlier "Game Night – Quiz Deck" prompt. That one used a midnight/neon game-show look, Bungee, and questions about Mars, chess and PUZZLE.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Question → answer quiz flow | The whole deck looks like a **colorful board game**: a sky-blue tabletop, a winding path of colored tiles, dice, pawns and cards |
| Chunky friendly titles | Titles sit on **game-card banners** (rounded, with dotted stitching), not on a notched green clipboard frame |
| Illustrated characters | Characters are **game pieces and animal mascots** (pawns, dice buddies, a fox host). **No** cartoon kids on swings or with flowers, **no** green jungle leaves |
| Answer buttons | Buttons are **chunky 3D-style game tiles** in 4 colors with a letter badge |
| — | Not midnight/neon. Not the earlier game-night deck's look |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Sky Table | `#BEE7FF` | Background |
| Ink | `#1E2A4A` | Text, outlines |
| Cherry | `#FF4D6D` | Button A, accents |
| Grass | `#3CCB7F` | Button B, correct answer |
| Ocean | `#3A86FF` | Button C, accents |
| Banana | `#FFD43B` | Button D, stars, highlights |
| Grape | `#9B5DE5` | Round banners, accents |
| Cream | `#FFF8E7` | Cards and question panels |

**Color rules:**
- Round banners rotate through these colors, one per round: Grape → Cherry → Ocean → Grass.
- Every slide shows a section of the **colored tile path** along one edge.

### Fonts

- **Titles:** Titan One (fallback: Lilita One).
- **Body:** Nunito (fallback: Quicksand).

| Style | Spec |
|---|---|
| Cover title | Titan One 130 |
| Slide title | Titan One 76–88 |
| Question | Nunito ExtraBold 48 |
| Button label | Nunito ExtraBold 34 |
| Body | 26–28 |

### Recurring motifs

1. **Game-card banner** for titles: a rounded rectangle with a dotted stitched inner border, colored per round.
2. **Answer tiles:** 380 × 110, radius 28, with a darker bottom edge for a 3D feel. The letter sits in a white circle.
3. **Tile path:** colorful squares with small stars along the bottom or side edge (Canva board-game path element, or plain squares plus star icons).
4. **Mascot host:** a fox in a bow tie (or a similar animal from the chosen set). It appears on most slides with a speech bubble.
5. **Dice, pawns and cards** scattered as decor. Score stars in Banana.

**Transition:** Push.

### Illustration style

- One flat, rounded, colorful set of game pieces plus one animal mascot set.
- The asset scout confirms that the fox host (or a substitute animal) exists in **several poses**.

## 3. Slide-by-slide spec

Each question slide has:
- a round banner,
- a Cream question panel (1680 × 300) at y 220,
- 4 answer tiles in a 2 × 2 grid at y 560 / 700, x 300 / 1000,
- a topic illustration (~360) at the top right,
- and the host's speech bubble.

Each answer slide has:
- the same banner,
- a big Grass "CORRECT!" burst,
- the answer in Titan One 120,
- a fun fact card,
- the host cheering.

### Builder A

**Slide 1 — Cover**
- Title on a big Banana game-card banner:
  > GAME NIGHT!
- Subtitle on a Grape pill:
  > Family Trivia Showdown
- Hero (~900): a board-game scene with giant dice, colorful pawns, cards, and the fox host waving, on a winding tile path.
- Decor: stars and confetti.

**Slide 2 — How to Play**
- Title: `How to Play`.
- Three game cards (Cherry / Ocean / Grass tints), each with a big number die (Canva) and an icon:
  1. `Make Teams` — Form 2–4 teams with a fun name.
  2. `Pick an Answer` — Agree as a team within 30 seconds.
  3. `Collect Stars` — 1 star per correct answer, 2 for the bonus.
- Host bubble: `No phones allowed!`

**Slide 3 — Meet the Teams**
- Title: `Meet the Teams`.
- Four team pawns in different colors (Cherry, Grass, Ocean, Banana). Each sits on a podium card with a `[Team Name]` placeholder and an empty star counter.
- Host bubble: `Who will win tonight?`

### Builder B

**Slide 4 — Round 1 · Animals (question)**
- Banner (Grape): `ROUND 1 · ANIMALS`.
- Question: `What is the largest mammal on Earth?`
- Answer tiles:
  - A — African Elephant
  - B — Blue Whale
  - C — Giraffe
  - D — Hippopotamus
- Topic illustration: a cute whale and an elephant side by side.

**Slide 5 — Round 1 · Answer**
- Answer: `BLUE WHALE`.
- Fun fact: `A blue whale's heart is about the size of a small car.`
- Hero: a smiling blue whale (~520).

**Slide 6 — Round 2 · Geography (question)**
- Banner (Cherry): `ROUND 2 · GEOGRAPHY`.
- Question: `Which is the largest ocean on Earth?`
- Answer tiles:
  - A — Atlantic
  - B — Indian
  - C — Pacific
  - D — Arctic
- Topic illustration: a cute globe with a boat.

### Builder C

**Slide 7 — Round 2 · Answer**
- Answer: `PACIFIC OCEAN`.
- Fun fact: `The Pacific is bigger than all of Earth's land put together.`
- Hero: a globe showing the Pacific, with waves and a smiling sun (~480).

**Slide 8 — Round 3 · Food (question)**
- Banner (Ocean): `ROUND 3 · FOOD`.
- Question: `Which fruit wears its seeds on the outside?`
- Answer tiles:
  - A — Banana
  - B — Strawberry
  - C — Mango
  - D — Grape
- Topic illustration: a fruit basket with cute faces.

**Slide 9 — Round 3 · Answer**
- Answer: `STRAWBERRY`.
- Fun fact: `One strawberry has around 200 tiny seeds on its skin.`
- Hero: a happy strawberry character (~460).

### Builder D

**Slide 10 — Bonus Round · True or False**
- Banner (Grass): `BONUS ROUND · 2 STARS`.
- Statement on the Cream panel: `An octopus has three hearts.`
- Two huge tiles: `TRUE` (Grass) and `FALSE` (Cherry), each 600 × 160.
- Topic illustration: a cute octopus with heart icons (~420).
- Speaker note: `Answer: TRUE.`

**Slide 11 — Scoreboard**
- Title: `Scoreboard`.
- Four colored lanes, one per team. Each lane has a pawn, `[Team Name]`, and 5 empty star outlines.
- Hero: a gold trophy with confetti (~460).
- Host bubble: `Count those stars!`

**Slide 12 — Thanks for Playing**
- Title on a big Banana banner:
  > THANKS FOR PLAYING!
- Subtitle: `See you at the next game night.`
- Contact pill (Grape): `@yourhandle  •  www.yourwebsite.com`
- Hero (~1300 wide along the bottom): all the game pieces and the fox host celebrating on the tile path, with confetti.

## 4. Speaker notes

| Slide | Note |
|---|---|
| 5 | `Answer: B — Blue whale.` |
| 7 | `Answer: C — Pacific.` |
| 9 | `Answer: B — Strawberry.` |
| 10 | `Answer: TRUE.` |

## 5. Deck-specific QA

- [ ] Answers on the answer slides match their questions.
- [ ] Each question has exactly one correct option.
- [ ] Nothing from the reference: no green clipboard frame, no jungle leaves, no kids on swings.
- [ ] Nothing from the earlier midnight/neon game-night deck.
