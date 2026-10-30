# Prompt set9-7 — "Spin the Record: Groovy Music Trivia Night" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set9-newyear-business-gamenight\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `groovy-music-trivia`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Spin the Record: Groovy Music Trivia Night"**. It is a ready-to-host music trivia game for friends, family, classrooms or office parties.

- The host reads the slides aloud, teams answer, and the **answers are only in the speaker notes** (never on the slides).
- Flow:
  1. cover
  2. how to play
  3. Round 1 — Name That Instrument
  4. Round 2 — Music Words
  5. Round 3 — Sounds of the World
  6. Round 4 — Hum It!
  7. Bonus challenge roll
  8. Lightning True or False
  9. Leaderboard and tie-breaker
  10. Thank you
- All questions are general music knowledge. **No real artists, songs-by-name from the charts, albums or lyrics.** The hum round uses only old public-domain folk and holiday tunes.

**Reference (direction only):** https://www.canva.com/templates/EAGjIDK69ds/ ("Blue and Red Retro Groovy Girls' Trivia Game Night Presentation").

- **Borrow the idea:**
  1. a **retro 1970s "groovy" music-trivia** mood;
  2. chunky, curvy script titles;
  3. vintage music objects (records, microphones, gramophone, music notes);
  4. one question per card, with a "Game Rules" slide and a big "Let's Play" moment.
- **Build from scratch.** Do **not** click "Use this template" and do **not** copy any layout, illustration, text or question from the reference. Do not copy its blue-stripe background, red oval title badge or halftone portraits.

**Must also differ from the earlier game-night decks** (the main agent should check these files before building):
- `set6-christmas-gamenight-newyear\prompt-set6-2-game-night-host.md`
- `set7-christmas-gamenight\prompt-set7-4-game-night-pixel-quest.md`
- `set7-christmas-gamenight\prompt-set7-5-game-night-guess-the-idiom.md`
- Earlier decks named inside those files: "Game Night: The Ultimate Quiz Party" and "Game Night: Family Trivia Showdown".
- The other set9 game-night decks (set9-8, set9-9, set9-10).

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Retro 70s groovy music mood | A **"Record Sleeve & Jukebox"** concept: every slide is a **record sleeve** (cream square-cornered card with a thick Cocoa outline and a hard colored offset shadow). Each slide carries a **"TRACK 01–10" tag** and a **groove-stripe band** (4 parallel rainbow stripes, retro style). |
| Curvy retro script titles | **Shrikhand** titles in **Cocoa Ink with a Tomato extruded shadow** (no red oval badge, no pill behind the title). |
| Blue and red | A warm **70s palette of 8 colors** (Tomato, Orange, Mustard, Teal, Powder Blue, Pink, Grape, Cream), at least 4 per slide. **No** blue-and-red-only look and **no vertical stripe background**. Backgrounds are **radial sunburst rays** in cream and soft tints. |
| One question per card | Question cards are **cassette-tape cards** (rounded rectangle with two little reels and a label strip). **No** A/B/C/D answer buttons. |
| Vintage music objects | Heroes are **flat, friendly illustrations** (no halftone photo portraits, no retro women-portrait photos). Dancing diverse people, a jukebox, instruments, a disco ball. |
| — | **No** pixel-art or retro-arcade (set7-4, set7-5). **No** sticker-bomb die-cut titles, suit confetti or spinner wheel (set6-2). **No** night quiz stage, Midnight or black backgrounds, Bungee or A/B/C/D (Quiz Party). **No** board-game tabletop, tile path, pawns, fox host or Titan One (Family Trivia). **No** real artist names, brands or logos. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Cream Sleeve | `#FFF3DC` | Card bodies, main background |
| Sunburst Butter | `#FFE7A8` | Rays on cream backgrounds |
| Powder Blue | `#CFEAF5` | Background tint (alternate slides), Ink text on it |
| Cocoa Ink | `#2B1A14` | Text, titles, card outlines |
| Tomato | `#D63A1F` | Round 1, cover, primary accent; white text allowed on it |
| Orange Groove | `#F58A2E` | Round 3, accents; Ink text on it |
| Mustard | `#F4B33A` | Intro pills, highlights; Ink text on it |
| Teal | `#167F76` | Round 2; white text allowed on it |
| Disco Pink | `#F2799F` | Round 4; Ink text on it |
| Grape | `#6B4FBB` | Lightning round, accents; white text allowed on it |

**Backgrounds** alternate (all light, no dark slides):
- Slides 1, 4, 7, 10: Cream Sleeve with Sunburst Butter rays.
- Slides 2, 5, 8: Powder Blue with white rays.
- Slides 3, 6, 9: Cream Sleeve with Sunburst Butter rays plus a Powder Blue corner blob.
- Never the same background fill on two consecutive slides.

**Color rules:**
- Each section uses its own color for the eyebrow chip, the track tag, the card offset shadows, the cassette label strips and the groove-stripe band's leading stripe:

  | Section | Slides | Color |
  |---|---|---|
  | Welcome | 1–2 | Tomato |
  | Round 1 — Instruments | 3 | Tomato |
  | Round 2 — Music Words | 4 | Teal |
  | Round 3 — World | 5 | Orange Groove |
  | Round 4 — Hum It | 6 | Disco Pink |
  | Bonus | 7 | Mustard |
  | Lightning | 8 | Grape |
  | Leaderboard | 9 | Teal and Tomato |
  | Finale | 10 | Rainbow (Tomato, Orange, Mustard, Teal, Grape) |

- The groove-stripe band always uses the same 4 stripes: Tomato, Orange, Mustard, Teal (leading stripe = section color; slide 10 uses the rainbow order).
- White text only on Tomato, Teal and Grape (contrast ≥ 4.5:1). Use Cocoa Ink text on Cream, Powder Blue, Orange, Mustard and Pink.
- Titles and body text are **Cocoa Ink** on every light background (never Tomato text on Cream, contrast too low).

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Shrikhand | — (whitelist; re-set to Shrikhand if substituted) | 76–96 (cover 110, Encore 140), tight leading, Tomato extruded shadow (offset 6, no blur) | Cocoa Ink |
| Body | Nunito SemiBold | — | 26–28 | Cocoa Ink |
| Card tags / labels | Nunito ExtraBold | — | 24, UPPERCASE | white on Tomato/Teal/Grape, Ink elsewhere |
| Eyebrow | Nunito ExtraBold | — | 22, UPPERCASE, letter spacing 200, inside a small tinted chip | Cocoa Ink |

Only these 2 families. Both are on the §D whitelist. Do **not** use Luckiest Guy, Lilita One, Chewy, Poppins or pixel fonts in this deck (they belong to other decks).

### Recurring motifs

1. **Record-sleeve cards:** cream cards, radius 12 (nearly square), 5 px Cocoa Ink outline, a **hard offset shadow** (10 px right and down, no blur) in the section color. A faint circular "record ring" outline is printed in one corner of big cards.
2. **Cassette-tape question cards:** a card with a colored label strip on top (holding the tag, such as `QUESTION 1`), two small reels at the bottom corners and a tiny window. Used on slides 3–8.
3. **Groove-stripe band:** four parallel curved stripes (Tomato, Orange, Mustard, Teal), about 140 px thick in total, running edge to edge or arcing around a corner. It sits under the title or along the bottom, and changes its leading stripe per section.
4. **Half-hidden vinyl record:** a big black-and-label vinyl record peeking from a slide corner (label in the section color). Different corner on each slide. (The only dark element in the deck, and only as an illustration.)
5. **Sunburst rays + sparkles:** soft radial rays behind the hero; four-point sparkles and small music notes in palette colors around heroes.
6. **Track tag footer:** bottom-left pill reading `TRACK 01` … `TRACK 10`, with a small play triangle. Bottom-right: a tiny "needle" progress line that moves along a short groove as the deck goes on.

**Transition:** Circle wipe ("Usap Lingkaran"), applied to all pages. Fallback: "Usap Warna", then "Larut".

### Illustration style

- One flat, warm, rounded, cheerful 1970s-flavored set: soft shapes, no outlines heavier than 3 px, warm skin tones in diverse variety, bell-bottoms, bold patterns allowed.
- Characters: diverse friends dancing, singing into a mic, holding instruments, a smiling "host" with a headset.
- Objects: vinyl records, jukebox, gramophone, retro microphone, headphones, retro radio, disco ball, piano keys, trumpet, trombone, double bass, clarinet, guitar, drums, sheet music, metronome, stopwatch, a world globe with music notes, a six-sided die.
- Icons: one consistent set (bold rounded line icons filled with palette colors).
- **No** photos, **no** halftone portraits, **no** real logos or brands, **no** real people.

**Search terms for the asset scout** (Canva Elements, English keywords):
- `retro vinyl record illustration`, `groovy 70s illustration`, `retro sunburst rays`, `rainbow stripes retro`, `retro music sparkle`
- `jukebox illustration`, `gramophone illustration`, `retro microphone illustration`, `retro radio illustration`, `boombox flat`, `cassette tape illustration`
- `disco ball illustration`, `people dancing flat retro`, `friends singing flat illustration`, `host with headset illustration`
- `piano keys illustration`, `trombone illustration`, `double bass illustration`, `clarinet illustration`, `trumpet illustration`, `saxophone illustration`, `acoustic guitar illustration`, `drum kit flat`
- `sheet music scroll illustration`, `metronome illustration`, `conductor baton`, `music notes doodle`
- `world globe music notes`, `stopwatch illustration`, `lightning bolt retro`, `die dice illustration`, `trophy golden record`, `podium 1 2 3 flat`
- Decor: `groovy flower retro`, `retro starburst`, `four point sparkle`, `halftone dots pattern`, `retro wavy lines`
- Icons: `music note icon`, `microphone icon`, `play button icon`, `headphones icon`, `trophy icon`, `phone icon`, `mail icon`, `web icon`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (title left, hero right; background Cream with Butter rays)
- Eyebrow chip (Tomato tint): `TONIGHT'S SHOW`
- Title at (110, 230), width 900, Shrikhand 110, 2 lines, Cocoa Ink with a Tomato extruded shadow:
  > Spin the / Record
- Subtitle pill (Tomato fill, white text, Nunito ExtraBold 30):
  > Groovy Music Trivia Night
- Info chip (Mustard fill, Ink text):
  > Teams of 2–4 · Pens ready · Let's groove!
- Presenter line (Nunito SemiBold 26, Ink):
  > Hosted by [Your Name] · [Organization]
- A row of three tinted circles (Teal / Pink / Orange) with icons: microphone, headphones, music note.
- Hero, right (~780): a giant vinyl record (Tomato label) rising behind a smiling host with a headset and a retro microphone, with two dancing friends on the sides and a disco ball above.
- Groove-stripe band: arcs around the bottom-left corner (y ≈ 860 to 1080), leading stripe Tomato.
- Decor: sunburst rays behind the hero, four-point sparkles, music notes in the top-left corner, a half-hidden vinyl at the bottom-right.
- Footer: `TRACK 01` pill.

**Slide 2 — How to Play** (hero left, 4 rule rows right; background Powder Blue with white rays)
- Eyebrow chip (Tomato tint): `HOUSE RULES`
- Title (right column, x 700): `Liner Notes: How to Play`
- Groove-stripe band under the title (Tomato leading).
- Hero, left (~520): a friendly flat jukebox glowing with colored lights, with two small characters picking a song.
- Four record-sleeve rule rows on the right (each with a numbered circle in Tomato / Teal / Orange / Grape and an icon):
  1. Make teams. `Make 2–5 teams of 2–4 players and pick a fun team name.`
  2. Answer together. `The host reads each question. Huddle for 20 seconds, then show your answer.`
  3. Score points. `Rounds 1–3 and the lightning round: 1 point each. The hum round: 2 points each.`
  4. Play fair. `No phones, no peeking. The host's decision is final.`
- Needs-chip (Mustard fill, Ink text):
  > You will need: paper, pens, one die and a timer
- Decor: a half-hidden vinyl at the top-right corner, sparkles and notes around the jukebox.
- Footer: `TRACK 02` pill.

**Slide 3 — Round 1: Name That Instrument** (2 × 2 cassette cards left, hero right; background Cream with a Powder Blue corner blob)
- Eyebrow chip (Tomato tint): `ROUND 1 · 1 POINT EACH`
- Title: `Name That Instrument`
- Groove-stripe band under the title (Tomato leading).
- Intro pill (Mustard, Ink text):
  > Listen to the clue, then name the instrument.
- Four cassette cards (Tomato label strips, white tag text):
  - `QUESTION 1` — I have 88 black and white keys. Which instrument am I?
  - `QUESTION 2` — I'm a brass instrument with a slide you push in and out. Who am I?
  - `QUESTION 3` — I'm the biggest bowed string instrument in the orchestra, and I stand on the floor. Who am I?
  - `QUESTION 4` — I'm a straight black wooden tube with a single reed, and jazz bands love me. Who am I?
- Hero, right (~520): a big retro microphone with headphones and a stack of instrument silhouettes (piano keys, trombone) behind it.
- Decor: half-hidden vinyl bottom-left, sparkles, small notes in four palette colors.
- Footer: `TRACK 03` pill.

### Builder B

**Slide 4 — Round 2: Music Words** (row of 4 tall cassette cards, hero band at the bottom; background Cream with Butter rays)
- Eyebrow chip (Teal tint): `ROUND 2 · 1 POINT EACH`
- Title (centered): `Music Words`
- Groove-stripe band under the title (Teal leading).
- Intro pill (Mustard, Ink text), centered:
  > Many music words come from Italian.
- Four tall cassette cards in one row (Teal label strips, white tag text; a small icon on each):
  - `QUESTION 1` — What does the music word "forte" mean?
  - `QUESTION 2` — What is a group of four singers or players called?
  - `QUESTION 3` — What does "tempo" tell the musicians?
  - `QUESTION 4` — Which is the highest singing voice: bass, tenor or soprano?
- Hero, bottom band (~1100 wide, y 720–1040): an unrolled sheet-music scroll with notes, a metronome and a conductor's baton, with a small conductor character.
- Decor: sparkles, notes, half-hidden vinyl at the top-right.
- Footer: `TRACK 04` pill.

**Slide 5 — Round 3: Sounds of the World** (hero center, 2 cards each side; background Powder Blue with white rays)
- Eyebrow chip (Orange tint): `ROUND 3 · 1 POINT EACH`
- Title (centered): `Sounds of the World`
- Groove-stripe band under the title (Orange leading).
- Hero, center (~520): a friendly globe with colorful music notes spinning around it and small dancing characters in different traditional-flavored outfits.
- Four cassette cards (Orange label strips, Ink tag text), two left and two right with short connector lines to the globe:
  - `QUESTION 1` — Gamelan orchestras come from which two Indonesian islands?
  - `QUESTION 2` — Flamenco music and dance are famous in which European country?
  - `QUESTION 3` — Reggae music began on which Caribbean island?
  - `QUESTION 4` — The didgeridoo is a traditional instrument of the Aboriginal peoples of which country?
- Decor: sparkles, notes, half-hidden vinyl at the bottom-left.
- Footer: `TRACK 05` pill.

**Slide 6 — Round 4: Hum It!** (4 stacked strips left, hero right; background Cream with a Powder Blue corner blob)
- Eyebrow chip (Pink tint): `ROUND 4 · 2 POINTS EACH`
- Title: `Hum It!`
- Groove-stripe band under the title (Pink leading).
- Intro card (Pink tint, Ink text):
  > The host hums or taps each tune. The first hand up gets one guess. A miss lets another team steal.
- Four cassette strips (wide, Pink label strips with a headphones icon and a big number):
  - `HUM 1` — A sparkly lullaby about the night sky.
  - `HUM 2` — A holiday song with sleigh bells.
  - `HUM 3` — The song everyone sings with a cake.
  - `HUM 4` — A gentle song about a boat on a stream.
- Hero, right (~540): a retro radio with soundwaves, a person humming with eyes closed and big headphones, and floating notes.
- Decor: half-hidden vinyl at the top-right, sparkles, notes.
- Footer: `TRACK 06` pill.

### Builder C

**Slide 7 — Bonus: Roll the Groove** (hero left, 2 × 3 grid right; background Cream with Butter rays)
- Eyebrow chip (Mustard tint): `BONUS TRACK · +2 POINTS`
- Title (right column): `Roll the Groove`
- Groove-stripe band under the title (Mustard leading).
- Instruction card (Mustard fill, Ink text), under the hero:
  > Roll one die. Do your challenge in 15 seconds to win 2 bonus points.
- Hero, left (~500): a giant six-sided die floating in front of a disco ball, with a cheering friend and sparkles.
- Six cassette cards in a 2 × 3 grid on the right, each with a die-face number badge (1–6) in rotating palette colors:
  - `1` — Name 3 instruments in 10 seconds.
  - `2` — Hum a tune for 5 seconds. Your team guesses it.
  - `3` — Clap a steady beat for 10 seconds.
  - `4` — Sing the alphabet in a silly opera voice.
  - `5` — Strike a rock-star pose and hold it for 10 seconds.
  - `6` — Name 3 dance styles in 10 seconds.
- Decor: half-hidden vinyl at the bottom-right, sparkles, notes.
- Footer: `TRACK 07` pill.

**Slide 8 — Lightning Round: True or False?** (row of 5 tall cards, hero bottom center; background Powder Blue with white rays)
- Eyebrow chip (Grape tint): `LIGHTNING ROUND · 1 POINT EACH`
- Title (centered): `True or False?`
- Groove-stripe band under the title (Grape leading).
- Rule chip (Mustard, Ink text), centered:
  > Stand up for TRUE. Sit down for FALSE.
- Five tall cassette cards in one row (Grape label strips, white tag text), each with a statement and two small decorative pills `TRUE` (Teal, white text) and `FALSE` (Tomato, white text):
  - `NO. 1` — A standard violin has four strings.
  - `NO. 2` — A trumpet is a woodwind instrument.
  - `NO. 3` — A quartet has five performers.
  - `NO. 4` — A metronome helps musicians keep a steady tempo.
  - `NO. 5` — A saxophone is a brass instrument because it's made of brass.
- Hero, bottom center (~500 wide, y 740–1040): a stopwatch with a lightning bolt, a game-show-style buzzer and two excited players.
- Decor: sparkles, lightning bolts in Mustard and Orange, half-hidden vinyl at the top-left.
- Footer: `TRACK 08` pill.

**Slide 9 — The Hit Parade** (chart rows left, hero right; background Cream with a Powder Blue corner blob)
- Eyebrow chip (Teal tint): `LEADERBOARD`
- Title: `The Hit Parade`
- Groove-stripe band under the title (Teal leading).
- Five chart rows on the left (record-sleeve strips, each with a big rank badge in Tomato / Orange / Mustard / Teal / Pink, a team line and a score line):
  - `#1` — `Team name: ________` — `Score: ___`
  - `#2` — `Team name: ________` — `Score: ___`
  - `#3` — `Team name: ________` — `Score: ___`
  - `#4` — `Team name: ________` — `Score: ___`
  - `#5` — `Team name: ________` — `Score: ___`
- Points card (Mustard tint, Ink text, clipboard icon):
  > Points on offer: Round 1: 4 · Round 2: 4 · Round 3: 4 · Round 4: 8 · Lightning: 5 · Total: 25, plus bonus rolls
- Tie-breaker card (Grape fill, white text, stopwatch icon):
  > TIE-BREAKER: How many white keys are on a standard 88-key piano? Closest guess wins.
- Hero, right (~500): a winners' podium (1-2-3) with a golden vinyl record trophy, confetti and cheering players.
- Decor: half-hidden vinyl at the top-right, sparkles, notes.
- Footer: `TRACK 09` pill.

**Slide 10 — Thank You** (centered; background Cream with Butter rays)
- Title: `Encore!` in Shrikhand 140, centered, Cocoa Ink with a Tomato extruded shadow.
- Groove-stripe band: rainbow (Tomato, Orange, Mustard, Teal, Grape), arcing across the full width under the title.
- Subtitle (Nunito SemiBold 30, centered):
  > Thanks for playing! See you at the next groove.
- Prize chip (Mustard fill, Ink text, trophy icon):
  > The winning team takes home the Golden Record!
- Three contact pills (Tomato / Teal / Grape, white text), each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): diverse friends dancing and singing under a disco ball, with a jukebox on one side and a golden record held high.
- Decor: sparkles and notes in both top corners, half-hidden vinyl bottom-left.
- Footer: `TRACK 10` pill.

## 4. Speaker notes

- Slide 1:
  > Welcome everyone. Explain that teams will compete across four rounds, a lightning round and a bonus roll. Set up paper, pens, one die and a timer before you start.
- Slide 2:
  > Read the four rules aloud. Give each team a name and a scorekeeper. Keep the 20-second huddle strict.
- Slide 3, add the answer key:
  > ANSWERS: 1 Piano. 2 Trombone. 3 Double bass. 4 Clarinet. Read each clue twice. 1 point per correct answer.
- Slide 4:
  > ANSWERS: 1 Forte means loud (play strongly). 2 A quartet. 3 Tempo is the speed of the music. 4 Soprano. 1 point per correct answer.
- Slide 5:
  > ANSWERS: 1 Java and Bali. 2 Spain. 3 Jamaica. 4 Australia. 1 point per correct answer.
- Slide 6:
  > ANSWERS: 1 Twinkle, Twinkle, Little Star. 2 Jingle Bells. 3 Happy Birthday to You. 4 Row, Row, Row Your Boat. Hum or tap the tune for about 10 seconds. 2 points per correct answer, and a steal wins the same 2 points.
- Slide 7:
  > Let each team roll the die once per bonus turn. The host judges each challenge and starts the 15-second timer. A completed challenge scores 2 bonus points.
- Slide 8:
  > ANSWERS: 1 TRUE. 2 FALSE, a trumpet is brass. 3 FALSE, a quartet has four. 4 TRUE. 5 FALSE, a saxophone is a woodwind because it uses a single reed. 1 point per correct answer.
- Slide 9:
  > ANSWER to the tie-breaker: 52 white keys (an 88-key piano has 52 white and 36 black keys). Add up the points, fill in the scoreboard and announce the winners.
- Slide 10:
  > Thank the players, hand out the prize and invite everyone to host the next game night. Replace the contact details with your own.
- All slides 2–9, also add:
  > Questions are general music knowledge. Check any answer you are unsure of before the event, and adapt the difficulty to your group.

## 5. Deck-specific QA

- [ ] 10 slides in order; Circle wipe ("Usap Lingkaran") on all pages (or the stated fallback).
- [ ] Every slide has the record-sleeve cards (Cocoa outline + hard offset shadow), the groove-stripe band, a half-hidden vinyl, and the `TRACK 0X` footer.
- [ ] Question slides (3–8) use cassette-tape cards; no A/B/C/D buttons anywhere.
- [ ] **No answers on any slide.** Answers appear only in the speaker notes.
- [ ] Question and rule text matches §3 word for word.
- [ ] At least 4 palette colors visible per slide; no dark or black slide backgrounds.
- [ ] Titles are Shrikhand with a Tomato extruded shadow; body is Nunito. Only those 2 families.
- [ ] Placeholders `[Your Name] · [Organization]` on the cover; contact pills on slide 10.
- [ ] No halftone portraits, no photos, no real artists, brands, logos or lyrics.
- [ ] Nothing from the earlier decks' identities: pixel art, sticker-bomb stickers, suit confetti, spinner wheel, night stage, board tabletop, tile path, pawns, fox host, A/B/C/D buttons.
- [ ] Hero on every slide is at least 480 px; every slide has 3–6 supporting items and at least 2 decor layers.
