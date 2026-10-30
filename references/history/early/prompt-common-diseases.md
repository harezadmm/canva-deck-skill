# Prompt — "Common Diseases and Their Prevention" Canva deck (fast pipeline, ~30–40 min)

> Copy everything below into a new task. One **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Common Diseases and Their Prevention"**.

It is an educational health-awareness deck for a general audience. It covers:
- why prevention matters
- 6 common diseases, each with its cause, symptoms and prevention
- daily healthy habits
- when to see a doctor
- a closing slide

**Language:** all deck content is in **English**. Report to the user in **Indonesian**.

**Reference (mood only):** https://www.canva.com/templates/EAHQTjfjNNU/ ("Teal and White Modern Kidney Disease Awareness Presentation").
- Borrow the *mood*: clean, clinical, trustworthy, white space, a clear info hierarchy.
- **Build from scratch.** Never click "Use this template", and never copy its pages or elements.

### Skills to load first (main agent)

- `anthropic-skills:pptx` to generate the .pptx skeleton.
- `elite-powerpoint-designer` for the design rules summarised in §3. Its "Corporate Professional" style fits best: grid-based, trustworthy, data-friendly.
- `presentation-design` for the QA pass in §8.

---

## 1. Hard rules (all agents)

1. **Built from scratch, every asset from Canva Elements.** (Project rule.)
   - The code skeleton may contain only **text** and **plain layout shapes**: background panels, cards, pills, divider lines, number circles.
   - **Everything visual** comes from Canva Elements (Elemen → Grafis / Stiker / Bentuk / Bingkai / Foto). That includes illustrations, icons, photos, frames, medical symbols and decorative graphics.
   - Pro elements are allowed.
2. **No Canva AI.** Do not use any of these:
   - Magic Media, Dream Lab, Magic Design, Magic Write
   - Magic Edit, Grab, Expand
   - "Tanya Canva", "AI Canva", "Buat Animasi"

   Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing or downloading, and no changes to sharing, access or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** All agents share one clipboard. Insert every asset fresh from the Elements panel.
6. **Medical content stays exactly as written in §6.** Don't add new medical claims, numbers or dosages. Don't shorten text in a way that changes the meaning.
7. **No real logos.** No hospital or brand logos, and no recognisable drug brands on packaging.
8. **No upsetting imagery.** No gore, open wounds, needles going into skin, or graphic illness images. Keep visuals friendly and educational.

---

## 2. Borrow vs. must differ

| Borrow (the mood) | Must differ (our identity) |
|---|---|
| Clean white space, clinical trust | Palette is **navy + sky blue + mint + coral**, not teal-on-white |
| Clear title + short body hierarchy | **No** curved teal swoosh in the bottom-right corner, and no cross watermark |
| Highlighted key points | Key points sit in **rounded info cards with icon badges**, not teal pill bars |
| Medical imagery | Heroes are **flat medical illustrations** (doctor, virus, mosquito, heart and so on), not stock photos of hands, doctors and stethoscopes |
| Small brand mark top-left | **No** "Primary Hospital" mark. Instead, each disease slide carries a small **disease-type chip** (`INFECTIOUS` or `LIFESTYLE`) |

---

## 3. Design system

**Canvas:**
- Size: 1920 × 1080.
- Margins: 120 left and right, 96 top and bottom.
- Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Navy | `#17254A` | Titles, dark slides, main text |
| Sky | `#3A86FF` | Accents, links, infectious chip |
| Ice | `#EEF4FF` | Main light background |
| White | `#FFFFFF` | Cards |
| Mint | `#2BB673` | "Prevention" color, ✓ marks |
| Coral | `#FF6B5B` | "Symptoms / warning" color, lifestyle chip |
| Slate | `#5B6785` | Secondary text, captions, sources |

### Fonts (max 2 families)

- **Titles:** Outfit Bold (fallback: Montserrat Bold).
- **Body and labels:** Open Sans (fallback: Lato).

| Style | Spec |
|---|---|
| Cover title | Outfit Bold 96–110, Navy |
| Slide title | Outfit Bold 64–76, Navy (White on Navy slides) |
| Card title | Outfit Bold 30–34 |
| Body | Open Sans 26–28, line spacing 1.45. Never below 22 |
| Chip / label | Open Sans Bold 20, UPPERCASE, letter spacing 150 |
| Source line | Open Sans 18–20, Slate (the only text allowed below 22) |

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per card.
- Max 4 font sizes per slide.
- Contrast at least 4.5:1.
- Transitions: Fade only.
- Max 2 animated elements per slide: title, then cards.

### Recurring motifs (identical on every slide)

1. **Disease-type chip:** a pill with radius 999 and White text.
   - `INFECTIOUS`: Sky fill.
   - `LIFESTYLE`: Coral fill.
2. **Info card:**
   - White, radius 28, with a subtle shadow (Efek → Bayangan, light).
   - Top-left: a 72 px icon badge. The colored circle (Coral for symptoms, Mint for prevention, Sky for cause) is a plain shape in the skeleton. The icon inside it comes from Canva Elements.
3. **Three-column disease layout:** `Cause` · `Symptoms` · `Prevention` cards. Prevention bullets use a Mint ✓.
4. **Source line:** bottom-left, Open Sans 18, Slate, e.g. `Source: WHO, CDC`.
5. **Page number:** bottom-right, Open Sans 18, Slate.

### Illustration style

**Flat, friendly medical illustrations** with soft shapes, in a palette close to §3 (blues and mint with coral accents). They must look consistent across the deck. The asset scout picks 1–2 anchor creators who have a large medical illustration set.

---

## 4. Pipeline

Text, colors and plain layout shapes are generated in code. Agents only add the visuals from Canva Elements.

### Phase 0A — main agent builds the skeleton .pptx (≈5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU), so Canva imports it as 1920 × 1080.
   - Convert px to EMU with `px * 9525`.
2. For every slide in §6, create:
   - the background
   - all text, with exact copy, font names, sizes, colors and letter spacing
   - the plain shapes: white cards, chips, icon-badge circles, divider lines, number circles
3. For every illustration, icon, photo or frame, place a **placeholder rectangle** at its exact position.
   - Fill: 20 % transparent Sky.
   - Add a label, e.g. `ILLUSTRATION: mosquito 520w` or `ICON: soap, in badge`.
4. Add the speaker notes from §7.
5. Save the file as `common-diseases-skeleton.pptx`.
   - If LibreOffice is available, render one slide to PNG as a sanity check.

### Phase 0B — asset scout subagent, in parallel with 0A (≈10 min)

1. Search Canva Elements for every hero illustration and icon in §6.
2. Write the results to `common-diseases-assets.md` with these columns:

   | Slide | Item | Exact search keyword | Creator | Result position (row, column) | Pro/free |

3. Prefer one anchor creator for all heroes, and one consistent icon set for the badge icons. Search tip: "medical icon line".
4. Insert nothing into the design.

### Phase 0C — main agent imports the skeleton (≈3 min)

1. In Canva, go to Buat desain → Impor file (or the Unggahan panel) and upload `common-diseases-skeleton.pptx` with the `file_upload` tool.
   - If the tool can't upload, ask the user to drag the file into Canva once.
2. Rename the design **Common Diseases and Their Prevention**.
3. Check 2–3 slides:
   - Fonts mapped correctly. If a font was substituted, re-set it on the affected text boxes.
   - Card radii survived.
   - Chips are intact.
4. **Fallback if the import is badly broken:** build slide 4 by hand as a fully styled "kit page", duplicate it for every slide, and let builders swap the text. Report which path you used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builder subagents in parallel (≈15 min)

Each builder gets §1, §2, §3, its own slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`. For each slide:
> 1. Insert every illustration and icon listed in the asset sheet (exact keyword, the listed result).
> 2. Lock the aspect ratio. Match each placeholder's size and position via Posisi (Lebar / Tinggi / X / Y).
> 3. Center badge icons inside their circles, at 44 px.
> 4. Delete the placeholders.
> 5. Fix only real problems: overlap, clipping, unreadable text. Don't restyle anything else.
> 6. Zoom-screenshot the slide to check it.
>
> The Canva UI is in Indonesian.
> - Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua".
> - Never copy/paste.
> - If your tab's screenshots time out twice, stop and report "BLOCKED".
>
> Report: per slide, done or issues; assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent: QA and report (≈5 min)

See §8 and §9.

---

## 5. Coordinates

All positions are in px on the 1920 × 1080 page; (x, y) is the top-left corner.

**Disease slides 4–9 share one layout:**
- Disease-type chip at (120, 96).
- Title at (120, 140), width 1100.
- One-line intro at (120, 236), width 1100, Open Sans 26, Slate.
- Hero illustration, about 460 wide, at (1340, 96).
- Three info cards, 540 × 560, at y 380, x = 120 / 690 / 1260:
  - `Cause` card: Sky badge.
  - `Symptoms` card: Coral badge.
  - `Prevention` card: Mint badge, ✓ bullets.
- Source line at (120, 990). Page number at (1760, 990).

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (bg Ice)**
- Label at (120, 220), Sky: `HEALTH AWARENESS`.
- Title at (120, 270), width 960, 3 lines:
  > Common Diseases
  > and Their
  > Prevention
- Subtitle at (120, 640), Open Sans 30, Slate, width 820:
  > A practical guide to staying healthy, every day.
- Presenter line at (120, 820), Open Sans 22, Navy:
  > Presented by: Your Name  •  Your Organization
- Hero: a friendly doctor or nurse illustration with a shield / heart-plus symbol, about 760 wide, at (1060, 160).
  - Behind it: a White circle, 820, at (1020, 140).
- 3 small floating icons around the hero: soap, apple, heart.

**Slide 2 — Why Prevention Matters (bg White)**
- Title at (120, 110):
  > Why Prevention Matters
- Intro at (120, 210), width 1100:
  > Many common illnesses can be avoided — or caught early — with simple daily habits.
- Big stat card, Navy, 760 × 420, at (120, 360):
  - `23–40%` in Outfit Bold 120, Mint.
  - Body below it, White, Open Sans 28:
    > Fewer diarrheal illnesses in communities that practice handwashing with soap.
- Second stat card, Navy, 760 × 420, at (1000, 360):
  - `16–21%` in Outfit Bold 120, Sky.
  - Body, White:
    > Fewer respiratory illnesses, like colds, with regular handwashing.
- Source line:
  > Source: CDC, "Show Me the Science – Why Wash Your Hands?"
- Icon: handwashing / soap, about 120, at the top-right of each card.

**Slide 3 — Two Kinds of Common Diseases (bg Ice)**
- Title at (120, 110):
  > Two Kinds of Common Diseases
- Two large White cards, 820 × 640, at y 280, x = 120 / 980.

  | Card | Chip | Title (Outfit 40) | Body | Bottom line (Open Sans Bold 24) |
  |---|---|---|---|---|
  | Left | `INFECTIOUS` | `Infectious Diseases` | `Caused by viruses, bacteria or parasites. They can spread from person to person, through food and water, or through insects.` | Sky: `Cold & Flu · Dengue · Diarrhea · Tuberculosis` |
  | Right | `LIFESTYLE` | `Lifestyle Diseases` | `Develop slowly and are linked to diet, activity, smoking and genes. They don't spread between people.` | Coral: `Hypertension · Type 2 Diabetes` |

- Each card has an illustration, about 260, at its top-right:
  - Left: virus / germs.
  - Right: heart with a pulse line.

### Builder B

**Slide 4 — Common Cold & Flu** · chip `INFECTIOUS`
- Intro:
  > Very common respiratory infections caused by viruses.
- `Cause`:
  > Viruses that spread through droplets from coughs and sneezes, and from touching contaminated surfaces.
- `Symptoms`:
  > Runny or blocked nose, sore throat, cough, fever, tiredness and body aches.
- `Prevention`, with ✓ bullets:
  - Get a yearly flu vaccine
  - Wash hands with soap for 20 seconds
  - Cover coughs and sneezes
  - Stay home when you're sick
- Hero: a person with a tissue, plus a thermometer.
- Source: WHO, CDC.

**Slide 5 — Dengue Fever** · chip `INFECTIOUS`
- Intro:
  > A viral infection spread by the bite of infected Aedes mosquitoes.
- `Cause`:
  > Dengue virus, carried by Aedes mosquitoes that breed in clean, standing water.
- `Symptoms`:
  > High fever, severe headache, pain behind the eyes, muscle and joint pain, nausea and rash.
- `Prevention`, with ✓ bullets:
  - Drain and cover water containers
  - Recycle or remove items that collect water
  - Use mosquito repellent and nets
  - Wear long sleeves and pants
- Small caption under the Prevention card, Open Sans 20, Slate:
  > Known in Indonesia as "3M Plus".
- Hero: a mosquito illustration, plus a water container.
- Source: WHO, Kemenkes RI.

**Slide 6 — Diarrhea** · chip `INFECTIOUS`
- Intro:
  > Loose, watery stools — often caused by contaminated food or water.
- `Cause`:
  > Viruses, bacteria or parasites from unsafe water, undercooked food or unwashed hands.
- `Symptoms`:
  > Frequent watery stools, stomach cramps, nausea, and signs of dehydration such as dry mouth and little urine.
- `Prevention`, with ✓ bullets:
  - Drink safe, boiled or treated water
  - Wash hands with soap before eating
  - Cook food thoroughly and keep it covered
  - Use oral rehydration solution (ORS) if diarrhea starts
- Hero: a glass of clean water, plus handwashing.
- Source: WHO.

### Builder C

**Slide 7 — Tuberculosis (TB)** · chip `INFECTIOUS`
- Intro:
  > A bacterial infection that mainly affects the lungs.
- `Cause`:
  > TB bacteria, spread through the air when a person with active TB coughs, sneezes or talks.
- `Symptoms`:
  > A cough lasting more than 2 weeks, fever, night sweats, weight loss and tiredness.
- `Prevention`, with ✓ bullets:
  - BCG vaccine for babies
  - Keep rooms well ventilated
  - Get tested if you have a long cough
  - Finish the full course of TB treatment
- Hero: lungs illustration, plus an open window.
- Source: WHO.

**Slide 8 — Hypertension (High Blood Pressure)** · chip `LIFESTYLE`
- Intro:
  > Often called a "silent killer" because it usually has no symptoms.
- `Cause`:
  > Linked to a salty diet, lack of exercise, excess weight, smoking, alcohol and family history.
- `Symptoms`:
  > Usually none. Very high blood pressure can cause headaches, blurred vision or chest pain.
- `Prevention`, with ✓ bullets:
  - Eat less salt (under 5 g a day)
  - Be active at least 150 minutes a week
  - Don't smoke; limit alcohol
  - Check your blood pressure regularly
- Hero: heart with a blood-pressure monitor.
- Source: WHO.

**Slide 9 — Type 2 Diabetes** · chip `LIFESTYLE`
- Intro:
  > A condition where the body can't use insulin properly, so blood sugar stays too high.
- `Cause`:
  > Linked to excess weight, physical inactivity, unhealthy diet, age and family history.
- `Symptoms`:
  > Feeling very thirsty, urinating often, tiredness, blurred vision and slow-healing wounds.
- `Prevention`, with ✓ bullets:
  - Keep a healthy weight
  - Cut down on sugary drinks
  - Choose whole grains, vegetables and fruit
  - Get your blood sugar checked
- Hero: a glucose meter, plus a healthy plate (no needles in skin).
- Source: WHO, CDC.

### Builder D

**Slide 10 — Daily Habits for a Healthy Life (bg Ice)**
- Title at (120, 110):
  > Daily Habits for a Healthy Life
- Six White habit cards in a 3 × 2 grid:
  - Card size 540 × 300.
  - x = 120 / 690 / 1260; y = 300 / 640.
- Each card holds an icon (about 96, from Canva Elements), a card title (Outfit 30, Navy) and one line of body text (Open Sans 24, Slate):

  | # | Title | Body |
  |---|---|---|
  | 1 | `Wash Your Hands` | `With soap, for at least 20 seconds.` |
  | 2 | `Eat Balanced Meals` | `Plenty of vegetables, fruit and whole grains.` |
  | 3 | `Move Every Day` | `Aim for 150 minutes of activity a week.` |
  | 4 | `Sleep Well` | `Most adults need 7–9 hours a night.` |
  | 5 | `Stay Up to Date on Vaccines` | `Protect yourself and the people around you.` |
  | 6 | `Get Regular Check-ups` | `Catch problems early, before symptoms start.` |

**Slide 11 — When to See a Doctor (bg White)**
- Coral chip at (120, 96): `DON'T WAIT`.
- Title at (120, 140):
  > When to See a Doctor
- Left: a list of 5 warning signs.
  - Each row has a Coral circle icon badge (from Canva Elements) and Open Sans 28 Navy text.
  - Rows at y = 340 / 440 / 540 / 640 / 740, x = 120, width 1000:
    - A high fever that lasts more than 3 days
    - Difficulty breathing or chest pain
    - Signs of dehydration: very little urine, dizziness, sunken eyes
    - Bleeding gums, nosebleeds or severe stomach pain during a fever
    - A cough that lasts more than 2 weeks
- Right: a friendly doctor illustration, about 600 tall, at (1260, 240).
- Disclaimer at (120, 900), Open Sans 20, Slate:
  > This presentation is for education only and does not replace professional medical advice.

**Slide 12 — Thank You (bg Navy)**
- Title, centered at y 300, Outfit Bold 110, White:
  > Thank You
- Subtitle, centered at y 470, Open Sans 32, White:
  > Small habits today, a healthier tomorrow.
- Pill, centered at y 580, Mint fill, Navy text, Open Sans Bold 24:
  > Questions? Let's talk.
- Contact line, centered at y 700, Open Sans 24, Ice:
  > www.yourwebsite.com  •  @yourhandle  •  hello@youremail.com
- Sources line, centered at y 900, Open Sans 18, Slate on Navy:
  > Sources: World Health Organization (WHO), U.S. CDC, Kementerian Kesehatan RI
- Decor: 3–4 small white-line medical icons from Canva Elements (heart, shield, leaf, drop), scattered at 30 % opacity near the corners.

---

## 7. Speaker notes (main agent adds them in the .pptx)

- Slide 2:
  > CDC figures: handwashing education reduces diarrheal illness by 23–40% and respiratory illness by 16–21% in the community.
- Slides 4–9:
  > Information is general. Verify against the latest WHO / CDC / Kemenkes guidance before presenting.
- Slide 11:
  > Encourage the audience to seek care early; the list is not exhaustive.

---

## 8. QA checklist (main agent, using `presentation-design`)

- [ ] 12 pages, in order. Every placeholder rectangle deleted.
- [ ] Every illustration, icon, frame and decoration comes from Canva Elements. The skeleton contributed only text and plain layout shapes.
- [ ] No Canva AI assets.
- [ ] Only Outfit + Open Sans (or the stated fallbacks).
- [ ] Body text ≥ 22 px everywhere; only source lines may be smaller.
- [ ] Contrast ≥ 4.5:1.
- [ ] Colors only from §3.
- [ ] Chips, info cards, badges, source lines and page numbers look identical across slides 4–9.
- [ ] Medical text matches §6 word for word. No new claims, numbers or dosages.
- [ ] Illustrations are friendly and consistent. No gore, no needles in skin, no brand or hospital logos.
- [ ] None of the §2 "must differ" items appear.
- [ ] No overlap, clipping or stray elements. Check each page's Lapisan (Layers) list once.
- [ ] Nothing shared, downloaded or published.

## 9. Final report to the user (in Indonesian)

1. The edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately done differently from the reference (§2).
5. Which path was used (pptx import or kit-page fallback), the time per phase, and anything not achieved.
6. A reminder that the medical content should be checked against current WHO / CDC / Kemenkes guidance before presenting.
