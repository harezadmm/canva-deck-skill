# Prompt 3 — "Causes, Symptoms and Treatment of Common Diseases" (colorful, fast pipeline)

> Copy everything below into a new task.
> Team: one **main agent** + **1 asset scout** + **4 builder subagents**.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Causes, Symptoms and Treatment of Common Diseases"**. It is an educational health deck for students and the general public.

### Client brief: COLORFUL, illustration-rich, not too simple

- Every slide must feel lively and layered, like a fun comic-style science poster.
- Every slide shows **at least 4 palette colors** and passes the richness checklist in §3.

### Language and timing

- All deck content is in **English**. Report to the user in **Indonesian**.
- Expected time: about 40–50 minutes.

### Reference (direction only)

https://www.canva.com/templates/EAHDbFJbn8M/ — "Red Green and Blue Illustrated Germs and Diseases Presentation".

- **Borrow the idea:**
  - cute, colorful germ illustrations
  - playful health-education tone
  - chunky titles
  - pill-shaped labels
  - a topic flow of germs → spread → diseases → symptoms → prevention
- **Build from scratch.** Never click "Use this template", and never copy its pages or elements.

### Skills to load first (main agent)

| Skill | Use |
|---|---|
| `anthropic-skills:pptx` | Skeleton |
| `elite-powerpoint-designer` | Creative Bold style |
| `ppt-visual` | Varied layouts |
| `presentation-design` | QA |

---

## 1. Hard rules (all agents)

1. **Built from scratch; all assets come from Canva Elements** (project rule).
   - The code skeleton contains **text and plain layout shapes only**: background, panels, pills, circles and lines.
   - Every visual comes from Canva Elements (Elemen → Grafis / Stiker / Bentuk / Bingkai). That includes characters, germs, icons, halftone patterns, bursts, speech bubbles and doodles.
   - Pro elements are allowed.
2. **No Canva AI.**
   - Do not use Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva" or "Buat Animasi".
   - Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.** No sharing, publishing or downloading, and no changes to sharing, access or account settings.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** The clipboard is shared between agents.
6. **Medical text exactly as written in §6.** No new claims, no medicine names beyond those listed, no dosages.
7. **No real logos** of hospitals, brands or drugs.
8. **Friendly imagery only.** No gore, vomit, open wounds or needles in skin. Sick characters should look cute, not distressing.

---

## 2. Borrow vs. must differ

| Borrow (the idea) | Must differ (our identity) |
|---|---|
| Cute colorful germs | Germs are **characters in a comic story**, "Germ Squad vs. Body Defenders" (immune-cell heroes). They are not just scattered as a border. |
| Colorful health-education tone | **No** white grid-paper background, **no** blue blobs in every corner, **no** germ frame around every slide |
| Chunky titles | Comic-style titles (Bangers) on **burst / banner shapes**, not plain coral slab titles |
| Pill labels | Pills are **color-coded by section**: Cause = Purple, Symptoms = Orange, Treatment = Green |
| Topic flow | Disease slides use a **3-panel comic strip** layout. No "Team Members" slide. No magnifying-glass + hands cover. |

---

## 3. Design system

**Canvas:** 1920 × 1080. Margins: 120 left and right, 96 top and bottom. Spacing in multiples of 24.

### Colors

| Token | Hex | Use |
|---|---|---|
| Sunny Cream | `#FFF6E0` | Main background |
| Ink | `#22223B` | Titles, body, comic outlines |
| Germ Purple | `#8E5CF7` | **Cause** color, germ characters |
| Zesty Orange | `#FF8A3D` | **Symptoms** color |
| Healing Green | `#2FBF71` | **Treatment** color |
| Pop Pink | `#FF4F8B` | Accents, title bursts |
| Sky Pop | `#3FA9F5` | Accents, "body defender" heroes |
| Lemon | `#FFD23F` | Highlights, speech bubbles, starbursts |

**Color rules (colorful brief):**
- Each comic panel has a **tinted fill** (20 % of its section color) and a 5 px Ink outline.
- Each slide adds a **halftone-dot pattern** (Canva element) in one accent color in 1–2 corners.
- Title bursts rotate through Pop Pink → Sky Pop → Lemon → Germ Purple across slides.
- Germs come in at least 3 colors per infectious slide.

### Fonts (max 2 families)

- **Titles:** Bangers (fallback: Luckiest Guy).
- **Body:** Nunito (fallback: Quicksand).

| Style | Spec |
|---|---|
| Cover title | Bangers 140–160, Ink, on a Lemon burst |
| Slide title | Bangers 76–88, Ink, on a colored banner or burst |
| Panel label pill | Nunito ExtraBold 22, UPPERCASE, White on the section color |
| Panel title | Bangers 40 |
| Body | Nunito 26–28, Ink, line spacing 1.4; never below 22 |
| Speech bubble | Nunito Bold 26 |

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per panel.
- Max 4 font sizes per slide.
- Contrast ≥ 4.5:1.
- Motion: panels Pop or Rise in sequence. Max 3 animated elements per slide. Transition: Push.

### Recurring motifs (identical on every slide)

1. **Title banner / burst** behind every title (Canva comic burst or ribbon banner).
2. **Comic panels:**
   - radius 24
   - 5 px Ink outline
   - tinted fill
   - a section pill at the top-left (`CAUSE` / `SYMPTOMS` / `TREATMENT`)
3. **Speech bubble** in Lemon. A germ or defender "says" a fun fact.
4. **Germ Squad:** cute germ characters, used on infectious slides.
5. **Body Defenders:** cute immune-cell / white-blood-cell hero characters, used on treatment panels.
6. **Halftone dots** in corners, plus a page number in a small Ink circle at the bottom right.

### Illustration style

- Flat, bright, cartoon / comic illustrations with bold shapes.
- The asset scout picks **one germ-character set** and **one people-character set** that match, and uses them everywhere.

### Richness checklist (every slide)

- 1 hero illustration (≥ 480 px).
- 3–6 supporting icons or characters.
- At least 2 decor layers (halftone, burst, doodles or sparkles).
- Text sits in panels or bubbles, never as a bare paragraph.
- **At least 4 palette colors visible.**

---

## 4. Pipeline

### Phase 0A — main agent: skeleton .pptx (~5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU).
   - Conversion: px × 9525 = EMU.
2. For every slide, create:
   - the background
   - all text (exact copy, fonts, sizes, colors)
   - the plain panels (tint fill + Ink outline), pills and circles
3. Mark every visual with a labeled placeholder rectangle at its exact position.
   - Fill: 20 % transparent Sky Pop.
   - Label example: `HERO: boy sneezing, comic style 520w`.
4. Add the speaker notes from §7.
5. Save as `causes-symptoms-treatment-skeleton.pptx`.

### Phase 0B — asset scout, in parallel (~10–12 min)

1. Search Canva Elements for every visual in §6, plus:
   - the burst/banner set
   - the halftone pattern
   - the speech bubble
   - the germ set and defender set
2. Write `causes-symptoms-treatment-assets.md` with these columns:

   | Slide | Item | Exact keyword | Creator | Result (row, col) | Pro/free |

3. Useful keywords:
   - "cute germ character"
   - "virus cartoon"
   - "white blood cell cartoon"
   - "comic burst"
   - "halftone dots"
   - "comic speech bubble"
   - "flat illustration sick kid"
4. Insert nothing into the design.

### Phase 0C — main agent: import (~3 min)

1. Upload the skeleton with the `file_upload` tool (Buat desain → Impor file, or Unggahan). If that fails, ask the user to drag the file in once.
2. Rename the design.
3. Check fonts and the panel outlines.
4. **Fallback:** if the import breaks, build slide 6 by hand as a kit page and duplicate it. Report which path you used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builders in parallel (~20–25 min)

Each builder gets §1–3, its slides from §6, the asset sheet, and this brief:

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`.
>
> For each slide:
> 1. Place the decor first: title burst/banner, halftone, doodles.
> 2. Then place the hero, characters, icons and speech bubble, using the exact keyword and result from the asset sheet.
> 3. Lock the aspect ratio and match each placeholder using Posisi. Delete the placeholders.
> 4. Run the richness checklist and the colorful check.
> 5. Fix only overlap and clipping.
> 6. Take a zoom screenshot.
>
> Rules:
> - The UI is in Indonesian.
> - Never use Tanya Canva, AI Canva, Bagikan, Unduh or "Ubah semua".
> - Never copy/paste.
> - If screenshots time out twice, stop and report "BLOCKED".
>
> Report per slide (done/issues) and the assets used (keyword + creator + Pro/free).

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

### Phase 2 — main agent: QA + report (~5 min)

---

## 5. Layouts

All positions are px on the 1920 × 1080 page, as top-left (x, y).

**Disease-slide comic strip (slides 6–10):**
- Title banner at (120, 80), up to 1100 wide.
- Hero character at the top right, ~460 wide, at (1340, 60).
- One-line intro at (120, 200), Nunito Bold 28.
- Three comic panels, each 540 × 600, at y 330, x 120 / 690 / 1260:
  - **CAUSE**: Purple pill, purple tint, plus a germ character (~150).
  - **SYMPTOMS**: Orange pill, orange tint, plus a symptom icon (~150).
  - **TREATMENT**: Green pill, green tint, plus a body-defender hero (~150).
- Lemon speech bubble overlapping the bottom edge of one panel, without covering text.

---

## 6. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (bg Sunny Cream)**
- Big Lemon comic burst behind the title at (80, 160).
- Title at (140, 230), width 960, Bangers 140, 3 lines:
  > CAUSES, SYMPTOMS
  > & TREATMENT
  > OF COMMON DISEASES
  - Shrink to 120 if needed to fit.
- Subtitle at (140, 720), Nunito Bold 30, width 860:
  > Meet the germs, read the signs, and learn how we get better.
- Presenter pill at (140, 830), Germ Purple, White text:
  > Presented by Your Name
- Hero at (1060, 140), ~780 wide: a comic scene of Body Defender heroes facing off against a colorful Germ Squad, with "POW!" and "ZAP!" bursts.
- Decor: halftone dots in 2 corners, and sparkles.

**Slide 2 — What's Inside (bg Sunny Cream)**
- Title banner (Pop Pink):
  > WHAT'S INSIDE
- 6 numbered comic tiles in a 3 × 2 grid.
  - Tile size: 540 × 300.
  - x = 120 / 690 / 1260; y = 300 / 640.
  - Each tile has a different section color tint, a number badge (Bangers 48 in a Lemon circle), a title (Bangers 36) and a small icon (~110).

  | No. | Title | Icon |
  |---|---|---|
  | 01 | What Causes Disease? | germ |
  | 02 | How Germs Spread | sneeze |
  | 03 | How Your Body Fights Back | shield |
  | 04 | 5 Common Diseases | thermometer |
  | 05 | Treatment & Care | medicine bottle |
  | 06 | When to See a Doctor | doctor |

**Slide 3 — What Causes Disease? (bg Sunny Cream)**
- Title banner (Sky Pop):
  > WHAT CAUSES DISEASE?
- Four germ "character cards" in a row.
  - Card size: 400 × 520.
  - x = 120 / 560 / 1000 / 1440; y = 280.
  - Each card has its own color (Purple / Green / Orange / Pink tint), a cute germ character (~220), a name (Bangers 40) and one line of text:

  | Germ | Text |
  |---|---|
  | Viruses | Tiny germs that cause colds, flu and dengue. |
  | Bacteria | Some cause typhoid and food poisoning. |
  | Parasites | Can live in dirty water and undercooked food. |
  | Fungi | Can cause skin and nail infections. |

- Bottom strip at y 860: a Lemon speech bubble from a defender hero:
  > Not all germs are bad — many bacteria actually help us digest food!

### Builder B

**Slide 4 — How Germs Spread (bg Sunny Cream)**
- Title banner (Germ Purple, White text):
  > HOW GERMS SPREAD
- Center hero: a person character with arrows radiating to 4 route panels (~520 tall), at (700, 300).
- 4 comic panels, 2 on each side, each 520 × 300, at x 120 / 1280 and y 300 / 640:

  | Panel | Title | Text | Icon |
  |---|---|---|---|
  | 1 | Coughs & Sneezes | Tiny droplets float through the air. | sneeze cloud |
  | 2 | Touching Surfaces | Germs on hands reach the eyes, nose and mouth. | hand + door handle |
  | 3 | Food & Water | Unsafe water and undercooked food carry germs. | glass + plate |
  | 4 | Insect Bites | Mosquitoes can carry viruses like dengue. | mosquito |

**Slide 5 — How Your Body Fights Back (bg Sky Pop tint)**
- Title banner (Lemon):
  > HOW YOUR BODY FIGHTS BACK
- Left: a big comic panel, 900 × 640, with a hero illustration of Body Defenders (white blood cells) battling germs.
- Right column at x 1080: three stacked step cards, each 720 × 190, in different colors:
  1. **Skin & Mucus** — Your first wall that keeps germs out.
  2. **White Blood Cells** — Defenders that find and fight germs.
  3. **Memory** — Your body remembers germs it has met, and vaccines train it too.
- Speech bubble at the bottom left:
  > Fever is often a sign your body is fighting an infection!

**Slide 6 — Common Cold** (comic strip layout)
- Title banner (Pop Pink):
  > COMMON COLD
- Intro:
  > A mild infection of the nose and throat.
- **CAUSE:**
  > Viruses — most often rhinoviruses — spread by droplets and hands.
- **SYMPTOMS:**
  > Runny or stuffy nose, sneezing, sore throat, mild cough, and sometimes a low fever.
- **TREATMENT:**
  > Rest, plenty of fluids, warm drinks and saltwater gargles. Most colds get better in 7–10 days.
- Speech bubble:
  > Antibiotics don't work on viruses like the cold!
- Hero: a kid with a tissue and a scarf.

### Builder C

**Slide 7 — Influenza (Flu)** (comic strip)
- Title banner (Sky Pop):
  > INFLUENZA (FLU)
- Intro:
  > A stronger respiratory infection that comes on quickly.
- **CAUSE:**
  > Influenza viruses, spread by coughs, sneezes and touching contaminated surfaces.
- **SYMPTOMS:**
  > Sudden fever, chills, body aches, headache, cough and strong tiredness.
- **TREATMENT:**
  > Rest and fluids. A doctor may prescribe antiviral medicine, which works best when started early.
- Speech bubble:
  > A yearly flu vaccine helps protect you!
- Hero: an adult under a blanket with a thermometer.

**Slide 8 — Diarrhea** (comic strip)
- Title banner (Zesty Orange):
  > DIARRHEA
- Intro:
  > Loose, watery stools — and the risk of losing too much water.
- **CAUSE:**
  > Viruses, bacteria or parasites from unsafe water, undercooked food or unwashed hands.
- **SYMPTOMS:**
  > Frequent watery stools, stomach cramps, nausea, and signs of dehydration like a dry mouth.
- **TREATMENT:**
  > Drink oral rehydration solution (ORS), keep eating light food, and children may be given zinc as advised by a health worker.
- Speech bubble:
  > See a doctor if there's blood in the stool or signs of severe dehydration.
- Hero: a boy holding his tummy, plus an ORS glass.

**Slide 9 — Dengue Fever** (comic strip)
- Title banner (Germ Purple, White text):
  > DENGUE FEVER
- Intro:
  > A viral infection spread by Aedes mosquitoes.
- **CAUSE:**
  > Dengue virus, passed on by the bite of an infected Aedes mosquito.
- **SYMPTOMS:**
  > High fever, severe headache, pain behind the eyes, muscle and joint pain, nausea and rash.
- **TREATMENT:**
  > There's no specific cure: rest, drink plenty of fluids, and use paracetamol for fever. Avoid aspirin and ibuprofen.
- Speech bubble:
  > Go to the hospital fast if there's bleeding, severe stomach pain or constant vomiting.
- Hero: a cartoon mosquito, plus a kid resting with a fever.

### Builder D

**Slide 10 — Typhoid Fever** (comic strip)
- Title banner (Healing Green, White text):
  > TYPHOID FEVER
- Intro:
  > A bacterial infection spread through contaminated food and water.
- **CAUSE:**
  > Salmonella Typhi bacteria, from unsafe water or food handled with unwashed hands.
- **SYMPTOMS:**
  > Long-lasting high fever, weakness, stomach pain, headache, and constipation or diarrhea.
- **TREATMENT:**
  > Antibiotics prescribed by a doctor — finish the full course — plus rest and plenty of fluids.
- Speech bubble:
  > Safe water, clean hands and the typhoid vaccine help prevent it.
- Hero: a person resting in bed with a glass of water.

**Slide 11 — Treatment & When to See a Doctor (bg Sunny Cream)**
- Title banner (Healing Green):
  > GETTING BETTER
- **Left** — a big Green panel, 820 × 680, labeled `CARE AT HOME`, with ✓ bullets:
  - ✓ Rest and sleep well
  - ✓ Drink plenty of fluids
  - ✓ Eat light, healthy food
  - ✓ Take medicine only as advised by a health worker
  - ✓ Antibiotics only for bacterial infections — never for colds or flu
- **Right** — a Pop Pink panel, 820 × 680, labeled `SEE A DOCTOR IF…`, with ! bullets:
  - ! A high fever lasts more than 3 days
  - ! Breathing is difficult
  - ! Signs of dehydration appear
  - ! There's bleeding or severe stomach pain
  - ! Symptoms keep getting worse
- Hero: a friendly doctor with a Body Defender sidekick (~360), placed between or below the panels.
- Disclaimer at the bottom, Nunito 20:
  > For education only — not a substitute for professional medical advice.

**Slide 12 — Thank You (bg Sunny Cream)**
- Giant Lemon burst in the center. On it:
  > THANK YOU!
  - Bangers 150, Ink.
- Subtitle below, Nunito Bold 32:
  > Wash your hands, stay curious, stay healthy!
- Three contact pills in Purple / Orange / Green:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources line, Nunito 20:
  > Sources: World Health Organization (WHO), U.S. CDC, Kementerian Kesehatan RI
- Hero: the Body Defenders celebrating with a defeated (but cute) Germ Squad waving goodbye, plus confetti and halftone.

---

## 7. Speaker notes

- Slides 5–11:
  > General information only. Verify against current WHO / CDC / Kemenkes guidance before presenting.
- Slide 9:
  > Dengue: avoid aspirin/ibuprofen because of bleeding risk; paracetamol is the usual fever reducer.

---

## 8. QA checklist (main agent, with `presentation-design`)

- [ ] 12 pages in order. All placeholders are deleted.
- [ ] The richness checklist and the **colorful check** (≥ 4 palette colors) pass on every slide.
- [ ] Section colors are consistent: Cause = Purple, Symptoms = Orange, Treatment = Green.
- [ ] Every visual comes from Canva Elements. No Canva AI assets.
- [ ] One germ set and one character set are used throughout.
- [ ] Only Bangers + Nunito (or the fallbacks). Body text ≥ 22. Contrast ≥ 4.5:1.
- [ ] Medical text matches §6 word for word. No gore, no needles, no logos.
- [ ] None of the §2 "must differ" items appear: no grid paper, no corner blobs, no germ border, no team slide.
- [ ] No overlap, clipping or stray elements (check Lapisan).
- [ ] Nothing shared, downloaded or published.

## 9. Final report (Indonesian)

Include:
1. The edit link.
2. One line per slide.
3. Assets used: keyword + creator + Pro/free.
4. The deliberate differences from the reference.
5. Which path was used, the time per phase, and anything not achieved.
6. A reminder to verify the medical content.
