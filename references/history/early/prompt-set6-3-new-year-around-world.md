# Prompt 3/3 — "Midnight Around the World: New Year 2027" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set6-christmas-gamenight-newyear\canva-shared-pipeline.md`.

That file holds:
- §A — hard rules
- §B — colorful brief and richness checklist
- §C — pipeline, builder brief, QA, and report

Deck slug: `new-year-around-world`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Midnight Around the World: New Year 2027"**. It follows midnight across time zones and shows how different countries welcome the new year.

**Reference (direction only):** https://www.canva.com/templates/EAG74O7fAb4/ ("Gold and Black Modern New Year Presentation").

- **Borrow the idea:**
  - a modern, bold, clean layout
  - strong display titles and big numerals
  - a celebratory countdown feeling
- **Build from scratch.** Do not copy any layout, image, or text from the reference.

**Must also differ from the earlier New Year decks in this project:**
- "New Year's Eve 2027" (midnight navy, champagne gold, art-deco arches, serif "2027" sunburst, clock motif)
- "New Year 2027: Goals & Fresh Starts" (lilac cream, Righteous titles, violet → pink → tangerine gradient, goal-setting people, vision board)

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Modern bold layout | A **bright, colorful "world countdown"** look on a light pearl background. **Not** black and gold |
| Big numerals | Numerals are **local midnight times** on colorful clock badges (e.g. `00:00 TOKYO`), not a giant gold year |
| Celebration | Each country has its **own color** and a **flat landmark scene** with diverse people celebrating |
| — | **No** black backgrounds, **no** gold foil or glitter textures, **no** champagne glasses or bottles, **no** art-deco arches, **no** goal-setting or vision-board items, **no** full-slide firework bursts behind titles (max 2 small fireworks per slide) |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Pearl Lilac | `#F5F2FF` | Main background |
| Ink | `#16133A` | Text |
| Electric Blue | `#2E6BFF` | Titles, Scotland |
| Aqua | `#12C2B5` | Accent, Indonesia |
| Violet | `#7A3CFF` | Accent, Japan |
| Hot Coral | `#FF5A5F` | Accent, Philippines |
| Sun Gold | `#FFC531` | Accent, Spain |
| Lime Spark | `#B6F03C` | Accent, Brazil |
| Party Pink | `#FF6FB5` | Accent, highlights |

**Aurora gradient** (slides 1, 3 and 12 only): Aqua → Electric Blue → Violet, diagonal. Text on it is white.

**Country colors** (title highlight, clock badge, cards):

| Country | Color |
|---|---|
| Japan | Violet |
| Philippines | Hot Coral |
| Indonesia | Aqua |
| Spain | Sun Gold |
| Scotland | Electric Blue |
| Brazil | Lime Spark |

Every slide has confetti dots and streamers in 3+ palette colors.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Archivo Black | Montserrat Black | 76–90 | Ink, with a country-color highlight bar behind the key word |
| Clock numerals | Archivo Black | Montserrat Black | 48–64 | White on the clock badge |
| Body | DM Sans Medium | Nunito | 26–28 | Ink |
| Eyebrow | DM Sans Bold | Nunito ExtraBold | 22 | UPPERCASE, letter spacing 200, country color |

### Recurring motifs

1. **Clock badge:** a round badge in the country color with `00:00` and the city name, top-right on each country slide.
2. **Time-zone ribbon:** a thin horizontal band of colored segments across the top edge; the current country's segment is highlighted.
3. **Landmark scene:** a flat illustration of the country's landmark with people celebrating.
4. **Tradition cards:** rounded cards (radius 28) with a tinted fill, a 3 px outline in the country color, and an icon.
5. **Small fireworks:** 1–2 small colorful bursts per slide, never behind a title.
6. **Footer:** a dotted world-line and the page number in an Electric Blue circle.

**Transition:** Slide (left to right, like time moving across the map).

### Illustration style

- **One** flat, modern, bright travel-and-celebration set: landmarks, diverse people, food, fireworks, confetti.
- The asset scout searches terms like:
  - "new year celebration flat illustration"
  - "people celebrating fireworks flat"
  - "landmark flat illustration" + country name
  - "world clock icon"
- **One** clean line-plus-color icon set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (Aurora gradient)
- Eyebrow: `NEW YEAR 2027`
- Title at (120, 220), width 980, 2 lines, white:
  > Midnight Around the World
- Pill (Lime Spark, Ink text):
  > One night. Many time zones. Countless traditions.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~860, right): a flat globe ringed by a chain of colorful clock badges, with diverse people waving from small landmark scenes and 2 small fireworks.
- Decor: confetti and streamers.

**Slide 2 — The Longest Countdown**
- Title: `The Longest Countdown`
- Big statement card (Electric Blue tint):
  > Because of time zones, New Year arrives in waves. It takes about 26 hours for midnight to reach every place on Earth.
- Two fact cards:
  - `First to celebrate` — Kiribati's Line Islands (UTC+14).
  - `Among the last` — American Samoa (UTC−11).
- Hero (~480): a row of 6 colorful clocks, each a different color, all ticking toward midnight.

**Slide 3 — Our Journey Tonight** (Aurora gradient)
- Title (white): `Our Journey Tonight`
- A horizontal route line left to right with 6 clock-badge stops, each in its country color, with the city and its UTC offset:
  1. `Tokyo, Japan` · UTC+9
  2. `Manila, Philippines` · UTC+8
  3. `Jakarta, Indonesia` · UTC+7
  4. `Madrid, Spain` · UTC+1
  5. `Edinburgh, Scotland` · UTC+0
  6. `Rio de Janeiro, Brazil` · UTC−3
- Decor: small airplane icon on the route, confetti.

### Builder B

**Slide 4 — Japan** (Violet)
- Clock badge `00:00 TOKYO` · Eyebrow `STOP 1 · JAPAN` · Title `Japan: Bells & Noodles`
- Three tradition cards:
  - `Joya no Kane` — Buddhist temples ring their bells 108 times to clear away the worries of the old year.
  - `Toshikoshi Soba` — Long buckwheat noodles eaten on New Year's Eve for a long life.
  - `Hatsumode` — The first shrine or temple visit of the new year.
- Hero (~520): a big temple bell with a family nearby holding bowls of noodles.

**Slide 5 — Philippines** (Hot Coral)
- Clock badge `00:00 MANILA` · Eyebrow `STOP 2 · PHILIPPINES` · Title `Philippines: Round & Lucky`
- Three tradition cards:
  - `Round fruits` — Families display round fruits, often 12, for good fortune — their shape looks like coins.
  - `Polka dots` — Wearing dots is said to bring prosperity.
  - `Loud welcome` — Horns, pots and noise-makers chase away bad luck.
- Hero (~520): a table piled with colorful round fruits and a family in polka-dot outfits.

**Slide 6 — Indonesia** (Aqua)
- Clock badge `00:00 JAKARTA` · Eyebrow `STOP 3 · INDONESIA` · Title `Indonesia: Fireworks & Feasts`
- Three tradition cards:
  - `Paper trumpets` — Colorful *terompet* sound out across towns at midnight.
  - `Grill night` — Families and friends gather for grilled corn, fish and satay.
  - `City countdowns` — Crowds watch fireworks together in city squares.
- Hero (~520): a family grilling corn in a backyard while small fireworks light the sky.

### Builder C

**Slide 7 — Spain** (Sun Gold)
- Clock badge `00:00 MADRID` · Eyebrow `STOP 4 · SPAIN` · Title `Spain: 12 Lucky Grapes`
- Statement card:
  > At midnight, people eat 12 grapes — one with each chime of the clock — for 12 months of good luck.
- Fun-fact bubble:
  > Crowds gather at Puerta del Sol in Madrid to eat their grapes with the famous clock.
- Hero (~540): friends with bowls of grapes in front of a clock tower.

**Slide 8 — Scotland** (Electric Blue)
- Clock badge `00:00 EDINBURGH` · Eyebrow `STOP 5 · SCOTLAND` · Title `Scotland: Hogmanay`
- Three tradition cards:
  - `First-footing` — The first guest after midnight brings small gifts, like shortbread, for luck.
  - `Auld Lang Syne` — Friends cross arms, join hands and sing together.
  - `Street parties` — Edinburgh hosts one of the world's best-known New Year festivals.
- Hero (~520): people in colorful scarves joining hands and singing in a snowy street with a castle behind.

**Slide 9 — Brazil** (Lime Spark)
- Clock badge `00:00 RIO` · Eyebrow `STOP 6 · BRAZIL` · Title `Brazil: White & the Waves`
- Three tradition cards:
  - `Wear white` — Many people dress in white for peace in the new year.
  - `Seven waves` — Jump over seven waves and make a wish with each one.
  - `Flowers for the sea` — Some offer flowers to Iemanjá, the sea goddess.
- Hero (~520): a beach at night with people in white, small fireworks over the water.

### Builder D

**Slide 10 — More Fun Traditions**
- Title: `More Fun Traditions`
- Four colorful cards in a 2 × 2 grid, each with a small landmark or object illustration:
  - `Denmark` — Old plates are smashed on friends' doorsteps; a big pile means lots of friends.
  - `Colombia` — Some people walk around the block with an empty suitcase, hoping for a year of travel.
  - `Greece` — A *vasilopita* cake hides a coin that brings luck to whoever finds it.
  - `Ecuador` — Families burn "año viejo" figures to say goodbye to the old year.
- Decor: confetti, 1 small firework.

**Slide 11 — Start Your Own Tradition**
- Title: `Start Your Own Tradition`
- Four numbered idea cards, each a different color:
  1. Write a letter to your future self.
  2. Fill a jar with the year's best moments.
  3. Try a lucky food from another country.
  4. Share three wishes at midnight.
- Hero (~480): a family at home counting down together, with a homemade clock and party hats.

**Slide 12 — Happy New Year!** (Aurora gradient)
- Title centered, Archivo Black 140, white:
  > Happy New Year!
- Subtitle:
  > Wherever you are, may 2027 be bright.
- Three contact pills (Lime / Pink / Sun Gold, Ink text):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): a colorful skyline of landmarks from the deck, with diverse people joining hands and 2 small fireworks.

## 4. Speaker notes

- **Slides 4–10:** Traditions vary by family and region. Check current details before presenting.
- **Slide 2:** Time-zone facts can change; confirm offsets for the year you present.

## 5. Deck-specific QA

- [ ] Each country slide uses its own country color for clock badge, title highlight and cards.
- [ ] Aurora gradient only on slides 1, 3 and 12; all others Pearl Lilac.
- [ ] No black, no gold foil, no champagne, no art-deco items, max 2 small fireworks per slide.
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier New Year decks (§0).
