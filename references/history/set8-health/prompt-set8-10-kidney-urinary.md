# Prompt set8-10 — "Kidney and Urinary Tract Diseases" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set8-health\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `kidney-urinary`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Kidney and Urinary Tract Diseases"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHSoIbE7lY/ ("Kidney Disease Overview Presentation" — beige, brown, teal, illustrated).

- **Borrow the idea:**
  1. a **friendly illustrated overview** (flat drawings, not photos);
  2. **teal as the accent color**;
  3. **clear info cards**, one topic per card;
  4. a clear medical flow:
     1. how the kidneys work
     2. the main conditions, one per slide
     3. who is at risk
     4. prevention and daily habits
     5. warning signs
- **Build from scratch.**

**Not a repeat.** This deck must look different from the earlier disease decks in this project and from the other set8 decks.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Friendly illustrated overview | A **"Clean Flow" concept**: water droplets, **flowing wave ribbons** and a **"filter" motif** (a bubble trail of droplets passing through) on every slide. |
| Teal accent | **Not** beige or brown. A light **Aqua Mist** background with **six bright accents**, at least 4 per slide. |
| Clear info cards | Every topic card sits on a **droplet- or wave-shaped panel**: "wave cards" with a wavy crest along the top, and "droplet tiles" with a teardrop icon badge. **No** plain beige boxes copied from the reference. |
| Medical subject | Heroes feature two cute flat **kidney-bean buddies** and diverse flat people. **No** stock photos, **no** realistic anatomy, **no** gross imagery (no blood, no realistic urine or stones close-ups), **no** logos. |
| — | **No** chain links, shield badges, Rubik or cobalt ("Infectious Diseases"). **No** sky clouds, cloud cards, lung buddy or Fredoka ("Respiratory"). **No** peach-cream winding path or fruit badges (earlier "Digestive"). **No** metro map, ECG / heartbeat line, monitor cards, neuron network or blueprint grid (other set8 decks). |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Aqua Mist | `#EAFBFA` | Background (with soft wave ribbons along the bottom) |
| Ink | `#1B2A3A` | Text, titles |
| Teal | `#14B8A6` | Main accent, water, cover; Ink text on it |
| Ocean Blue | `#1F6FE0` | Kidney basics, risk; white text allowed on it |
| Coral | `#FF6F61` | Infection, warnings; Ink text on it |
| Sunshine | `#FFC93C` | Highlights, kidney stones; Ink text on it |
| Lilac | `#A78BFA` | Long-term condition; Ink text on it |
| Lime | `#9BD84A` | Healthy habits; Ink text on it |
| White | `#FFFFFF` | Tile bodies, list card |

**Color rules:**
- Each section has its own color for the eyebrow chip, card icon badges, kidney-buddy badge ring and footer droplet:

  | Section | Slides | Section color |
  |---|---|---|
  | Welcome | 1 | Teal |
  | How kidneys work | 2 | Ocean Blue |
  | Urinary tract infection | 3 | Coral |
  | Kidney stones | 4 | Sunshine |
  | Chronic kidney disease | 5 | Lilac |
  | Who is at risk | 6 | Ocean Blue |
  | Stay hydrated | 7 | Teal |
  | Kidney-friendly habits | 8 | Lime |
  | When to see a doctor | 9 | Coral |
  | Finale | 10 | All six (rainbow wave) |

- The **bubble trail** under each title always uses 4–5 different palette colors.
- Tiles, side cards and wave ribbons rotate through the palette so that **at least 4 accents** are clearly visible on every slide.
- White text only on Ocean Blue (contrast ≥ 4.5:1). Use Ink text on Teal, Coral, Sunshine, Lilac and Lime.

### Fonts

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Chewy | — (whitelist; re-set to Chewy if substituted) | 72–100 (Thank You 140), no highlight behind it | Ink |
| Body | Quicksand | — | 24–28 (never below 22) | Ink |
| Card headers / labels | Quicksand Bold (family "Quicksand" + bold) | — | 26–30 | Ink (white on Ocean Blue) |
| Eyebrow | Quicksand Bold | — | 22, UPPERCASE, letter spacing 200, in a small tinted chip | Ink |

Only these 2 families. Both are on the §D whitelist. In Canva, set bold with the font panel's **Cetak Tebal**, not by picking a separate font name.

### Recurring motifs

1. **Wave ribbons:** 2–3 overlapping flowing wave ribbons (Teal / Ocean Blue / Lilac, or the section color plus two others) along the bottom edge of every slide, below all content. Canva wave elements, recolored.
2. **Kidney-bean buddies:** two cute flat kidney-bean characters (simple faces, little arms and legs) that appear on every slide — inside the hero, or in a round badge at the top right with a ring in the section color. Same two character designs on every slide; only the pose and prop change (water glass, stop sign, clipboard, stethoscope, sneakers).
3. **Wave cards:** tinted rounded panels (radius 32, section-color tint) with a **wavy crest** along the top edge (Canva wave shape, recolored to the section color) and a round icon badge in the section color. Used for the "What it is / Signs / Care" cards.
4. **Droplet tiles:** white rounded tiles with a 4 px outline in a palette color and a **teardrop / droplet badge** (Canva droplet shape) holding the icon. Used for risk factors and habits.
5. **Filter bubble trail:** a row of 5 shrinking droplet-bubbles in 4–5 palette colors directly under each title, like water passing through a filter.
6. **Footer:** a small **droplet** in the section color holding the page number, bottom right.

**Transition:** Slide ("Meluncur"), applied to all pages.

### Illustration style

- One flat, cheerful, rounded set with:
  - the two kidney-bean buddies (and one simple, friendly urinary-tract diagram — no realistic anatomy)
  - diverse people of all ages: drinking water, jogging, cycling, visiting a doctor or nurse
  - simple health objects: water glass, water bottle, stethoscope, clipboard, blood-pressure cuff, salt shaker
  - water: droplets, splashes, waves, a fountain
- One consistent icon set (bold rounded line icons, filled with palette colors).

**Search terms for the asset scout** (Canva Elements, English keywords):
- `cute kidney character`, `kidney mascot flat`, `kidney cartoon cute`, `kidney bean character`
- `urinary system illustration flat`, `urinary tract diagram`, `kidney anatomy flat illustration`
- `water droplet flat`, `water drop character`, `water splash flat`, `wave ribbon`, `wave border`, `water wave shape`
- `drinking water illustration flat`, `water glass flat`, `water bottle flat`, `water fountain flat`
- `doctor patient flat illustration`, `nurse blood pressure flat`, `elderly checkup illustration`
- `family jogging flat illustration`, `cycling people flat`, `cartoon germs cute`, `small stones cartoon`
- `bubbles doodle`, `droplet confetti`, `sparkle doodle`
- Icons: `kidney icon`, `bladder icon`, `filter icon`, `blood pressure icon`, `diabetes icon`, `salt shaker icon`, `pill icon`, `toilet icon`, `fever thermometer icon`, `swelling leg icon`, `stethoscope icon`, `water drop icon`

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover** (Teal; title left, hero right)
- Eyebrow chip (Teal tint): `KIDNEY HEALTH EDUCATION`
- Title at (120, 210), width 860, Chewy 100, 3 lines:
  > Kidney and / Urinary Tract / Diseases
- Filter bubble trail under the title.
- Pill (Teal, Ink text):
  > Keep the flow clean.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- A row of three droplet badges (Ocean Blue / Sunshine / Lilac) with icons: water glass, kidney, stethoscope.
- Hero, right side (~800): the two kidney-bean buddies high-fiving beside a big glass of water, with droplets, splashes and wave ribbons, and people drinking water around them.
- Decor: droplets and bubbles in the top-left corner; wave ribbons along the bottom.

**Slide 2 — How Your Kidneys Work** (Ocean Blue; two card columns, center hero)
- Eyebrow chip (centered): `THE BODY'S FILTER`
- Title (centered): `How Your Kidneys Work`
- Filter bubble trail under the title.
- Left column, header pill `What your kidneys do`, then four small wave cards, each with an icon:
  - `Filter blood` (Ocean Blue) — Clean your blood all day and night.
  - `Remove waste` (Sunshine) — Turn waste and extra water into urine.
  - `Balance water & salts` (Teal) — Keep the right amount of fluid and minerals in your body.
  - `Help control blood pressure` (Coral) — Make hormones that help keep blood pressure steady.
- Center hero (~560): a friendly flat diagram of the urinary tract — kidneys, ureters, bladder, urethra — with the kidney buddies' faces on the kidneys. No realistic anatomy.
- Right column, header pill `Your urinary tract`, then four small wave cards:
  - `Kidneys` (Lilac) — Two bean-shaped filters below your ribs, near your back.
  - `Ureters` (Teal) — Thin tubes that carry urine to the bladder.
  - `Bladder` (Sunshine) — A stretchy bag that stores urine.
  - `Urethra` (Ocean Blue) — The tube that carries urine out of the body.
- Fun-fact bubble (Sunshine tint, under the hero):
  > Each kidney is about the size of your fist.
- Kidney-buddy badge, top right.

**Slide 3 — Urinary Tract Infection (UTI)** (Coral; hero left, cards right)
- Eyebrow chip: `INFECTION`
- Title, 2 lines: `Urinary Tract Infection` / `(UTI)`
- Filter bubble trail under the title.
- Three stacked wave cards (Coral):
  - **What it is:** Germs, usually bacteria, get into the urinary tract — most often the bladder.
  - **Signs:** Pain or burning when urinating, needing to urinate often, and cloudy or strong-smelling urine.
  - **Care & prevention:** See a doctor — antibiotics may be needed. Drink enough water and don't hold urine for long.
- Hero, left (~520): a person drinking water while the kidney buddies hold a "stop" sign up to cute cartoon germs. Friendly, not gross.
- Fun-fact bubble (Lilac tint, under the hero):
  > UTIs are more common in women, because their urethra is shorter.
- Kidney-buddy badge, top right.

### Builder B

**Slide 4 — Kidney Stones** (Sunshine; cards row on top, hero bottom center)
- Eyebrow chip (centered): `COMMON CONDITION`
- Title (centered): `Kidney Stones`
- Filter bubble trail under the title.
- Three wave cards in a row (Sunshine):
  - **What it is:** Hard, pebble-like bits that form from minerals and salts in urine.
  - **Signs:** Severe pain in the side or back, pain when urinating, and pink, red or brown urine.
  - **Care & prevention:** Small stones may pass on their own; a doctor can help with pain and larger stones. Drink plenty of water and limit salt.
- Hero, bottom center (~680): a kidney buddy happily drinking water while tiny cute pebbles slide away on a wave. No realistic stones.
- Fun-fact bubble (Teal tint, bottom left):
  > Not drinking enough water raises the risk of kidney stones.
- Decor, bottom right: droplets and bubbles.
- Kidney-buddy badge, top right.

**Slide 5 — Chronic Kidney Disease (CKD)** (Lilac; statement band, cards left, hero right)
- Eyebrow chip: `LONG-TERM CONDITION`
- Title: `Chronic Kidney Disease (CKD)`
- Filter bubble trail under the title.
- Statement band (Lilac tint):
  > Diabetes and high blood pressure are the leading causes of CKD.
- Three stacked wave cards (Lilac):
  - **What it is:** The kidneys slowly lose their ability to filter blood over months or years.
  - **Signs:** Often no signs early on. Later: tiredness, swelling in the legs or feet, and changes in urination.
  - **Managing it:** Control blood sugar and blood pressure, take medicines as prescribed, and get regular kidney tests.
- Hero, right (~520): an older adult at a health check, a friendly nurse with a blood-pressure cuff, and a kidney buddy holding a clipboard.
- Tip chip (Lime tint, under the hero):
  > Simple blood and urine tests can find CKD early.
- Kidney-buddy badge, top right.

**Slide 6 — Who Is at Risk?** (Ocean Blue; hero left, 3 × 2 droplet tiles right, banner)
- Eyebrow chip: `RISK FACTORS`
- Title: `Who Is at Risk?`
- Filter bubble trail under the title.
- Six droplet tiles in a 3 × 2 grid, each with a droplet badge, an icon and a label:
  - `Diabetes` (Coral)
  - `High blood pressure` (Ocean Blue)
  - `Family history of kidney disease` (Lilac)
  - `Older age` (Sunshine)
  - `Frequent painkiller use` (Teal)
  - `Obesity` (Lime)
- Hero, left (~520): a diverse group (an older adult, a middle-aged adult, a young adult) with a kidney buddy holding a checklist.
- Bottom banner (Ocean Blue fill, white text):
  > If you have a risk factor, ask your doctor about a simple kidney check.
- Kidney-buddy badge, top right.

### Builder C

**Slide 7 — Stay Hydrated** (Teal; hero center, cards both sides, banner)
- Eyebrow chip (centered): `DRINK UP`
- Title (centered): `Stay Hydrated`
- Filter bubble trail under the title.
- Hero, center (~520): the two kidney buddies splashing happily in a giant glass of water, with droplets flying out.
- Left, two wave cards:
  - `Water first` (Teal) — Make water your main drink. Many adults need about 8 glasses a day — more in hot weather.
  - `Sip through the day` (Ocean Blue) — Keep a water bottle nearby and drink regularly, not all at once.
- Right, wave card `The color check` (Sunshine):
  - Intro: `Look at the color of your urine:`
  - Swatch (pale yellow `#FFF3A6`) + label: `Pale yellow — well hydrated`
  - Swatch (dark yellow `#D9A21B`) + label: `Dark yellow — drink more water`
  - Caption: `A quick, simple check — not a medical test.`
- Bottom banner (Teal fill, Ink text):
  > Drink more when it's hot or when you exercise and sweat.
- Kidney-buddy badge, top right.

**Slide 8 — Kidney-Friendly Habits** (Lime; title + hero on top, 6 droplet tiles in a row)
- Eyebrow chip: `EVERY DAY COUNTS`
- Title: `Kidney-Friendly Habits`
- Filter bubble trail under the title.
- Intro chip (Lime tint):
  > Small daily habits help your kidneys work well for life.
- Hero, top right (~580): the kidney buddies jogging with a family past a park water fountain.
- Six tall droplet tiles in one row, each outlined in a different palette color, with a droplet badge and icon:
  - `Limit salt` (Coral)
  - `Control blood sugar & blood pressure` (Ocean Blue)
  - `Don't overuse painkillers` (Lilac)
  - `Don't hold urine for long` (Sunshine)
  - `Stay active` (Lime)
  - `Get checked regularly` (Teal)

**Slide 9 — When to See a Doctor** (Coral; list card left, hero right)
- Eyebrow chip: `WARNING SIGNS`
- Title: `When to See a Doctor`
- Filter bubble trail under the title.
- White card with a Coral border, header `See a doctor if you notice:`, and ! bullets (Coral circles):
  - ! Pain or burning when urinating
  - ! Blood in your urine (pink, red or brown)
  - ! Severe pain in your side or back
  - ! Fever with back or side pain
  - ! Swelling of the legs, feet or face
  - ! Passing much less urine than usual
- Hero, right (~580): a friendly doctor talking with a smiling patient, a kidney buddy holding a stethoscope.
- Banner (Coral tint, under the hero):
  > Don't wait — early care protects your kidneys.
- Disclaimer chip:
  > For education only — not a substitute for professional medical advice.
- Kidney-buddy badge, top right.

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Chewy 140, centered.
- Filter bubble trail (wide) under the title.
- Subtitle:
  > Keep your kidneys happy — keep the flow clean.
- Three contact pills, each with an icon:
  - `123-456-7890` (Teal, Ink text)
  - `hello@yourwebsite.com` (Ocean Blue, white text)
  - `www.yourwebsite.com` (Lilac, Ink text)
- Sources chip:
  > Sources: World Health Organization (WHO), U.S. NIH (NIDDK), Kementerian Kesehatan RI
- Hero along the bottom (~1400): diverse people of all ages raising water bottles with the two kidney buddies riding a rainbow wave (all six palette colors), with droplets and splashes.
- Decor: droplets and sparkles in both top corners.

## 4. Speaker notes

- Slides 2–9:
  > General information only. Verify with current WHO / NIH (NIDDK) / Kemenkes guidance before presenting.
- Slide 3, add:
  > Take antibiotics only when prescribed, and finish the course as directed.
- Slide 6, add:
  > "Painkillers" here mainly means NSAIDs such as ibuprofen used often or in high doses. Ask a doctor or pharmacist before long-term use.
- Slide 7, add:
  > Fluid needs differ by person. People with kidney failure or heart failure may need to limit fluids — follow your doctor's advice.
- Slide 9, add:
  > In Indonesia, call 119 for medical emergencies. Check the local emergency number for your audience.

## 5. Deck-specific QA

- [ ] 10 pages in order; Slide ("Meluncur") on all pages.
- [ ] Every slide has the wave ribbons, the filter bubble trail and the kidney-bean buddies (in the hero or the badge).
- [ ] Disease slides (3–5) use wave cards in their section color; slides 6 and 8 use droplet tiles.
- [ ] At least 4 palette accents visible per slide; Aqua Mist background; no beige or brown.
- [ ] Only Chewy and Quicksand.
- [ ] Medical text matches §3 word for word; the disclaimer is on slide 9.
- [ ] No stock photos, no realistic anatomy, no gross imagery, no logos.
- [ ] Nothing from the earlier decks' identities (chain links, shields, clouds, lung buddy, winding path, fruit badges, metro map, ECG line, monitor cards, neurons, blueprint).
