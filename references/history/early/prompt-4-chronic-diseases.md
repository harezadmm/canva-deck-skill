# Prompt 4 — "Chronic Diseases: Management and Prevention" (colorful, fast pipeline)

> Copy everything below into a new task.
> Team: **one main agent**, **one asset scout**, and **four builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Chronic Diseases: Management and Prevention"**.

It is an educational deck for adults, families, and community health sessions. It covers:
- what chronic diseases are,
- the main types,
- risk factors,
- how to manage 4 common conditions,
- prevention habits,
- living well,
- "know your numbers".

**Client brief: COLORFUL, illustration-rich, not too simple.**
- The deck must feel warm, hopeful and lively.
- Chronic illness is shown as something you can *manage*: active, smiling people of all ages doing healthy things.
- Every slide shows **at least 4 palette colors** and passes the richness checklist in §3.

**Language:** all deck content in **English**. Report to the user in **Indonesian**.

**Reference (direction only):** https://www.canva.com/templates/EAHQTjfjNNU/ ("Teal and White Modern Kidney Disease Awareness Presentation").
- Borrow the *idea*: a clear medical info hierarchy, a step / process slide, a "daily habits" slide, and a trustworthy tone.
- **Build from scratch.** Never click "Use this template", and never copy its pages or elements.

**Not a repeat:** this deck must also look different from the earlier "Common Diseases and Their Prevention" prompt, which was navy/sky/mint/coral with flat medical illustrations and info cards.

**Expected time:** about 40–50 minutes.

### Skills to load first (main agent)

- `anthropic-skills:pptx` — build the skeleton.
- `elite-powerpoint-designer` — warm, hopeful version of Creative Bold.
- `ppt-visual` — layouts.
- `presentation-design` — QA.

---

## 1. Hard rules (all agents)

1. **Built from scratch; all assets from Canva Elements** (project rule).
   - The code skeleton may contain **only text and plain layout shapes**: background, panels, pills, circles, lines.
   - Every visual comes from Canva Elements (Elemen → Grafis / Stiker / Bentuk / Bingkai): characters, organs, icons, blobs, patterns, frames, decorations.
   - Pro elements are allowed.
2. **No Canva AI.**
   - Don't use Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva", or "Buat Animasi".
   - Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing, or downloading, and no changes to sharing, access, or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes, or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** The clipboard is shared across agents.
6. **Medical text exactly as in §6.**
   - Add no new claims, numbers, medicine names, or dosages.
   - Numbers on slide 11 must keep their "general adult reference" label.
7. **No logos.** No real hospital, brand, or drug logos.
8. **Hopeful, respectful imagery.**
   - No gore, no needles in skin, no sad or bedridden "victim" imagery.
   - Show older adults and people of different body types positively.

---

## 2. Borrow vs. must differ

| Borrow (the idea) | Must differ (our identity) |
|---|---|
| Clear info hierarchy, trustworthy tone | **Warm sunrise palette** (plum, coral, sunflower, fresh green, sky) on cream — **not** teal/white, and **not** the navy/sky/mint/coral of the earlier prompt |
| Process / step slide | Steps shown as a **winding "care journey" path** with colorful milestone circles, not three teal circles |
| Daily habits slide | Habits shown as a colorful **habit-tracker board** (week grid with checkmarks), not pill bars |
| Medical content | **Illustrations of active people** (walking, cooking, gardening, checking blood pressure at home) plus **cute organ characters** (heart, lungs, kidney, pancreas). **No** stock photos of doctors, hands, or pills |
| — | **No** curved teal swoosh corner, no cross watermark, no hospital mark, no full-width photo halves |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins 120 left/right, 96 top/bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Warm Cream | `#FFF8F0` | Main background |
| Deep Plum | `#4A2C6D` | Titles, dark slides |
| Coral | `#FF6F59` | Heart/blood-pressure theme, highlights |
| Sunflower | `#FFC145` | Diabetes theme, stars, numbers |
| Fresh Green | `#4CB963` | Prevention / "good" color, ✓ marks |
| Sky | `#4D96FF` | Lungs/breathing theme, accents |
| Berry | `#D64291` | Kidney theme, accents |
| Charcoal | `#2E2A33` | Body text |

**Color rules (colorful brief):**
- **Theme colors.** Each condition has its own theme color, used for its title highlight, organ blob, and card borders:
  - heart & blood pressure: Coral
  - diabetes: Sunflower
  - lungs: Sky
  - kidneys: Berry
- **Cards.** Card fills alternate between White and 18 % tints of the palette. No more than 2 neighbouring cards share a tint.
- **Background.** Every slide adds 2–3 soft **organic blobs** in different tints, plus a **dotted or wavy pattern** in one corner.

### Fonts (max 2 families)

- **Titles:** Sniglet ExtraBold (fallback: Baloo 2 ExtraBold). It's rounded, warm and friendly, and different from the fonts in the earlier decks.
- **Body:** Nunito Sans (fallback: Nunito).

| Style | Spec |
|---|---|
| Cover title | Sniglet 120–140, Deep Plum, on a Sunflower highlight swipe |
| Slide title | Sniglet 70–82, Deep Plum, on a theme-tint highlight |
| Eyebrow | Nunito Sans ExtraBold 22, UPPERCASE, letter spacing 200, theme color |
| Card title | Sniglet 34–38 |
| Body | Nunito Sans 26–28, Charcoal, line spacing 1.45; never below 22 |
| Big number | Sniglet 96–120, theme color |

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per card.
- Max 4 font sizes per slide.
- Contrast ≥ 4.5:1.
- Motion: titles Fade, cards Rise. Max 3 animated elements per slide. Transition: Push.

### Recurring motifs (identical on every slide)

1. **Highlight swipe** (Canva marker element) behind every title, in the theme tint.
2. **Organ buddy:** a cute organ character for that slide's condition (heart, pancreas, lungs, kidney) in a theme-colored circle badge (~200), at the top-right of each condition slide.
3. **Care cards:** White or tinted, radius 32, 4 px theme-color border, with a 72 px icon circle top-left. The icon comes from Canva Elements.
4. **Journey dots:** a small dotted path (Canva element) linking elements on each slide.
5. **Footer:** a thin wavy line in the theme color, plus the page number in a small Plum circle at bottom-right.

### Illustration style

- **Flat, warm, friendly illustrations** of diverse adults and seniors being active, plus cute **kawaii organ characters**.
- The asset scout picks **one people set** and **one organ-character set** that match, and uses them everywhere.

### Richness checklist (every slide)

Every slide must have all of these:
- 1 hero illustration (≥ 480 px).
- 3–6 supporting icons or small illustrations.
- At least 2 decor layers (blobs, dotted path, pattern, sparkles).
- Text inside cards or badges, never a bare paragraph.
- **At least 4 palette colors visible.**

---

## 4. Pipeline

### Phase 0A — main agent: skeleton .pptx (~5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU).
   - px → EMU: `px * 9525`.
2. For each slide, create:
   - the background,
   - all text (exact copy, fonts, sizes, colors),
   - plain cards, pills, circles, badge circles, and the grid on slide 9.
3. Mark every visual with a labeled placeholder rectangle at its exact spot.
   - Fill: 20 % transparent Sky.
   - Label example: `HERO: senior couple walking in park 640w`.
4. Add the speaker notes from §7.
5. Save as `chronic-diseases-skeleton.pptx`.

### Phase 0B — asset scout, in parallel (~10–12 min)

1. Search Canva Elements for every visual in §6, plus:
   - the highlight swipe,
   - blobs,
   - the dotted path,
   - the wavy footer,
   - the organ-character set,
   - the people set.
2. Write `chronic-diseases-assets.md` with these columns:

   | Slide | Item | Exact keyword | Creator | Result (row, col) | Pro/free |

3. Useful keywords:
   - "cute heart character"
   - "kawaii organ"
   - "kawaii lungs"
   - "kawaii kidney"
   - "flat illustration elderly exercise"
   - "flat illustration healthy cooking"
   - "blood pressure monitor flat"
   - "organic blob"
4. Insert nothing into the design.

### Phase 0C — main agent: import (~3 min)

1. Upload the skeleton with the `file_upload` tool (Buat desain → Impor file, or Unggahan).
   - If that fails, ask the user to drag the file in once.
2. Rename the design.
3. Check fonts, borders, and the slide 9 grid.
4. **Fallback:** if the import is broken, build slide 5 by hand as a kit page and duplicate it. Report which path was used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builders in parallel (~20–25 min)

Each builder gets §1–3, their slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`.
>
> For each slide:
> 1. Place decor first: blobs, highlight swipe, pattern, dotted path, wavy footer.
> 2. Place the hero, organ buddy, and icons, using the exact keyword and result from the asset sheet.
> 3. Lock the aspect ratio and match each placeholder via Posisi. Delete the placeholders.
> 4. Run the richness checklist and the colorful check.
> 5. Fix only overlap and clipping.
> 6. Take a zoom screenshot.
>
> The UI is in Indonesian. Never use Tanya Canva, AI Canva, Bagikan, Unduh, or "Ubah semua". Never copy/paste. If screenshots time out twice, stop and report "BLOCKED".
>
> Report per slide (done / issues) and the assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent: QA + report (~5 min)

---

## 5. Layouts

All positions are px on the 1920 × 1080 page, as the top-left corner (x, y).

**Condition-slide layout (slides 5–8):**
- Eyebrow at (120, 96).
- Title at (120, 136), width 1100.
- Intro at (120, 250), width 1100.
- Organ buddy badge (200) at (1600, 96).
- Hero (~520) at (1300, 340), standing on a theme blob.
- Two care cards stacked on the left, each 1080 × 300, at (120, 360) and (120, 690):
  - **`Manage it`**: theme border, with ✓ bullets.
  - **`Watch out for`**: Coral or Berry border, with ! bullets.

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (bg Warm Cream)**
- Eyebrow pill at (120, 200): Fresh Green fill, White text, `COMMUNITY HEALTH SERIES`.
- Title at (120, 260), width 960, 3 lines:
  > Chronic Diseases:
  > Management &
  > Prevention
- Highlight swipes: Sunflower behind "Chronic", Coral tint behind "Prevention".
- Subtitle at (120, 650), Nunito Sans 30, width 820:
  > Small daily choices, big lifelong impact.
- Presenter row at (120, 800):
  > Presented by Your Name  •  Your Organization
- Hero at (1000, 140), ~840 wide: a lively scene of diverse adults and seniors walking, cycling and carrying a basket of vegetables, on a big multi-color blob cluster.
  - Around them: 3 small organ buddies (heart, lungs, kidney) smiling.
- Decor: dotted path, sparkles, wavy footer.

**Slide 2 — What Are Chronic Diseases? (bg Warm Cream)**
- Eyebrow `THE BASICS`. Title:
  > What Are Chronic Diseases?
- Left definition card (White, Plum border), 900 × 360, at (120, 300):
  > Long-lasting health conditions that usually develop slowly and need ongoing care. They are not passed from person to person.
- Right: a big stat badge — Sunflower circle (520) at (1180, 260):
  - Sniglet 120, Deep Plum: `41 million`
  - Nunito Sans Bold 26: `deaths each year worldwide — about 74% of all deaths`
  - Source line under the badge, Nunito Sans 20:
    > Source: WHO, Noncommunicable diseases fact sheet
- Bottom row: 3 small tinted chips with icons at y 760:
  - `Lasts for years`
  - `Develops slowly`
  - `Can be managed`
- Hero: a small illustration of a senior smiling with a calendar (~360), bottom-left.

**Slide 3 — The Big Four (bg Warm Cream)**
- Eyebrow `MAIN TYPES`. Title:
  > The Big Four Chronic Diseases
- Four tall cards, 400 × 600, at y 300, x = 120 / 560 / 1000 / 1440.
- Each card has its theme tint, an organ/icon illustration (~220), a title, and one line:

| Card | Theme | Illustration | Title | Line |
|---|---|---|---|---|
| 1 | Coral | heart | `Heart Disease & Stroke` | `Problems with the heart and blood vessels.` |
| 2 | Sky | lungs | `Chronic Lung Disease` | `Including asthma and COPD.` |
| 3 | Sunflower | pancreas | `Diabetes` | `Too much sugar in the blood.` |
| 4 | Berry | cell / ribbon | `Cancer` | `Abnormal cells that grow out of control.` |

- Speech bubble from a heart buddy:
  > Many of these share the same risk factors!

### Builder B

**Slide 4 — Risk Factors (bg Warm Cream)**
- Eyebrow `WHAT RAISES THE RISK`. Title:
  > Risk Factors
- Two big panels side by side, each 820 × 640, at y 300.
- **Left panel** — Fresh Green border, title `You Can Change`, with 5 icon rows:
  - Tobacco use
  - Unhealthy diet
  - Not enough physical activity
  - Harmful use of alcohol
  - Air pollution
- **Right panel** — Plum border, title `You Can't Change`, with 3 icon rows:
  - Age
  - Family history
  - Genes
- Under the right panel, a small note card:
  > Knowing these helps you get checked early.
- Hero: a person at a crossroads with signposts "Healthy habits" / "Risky habits" (~420), centered between or below the panels.

**Slide 5 — High Blood Pressure & Heart Health** (condition layout, theme Coral)
- Eyebrow `HEART & BLOOD PRESSURE`. Title:
  > High Blood Pressure & Heart Health
- Intro:
  > High blood pressure often has no symptoms but raises the risk of heart attack and stroke.
- `Manage it`:
  - ✓ Take medicines exactly as prescribed
  - ✓ Eat less salt (under 5 g a day)
  - ✓ Move at least 150 minutes a week
  - ✓ Check your blood pressure regularly
- `Watch out for`:
  - ! Chest pain or pressure
  - ! Sudden weakness or a drooping face
  - ! Trouble speaking — call emergency help
- Organ buddy: heart. Hero: a senior checking blood pressure at home with a friendly home monitor.

**Slide 6 — Type 2 Diabetes** (condition layout, theme Sunflower)
- Eyebrow `BLOOD SUGAR`. Title:
  > Living With Type 2 Diabetes
- Intro:
  > When the body can't use insulin well, blood sugar stays too high and can damage organs over time.
- `Manage it`:
  - ✓ Check blood sugar as advised
  - ✓ Choose whole grains, vegetables and fewer sugary drinks
  - ✓ Stay active every day
  - ✓ Take medicines or insulin as prescribed
- `Watch out for`:
  - ! Very high or very low blood sugar symptoms
  - ! Foot wounds that heal slowly
  - ! Changes in vision — get yearly eye and foot checks
- Organ buddy: pancreas. Hero: an adult cooking a colorful healthy meal, with a glucose meter on the counter (no needles in skin).

### Builder C

**Slide 7 — Asthma & COPD** (condition layout, theme Sky)
- Eyebrow `BREATHING`. Title:
  > Asthma & COPD
- Intro:
  > Long-term lung conditions that make breathing harder, but they can be controlled.
- `Manage it`:
  - ✓ Use inhalers exactly as prescribed
  - ✓ Avoid smoke and known triggers
  - ✓ Ask about flu and pneumonia vaccines
  - ✓ Stay active with breathing-friendly exercise
- `Watch out for`:
  - ! Breathlessness that gets worse
  - ! Lips or fingertips turning bluish
  - ! An inhaler that isn't helping — get care fast
- Organ buddy: lungs. Hero: a person doing gentle outdoor exercise or yoga in fresh air with trees.

**Slide 8 — Chronic Kidney Disease** (condition layout, theme Berry)
- Eyebrow `KIDNEYS`. Title:
  > Chronic Kidney Disease
- Intro:
  > Often caused by diabetes and high blood pressure, and usually silent in its early stages.
- `Manage it`:
  - ✓ Keep blood pressure and blood sugar on target
  - ✓ Drink water and limit salt
  - ✓ Avoid overusing painkillers like ibuprofen
  - ✓ Get kidney blood and urine tests as advised
- `Watch out for`:
  - ! Swollen feet or ankles
  - ! Foamy urine or urinating much less
  - ! Ongoing tiredness
- Organ buddy: kidney. Hero: an adult filling a water bottle, with a happy kidney buddy beside them.

**Slide 9 — Prevention Habit Tracker (bg Warm Cream)**
- Eyebrow `PREVENTION`. Title:
  > Your Weekly Habit Tracker
- A big colorful tracker board, White, radius 32, 1680 × 620, at (120, 300):
  - 6 rows, one per habit. Each row has an icon + label on the left, in a different palette tint.
  - 7 day columns `M T W T F S S` (Sniglet 28).
  - Some cells show colorful ✓ stickers from Canva Elements as an example.

| Row | Habit |
|---|---|
| 1 | `Move 30 minutes` |
| 2 | `Eat 5 portions of fruit & veg` |
| 3 | `No tobacco` |
| 4 | `Limit alcohol` |
| 5 | `Sleep 7–9 hours` |
| 6 | `Drink water` |

- Hero: a person proudly ticking a calendar (~360), bottom-right, overlapping the board edge without covering any cells.

### Builder D

**Slide 10 — The Care Journey (bg Warm Cream)**
- Eyebrow `LIVING WELL`. Title:
  > Your Care Journey
- A winding dotted path (Canva element) across the slide with 5 colorful milestone circles (160 each, different palette colors, Sniglet 48 numbers).
- Under each circle, a title (Sniglet 30) and one line (Nunito Sans 22):

| # | Title | Line |
|---|---|---|
| 1 | `Get Checked` | `Regular screenings catch problems early.` |
| 2 | `Make a Plan` | `Agree on goals with your health worker.` |
| 3 | `Take Medicines` | `Exactly as prescribed — don't skip.` |
| 4 | `Track Your Numbers` | `Blood pressure, sugar and weight.` |
| 5 | `Get Support` | `Family, friends and support groups help.` |

- Hero: a family walking together along the path's end (~460), bottom-right.

**Slide 11 — Know Your Numbers (bg Deep Plum, colorful dark slide)**
- Eyebrow, Sunflower: `KNOW YOUR NUMBERS`. Title in White:
  > Know Your Numbers
- Three big number cards, each 520 × 520, at y 300, x = 120 / 700 / 1280, in Coral / Sunflower / Fresh Green tints at 25 % on Plum, with White text:

| Card | Label | Big number (Sniglet 88, White) | Line |
|---|---|---|---|
| 1 | `Blood Pressure` | `< 120/80` | `mmHg is a healthy reading for most adults.` |
| 2 | `Fasting Blood Sugar` | `< 100` | `mg/dL is the usual normal range.` |
| 3 | `Body Mass Index` | `18.5–24.9` | `is the healthy range for adults (WHO).` |

- Each card has an icon at its top (monitor, glucose meter, scale).
- Note at y 900, Nunito Sans 22, White at 80 %:
  > General adult reference values — your doctor may set different targets for you.
- Decor: colorful sparkles and blobs at the edges.

**Slide 12 — Thank You (bg Warm Cream)**
- Title, centered at y 280, Sniglet 140, Deep Plum, on a big multi-color swipe:
  > Thank You!
- Subtitle, centered at y 470, Nunito Sans 32:
  > Small steps today, a healthier tomorrow.
- Three contact pills at y 590, in Coral / Sky / Fresh Green:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources line at y 900, Nunito Sans 20:
  > Sources: World Health Organization (WHO), U.S. CDC, American Heart Association, Kementerian Kesehatan RI
- Hero: all the organ buddies plus the people from the cover, waving and celebrating along the bottom (~1300 wide), with confetti.

---

## 7. Speaker notes

- **Slide 2:**
  > WHO estimates noncommunicable diseases cause about 41 million deaths a year (~74% of all deaths). Check the latest WHO fact sheet.
- **Slides 5–8:**
  > General information only. Verify against current WHO / CDC / Kemenkes guidance before presenting.
- **Slide 11:**
  > Reference values: BP < 120/80 mmHg (AHA "normal"), fasting glucose < 100 mg/dL (ADA "normal"), BMI 18.5–24.9 (WHO). Targets differ per person.

---

## 8. QA checklist (main agent, with `presentation-design`)

- [ ] 12 pages in order; all placeholders deleted.
- [ ] Richness checklist and the **colorful check** (≥ 4 palette colors) pass on every slide.
- [ ] Theme colors are consistent: heart = Coral, diabetes = Sunflower, lungs = Sky, kidney = Berry.
- [ ] Every visual comes from Canva Elements; no Canva AI assets.
- [ ] One people set and one organ set are used throughout; imagery is hopeful and inclusive.
- [ ] Only Sniglet + Nunito Sans (or fallbacks); body ≥ 22; contrast ≥ 4.5:1.
- [ ] Medical text matches §6 word for word; slide 11 keeps its reference disclaimer.
- [ ] None of the §2 "must differ" items appear: no teal swoosh, no cross watermark, no doctor/hand stock photos, and no navy/sky/mint/coral look from the earlier deck.
- [ ] No overlap, clipping, or stray elements (check Lapisan).
- [ ] Nothing shared, downloaded, or published.

## 9. Final report (Indonesian)

1. Edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately different from the reference.
5. Path used, time per phase, and anything not achieved.
6. Reminder to verify the medical content and numbers.
