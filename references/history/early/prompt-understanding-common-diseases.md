# Prompt — "Understanding Common Diseases" Canva deck (colorful, illustration-rich, fast pipeline)

> Copy everything below into a new task. One **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Understanding Common Diseases"**. It is an educational health deck for students and the general public.

### Client brief (most important)

- The design must be **colorful** and **illustration-led**, and it must **not be too simple**.
- Every slide should feel lively and layered, like a well-designed educational poster, not text on a plain background with one picture.
- Every slide must pass the **richness checklist** in §3.

### Basics

- **Language:** all deck content in **English**. Report to the user in **Indonesian**.
- **Reference (direction only):** https://www.canva.com/templates/EAHX0FxOhxM/ ("Gray and Pink Illustrated Understanding Common Diseases Presentation").
  - Borrow the *idea*: friendly flat character illustrations of people with each illness, bold uppercase titles, and the topic list (cold & flu, diarrhea, dengue, lifestyle diseases, prevention, symptoms & treatment).
  - **Build from scratch.** Never click "Use this template", and never copy its pages or elements.
- **Expected time:** about 40–50 minutes. That is a bit longer than a minimal deck, because every slide carries many more visuals.

### Skills to load first (main agent)

- `anthropic-skills:pptx` → generates the .pptx skeleton.
- `elite-powerpoint-designer` → design rules. Use its "Creative Bold" direction: bright colors, dynamic layouts, playful spacing.
- `ppt-visual` → layout concepts that keep each slide's composition different.
- `presentation-design` → used for the QA pass in §8.

---

## 1. Hard rules (all agents)

1. **Built from scratch; every asset comes from Canva Elements.** (Project rule.)
   - The code skeleton may contain only **text** and **plain layout shapes**: background color, cards, pills, circles, divider lines.
   - **Everything visual** comes from Canva Elements (Elemen → Grafis / Stiker / Bentuk / Bingkai). That includes characters, scene illustrations, icons, germs, blobs, patterns, doodles, confetti and frames.
   - Pro elements are allowed.
2. **No Canva AI.**
   - Do not use Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva" or "Buat Animasi".
   - Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing or downloading, and no changes to sharing, access or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** All agents share one clipboard. Insert every asset fresh from the Elements panel.
6. **Keep the medical text exact.** Medical content stays exactly as written in §6. Add no new claims, numbers or dosages.
7. **No real logos** of hospitals, brands or drugs.
8. **Friendly, non-scary imagery only:**
   - no gore, open wounds, vomit or needles in skin;
   - sick characters look unwell but cute, not distressing.

---

## 2. Borrow vs. must differ

| Borrow (the idea) | Must differ (our identity) |
|---|---|
| Flat, friendly character illustrations of sick people | Characters appear inside **colored scenes** (bedroom, kitchen, park, clinic), not alone on a plain background |
| Bold uppercase titles | Titles sit on **colored highlight shapes** (marker swipes or blobs) and use a rounded display font |
| One topic per slide | Each slide is **layered**: hero scene + 3–6 icons + info cards + decoration (see §3 richness checklist) |
| Text left, picture right | Layouts **vary** across 6 distinct layout types (see §5); never the same layout twice in a row |
| — | **No** gray background, no magenta 8-point asterisk star, no ">>>" chevron arrows, no small black/pink triangle clusters |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins: 120 left and right, 96 top and bottom. Spacing in multiples of 24.

### Colors (bright, multi-color; each disease gets its own theme color)

| Token | Hex | Use |
|---|---|---|
| Cream | `#FFF7EC` | Main background |
| Ink | `#1F2041` | Titles and body text |
| Berry | `#E63E6D` | Accent; theme color for Cold & Flu |
| Tangerine | `#FF8C42` | Accent; theme color for Diarrhea |
| Sunshine | `#FFC93C` | Highlights and stars; theme color for Symptoms |
| Leaf | `#3BB273` | Prevention color; theme color for Healthy Habits |
| Ocean | `#2E86DE` | Accent; theme color for Dengue |
| Grape | `#7B4DD8` | Accent; theme color for TB and Lifestyle |
| Soft tints | the same colors at 15–20 % | Background blobs and card fills |

**Theme color in use:** on each disease slide, the theme color drives the title highlight, the hero blob and the card borders. The other colors appear only as small accents.

### Fonts (max 2 families)

- **Titles:** Baloo 2 ExtraBold (fallback: Lilita One).
- **Body:** Nunito (fallback: Quicksand).

| Style | Spec |
|---|---|
| Cover title | Baloo 2 ExtraBold 110–130, Ink, on Sunshine/Berry highlight swipes |
| Slide title | Baloo 2 ExtraBold 68–80, UPPERCASE, Ink, on a theme-color highlight shape (tint) |
| Subtitle | Nunito Bold 28, theme color |
| Card title | Baloo 2 Bold 32–36 |
| Body | Nunito Regular 26–28, line spacing 1.4. Never below 22 |
| Fun-fact bubble | Nunito Bold 24 |

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per card.
- Max 4 font sizes per slide.
- Contrast ≥ 4.5:1: Ink text on Cream or tints; White text only on full-strength Berry, Ocean, Grape or Leaf.
- Motion: titles Fade; cards Rise, staggered. Max 3 animated elements per slide. Transition: Push for the whole deck.

### Richness checklist (every slide must have ALL of these)

1. **1 hero illustration or scene**, at least 520 px. On disease slides, use a character showing that illness.
2. **3–6 supporting icons or small illustrations**: germs, mosquito, water drop, soap, pills, thermometer, and so on.
3. **At least 2 decorative layers**:
   - a soft organic **blob** behind the hero, in a theme tint;
   - plus **doodles, dots, sparkles, wavy lines or a subtle pattern** in 1–2 corners.
4. **Structured text** in colored cards, numbered badges or speech/fact bubbles. Never a bare paragraph alone.
5. **At least 3 colors visible** from the palette, with the theme color dominant.

### Recurring motifs (identical on every slide)

1. **Title highlight:** a hand-drawn marker swipe or rounded blob behind the title, theme tint, from Canva Elements.
2. **Info cards:** White, radius 32, 4 px border in the theme color. Each has a 72 px colored icon circle at the top-left; the icon inside comes from Canva Elements.
3. **Fun-fact bubble:** a speech-bubble shape (Canva Elements) in Sunshine, labeled `DID YOU KNOW?`.
4. **Germ friends:** 2–4 cute cartoon germs/virus characters scattered as decoration on infectious-disease slides. Use the same germ style throughout.
5. **Footer strip:** a thin wavy line in the theme color along the bottom (Canva Elements), plus the page number at the bottom right.

### Illustration style

Use **flat, vibrant, friendly character illustrations** with clean shapes and no outlines, or soft outlines. Use a consistent skin-tone variety and consistent proportions.

The asset scout must pick **one anchor creator or set** that has many "sick person" and medical characters, and use it for every hero. Icons come from **one consistent icon set**: colored flat icons, not line icons.

---

## 4. Pipeline

### Phase 0A — main agent: skeleton .pptx (about 5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU), so Canva imports it at 1920 × 1080.
   - Convert px to EMU as `px * 9525`.
2. For every slide in §6, create:
   - the background (Cream);
   - all text, with exact copy, font names, sizes and colors;
   - plain shapes: white cards with theme-color borders, icon circles, number badges, pills.
3. Mark every visual from §6 with a labeled **placeholder rectangle** at its exact position.
   - Fill: 20 % transparent Ocean.
   - Example labels: `HERO: girl sneezing, bedroom scene 700w`, `ICON: thermometer`, `DECOR: blob Berry tint behind hero`.
4. Add the speaker notes from §7.
5. Save as `understanding-common-diseases-skeleton.pptx`.

### Phase 0B — asset scout subagent, in parallel with Phase 0A (about 10–12 min)

1. Search Canva Elements for every hero, icon, germ, blob, highlight swipe, speech bubble, doodle and wavy line in §6.
2. Write `understanding-common-diseases-assets.md` with these columns:

| Slide | Item | Exact search keyword | Creator | Result position (row, column) | Pro/free |

3. Choose:
   - one hero character creator/set;
   - one icon set;
   - one germ-character set;
   - one blob/highlight style.
4. Write useful search phrases into the file, for example: "flat illustration sick boy sneezing", "cute virus character", "colorful medical icon flat", "organic blob shape", "marker highlight swipe", "doodle sparkle".
5. Insert nothing into the design.

### Phase 0C — main agent: import (about 3 min)

1. Upload the skeleton with the `file_upload` tool: Buat desain → Impor file (or the Unggahan panel). If upload through the tool fails, ask the user to drag the file in once.
2. Rename the design **Understanding Common Diseases**.
3. Check 2–3 slides:
   - fonts are mapped correctly; re-set any substituted fonts;
   - card borders and radii survived.
4. **Fallback** if the import is broken: build slide 4 by hand as a "kit page", duplicate it, and swap the content per slide. Report which path you used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builder subagents in parallel (about 20–25 min)

Each builder gets §1, §2, §3, its own slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`. For each slide:
> 1. Place the decorative layers first: blob behind the hero, title highlight, corner doodles/pattern, wavy footer.
> 2. Place the hero, then the icons, germs and fun-fact bubble, as listed in the asset sheet. Use the exact keyword and the listed result.
> 3. Lock the aspect ratio. Match each placeholder's size and position via Posisi (Lebar / Tinggi / X / Y). Send blobs and patterns to the back. Center icons inside their circles at 44 px.
> 4. Recolor decorative shapes to the slide's theme tint where Canva allows it.
> 5. Delete the placeholders.
> 6. Run the §3 **richness checklist**. If an item is missing, add a fitting Canva element.
> 7. Fix overlap and clipping. Text must stay readable and must not sit on busy decoration.
> 8. Take a zoom screenshot to check.
>
> The UI is in Indonesian. Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua". Never copy/paste. If your tab's screenshots time out twice, stop and report "BLOCKED".
>
> Report back:
> - for each slide: done / issues, and the richness checklist result;
> - assets used: keyword + creator + Pro/free.

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent: QA and report (about 5 min)

See §8.

---

## 5. Layout types (vary them; never the same one twice in a row)

- **L1 Hero split:** text column left (x 120, width 860); hero scene right, on a large blob.
- **L2 Hero center:** title on top, hero in the center, cards orbiting left and right.
- **L3 Three cards:** title top-left, hero top-right (smaller, about 520), three cards across the bottom (`Cause` · `Symptoms` · `Prevention`).
- **L4 Grid:** title top, a 2×2 or 3×2 grid of illustrated cards.
- **L5 Body map:** hero character centered, with callout labels and lines pointing to body areas.
- **L6 Banner:** full-width colored band (theme color) with the title, plus illustrations breaking out of the band.

All positions are in px on the 1920 × 1080 page; (x, y) is the top-left corner.

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (L1, theme Berry + Sunshine)**
- Label pill at (120, 180), Leaf, White text: `HEALTH EDUCATION`.
- Title at (120, 240), width 900, 3 lines, with highlight swipes behind "COMMON" (Sunshine) and "DISEASES" (Berry tint):
  > UNDERSTANDING
  > COMMON
  > DISEASES
- Subtitle at (120, 640), Nunito Bold 30, Ink, width 780:
  > Learn the causes, spot the symptoms, and stay one step ahead.
- Presenter row at (120, 820), Nunito 22:
  > Presented by Your Name  •  Your School / Organization
- Hero at (980, 140), about 820 wide: a lively scene of 3 diverse characters — one sneezing, one with a thermometer, one healthy doctor or nurse waving — on a big Sunshine-tint blob.
- Decoration:
  - 3–4 cute germ characters floating around the scene;
  - sparkles and dots;
  - wavy footer;
  - a doodle cluster at the top-left.

**Slide 2 — What Are Common Diseases? (L2, theme Ocean)**
- Title, centered at y 96:
  > WHAT ARE COMMON DISEASES?
- Subtitle, centered at y 200:
  > Illnesses that many people catch or develop at some point in life.
- Hero in the center: a globe or a group of people (about 560) on an Ocean-tint blob.
- Four illustrated cards around the hero, each 440 × 230, 2 on the left and 2 on the right, at y 360 and y 640. Each card has an icon (Canva) and a card title + one line:

| Card | Title | Text |
|---|---|---|
| 1 | `Through the Air` | `Coughs and sneezes spread germs.` |
| 2 | `Food & Water` | `Unsafe water and food carry germs.` |
| 3 | `Insect Bites` | `Mosquitoes can carry viruses.` |
| 4 | `Daily Habits` | `Diet, activity and smoking affect long-term health.` |

- Fun-fact bubble, bottom center:
  > Many common diseases can be prevented with simple habits.

**Slide 3 — What Causes Disease? (L4, theme Grape)**
- Title at (120, 96):
  > WHAT CAUSES DISEASE?
- Subtitle:
  > Tiny germs and everyday habits.
- Five cards in two rows:
  - Top row: 3 cards, each 520 × 300, at y 300, x 120 / 700 / 1280.
  - Bottom row: 2 cards, each 810 × 300, at y 640, x 120 / 990.
  - Each card has a cute germ character or illustration (about 160) plus a title and one line:

| Card | Title | Text |
|---|---|---|
| 1 | `Viruses` | `Cause colds, flu and dengue.` |
| 2 | `Bacteria` | `Cause tuberculosis and some diarrhea.` |
| 3 | `Parasites` | `Can spread through dirty water and food.` |
| 4 | `Lifestyle` | `Unhealthy diet, little exercise and smoking.` |
| 5 | `Genes & Age` | `Family history can raise the risk of some diseases.` |

- Decoration: a microscope illustration in the top-right corner, a dotted pattern, and the wavy footer.

### Builder B

**Slide 4 — Common Cold & Influenza (L3, theme Berry)**
- Title:
  > COMMON COLD & INFLUENZA
- Subtitle:
  > Understanding respiratory infections
- Hero (top-right, about 560): a girl sneezing into a tissue in a cozy bedroom scene, with floating cute virus characters.
- Three cards, each 540 × 520, at y 420:

  `Cause`:
  > Viruses spread through droplets from coughs and sneezes, and from touching contaminated surfaces.

  `Symptoms`:
  > Runny or blocked nose, sore throat, cough, fever, tiredness and body aches.

  `Prevention` (✓ bullets):
  - ✓ Yearly flu vaccine
  - ✓ Wash hands with soap for 20 seconds
  - ✓ Cover coughs and sneezes
  - ✓ Stay home when sick

- Icons inside or near the cards: tissue box, thermometer, soap, vaccine vial (no needle in skin).

**Slide 5 — Dengue Fever (L1, theme Ocean)**
- Title:
  > DENGUE FEVER
- Subtitle:
  > A mosquito-borne viral infection
- Left column, stacked cards:

  `How it spreads`:
  > Bites from infected Aedes mosquitoes, which breed in clean, standing water.

  `Symptoms`:
  > High fever, severe headache, pain behind the eyes, muscle and joint pain, nausea and rash.

  `Prevention` (✓ bullets):
  - ✓ Drain and cover water containers
  - ✓ Recycle items that collect water
  - ✓ Use repellent and mosquito nets
  - ✓ Wear long sleeves and pants

- Fun-fact bubble:
  > In Indonesia this is called "3M Plus".
- Hero (right, about 760): a boy with a fever resting, a cartoon mosquito nearby, and a water container being covered. Place it on an Ocean-tint blob with water-drop doodles.

**Slide 6 — Diarrhea (L5 body map, theme Tangerine)**
- Title:
  > DIARRHEA
- Subtitle:
  > The importance of clean food and water
- Hero in the center (about 600 tall): a boy holding his stomach.
- Callout lines point to three labels:
  - stomach: `Cramps & pain`
  - mouth: `Dry mouth (dehydration)`
  - head: `Tiredness & dizziness`
- Left card — `Common Causes`:
  > Unsafe water, undercooked food, and unwashed hands carrying viruses, bacteria or parasites.
- Right card — `Prevention` (✓ bullets):
  - ✓ Drink safe, boiled or treated water
  - ✓ Wash hands before eating
  - ✓ Cook food thoroughly and keep it covered
  - ✓ Use oral rehydration solution (ORS) if diarrhea starts
- Icons: water glass, soap, cooking pot, ORS sachet. Add 2 cute germ characters.

### Builder C

**Slide 7 — Tuberculosis (TB) (L6 banner, theme Grape)**
- A Grape full-width band, 1920 × 300, at y 0. Title in White:
  > TUBERCULOSIS (TB)
- Subtitle in White:
  > A bacterial infection that mainly affects the lungs
- A lungs illustration breaks out of the band at the top-right (about 420).
- Three cards below at y 400:

  `How it spreads`:
  > Through the air when a person with active TB coughs, sneezes or talks.

  `Symptoms`:
  > A cough lasting more than 2 weeks, fever, night sweats, weight loss and tiredness.

  `Prevention` (✓ bullets):
  - ✓ BCG vaccine for babies
  - ✓ Keep rooms well ventilated
  - ✓ Get tested for a long cough
  - ✓ Finish the full TB treatment

- Hero, bottom-right corner (about 480): a person coughing into their elbow next to an open window.

**Slide 8 — Lifestyle-Related Diseases (L4, theme Grape + Leaf)**
- Title:
  > LIFESTYLE-RELATED DISEASES
- Subtitle:
  > The effects of daily habits
- Four illustrated cards in a 2×2 grid, each 820 × 300, at x 120 / 980 and y 300 / 640. Each has an illustration of about 200:

| Card | Illustration | Title | Text |
|---|---|---|---|
| 1 | heart with a blood-pressure cuff | `Hypertension` | `Often has no symptoms. Linked to salty food, inactivity and stress.` |
| 2 | glucose meter + healthy plate | `Type 2 Diabetes` | `High blood sugar linked to excess weight and inactivity.` |
| 3 | heart | `Heart Disease` | `Linked to smoking, unhealthy diet and high blood pressure.` |
| 4 | scale + vegetables | `Obesity` | `Excess body fat that raises the risk of many diseases.` |

- Fun-fact bubble:
  > Being active 150 minutes a week lowers the risk of many of these.

**Slide 9 — Common Symptoms to Watch (L5, theme Sunshine)**
- Title:
  > COMMON SYMPTOMS TO WATCH
- Subtitle:
  > Your body's warning signs
- Hero in the center (about 620 tall): a friendly character looking unwell, on a Sunshine-tint blob.
- Six symptom icons with labels arranged around the character, 3 per side, each in a colored icon circle (96) with Nunito Bold 26:
  - Left: `Fever`, `Cough`, `Headache`
  - Right: `Stomach Pain`, `Skin Rash`, `Tiredness`
- Bottom note, Nunito 24:
  > Symptoms can overlap between diseases — a health worker can tell them apart.

### Builder D

**Slide 10 — Disease Prevention (L4, theme Leaf)**
- Title:
  > DISEASE PREVENTION
- Subtitle:
  > Simple ways to stay healthy
- Six habit cards in a 3×2 grid, each 540 × 300, at x 120 / 690 / 1260 and y 300 / 640. Each has a colorful illustration of about 140, a title and one line:

| Card | Title | Text |
|---|---|---|
| 1 | `Wash Your Hands` | `With soap, for at least 20 seconds.` |
| 2 | `Eat Balanced Meals` | `Plenty of vegetables, fruit and whole grains.` |
| 3 | `Move Every Day` | `Aim for 150 minutes of activity a week.` |
| 4 | `Sleep Well` | `Most adults need 7–9 hours a night.` |
| 5 | `Get Vaccinated` | `Protect yourself and the people around you.` |
| 6 | `Keep Surroundings Clean` | `Clean water, clean home, no standing water.` |

- Decoration: leaves, sparkles and the wavy footer in Leaf.

**Slide 11 — Symptoms & Treatment (L1, theme Berry + Leaf)**
- Title:
  > SYMPTOMS AND TREATMENT
- Subtitle:
  > Knowing when to seek medical help
- Left: two stacked cards.

  `Care at Home` (Leaf border, ✓ bullets):
  - ✓ Rest and drink plenty of fluids
  - ✓ Eat light, nourishing food
  - ✓ Take medicine only as advised by a health worker

  `See a Doctor If…` (Berry border, ! bullets):
  - ! A high fever lasts more than 3 days
  - ! Breathing is difficult
  - ! There are signs of dehydration
  - ! There is bleeding or severe stomach pain during a fever
  - ! A cough lasts more than 2 weeks

- Right: hero (about 720), a friendly doctor examining a smiling patient in a colorful clinic scene, on a Berry-tint blob.
- Disclaimer, bottom-left, Nunito 20:
  > For education only — not a substitute for professional medical advice.

**Slide 12 — Thank You (L2, multi-color)**
- Title, centered at y 280, Baloo 2 ExtraBold 130, on a Sunshine highlight swipe:
  > THANK YOU!
- Subtitle, centered at y 470, Nunito Bold 32:
  > Stay curious, stay healthy.
- Three contact pills, centered at y 600, in Berry, Ocean and Leaf, White text, Nunito Bold 24:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources line, centered at y 880, Nunito 20:
  > Sources: World Health Organization (WHO), U.S. CDC, Kementerian Kesehatan RI
- Decoration: a celebratory illustration of the cast of characters from the cover, now healthy and waving, along the bottom (about 1200 wide); confetti; sparkles; and happy germ-free hearts.

---

## 7. Speaker notes (main agent adds them in the .pptx)

- Slides 4–9 and 11:
  > Information is general. Verify against the latest WHO / CDC / Kemenkes guidance before presenting.
- Slide 11:
  > Encourage the audience to seek care early; the list is not exhaustive.

---

## 8. QA checklist (main agent, run with `presentation-design`)

- [ ] 12 pages, in order; every placeholder deleted.
- [ ] **Richness checklist** (§3) passes on **every** slide. If it fails, add Canva elements until it passes.
- [ ] At least 4 different layout types are used across the deck (§5), and the same layout never appears twice in a row.
- [ ] Every visual comes from Canva Elements. The skeleton contributed only text and plain layout shapes. No Canva AI assets.
- [ ] Hero characters share one consistent style; icons come from one consistent set.
- [ ] Fonts: only Baloo 2 and Nunito (or the fallbacks). Body text ≥ 22 px. Contrast ≥ 4.5:1. Text never sits on busy decoration.
- [ ] Medical text matches §6 word for word. No gore, no needles in skin, no logos.
- [ ] None of the §2 "must differ" items appear: no gray background, no magenta asterisk, no ">>>" chevrons, no triangle clusters.
- [ ] No overlap, clipping or stray elements (check each page's Lapisan list once).
- [ ] Nothing shared, downloaded or published.

## 9. Final report to the user (in Indonesian)

1. The edit link.
2. One line per slide, including its layout type.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately different from the reference (§2), and how the "colorful, not too simple" brief was met.
5. Which path was used (pptx import or kit-page fallback), time per phase, and anything not achieved.
6. A reminder to verify the medical content against current WHO / CDC / Kemenkes guidance.
