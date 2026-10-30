# Prompt set8-7 — "Digestive System Disorders" (Digestion Station, colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A pages 1–3, B pages 4–6, C pages 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set8-health\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, the **font whitelist** and the **10-slide rule** (builders: A = 1–3, B = 4–6, C = 7–10)

Deck slug: `digestive-station`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Digestive System Disorders"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAGpZIqxd9U/ ("Digestive System Presentation").

- **Borrow the idea:** a clean, illustrated, educational **organ-diagram structure**:
  1. what the digestive system is and what each organ does
  2. one slide per common disorder (what it is, signs, care and prevention)
  3. healthy habits
  4. when to get help

  Also borrow the **friendly labeled organ diagram** idea for the overview slide.
- **Build from scratch.** Only the reference's title is known; do not open it to copy pages or elements.

**Not a repeat.** This deck must look different from the earlier decks in this project (see §1).

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Clean, illustrated, educational organ diagram | A **"Digestion Station" concept**: the digestive tract is drawn as a colorful **metro / subway line map** (straight lines with 45° turns, round station dots, line roundels). Not a winding "Food's Journey" path. |
| One slide per disorder, same card structure | Each disorder slide is a **"station"** with an Ink **station sign**, its own **line color** and a cute flat **organ character standing on the platform**. **No** organ buddies in circle badges, **no** fruit-shaped number badges. |
| Friendly, plain-language health copy | Info sits on **metro-ticket cards** (white, colored top strip, punched half-circle notches). **No** cloud cards, **no** shield badges, **no** chain links. |
| Light, airy background | **Cloud Mint** background with a faint transit grid. **No** peach cream, **no** sky-and-clouds, **no** ECG line, neuron network, water flow or blueprint grid. |
| — | Fonts **Archivo Black + DM Sans** only. **No** Lilita One, Rubik or Fredoka. Transition **Slide (Meluncur)**, not Push or Fade. |
| — | **No** stock photos, **no** gross imagery (no vomit or stool depictions), **no** logos or real transit-brand marks. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Cloud Mint | `#EEF9F4` | Background (with a faint Ink 5 % transit grid) |
| Ink | `#1D2340` | Text, station signs, station-dot outlines |
| Tangerine | `#FF7A2F` | Esophagus Line (GERD) |
| Magenta | `#D62A80` | Stomach Line (Peptic Ulcer) |
| Sky Blue | `#2F9BF0` | Small Intestine Line (Gastroenteritis) |
| Violet | `#7B4DFF` | Large Intestine Line (IBS) |
| Lime | `#8CD43A` | Branch Line: liver, gallbladder, pancreas (Gallstones) |
| Sunshine | `#FFC928` | Mouth Line, highlights, "You are here" marker |
| White | `#FFFFFF` | Ticket cards, station dots |

**Color rules:**
- Each station slide uses its line color for the line, the roundel, the ticket-card top strips and the platform under the organ character:

  | Station | Line | Roundel code | Line color |
  |---|---|---|---|
  | GERD (Acid Reflux) | Esophagus Line | `E` | Tangerine |
  | Peptic Ulcer | Stomach Line | `S` | Magenta |
  | Gastroenteritis (Stomach Flu) | Small Intestine Line | `SI` | Sky Blue |
  | Irritable Bowel Syndrome (IBS) | Large Intestine Line | `LI` | Violet |
  | Gallstones | Branch Line | `B` | Lime |

- Every slide shows **at least 4 palette colors**: its own line color plus at least 3 other line colors in the footer mini-map, decor and icons.
- **Contrast:** white text only on Ink, Magenta or Violet. Ink text on Tangerine, Sky Blue, Lime, Sunshine and White. Colored text is never used for body copy.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Archivo Black | — | 72–84 (cover 96, Thank You 140) | White on the Ink station sign, or Ink on Cloud Mint |
| Body | DM Sans Medium | DM Sans | 26–28 | Ink |
| Card headers, pills | DM Sans Bold | — | 28 | Ink (or white on Ink/Magenta/Violet) |
| Eyebrow | DM Sans Bold | — | 22, UPPERCASE, letter spacing 200 | Ink, next to a line-color dot |

Both fonts are on the shared whitelist (§D). In the skeleton, fonts are set as the family name plus the bold flag (`DM Sans` + bold), never "DM Sans Bold".

### Recurring motifs

1. **Metro line:** a thick (16 px) rounded line in the slide's line color, running horizontally with one 45° turn, with white station dots (Ink 4 px outline). Built from plain shapes in the skeleton.
2. **Station sign:** an Ink rounded plate (radius 20) holding the title in white Archivo Black, with a line-color **roundel** on its left showing the line code (`E`, `S`, `SI`, `LI`, `B`).
3. **Organ character on a platform:** a cute flat organ character (Canva element) standing on a short line-color platform bar. Never inside a circle badge.
4. **Ticket cards:** white rounded cards (radius 24) with a 14 px line-color top strip and two Cloud Mint half-circle "punch" notches on the left and right edges. Card headers: `What it is`, `Signs`, `Care & prevention`.
5. **Footer mini-map:** a small six-dot line strip bottom-left (one dot per line color) with a Sunshine **"You are here"** ring on the current line, plus the page number in an Ink roundel bottom-right.
6. **Fun-fact bubble:** a white speech bubble with a 3 px line-color outline and a small train icon.

**Transition:** Slide (Meluncur), applied to all pages with "Terapkan ke semua halaman".

### Illustration style

- One flat, cheerful, rounded set with:
  - cute **kawaii organ characters** (esophagus, stomach, intestines, liver, gallbladder, pancreas) with simple faces
  - diverse people eating, drinking water, washing hands, relaxing, visiting a doctor
  - colorful healthy food (fruit, vegetables, grains, water)
  - a cute flat train / metro car
- One consistent icon set (bold outline, rounded).
- **Canva Elements search terms** (asset scout starts here):
  - Organs: `cute stomach character`, `kawaii organ`, `cute intestine cartoon`, `cute liver character`, `gallbladder cartoon`, `esophagus illustration flat`, `digestive system flat illustration`
  - Metro: `subway map line`, `metro station sign`, `cute train flat`, `train icon`, `ticket icon`, `map pin`
  - People / food: `family healthy meal flat`, `washing hands illustration`, `drinking water flat`, `yoga relax flat illustration`, `doctor patient flat illustration`, `fiber food flat`
  - Icons: `digestion icon bold outline`, `heartburn icon`, `pill icon outline`, `soap icon`, `water glass icon`, `warning icon rounded`
  - Decor: `sparkle doodle`, `confetti dots`, `dashed route line`, `circle dots pattern`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (text left, hero right, metro line along the bottom)
- Eyebrow: `DIGESTIVE HEALTH EDUCATION`
- Title at (120, 220), width 940, 3 lines, Archivo Black 96, Ink:
  > Digestive System Disorders
- Station-sign pill (Ink, white text, Sunshine roundel `ALL`):
  > Welcome to Digestion Station
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero, right side (~760 w): a cute flat metro train whose cars carry smiling organ characters (stomach, intestines, liver), with colorful food sparkles around it.
- A six-color metro line (Sunshine → Tangerine → Magenta → Sky Blue → Violet, Lime branch) sweeps across the bottom with white station dots.
- Decor: sparkles, confetti dots.

**Slide 2 — Your Digestion Line** (full-width metro map)
- Eyebrow: `ROUTE MAP`
- Title: `Your Digestion Line`
- A horizontal metro map across the slide. Main line stations (left to right), each a white dot with a line-color roundel and a small ticket label with a one-line job:
  - `Mouth` (Sunshine) — Chews food and mixes it with saliva.
  - `Esophagus` (Tangerine) — Pushes food down to the stomach.
  - `Stomach` (Magenta) — Churns food with acid and enzymes.
  - `Small Intestine` (Sky Blue) — Absorbs most nutrients into the blood.
  - `Large Intestine` (Violet) — Absorbs water and forms waste.
- Branch Line (Lime) drops down from between Stomach and Small Intestine with three stations:
  - `Liver` — Makes bile to help digest fat.
  - `Gallbladder` — Stores bile until it's needed.
  - `Pancreas` — Makes digestive enzymes.
- Hero, bottom-right (~520 w): a friendly flat digestive-system diagram character waving.
- Fun-fact bubble:
  > The small intestine is the longest part of the digestive tract.

**Slide 3 — GERD (Acid Reflux)** (Esophagus Line, Tangerine; hero left, tickets stacked right)
- Eyebrow: `STATION 03 · ESOPHAGUS LINE`
- Station sign with roundel `E`: `GERD (Acid Reflux)`
- Three ticket cards:
  - **What it is:** Stomach acid often flows back up into the esophagus and irritates its lining.
  - **Signs:** Heartburn (a burning feeling in the chest), a sour taste in the mouth, and trouble swallowing.
  - **Care & prevention:** Eat smaller meals, wait about 3 hours after eating before lying down, limit trigger foods, and don't smoke.
- Hero, left (~520 w): a cute esophagus-and-stomach character on a Tangerine platform, next to a person sitting upright after a meal.
- Fun-fact bubble:
  > Heartburn more than twice a week? Talk to a doctor.

### Builder B

**Slide 4 — Peptic Ulcer** (Stomach Line, Magenta; ticket row on top, hero bottom center)
- Eyebrow: `STATION 04 · STOMACH LINE`
- Station sign with roundel `S`: `Peptic Ulcer`
- Three ticket cards in a row:
  - **What it is:** An open sore in the lining of the stomach or the first part of the small intestine.
  - **Signs:** A burning or gnawing pain in the upper belly, bloating, and feeling full quickly.
  - **Care & prevention:** See a doctor for testing and treatment. Use pain relievers only as directed, and avoid smoking and alcohol.
- Hero, bottom center (~520 w): a cute stomach character on a Magenta platform, holding a doctor's clipboard.
- Fun-fact bubble:
  > Most ulcers are caused by H. pylori bacteria or long-term use of NSAID pain relievers. Stress and spicy food don't cause ulcers, but may make symptoms worse.

**Slide 5 — Gastroenteritis (Stomach Flu)** (Small Intestine Line, Sky Blue; tickets stacked left, hero right)
- Eyebrow: `STATION 05 · SMALL INTESTINE LINE`
- Station sign with roundel `SI`: `Gastroenteritis (Stomach Flu)`
- Three ticket cards:
  - **What it is:** An infection of the stomach and intestines, usually caused by viruses such as norovirus or rotavirus.
  - **Signs:** Diarrhea, nausea, vomiting, stomach cramps and sometimes a fever.
  - **Care & prevention:** Drink plenty of fluids or oral rehydration solution (ORS), wash hands with soap, and keep food clean and safe.
- Hero, right (~520 w): a child washing hands with soap next to a glass of water, with a cute intestine character on a Sky Blue platform. **No** sick or vomiting imagery.
- Fun-fact bubble:
  > Despite its name, it is not caused by the influenza (flu) virus.

**Slide 6 — Irritable Bowel Syndrome (IBS)** (Large Intestine Line, Violet; sign + hero top, ticket row bottom)
- Eyebrow: `STATION 06 · LARGE INTESTINE LINE`
- Station sign with roundel `LI`: `Irritable Bowel Syndrome (IBS)`
- Three ticket cards in a row along the bottom:
  - **What it is:** A common long-term condition where the gut is extra sensitive, causing belly pain and changes in bowel habits.
  - **Signs:** Belly pain or cramps, bloating, and diarrhea, constipation, or both.
  - **Care & prevention:** Eat regular meals, notice trigger foods, manage stress, stay active, and follow your doctor's plan.
- Hero, top right (~520 w): a person relaxing with gentle stretching, with a calm intestine character on a Violet platform.
- Fun-fact bubble:
  > IBS does not damage the intestines, but it can affect daily life.

### Builder C

**Slide 7 — Gallstones** (Branch Line, Lime; vertical branch line with tickets, hero right)
- Eyebrow: `STATION 07 · BRANCH LINE`
- Station sign with roundel `B`: `Gallstones`
- A vertical Lime branch line on the left with three station dots; each dot leads to a ticket card:
  - **What it is:** Hard, pebble-like pieces that form in the gallbladder from substances in bile.
  - **Signs:** Many people have no symptoms. A stone that blocks a duct can cause sudden pain in the upper right belly, sometimes with nausea.
  - **Care & prevention:** Keep a healthy weight, avoid crash diets, eat fiber-rich foods, and see a doctor if pain comes.
- Hero, right (~520 w): cute liver, gallbladder and pancreas characters waiting together on a Lime branch-line platform.
- Fun-fact bubble:
  > The gallbladder stores bile made by the liver to help digest fat.

**Slide 8 — Gut-Friendly Habits** (hero left, 2 × 3 ticket grid right)
- Eyebrow: `EVERY STOP COUNTS`
- Title: `Gut-Friendly Habits`
- Six ticket tiles, each with a different line-color top strip, a numbered roundel and an icon:
  1. `Eat more fiber: fruits, vegetables & whole grains`
  2. `Drink enough water every day`
  3. `Wash your hands before eating`
  4. `Eat smaller meals, slowly`
  5. `Stay active every day`
  6. `Limit alcohol and don't smoke`
- Hero, left (~520 w): a happy diverse family sharing a colorful healthy meal, with a smiling stomach character.

**Slide 9 — When to See a Doctor** (warning board left, hero right, disclaimer bar bottom)
- Eyebrow: `PLEASE STOP HERE`
- Title: `When to See a Doctor`
- A white "service alert" board with a Magenta border and ! bullets:
  - ! Severe or long-lasting belly pain
  - ! Vomiting blood, or blood in your stool
  - ! Signs of dehydration: very little urine, dizziness, a dry mouth
  - ! Trouble swallowing or unexplained weight loss
  - ! Yellowing of the skin or eyes
  - ! Diarrhea or vomiting that does not stop
- Hero, right (~480 w): a friendly doctor talking with a smiling patient, with a cute stomach character beside them.
- Disclaimer bar (Ink, white text):
  > For education only — not a substitute for professional medical advice.

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Archivo Black 140, Ink, over a Sunshine station roundel shape.
- Subtitle:
  > Next stop: a healthier gut.
- Three contact pills (Magenta / Violet / Sky Blue):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources:
  > Sources: World Health Organization (WHO), U.S. NIH (NIDDK), Kementerian Kesehatan RI
- Hero along the bottom (~1300 w): a long cute metro train with organ-character passengers waving, on a six-color line.

## 4. Speaker notes

- Slides 3–9:
  > General information only. Verify with current WHO / NIDDK / Kemenkes guidance before presenting.
- Slide 2:
  > Walk the route from Mouth to Large Intestine, then the Branch Line. Each disorder slide is a stop on this map.

## 5. Deck-specific QA

- [ ] 10 pages in order; each station slide uses its line color, roundel code, platform and organ character.
- [ ] Only Archivo Black and DM Sans; no Lilita One, Rubik or Fredoka.
- [ ] Medical text matches §3 word for word; disclaimer present on slide 9.
- [ ] No stock photos, no vomit or stool depictions, no logos or real transit-brand marks.
- [ ] No circle organ badges, fruit number badges, winding path, cloud cards, shield badges, chain links, ECG line, neuron network, water flow or blueprint grid.
- [ ] Footer mini-map and page roundel on every slide; Slide (Meluncur) transition on all pages.
