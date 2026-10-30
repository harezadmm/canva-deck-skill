# Prompt 1/5: "Sing Along! The Stories Behind Christmas Carols" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set7-christmas-gamenight\canva-shared-pipeline.md`.

That file holds:
- §A: hard rules
- §B: colorful brief and richness checklist
- §C: pipeline, builder brief, QA, and report
- §D: lessons learned from earlier runs

Deck slug: `christmas-carol-stories`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Sing Along! The Stories Behind Christmas Carols"**. It is a cheerful, illustrated deck about where five favorite carols come from, plus carols around the world and tips for a caroling night. It is for schools, families, and community events.

**Reference (direction only):** https://www.canva.com/templates/EAG7wLqIypU/ ("Red and Gold Simple Bold Traditional Christmas Carol Service Presentation").

- **Borrow the idea:**
  - a simple, bold, traditional carol-program feel
  - a clear "order of carols" running through the deck
  - strong, heavy titles
  - red as the lead title color
  - a centered, balanced cover
- **Build from scratch.** Do not copy any layout, image, or text from the reference.

**Must also differ from the earlier Christmas decks in this project:**
- Eco-Friendly Christmas
- Christmas Around the World (world-tour stop tags, dashed travel path, globe)
- Family Fun Guide (mint background, scrapbook polaroids, washi tape)
- Season's Greetings (midnight-blue sky, penguins, frosted-glass panels)
- Christmas Through the Senses (papercraft layers, emerald and berry, sense badges)
- The Magic of Christmas (storybook pages, chapter ribbons, dusk gradient, Chewy)
- The other two Christmas decks in this set:
  - set7-2 Cookie Workshop: bakery, cookie-cutter cards
  - set7-3 Dear North Pole: postal stamps, envelopes

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Bold traditional carol program | A **colorful "songbook & vinyl" concept**: each carol is a **track** with a vinyl-record badge in its own track color |
| Red and gold | Red is joined by **5 bright accents** (pine, butter, sky, plum, tangerine). Every slide shows 4+ colors. **No gold foil or glitter textures** |
| Order of carols | Becomes a **"Tonight's Setlist"** slide styled as a playlist with track numbers |
| Heavy titles | Slab-serif titles with a **music-staff underline** (five thin lines with a few notes) |
| — | **No** church interiors or stained glass, **no** hymn-sheet columns, **no** candle-only slides, **no** dark backgrounds, **no** items from the earlier decks in §0 |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Song Ivory | `#FFF8EC` | Main background |
| Ink Navy | `#1F2147` | Text |
| Holly Red | `#E23A3F` | Titles, setlist header |
| Pine Green | `#1E8C5A` | Accent, Track 03 |
| Butter | `#FFC63F` | Accent, Track 02 |
| Sky Note | `#3FA7F5` | Accent, Track 01 |
| Plum | `#8C4FD8` | Accent, Track 05 |
| Tangerine | `#FF8740` | Accent, Track 04 |

**Background:** Song Ivory on every slide, plus faint music-staff lines (Ink Navy at 6 % opacity) drifting across one corner.

**Track colors** (vinyl badge, card outlines, eyebrow):

| Track | Carol | Color |
|---|---|---|
| 01 | Silent Night | Sky Note |
| 02 | Jingle Bells | Butter |
| 03 | Deck the Halls | Pine Green |
| 04 | We Wish You a Merry Christmas | Tangerine |
| 05 | O Christmas Tree | Plum |

Every slide has music-note confetti (♪ ♫) and small holly or star doodles in 3+ palette colors.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Alfa Slab One | Lilita One | 74–88 | Holly Red, with a music-staff underline |
| Body | Lexend Medium | Nunito | 26–28 | Ink Navy |
| Eyebrow | Lexend Bold | Nunito ExtraBold | 22 | UPPERCASE, letter spacing 200, track color |

### Recurring motifs

1. **Vinyl badge:** a round record (Canva vinyl element) with a colored center label reading `TRACK 01`–`TRACK 05`. It sits top-right on each track slide.
2. **Music-staff underline:** five thin lines under each title, with 2–3 notes in palette colors.
3. **Lyric-sheet cards:** rounded cards (radius 24) with a white fill, a 3 px outline in the track color, and a small note icon.
4. **Note confetti:** ♪ ♫ shapes scattered at the edges.
5. **Footer:** a small treble-clef icon and the page number in a Holly Red circle.

**Transition:** Colour wipe ("Sapuan warna"). If it is not available, use Slide ("Meluncur").

### Illustration style

- **One** flat, bright, friendly Christmas set:
  - diverse carolers (kids, adults, and grandparents) with songbooks, lanterns, bells, and instruments
  - snowy streets and front doors
  - sleighs, holly, and fir trees
- The asset scout searches terms like:
  - "christmas carolers flat illustration"
  - "choir singing flat"
  - "christmas music notes"
  - "vinyl record"
  - "sleigh illustration"
- **One** rounded line-plus-color icon set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1: Cover**
- Centered layout, borrowing the reference's balanced cover idea.
- Eyebrow: `A CHRISTMAS SING-ALONG`
- Title (2 lines, centered, y ≈ 200):
  > Sing Along!
  > The Stories Behind Christmas Carols
- Pill (Pine Green, white text):
  > Sing along, learn along.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~1100 wide, lower half): a diverse group of carolers singing from songbooks under a snowy street lamp, with music notes swirling up in 4 colors.
- Decor: note confetti, holly, small stars.

**Slide 2: What Is a Carol?**
- Title: `What Is a Carol?`
- Statement card (Sky Note tint):
  > A carol is a joyful song sung at Christmas. The word comes from the Old French "carole" — a song people danced to in a circle.
- Two fact cards:
  - `Caroling` — Groups go door to door, singing for neighbors and spreading cheer.
  - `Wassailing` — In old England, singers wished their neighbors good health and were given warm drinks and treats.
- Hero (~520, left): carolers with a lantern singing at a friendly front door.

**Slide 3: Tonight's Setlist**
- Title: `Tonight's Setlist`
- A playlist card with 5 track rows. Each row has a mini vinyl badge in its track color, the carol name, and its origin:
  1. `Silent Night` · Austria · 1818
  2. `Jingle Bells` · USA · 1857
  3. `Deck the Halls` · Wales · words published 1862
  4. `We Wish You a Merry Christmas` · England · traditional
  5. `O Christmas Tree` · Germany · 1824
- Bonus row (dashed outline):
  > Bonus: Carols Around the World
- Hero (~440, right): a record player with a spinning colorful record and notes floating out.

### Builder B

**Slide 4: Track 01, Silent Night** (Sky Note)
- Vinyl badge `TRACK 01` · Eyebrow `TRACK 01 · AUSTRIA` · Title `Silent Night`
- Three lyric-sheet cards:
  - `The story` — First sung on Christmas Eve 1818 in the village of Oberndorf, Austria. A young priest wrote the words, and a schoolteacher wrote the music.
  - `A popular story` — It was first played on a guitar, because the church organ was broken.
  - `Today` — It has been translated into hundreds of languages.
- Hero (~520, left): two musicians, one with a guitar, singing in a snowy little village with glowing windows.

**Slide 5: Track 02, Jingle Bells** (Butter)
- Vinyl badge `TRACK 02` · Eyebrow `TRACK 02 · USA` · Title `Jingle Bells`
- Three lyric-sheet cards:
  - `The story` — Published in 1857 as "The One Horse Open Sleigh," it's about sleigh rides and races in the snow.
  - `Surprise!` — The words never mention Christmas.
  - `Out of this world` — In 1965, astronauts played it in space on a tiny harmonica and bells.
- Hero (~540, right): friends laughing in a horse-drawn sleigh with jingle bells.
- **Layout:** mirror Slide 4 (hero right, cards left).

**Slide 6: Track 03, Deck the Halls** (Pine Green)
- Vinyl badge `TRACK 03` · Eyebrow `TRACK 03 · WALES` · Title `Deck the Halls`
- Three lyric-sheet cards in a row under the hero:
  - `The tune` — The melody comes from an old Welsh New Year's song called "Nos Galan."
  - `The words` — The English lyrics we sing today were published in 1862.
  - `Fa la la!` — The cheerful "fa la la" lines are a refrain with no words needed — just fun to sing.
- Hero (~520, top center): a family hanging holly garlands and ribbons around a doorway.

### Builder C

**Slide 7: Track 04, We Wish You a Merry Christmas** (Tangerine)
- Vinyl badge `TRACK 04` · Eyebrow `TRACK 04 · ENGLAND` · Title `We Wish You a Merry Christmas`
- Statement card:
  > A traditional carol from England's West Country, sung by carolers going from house to house.
- Fun-fact speech bubble:
  > The carolers ask for "figgy pudding" — a steamed Christmas pudding — and promise not to leave until they get some!
- Hero (~540): carolers at a door while a neighbor holds out a round pudding with a holly sprig.

**Slide 8: Track 05, O Christmas Tree** (Plum)
- Vinyl badge `TRACK 05` · Eyebrow `TRACK 05 · GERMANY` · Title `O Christmas Tree`
- Three lyric-sheet cards:
  - `The story` — Based on the German folk song "O Tannenbaum." A popular version was written in 1824.
  - `The meaning` — It praises the fir tree for staying green all winter — a sign of faithfulness.
  - `Fun fact` — Early versions were about the evergreen tree itself, not about Christmas.
- Hero (~520): kids singing in a circle around a decorated fir tree outdoors in the snow.

**Slide 9: Carols Around the World**
- Title: `Carols Around the World`
- Four colorful cards in a 2 × 2 grid, each with a small object illustration (no globe and no travel path):
  - `Ukraine` — The tune of "Carol of the Bells" comes from "Shchedryk," a Ukrainian New Year's song.
  - `Philippines` — Children go caroling with homemade instruments, like tambourines made from bottle caps.
  - `Australia` — Carols by Candlelight brings crowds together outdoors on warm summer nights.
  - `Mexico` — During Las Posadas, people sing as they walk from house to house.
- Decor: note confetti, 4 small instrument icons (bells, tambourine, candle, maracas).

### Builder D

**Slide 10: Host a Caroling Night**
- Title: `Host a Caroling Night`
- Six numbered steps, each number on a mini vinyl badge in a different color:
  1. Pick 4–5 songs everyone knows.
  2. Print simple song sheets.
  3. Practice once together.
  4. Bring lanterns or flashlights.
  5. Ask neighbors before you sing.
  6. Share treats and warm drinks after.
- Hero (~480): a small group walking down a snowy street with lanterns and song sheets.

**Slide 11: Sing-Along Tips**
- Title: `Sing-Along Tips`
- Four tip cards, each a different color, with an icon:
  - `Warm up` — Hum and do gentle lip trills for one minute.
  - `Breathe deep` — Breathe from your belly, not your shoulders.
  - `Everyone joins` — Give kids bells and shakers to play along.
  - `Have fun` — Smiles matter more than perfect notes!
- Hero (~460): a kid shaking jingle bells next to a teen playing a guitar.

**Slide 12: Keep Singing!**
- Title centered, Alfa Slab One 130, Holly Red:
  > Keep Singing!
- Subtitle:
  > Wishing you a season full of music and joy.
- Three contact pills (Pine / Sky Note / Plum, white text):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): a long line of diverse carolers singing together, with music notes rising in every palette color.

## 4. Speaker notes

- **Slides 4–9:** Song histories have several versions and some legends. Present them as popular stories, and check details before presenting.
- **Slide 10:** Respect quiet hours, and always ask neighbors first.

## 5. Deck-specific QA

- [ ] Each track slide uses its own track color for the vinyl badge, eyebrow and card outlines.
- [ ] Song Ivory background on all 12 slides; no dark backgrounds.
- [ ] No gold foil, glitter, church interiors, stained glass, or hymn-sheet columns.
- [ ] No song lyrics beyond the titles quoted in §3.
- [ ] Slides 4–6 do not share the same layout (left / right / top hero).
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier Christmas decks (§0).
