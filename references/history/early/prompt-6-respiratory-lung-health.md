# Prompt 6 — "Respiratory Diseases and Lung Health" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + four builder subagents.

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report

Deck slug: `respiratory-lung-health`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Respiratory Diseases and Lung Health"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHQ6kd5Euc/ ("Navy Blue White Gradient Modern Kidney Disease Presentation").

- **Borrow the idea:** a structured medical flow:
  1. background
  2. what it is
  3. causes
  4. symptoms
  5. diagnosis
  6. treatment
  7. prevention
  8. who is at risk
  9. impact

  Also borrow the **row-of-icon-tiles** idea for causes and prevention.
- **Build from scratch.**

**Not a repeat.** This deck must look different from the earlier disease decks in this project.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Structured medical flow | A **"fresh air" concept**: a light sky background with clouds, wind swirls, trees and leaves. Not a navy glossy gradient. |
| Icon tiles for causes / prevention | Tiles are **colorful rounded cloud-shaped cards** with flat icons. **No** photo tiles. |
| Medical subject | Heroes are **cute flat lung characters** and people breathing, exercising and planting trees. **No** 3D anatomical model photos and **no** stock photos of patients or hands. |
| — | **No** frosted navy glass pills, **no** "Bright Clinic" logo, **no** white dot grids on navy |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Cloud Sky | `#EAF6FF` | Background (with soft white cloud shapes) |
| Ink Navy | `#1D2B4F` | Text |
| Breeze Mint | `#3DD6A3` | Healthy lungs, prevention |
| Coral | `#FF6B6B` | Symptoms, warnings |
| Sunshine | `#FFCC3E` | Highlights, sun |
| Lavender | `#9B7BFF` | Accent |
| Sky Blue | `#3A9BFF` | Titles, accent |
| Peach | `#FFA372` | Accent |

**Color rules:**
- Each disease slide has its own theme color for its title highlight, cards and lung-buddy badge:

  | Disease | Theme color |
  |---|---|
  | Asthma | Lavender |
  | Pneumonia | Coral |
  | COPD | Peach |
  | Tuberculosis | Sky Blue |
  | Acute Respiratory Infections (ARI) | Sunshine |

- Every slide also has white clouds and colored wind-swirl lines (Canva) in 2–3 colors.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Fredoka SemiBold | Baloo 2 | 70–84 | Ink Navy, on a theme-color highlight blob |
| Body | Nunito | — | 26–28 | Ink Navy |
| Eyebrow | Nunito ExtraBold | — | 22, UPPERCASE, letter spacing 200 | theme color |

### Recurring motifs

1. **Lung buddy:** a cute flat lung character in a circle badge, placed top-right, colored with the slide's theme.
2. **Cloud cards:** rounded cards with a soft cloud bump on top (Canva cloud shape plus a rectangle), tinted fill.
3. **Wind swirls and leaves:** used as decor on every slide.
4. **Breath meter:** a small colorful bar used on some slides as a visual accent.
5. **Footer:** a thin wavy line in the theme color, plus the page number.

**Transition:** Fade.

### Illustration style

- One flat, cheerful set with:
  - cute organ / lung characters
  - diverse people outdoors (walking, cycling, breathing exercises)
  - nature (trees, clouds, sun)
- One consistent icon set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover**
- Eyebrow: `LUNG HEALTH EDUCATION`
- Title at (120, 240), width 960, 2 lines:
  > Respiratory Diseases and Lung Health
- Pill (Breeze Mint):
  > Every breath counts.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero, right side (~820): a big happy lung character in a park with trees, sun and clouds, and people jogging and cycling around.
- Decor: wind swirls and leaves.

**Slide 2 — How Your Lungs Work**
- Title: `How Your Lungs Work`
- Center hero: a friendly flat diagram of the airway (nose → windpipe → lungs → air sacs), ~620 tall.
- Callout labels are cloud cards with lines pointing to the diagram:
  - `Nose & Mouth` — Air comes in and is warmed.
  - `Windpipe` — Carries air to the lungs.
  - `Lungs` — Two spongy organs in your chest.
  - `Air Sacs (Alveoli)` — Hundreds of millions of tiny sacs where oxygen enters the blood.
- Fun-fact bubble:
  > At rest, adults usually breathe about 12–20 times a minute.

**Slide 3 — What Harms Our Lungs**
- Title: `What Harms Our Lungs?`
- Six colorful cloud tiles in a 3 × 2 grid. Each has an icon and a label:
  - `Tobacco smoke`
  - `Air pollution & haze`
  - `Germs (viruses & bacteria)`
  - `Dust & chemicals at work`
  - `Indoor smoke from cooking fuels`
  - `Allergens like dust mites & pollen`
- Hero: a sad-but-cute lung buddy wearing a mask under a gray cloud (~340).

### Builder B

**Slide 4 — Asthma** (theme Lavender)
- Eyebrow: `LONG-TERM CONDITION`
- Title: `Asthma`
- Three cloud cards:
  - **What it is:** The airways become swollen and narrow, making breathing hard at times.
  - **Signs:** Wheezing, coughing (often at night), chest tightness and shortness of breath.
  - **Managing it:** Avoid triggers, use inhalers exactly as prescribed, and follow an asthma action plan.
- Hero: a kid using an inhaler with a parent (~520).
- Lung buddy in Lavender.

**Slide 5 — Pneumonia** (theme Coral)
- Eyebrow: `INFECTION`
- Title: `Pneumonia`
- Three cloud cards:
  - **What it is:** An infection that fills the lungs' air sacs with fluid.
  - **Signs:** Fever, cough with phlegm, fast or difficult breathing, and chest pain.
  - **Care & prevention:** See a doctor for treatment; vaccines, handwashing and clean air lower the risk.
- Hero: a person resting with a warm drink and a health worker checking on them (~520).
- Fun-fact bubble:
  > Fast breathing in a child can be a sign of pneumonia — seek care quickly.

**Slide 6 — COPD** (theme Peach)
- Eyebrow: `LONG-TERM CONDITION`
- Title: `COPD (Chronic Obstructive Pulmonary Disease)`
- Three cloud cards:
  - **What it is:** Long-term lung damage that blocks airflow and gets worse over time.
  - **Main cause:** Smoking, plus long exposure to smoke, dust and fumes.
  - **Managing it:** Stop smoking, use prescribed inhalers, stay active and get vaccinated.
- Hero: an older adult doing gentle breathing exercises outdoors (~520).

### Builder C

**Slide 7 — Tuberculosis (TB)** (theme Sky Blue)
- Eyebrow: `INFECTION`
- Title: `Tuberculosis (TB)`
- Three cloud cards:
  - **What it is:** A bacterial infection that mainly affects the lungs and spreads through the air.
  - **Signs:** A cough lasting more than 2 weeks, fever, night sweats and weight loss.
  - **Care:** TB is curable — take all medicines for the full course as prescribed.
- Hero: a person opening a window for fresh air, with sunlight streaming in (~500).

**Slide 8 — Acute Respiratory Infections (ARI)** (theme Sunshine)
- Eyebrow: `COMMON & SEASONAL`
- Title: `Acute Respiratory Infections (ARI)`
- Intro card:
  > Short-term infections of the nose, throat or lungs, like colds and flu — very common, especially in children.
- Two columns:
  - `Signs`: Cough, runny nose, sore throat, fever.
  - `Care`: Rest, fluids, cover coughs, and see a health worker if breathing becomes difficult.
- Fun-fact bubble:
  > In Indonesia, ARI is known as "ISPA".
- Hero: kids covering coughs with their elbows (~460).

**Slide 9 — Who Is at Risk?**
- Title: `Who Is at Higher Risk?`
- Five colorful circle portraits (flat illustrations) in a row. Each has a label below:
  - `Young children`
  - `Older adults`
  - `People who smoke`
  - `People with weak immune systems`
  - `People exposed to smoke or dust`
- Bottom banner:
  > Protecting these groups protects the whole community.

### Builder D

**Slide 10 — Keep Your Lungs Healthy**
- Title: `Keep Your Lungs Healthy`
- Hero: a big happy lung buddy holding a heart in a green park (~480).
- Six cloud tiles, each in a different palette color, with an icon:
  - `Don't smoke or vape`
  - `Avoid secondhand smoke`
  - `Wear a mask on high-pollution days`
  - `Exercise regularly`
  - `Get your flu & pneumonia vaccines`
  - `Keep rooms well ventilated`

**Slide 11 — When to See a Doctor**
- Title: `When to See a Doctor`
- A card with a Coral border and ! bullets:
  - ! Difficulty breathing or very fast breathing
  - ! Lips or fingertips turning bluish
  - ! A cough lasting more than 2 weeks
  - ! Coughing up blood
  - ! Chest pain when breathing
- Hero: a friendly doctor listening with a stethoscope to a smiling patient (~420).
- Disclaimer:
  > For education only — not a substitute for professional medical advice.

**Slide 12 — Thank You**
- Title: `Thank You!` in Fredoka 140, on a Sunshine sun-burst.
- Subtitle:
  > Breathe easy, live well.
- Three contact pills (Mint / Sky / Lavender):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources:
  > World Health Organization (WHO), U.S. CDC, Kementerian Kesehatan RI
- Hero along the bottom (~1300): people flying kites in a park, a happy lung buddy, trees, sun and clouds.

## 4. Speaker notes

- Slides 4–11:
  > General information only. Verify with current WHO / CDC / Kemenkes guidance before presenting.

## 5. Deck-specific QA

- [ ] Each disease slide uses its theme color and lung buddy.
- [ ] Medical text matches §3 word for word.
- [ ] No navy glossy gradient, no 3D anatomical photos, no stock photos.
- [ ] Nothing from the earlier disease decks' identities.
