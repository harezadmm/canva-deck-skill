# Prompt set8-8 — "Cardiovascular Diseases and Heart Health" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set8-health\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `heart-health`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Cardiovascular Diseases and Heart Health"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHO4KJNgKw/ ("Red Blue and White Illustrated Cardiovascular Health Presentation").

- **Borrow the idea:**
  1. a friendly **illustrated medical style** (flat drawings, not photos);
  2. **red as the heart color**;
  3. a clear medical flow:
     1. how the heart works
     2. risk factors
     3. the main conditions, one per slide
     4. warning signs
     5. numbers to know
     6. prevention
- **Build from scratch.**

**Not a repeat.** This deck must look different from the earlier disease decks in this project and from the other set8 decks.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Illustrated medical style | A **"Heartbeat" concept**: a colorful **ECG pulse line** runs across every slide and **changes color per section**. |
| Red as the heart color | **Not** a red/blue/white-only look. A warm **Blush Cream** background with **six bright accents**, at least 4 per slide. |
| One condition per slide | Content sits in rounded **"monitor screen" cards** (colored header bar with three status dots). **No** plain white boxes copied from the reference. |
| Medical subject | Heroes are a cute flat **heart buddy** character and diverse flat people. **No** stock photos, **no** realistic anatomy or gore, **no** logos. |
| — | **No** chain links, shield badges, Rubik or cobalt ("Infectious Diseases"). **No** sky clouds, cloud cards, lung buddy or Fredoka ("Respiratory"). **No** peach-cream winding path, fruit badges or Lilita One **title pills** (earlier "Digestive"). **No** metro map, neuron network, water flow or blueprint grid (other set8 decks). |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Blush Cream | `#FFF4F1` | Background (with soft tinted blobs) |
| Ink Plum | `#2A1B3D` | Text, titles |
| Heart Red | `#D92B45` | Heart, warnings, cover; white text allowed on it |
| Sky Blue | `#3AA0FF` | Accent; Ink text on it |
| Mint | `#2FCB98` | Prevention, healthy; Ink text on it |
| Sunny Yellow | `#FFC83D` | Highlights, basics; Ink text on it |
| Grape | `#7B4FE0` | Accent; white text allowed on it |
| Peach | `#FF9A76` | Accent; Ink text on it |
| White | `#FFFFFF` | Card bodies |

**Color rules:**
- The **ECG pulse line** changes color per section:

  | Section | Slides | ECG line color |
  |---|---|---|
  | Welcome | 1 | Heart Red |
  | Heart basics | 2–3 | Sunny Yellow |
  | High blood pressure | 4 | Grape |
  | Coronary artery disease | 5 | Peach |
  | Heart attack | 6 | Heart Red |
  | Heart failure | 7 | Sky Blue |
  | Prevention | 8–9 | Mint |
  | Finale | 10 | Rainbow (Red → Sunny → Mint → Sky → Grape) |

- Each condition slide (4–7) uses its section color for the eyebrow chip, card header bars, footer heart and heart-buddy accessory.
- Cards and tiles on slides 2, 3, 8 and 9 rotate through the palette so that **at least 4 accents** are clearly visible on every slide.
- White text only on Heart Red and Grape (contrast ≥ 4.5:1). Use Ink Plum text on Sky, Mint, Sunny and Peach.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Lilita One | — (whitelist; re-set to Lilita One if substituted) | 76–96 (Thank You 140), no pill or highlight behind it | Ink Plum |
| Body | Poppins | — | 26–28 | Ink Plum |
| Card headers / labels | Poppins Bold | — | 26–28 | white on Red/Grape, Ink elsewhere |
| Eyebrow | Poppins Bold | — | 22, UPPERCASE, letter spacing 200, in a small tinted chip | Ink Plum |
| Monitor readings (slide 8) | Lilita One | — | 44 | section color on an Ink screen |

Only these 2 families. Both are on the §D whitelist.

### Recurring motifs

1. **ECG pulse line:** a thin (≈6 px) heartbeat line with one or two spikes running edge to edge, usually in a band right under the title. Colored by section (see table). Canva element, recolored.
2. **Heart buddy:** a cute flat heart character (face, little arms and legs) that appears on every slide — as the hero, or as a small character riding the ECG line or peeking beside the title. Same character design on every slide; only the pose and accessory change.
3. **Monitor-screen cards:** white rounded cards (radius 28) with a 4 px outline and a **colored header bar** carrying the card label and **three small white status dots** at its left, like a vital-signs monitor.
4. **Pulse confetti:** tiny plus signs, dots and mini hearts in palette colors around heroes and corners.
5. **Footer:** a small **heart shape** in the section color holding the page number, bottom right.

**Transition:** Dissolve ("Larut"), applied to all pages.

### Illustration style

- One flat, cheerful, rounded set with:
  - the heart buddy character (and simple friendly organ/vessel diagrams — no realistic anatomy, no blood or gore)
  - diverse people of all ages: walking, cycling, eating healthy food, visiting a nurse
  - simple health objects: stethoscope, blood-pressure monitor, pill organizer, phone
- One consistent icon set (bold rounded line icons, filled with palette colors).

**Search terms for the asset scout** (Canva Elements, English keywords):
- `cute heart character`, `heart mascot flat`, `heart cartoon stethoscope`
- `ecg line`, `heartbeat line`, `pulse line`
- `heart anatomy flat illustration`, `artery plaque illustration`, `blood vessel flat`
- `blood pressure monitor flat`, `doctor patient flat illustration`, `nurse blood pressure`
- `heart attack illustration flat`, `calling ambulance phone illustration`
- `family cycling flat illustration`, `jogging people flat`, `healthy food plate flat`
- `plus sign confetti`, `heart confetti`, `medical doodle`
- Icons: `heart health icon`, `cholesterol icon`, `diabetes icon`, `no smoking icon`, `salt shaker icon`, `sleep icon`, `stethoscope icon`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (title left, hero right)
- Eyebrow chip (Heart Red tint): `HEART HEALTH EDUCATION`
- Title at (120, 220), width 900, Lilita One 96, 3 lines:
  > Cardiovascular / Diseases and / Heart Health
- Pill (Heart Red, white text):
  > Keep the beat strong.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- A row of three tinted circles (Sky / Mint / Sunny) with icons: stethoscope, apple, running shoe.
- Hero, right side (~760): a big happy heart buddy with a stethoscope beside a monitor screen showing a heartbeat, with people jogging and cycling around.
- ECG line: Heart Red, full width along the bottom band (y ≈ 880).
- Decor: soft blobs and pulse confetti in the top-left corner.

**Slide 2 — How Your Heart Works** (center hero, 4 callouts)
- Title (centered): `How Your Heart Works`
- ECG line: Sunny Yellow, under the title.
- Center hero: a friendly flat heart diagram showing chambers, valves and vessels, ~520 wide. No realistic anatomy.
- Four monitor cards (two left, two right), each with an icon and a short connector line to the diagram:
  - `Heart Muscle` (Heart Red) — A strong muscle about the size of your fist that pumps blood all day and night.
  - `Four Chambers` (Sky Blue) — Two upper atria receive blood; two lower ventricles pump it out.
  - `Valves` (Grape) — Four valves open and close to keep blood flowing one way.
  - `Blood Vessels` (Mint) — Arteries carry blood away from the heart; veins bring it back.
- Fun-fact bubble (Peach tint):
  > At rest, an adult heart usually beats about 60–100 times a minute.
- Heart buddy waving, top right.

**Slide 3 — Risk Factors** (3 × 2 tile grid left, hero right)
- Eyebrow chip (Sunny tint): `RISK FACTORS`
- Title: `What Raises Your Risk?`
- ECG line: Sunny Yellow, under the title.
- Six tinted monitor tiles in a 3 × 2 grid, each with a white icon circle and a label:
  - `High blood pressure` (Heart Red)
  - `High cholesterol` (Sunny Yellow)
  - `Smoking & tobacco` (Grape)
  - `Diabetes` (Sky Blue)
  - `Physical inactivity` (Peach)
  - `Unhealthy diet & obesity` (Mint)
- Hero, right (~480): a worried-but-cute heart buddy surrounded by soda, fast food and a cigarette with a crossed-out sign.
- Bottom banner (Mint tint):
  > The good news: many risk factors can be prevented or controlled.

### Builder B

**Slide 4 — High Blood Pressure (Hypertension)** (theme Grape; hero left, cards right)
- Eyebrow chip: `OFTEN NO SYMPTOMS`
- Title, 2 lines: `High Blood Pressure` / `(Hypertension)`
- Three stacked monitor cards (Grape header bars):
  - **What it is:** The force of blood pushing on artery walls stays too high, so the heart has to work harder.
  - **Why it matters:** It often has no symptoms, but it raises the risk of heart attack, stroke and kidney disease.
  - **Managing it:** Check it regularly, eat less salt, stay active, don't smoke, and take medicines as prescribed.
- Hero, left (~520): a person relaxing on a sofa beside a big pressure gauge (needle in the red zone), with the heart buddy holding a salt shaker and a "less" sign.
- Fun-fact bubble (under the hero):
  > Many people with high blood pressure don't know they have it — get checked.
- ECG line: Grape, full width along the bottom band.
- Heart buddy (Grape accessory) beside the title.

**Slide 5 — Coronary Artery Disease** (theme Peach; cards row on top, hero bottom center)
- Eyebrow chip: `THE MOST COMMON TYPE`
- Title (centered): `Coronary Artery Disease`
- ECG line: Peach, under the title.
- Three monitor cards in a row (Peach header bars):
  - **What it is:** Fatty deposits (plaque) build up inside the heart's arteries, making them narrow and stiff.
  - **Signs:** Chest pain or pressure (angina), often during activity, and shortness of breath. For some people, a heart attack is the first sign.
  - **Lowering the risk:** Don't smoke, eat heart-healthy foods, stay active, and manage cholesterol, blood pressure and blood sugar.
- Hero, bottom center (~680): a simple flat comparison of a healthy artery and an artery narrowed by plaque. Friendly, no gore.
- Two label pills beside the hero:
  - `Healthy artery` (Mint)
  - `Narrowed by plaque` (Peach)
- Heart buddy pointing at the artery, bottom left.

**Slide 6 — Heart Attack — Warning Signs** (theme Heart Red; list card left, hero right)
- Eyebrow chip: `EMERGENCY`
- Title: `Heart Attack — Warning Signs`
- ECG line: Heart Red, under the title.
- Intro card (Heart Red tint):
  > A heart attack happens when blood flow to part of the heart muscle is blocked.
- Monitor card `Warning signs` (Heart Red header) with ! bullets:
  - ! Chest pain, pressure or squeezing
  - ! Pain in the arm, back, neck, jaw or stomach
  - ! Shortness of breath
  - ! Cold sweat, nausea or light-headedness
  - ! Signs can start slowly — don't ignore mild discomfort
- Emergency banner (Heart Red fill, white text, phone icon):
  > Call emergency services right away
  >
  > Every minute counts — don't wait, and don't drive yourself.
- Disclaimer chip:
  > For education only — not a substitute for professional medical advice.
- Hero, right (~540): a person holding their chest while a friend calls for help on a phone, with the heart buddy holding an alert sign. Calm, not scary.

### Builder C

**Slide 7 — Heart Failure** (theme Sky Blue; statement band, hero left, cards right)
- Eyebrow chip: `LONG-TERM CONDITION`
- Title: `Heart Failure`
- ECG line: Sky Blue, under the title.
- Statement band (Sky tint):
  > Heart failure doesn't mean the heart has stopped — it means the heart can't pump as well as it should.
- Three stacked monitor cards (Sky header bars):
  - **Signs:** Shortness of breath, tiredness, and swelling in the legs, ankles or feet.
  - **Common causes:** Coronary artery disease, a past heart attack, and long-term high blood pressure.
  - **Living with it:** Take medicines as prescribed, limit salt, stay as active as your doctor advises, and keep regular check-ups.
- Hero, left (~520): an older adult resting with feet up and a glass of water, with a caregiver and the heart buddy holding a pill organizer.

**Slide 8 — Know Your Numbers** (theme Mint; 3 monitors left, hero right)
- Eyebrow chip: `PREVENTION`
- Title (centered): `Know Your Numbers`
- ECG line: Mint, under the title.
- Three tall monitor cards in a row. Each has a colored header bar, an icon, a dark Ink "screen" with a Lilita One reading, and a caption:
  - `Blood Pressure` (Heart Red) — screen: `Below 120/80` / `mmHg` — caption: Normal for most adults. Get it checked regularly.
  - `Cholesterol` (Sunny Yellow) — screen: `Check it` / `regularly` — caption: A simple blood test shows your levels. Ask your doctor how often.
  - `Blood Sugar` (Grape) — screen: `Check it` / `regularly` — caption: Screening helps find diabetes early, when it's easier to manage.
- Tip banner (Sunny tint, clipboard icon):
  > Your doctor can tell you which targets are right for you.
- Hero, right (~500): a friendly nurse checking the heart buddy's blood pressure with a cuff, with clipboard and blood-test icons.

**Slide 9 — Heart-Healthy Habits** (theme Mint; hero center, 3 tiles each side)
- Eyebrow chip: `EVERY DAY COUNTS`
- Title (centered): `Heart-Healthy Habits`
- ECG line: Mint, under the title.
- Hero, center (~520): the heart buddy jogging with a family cycling and walking a dog in a sunny park.
- Six tiles (white, outlined in a different palette color each), each with a tinted icon circle:
  - `Get 150 minutes of moderate activity a week` (Mint)
  - `Fill half your plate with fruits & vegetables` (Sunny Yellow)
  - `Cut down on salt, sugar & fried food` (Peach)
  - `Don't smoke — and avoid secondhand smoke` (Heart Red)
  - `Sleep 7–9 hours a night` (Grape)
  - `Keep a healthy weight & manage stress` (Sky Blue)

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Lilita One 140, centered.
- ECG line: rainbow (Red → Sunny → Mint → Sky → Grape), full width under the title.
- Subtitle:
  > Keep your heart happy — one healthy beat at a time.
- Three contact pills (Mint / Sky / Grape), each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources chip:
  > Sources: World Health Organization (WHO), U.S. CDC, American Heart Association, Kementerian Kesehatan RI
- Hero along the bottom (~1400): diverse people of all ages dancing and walking with the heart buddy, hearts and a colorful ECG line.
- Decor: pulse confetti in both top corners.

## 4. Speaker notes

- Slides 2–9:
  > General information only. Verify with current WHO / CDC / AHA / Kemenkes guidance before presenting.
- Slide 6, add:
  > In Indonesia, call 119 for medical emergencies. Check the local emergency number for your audience.
- Slide 8, add:
  > Healthy targets can differ by age and health condition.

## 5. Deck-specific QA

- [ ] 10 pages in order; Dissolve ("Larut") on all pages.
- [ ] Every slide has the ECG pulse line in its section color (slide 10 rainbow) and the heart buddy.
- [ ] Monitor-screen cards (colored header bar + three status dots) on every content slide.
- [ ] At least 4 palette accents visible per slide; not a red/blue/white-only look.
- [ ] Only Lilita One and Poppins.
- [ ] Medical text matches §3 word for word; the emergency banner and disclaimer are on slide 6.
- [ ] No stock photos, no realistic anatomy or gore, no logos.
- [ ] Nothing from the earlier decks' identities (chain links, shields, clouds, lung buddy, winding path, fruit badges, title pills, metro map, neurons, water flow, blueprint).
