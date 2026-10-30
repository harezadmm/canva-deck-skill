# Prompt — "Game Night: The Ultimate Quiz Party" Canva deck (fast pipeline, ~30–40 min)

> Copy everything below into a new task. One **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Game Night – Quiz Deck"**. It is a playable quiz-night deck with a cover, rules, 4 question/answer rounds, a scoreboard, and a closing slide.

- **Language:** all deck content in **English**. Report to the user in **Indonesian**.
- **Reference (mood only):** https://www.canva.com/templates/EAGVsh1mGZg/ ("Hijau Ilustrasi Game Tema Alam" — green nature-themed quiz game).
  - Borrow the *format*: a playful quiz flow (question slide → answer slide), chunky display titles, pill-shaped answer buttons.
  - **Build from scratch.** Never click "Use this template", never copy its pages or elements.

### Skills to load first (main agent)

- `anthropic-skills:pptx` → to generate the .pptx skeleton.
- `elite-powerpoint-designer` → design rules (summarised in §3).
- `presentation-design` → for the QA pass in §8.

---

## 1. Hard rules (all agents)

1. Assets come from **Canva Elements only** (Elemen → Grafis / Stiker / Bentuk / Foto). Pro is allowed.
2. **No Canva AI:** no Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva", "Buat Animasi". Skip any asset whose creator is "Canva AI Elements Lab".
3. No sharing, publishing, downloading, or changes to sharing/access/account settings.
4. **Stay in your lane.** Builders edit only their own pages. Nobody but the main agent adds, deletes, or reorders pages. Never click "Ubah semua".
5. **No copy/paste between pages.** All agents share one clipboard, so a paste can land another agent's elements. Insert assets fresh from the Elements panel instead.
6. Quiz questions and answers stay exactly as written in §6.
7. No brand logos, no trademarked game characters or game boxes (no Monopoly, Scrabble, Nintendo, etc.).

---

## 2. Borrow vs. must differ

| Borrow (the mood) | Must differ (our identity) |
|---|---|
| Playful quiz-show flow, question → answer | **Night-time game-show** look, not daytime nature |
| Chunky, friendly display titles | **No** green leafy jungle borders, no lime-green palette |
| Pill-shaped answer buttons | Buttons are **4 colors (A coral, B mint, C sky, D yellow)**, not one yellow |
| A framed content panel | **No** notched clipboard/ticket frame. Our panel is a rounded "game card" with a dotted inner border |
| Illustrated hero per slide | **No** cartoon kids on swings or with flowers. Heroes are **game objects**: dice, cards, controllers, game pieces, trophies, stars |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins 120 left/right, 96 top/bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Midnight | `#1B1442` | Main background |
| Grape | `#3A2A7A` | Panels, cards on dark |
| Cloud | `#F7F5FF` | Light panels, main text on dark |
| Neon Yellow | `#FFD23F` | Titles' highlight word, stars, button D |
| Hot Coral | `#FF5D73` | Accent, button A |
| Mint | `#3DDC97` | Correct-answer highlight, button B |
| Sky | `#4CC9F0` | Accent, button C |

### Fonts (max 2 families)

- **Titles:** Bungee (fallback: Lilita One).
- **Body / buttons:** Poppins (fallback: Nunito).

| Style | Spec |
|---|---|
| Hero title (cover, closing) | Bungee 120–140, Cloud, one word in Neon Yellow |
| Slide title | Bungee 72–88 |
| Question text | Poppins SemiBold 44–52, Cloud, max 2 lines |
| Button label | Poppins Bold 32–36 |
| Body | Poppins Regular 28–30, line spacing 1.4. Never below 24 |
| Small label / tag | Poppins Bold 22, UPPERCASE, letter spacing 200 |

### Design rules (from elite-powerpoint-designer)

- One idea per slide. Max 6 lines of body text. Max 4 font sizes per slide.
- Text contrast at least 4.5:1 (light text on Midnight/Grape, dark text only on Cloud/Yellow/Mint).
- Max 3 animated elements per slide. Transitions: Fade or Push only, one type for the whole deck.

### Recurring motifs (same on every slide so 4 builders match)

1. **Round tag:** pill (radius 999), Hot Coral fill, Cloud text: `ROUND 1 · SCIENCE`.
2. **Game card panel:** Grape rounded rectangle (radius 40) with a 4 px Cloud **dotted** inner border inset 24 px.
3. **Answer buttons:** pills 360 × 96 (radius 48), colors A coral / B mint / C sky / D yellow, letter in a Cloud circle (64) at the left.
4. **Score star:** small Neon Yellow star (40–60) next to the round tag, plus 2–4 tiny sparkle dots per slide.
5. **Correct answer badge:** Mint pill with "✓ CORRECT ANSWER" (Poppins Bold 22, Midnight).

### Illustration style

Bold, glossy **3D or flat-vector game objects** with a soft glow, consistent across the deck. The asset scout picks 1–2 anchor creators in Phase 0.

---

## 4. Pipeline (why this is fast)

The slow part last time was clicking text, fonts, colors and shapes one by one (260–350 actions per agent). This time **all of that is generated in code**; agents only add illustrations.

### Phase 0A — main agent: build the skeleton .pptx (≈5 min)

1. Use python-pptx. Slide size **20 in × 11.25 in** (18288000 × 10287000 EMU) so Canva imports it as 1920 × 1080. Convert px → EMU with `px * 9525`.
2. For every slide in §6, create: background fill, all text boxes (exact copy, font names, sizes, colors), panels, pills, buttons, circles, dotted borders, stars as simple shapes.
3. For each hero illustration, place a **placeholder rectangle** at the hero's exact position, 20 % transparent Cloud, with a small label inside (e.g. `HERO: dice 640w`). Builders delete it after placing the real asset.
4. Save as `game-night-skeleton.pptx` in the working folder. Render one slide to PNG (LibreOffice, if available) to sanity-check.

### Phase 0B — asset scout subagent, in parallel with 0A (≈10 min)

Search Canva Elements for every hero and icon in §6 and write `game-night-assets.md`:

| Slide | Item | Exact search keyword | Creator | Result position (row, column) | Pro/free |

Pick 1–2 anchor creators with a consistent glossy game-object style. Insert nothing into the design.

### Phase 0C — main agent: import (≈3 min)

1. In Canva: Buat desain → Impor file (or the Unggahan panel) → upload `game-night-skeleton.pptx` with the `file_upload` tool. If uploading through the tool isn't possible, ask the user to drag the file into Canva once.
2. Open the imported design, rename it **Game Night – Quiz Deck**, and check 2–3 slides:
   - fonts mapped to Bungee/Poppins (if Canva substituted a font, the main agent re-sets it on the affected text boxes before builders start),
   - dotted borders and pill radii survived.
3. **Fallback if the import is badly broken:** build slide 4 by hand as a fully styled "kit page", duplicate it for every slide, then let builders swap the text. Report which path was used.
4. Copy the edit URL into each builder brief.

### Phase 1 — 4 builder subagents in parallel (≈15 min)

Each builder gets §1, §2, §3, its slides in §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`. For each slide:
> 1. Insert the asset listed in the asset sheet (search the exact keyword, pick the listed result).
> 2. Lock aspect ratio, then match the placeholder's size and position via Posisi (Lebar/Tinggi/X/Y).
> 3. Delete the placeholder rectangle.
> 4. Fix only real problems: overlapping, clipped or unreadable text. Do not restyle anything else.
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

**Slide 1 — Cover (bg Midnight)**
- Small label at (120, 200): `FRIDAY NIGHT FUN` in Neon Yellow.
- Hero title at (120, 250), width 1000, Bungee 130, 2 lines: `GAME` (Cloud) / `NIGHT!` (Neon Yellow).
- Subtitle at (120, 560), Poppins 34, Cloud, width 820: `The ultimate quiz party — grab your team and your best guesses.`
- Two pills at y 700: Hot Coral `4 ROUNDS` (x 120) and Sky `1 BIG WINNER` (x 420), 260 × 72.
- Hero: big pair of glossy dice + a game controller, ~760 wide, at (1060, 180), over a Grape circle 820 at (1020, 140) with a soft glow.
- 4 sparkle stars around the hero.

**Slide 2 — How to Play (bg Midnight)**
- Title at (120, 110): `HOW TO PLAY`.
- Three game cards 520 × 560 at y 300, x 120 / 700 / 1280, each with a number circle (Neon Yellow, 96, Bungee 48 Midnight), a title (Poppins Bold 34 Cloud) and body (Poppins 26 Cloud):
  1. `Form Teams` — `Split into 2–4 teams and pick a fun team name.`
  2. `Answer Fast` — `Each question has a 30-second timer. Write your answer down.`
  3. `Score Points` — `1 point per correct answer. The bonus round is worth 2.`
- Small icon on each card (~140): team/people icon, stopwatch, trophy.

**Slide 3 — Are You Ready? (bg Grape)**
- Centered title, Bungee 110, Cloud: `ARE YOU READY?`
- Below it, three big countdown circles 220 at y 560, centers x 660 / 960 / 1260: `3` (Hot Coral), `2` (Sky), `1` (Neon Yellow), Bungee 120 Midnight.
- Caption at y 860, Poppins 30, Cloud: `Phones down, pencils up!`
- Hero: a rocket or a stopwatch (~300) at the top-right corner (1540, 120).

### Builder B

**Slide 4 — Round 1 · Question (bg Midnight)**
- Round tag at (120, 110): `ROUND 1 · SCIENCE`.
- Game card 1680 × 760 at (120, 200).
- Question inside, Poppins SemiBold 52, Cloud, at (200, 280), width 1000: `Which planet is known as the Red Planet?`
- Four answer buttons in a 2 × 2 grid at x 200 / 600, y 560 / 680: `A  Venus`, `B  Mars`, `C  Jupiter`, `D  Saturn`.
- Hero: cartoon/3D planet (~520) at (1260, 300).

**Slide 5 — Round 1 · Answer (bg Midnight)**
- Same round tag and game card as slide 4.
- Correct-answer badge at (200, 280).
- Big answer, Bungee 140, Mint, at (200, 360): `MARS`.
- Fun fact, Poppins 30, Cloud, width 960, at (200, 600): `Iron-rich dust gives Mars its rusty red color.`
- Hero: the same planet style, a red planet (~520) at (1260, 300).

**Slide 6 — Round 2 · Picture Clue (bg Midnight)**
- Round tag: `ROUND 2 · GAMES`.
- Left: Cloud rounded "photo card" 640 × 640 at (120, 240) with a picture clue inside: a chess knight piece (~480).
- Right column at x 840, width 960:
  - Question, Poppins SemiBold 48: `Which board game uses pieces called the rook, bishop and knight?`
  - Three buttons stacked at y 600 / 720 / 840, 520 wide: `A  Checkers`, `B  Chess`, `C  Ludo`.

### Builder C

**Slide 7 — Round 2 · Answer (bg Midnight)**
- Round tag `ROUND 2 · GAMES`, correct-answer badge, big answer Bungee 140 Mint: `CHESS`.
- Fun fact, Poppins 30, Cloud: `Each player starts with 16 pieces, including 2 knights.`
- Hero: full chess set or a king piece (~600) at (1180, 220) on a Grape circle.

**Slide 8 — Round 3 · Fill the Blanks (bg Midnight)**
- Round tag: `ROUND 3 · WORDS`.
- Title, Bungee 72, Cloud, centered at y 230: `COMPLETE THE WORD`.
- Six letter tiles (Cloud rounded squares 160 × 160, radius 24, Bungee 96 Midnight) in a row centered at y 440, gaps 24: `?`, `U`, `Z`, `Z`, `?`, `E`. The two `?` tiles are Neon Yellow.
- Hint at y 700, Poppins 30, Cloud: `Hint: you put the pieces together to finish it.`
- Hero: jigsaw puzzle pieces (~320) at the bottom-right corner, bleeding slightly off the edge.

**Slide 9 — Round 3 · Answer (bg Midnight)**
- Same tile row, now spelling `P U Z Z L E`, the two revealed tiles in Mint.
- Correct-answer badge above the tiles; big word below is not needed.
- Fun fact at y 720, Poppins 30, Cloud: `The first jigsaw puzzles were maps glued to wood.`
- Hero: a finished puzzle piece with a sparkle (~260) at the top-right.

### Builder D

**Slide 10 — Bonus Round · True or False (bg Grape)**
- Round tag in Neon Yellow with Midnight text: `BONUS ROUND · 2 POINTS`.
- Statement in a Cloud game card (1400 × 360, Midnight text, Poppins SemiBold 48) centered at y 280:
  `A group of flamingos is called a "flamboyance".`
- Two huge buttons 520 × 140 at y 740, x 380 / 1020: `TRUE` (Mint) and `FALSE` (Hot Coral), Bungee 64.
- Hero: a cute flamingo (~360) at (1500, 600), partly overlapping the card's right edge but not the text.
- *(Answer: TRUE — the main agent adds it as a speaker note, not on the slide.)*

**Slide 11 — Scoreboard (bg Midnight)**
- Title `SCOREBOARD`, Bungee 88, Cloud, at (120, 110).
- A table-like set of 4 rows, each a Grape pill 1200 × 110 at x 120, y 280 / 410 / 540 / 670:
  - left: team-color dot (coral / mint / sky / yellow, 48) + `Team 1` … `Team 4` (Poppins Bold 34 Cloud),
  - right: an empty Cloud score box 200 × 80 with `—`.
- Hero: a gold trophy (~520) at (1380, 280) with confetti.

**Slide 12 — Thanks for Playing (bg Midnight)**
- Centered hero title, Bungee 130: `THANKS FOR` (Cloud) / `PLAYING!` (Neon Yellow), at y 300.
- Subtitle, Poppins 32, Cloud, y 620: `Same time next week? Bring your A-game.`
- Pill at y 740, Hot Coral, Cloud text: `@yourhandle  •  www.yourwebsite.com`.
- Hero: scattered dice, cards and confetti along the bottom edge (2–3 elements, ~300 each), plus sparkles.

---

## 7. Speaker notes (main agent adds in the .pptx)

- Slide 5: `Answer: B — Mars.`
- Slide 7: `Answer: B — Chess.`
- Slide 9: `Answer: PUZZLE.`
- Slide 10: `Answer: TRUE.`

---

## 8. QA checklist (main agent, run with `presentation-design`)

- [ ] 12 pages in order; every placeholder rectangle deleted.
- [ ] Only Bungee + Poppins (or stated fallbacks); body ≥ 24 px; contrast ≥ 4.5:1.
- [ ] Colors only from §3. Round tags, game cards, buttons and badges identical across slides.
- [ ] Answers on slides 5/7/9 match the questions on 4/6/8 exactly.
- [ ] No overlap, clipping, or stray elements (check each page's Lapisan list once).
- [ ] Illustration style consistent; none of the §2 "must differ" items; no AI assets; no brand logos.
- [ ] Nothing shared, downloaded, or published.

## 9. Final report to the user (Indonesian)

1. Edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately different from the reference (§2).
5. Path used (pptx import or kit-page fallback), total time per phase, and anything not achieved.
