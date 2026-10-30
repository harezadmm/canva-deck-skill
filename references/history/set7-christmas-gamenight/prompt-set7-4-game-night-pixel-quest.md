# Prompt 4/5: "Game Night Quest: Level Up Your Game Night" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set7-christmas-gamenight\canva-shared-pipeline.md`.

That file holds:
- §A: hard rules
- §B: colorful brief and richness checklist
- §C: pipeline, builder brief, QA, and report
- §D: lessons learned from earlier runs

Deck slug: `game-night-pixel-quest`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Game Night Quest: Level Up Your Game Night"**. It is a pixel-game-style party guide.

- **Party roles:** a "choose your party" slide assigns the hosting jobs.
- **World map:** an agenda slide lays out the night.
- **Five levels:** one easy, screen-free game each:
  1. Two Truths & a Lie
  2. Whisper Chain
  3. Memory Tray
  4. Freeze Dance
  5. Rock-Paper-Scissors Tournament
- **Boss level:** a team tower challenge.
- **Wrap-up slides:** power-up tips, a leaderboard, and a "quest complete" ending.

**Reference (direction only):** https://www.canva.com/templates/EAHDI4qZAnM/ ("Blue and Green Pixel Game Adventure Presentation").

- **Borrow the idea:**
  - a pixel-art adventure game feel
  - a blue-and-green outdoor world
  - game-UI touches such as a start screen and level labels
  - a pixel display font
- **Build from scratch.** Do not copy any layout, illustration, or text from the reference.

**Must also differ from these decks:**
- Earlier game-night decks in this project:
  - "Game Night: The Ultimate Quiz Party": night-time quiz show, Midnight background, Bungee, A/B/C/D answer buttons
  - "Game Night: Family Trivia Showdown": board-game tabletop, tile path, pawns, fox host, Titan One
  - "Host the Ultimate Game Night": sticker-bomb, die-cut stickers, Luckiest Guy, ticket stubs. It covered Charades, Draw & Guess, card games, word games and Bingo, so none of those games appear here.
- The sibling deck in this set, set7-5 "Guess the Idiom!": a pixel arcade handheld screen on lilac, with magenta and cyan.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Pixel adventure feel | A **bright daytime "world map" quest**: pixel clouds, trees, flags, coins and hearts, with **6 bright colors** on every slide |
| Blue and green world | Blue and green are joined by **coin gold, heart red, grape and tangerine**. Each level has its own color |
| Game UI | A **HUD bar** on every slide (hearts, coin counter, level flag) and an **XP progress bar** footer that fills as the deck goes on |
| — | **No** dark or black backgrounds, **no** board-game tabletop or pawns, **no** quiz-show stage or A/B/C/D buttons, **no** die-cut sticker titles, **no** brand-name games, consoles or game characters. That includes plumber heroes, mushrooms, pipes and "?" blocks |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Pixel Sky | `#DDF2FF` | Background A (with pixel clouds) |
| Meadow | `#E6F9DD` | Background B (with pixel grass strip) |
| Ink | `#1B1F3B` | Text, pixel outlines |
| Quest Blue | `#2F7BFF` | Titles, Level 2 |
| Grass Green | `#34C759` | Level 1 |
| Tangerine | `#FF8A2E` | Level 3 |
| Grape | `#8A5CFF` | Level 4 |
| Heart Red | `#FF4D5E` | Level 5, hearts |
| Coin Gold | `#FFC531` | Boss level, coins, highlights |

**Backgrounds** alternate Pixel Sky (odd slides) and Meadow (even slides).

**Level colors** (level flag, card outlines, eyebrow):

| Level | Game | Color |
|---|---|---|
| 1 | Two Truths & a Lie | Grass Green |
| 2 | Whisper Chain | Quest Blue |
| 3 | Memory Tray | Tangerine |
| 4 | Freeze Dance | Grape |
| 5 | Rock-Paper-Scissors Tournament | Heart Red |
| Boss | Team Tower Challenge | Coin Gold |

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Press Start 2P | Silkscreen → Lilita One | 54–66 (pixel fonts run wide) | Ink, with a 6 px offset shadow in the level color |
| Body | Rubik Medium | Nunito | 26–28 | Ink |
| Eyebrow / HUD | Rubik Bold | Nunito ExtraBold | 22 | UPPERCASE, letter spacing 150, level color |

### Recurring motifs

1. **Pixel window cards:** white cards with a 4 px Ink border, square corners with a 1-step pixel notch, and a solid 8 px offset shadow in the slide color.
2. **HUD bar** (top right, every slide): 3 pixel hearts, a coin icon with `× 12`, and a small level flag.
3. **Level flag:** a pixel pennant on a pole showing `LEVEL 1`–`LEVEL 5` or `BOSS`.
4. **XP bar footer:** a pixel progress bar along the bottom that is filled to (page ÷ 12). The page number sits at the right end in a coin.
5. **Pixel decor:** pixel clouds, trees, sparkles, coins and small bushes from Canva pixel-art elements.
6. **Info chips:** pixel-bordered chips for `Players`, `Time` and `You need`.

**Transition:** Line wipe ("Sapuan garis"). If it is not available, use Slide ("Meluncur").

### Illustration style

- **One** pixel-art set (8-bit / 16-bit look, flat colors):
  - diverse pixel characters (kids, teens, adults, grandparents)
  - pixel landscapes, flags, coins, hearts, trophies, potions and a friendly dragon
- Pixel art must be **original and generic**. Use no character that looks like a famous game hero.
- The asset scout searches terms like:
  - "pixel art character"
  - "pixel landscape"
  - "8 bit coin"
  - "pixel heart"
  - "pixel trophy"
  - "pixel dragon"
  - "pixel cloud"
- **One** pixel icon set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1: Cover, the start screen** (Pixel Sky)
- Eyebrow: `GAME NIGHT QUEST`
- Title at (120, 220), width 980, 2 lines:
  > Level Up Your Game Night
- Pill (Grass Green, white text):
  > Easy, screen-free games for the whole crew.
- Blinking-style label (Coin Gold pixel box, Ink text): `▶ PRESS START`
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~860, right): a pixel world with green hills, trees and flags, and a diverse group of pixel friends cheering with coins popping above them.
- Decor: pixel clouds, sparkles, HUD bar.

**Slide 2: Choose Your Party** (Meadow)
- Title: `Choose Your Party`
- Four character-select cards in a row, each with a pixel character on a colored stand:
  - `The Host` — Picks the games and keeps time.
  - `Snack Master` — Keeps everyone fueled.
  - `Scorekeeper` — Tracks points on the leaderboard.
  - `Hype Captain` — Cheers loud and keeps the energy up!
- Small pixel arrow cursor (`▶`) pointing at the first card.

**Slide 3: World Map** (Pixel Sky)
- Title: `The World Map`
- A winding pixel path left to right, with 6 flag stops in their level colors:
  1. `Level 1 · Two Truths & a Lie`
  2. `Level 2 · Whisper Chain`
  3. `Level 3 · Memory Tray`
  4. `Level 4 · Freeze Dance`
  5. `Level 5 · Rock-Paper-Scissors Tournament`
  6. `Boss Level · Team Tower Challenge`
- Decor: pixel trees, a river, coins along the path, and a small pixel castle at the end (generic, not from any game).

### Builder B

**Slide 4: Level 1, Two Truths & a Lie** (Meadow, Grass Green)
- Flag `LEVEL 1` · Eyebrow `LEVEL 1 · ICEBREAKER` · Title `Two Truths & a Lie`
- Info chips: `Players: 3+` · `Time: 15 min` · `You need: nothing!`
- Card **How to play:**
  > Each player shares three facts about themselves — two true and one made up. Everyone guesses the lie.
- Card **Power-up tip:**
  > Mix silly facts with surprising true ones.
- Hero (~520, **left**): pixel friends in a circle with thought bubbles.

**Slide 5: Level 2, Whisper Chain** (Pixel Sky, Quest Blue)
- Flag `LEVEL 2` · Eyebrow `LEVEL 2 · LISTEN UP` · Title `Whisper Chain`
- Info chips: `Players: 6+` · `Time: 10 min` · `You need: a list of funny sentences`
- Card **How to play:**
  > Sit in a line. The first player whispers a sentence once to the next player, and it passes down the line. The last player says it out loud!
- Card **Power-up tip:**
  > Longer sentences make funnier mix-ups.
- Hero (~520, **right**): a row of pixel characters whispering, with tangled speech bubbles.

**Slide 6: Level 3, Memory Tray** (Meadow, Tangerine)
- Flag `LEVEL 3` · Eyebrow `LEVEL 3 · BRAIN POWER` · Title `Memory Tray`
- Info chips: `Players: 2+` · `Time: 10 min` · `You need: a tray, 15 small objects, a cloth`
- Card **How to play:**
  > Show the tray for 60 seconds, then cover it. Players write down every object they remember.
- Card **Power-up tip:**
  > Secretly remove one item and ask, "What's missing?"
- Hero (~480, **top center**, with both cards side by side below it): a pixel tray of small objects (key, apple, coin, star, cup) with a timer.

### Builder C

**Slide 7: Level 4, Freeze Dance** (Pixel Sky, Grape)
- Flag `LEVEL 4` · Eyebrow `LEVEL 4 · GET MOVING` · Title `Freeze Dance`
- Info chips: `Players: 4+` · `Time: 10 min` · `You need: music and a speaker`
- Card **How to play:**
  > Dance while the music plays. When it stops, freeze! Anyone who moves sits out until the next round.
- Card **Power-up tip:**
  > Call out fun poses like "robot" or "flamingo."
- Hero (~540, **left half, full height**): pixel friends frozen in funny dance poses with music notes.

**Slide 8: Level 5, Rock-Paper-Scissors Tournament** (Meadow, Heart Red)
- Flag `LEVEL 5` · Eyebrow `LEVEL 5 · TOURNAMENT` · Title `Rock-Paper-Scissors Tournament`
- Info chips: `Players: 4+` · `Time: 15 min` · `You need: a bracket on paper`
- **Full-width bracket graphic** (8 slots → 4 → 2 → champion crown) built from pixel lines
- Card **How to play:**
  > Players face off in best-of-three matches. Winners move up the bracket until one champion remains.
- Card **Power-up tip:**
  > Players who are out join the winner's cheering squad!
- Small pixel rock, paper and scissors hand icons.

**Slide 9: Boss Level, Team Tower Challenge** (Pixel Sky, Coin Gold)
- Flag `BOSS` · Eyebrow `BOSS LEVEL · TEAMWORK` · Title `Team Tower Challenge`
- Info chips: `Teams: 2–4` · `Time: 5 min a round` · `You need: paper cups or blocks`
- Card **How to play:**
  > Each team builds the tallest tower it can before the timer ends. The tower must stand on its own for 5 seconds.
- Card **Power-up tip:**
  > Wide base, steady hands!
- Hero (~520): a friendly pixel dragon cheering beside a tall, wobbly block tower.

### Builder D

**Slide 10: Power-Ups for Hosts** (Meadow)
- Title: `Power-Ups for Hosts`
- Six pixel item tiles in a 3 × 2 grid, each a different color with a pixel item icon:
  - `Snack Potion` — Set out finger foods between levels.
  - `Shield` — Agree on kind house rules before you start.
  - `Extra Life` — Let younger players have a second try.
  - `Timer Crystal` — Keep each game short and snappy.
  - `Map Scroll` — Plan the order: calm, active, calm.
  - `Star Boost` — Cheer for every great move.

**Slide 11: Leaderboard & Badges** (Pixel Sky)
- Title: `Leaderboard & Badges`
- Left: a pixel-bordered leaderboard table:
  - 4 team rows: Green / Blue / Orange / Purple
  - columns `L1`–`L5`, `Boss` and `Total`
  - empty cells
- Right: four pixel badges, each a different color:
  - `MVP`
  - `Team Spirit`
  - `Quick Thinker`
  - `Dance Legend`
- Decor: pixel trophy (~260), coins.

**Slide 12: Quest Complete** (Meadow)
- Eyebrow: `QUEST COMPLETE`
- Title centered, Press Start 2P 100, Ink with a Coin Gold shadow:
  > Thanks for Playing!
- Subtitle:
  > Continue? Same time next week!
- Three contact pills (Grass Green / Quest Blue / Grape, white text):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): a pixel party scene with all the characters celebrating, pixel fireworks and coins raining.
- XP bar full.

## 4. Speaker notes

- **Slides 4–9:** Adjust the time and player counts to your group. Keep the play area clear for Freeze Dance and the tower challenge.

## 5. Deck-specific QA

- [ ] Backgrounds alternate Pixel Sky / Meadow as listed.
- [ ] Each level slide uses its own level color for the flag, eyebrow and card shadows.
- [ ] The HUD bar and the XP bar appear on every slide; the XP bar grows slide by slide.
- [ ] Slides 4–8 each use a different layout (hero left / right / top / half / bracket).
- [ ] No dark backgrounds; no brand-name games, consoles or look-alike game characters; no A/B/C/D buttons.
- [ ] None of the games from "Host the Ultimate Game Night".
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier game-night decks (§0).
