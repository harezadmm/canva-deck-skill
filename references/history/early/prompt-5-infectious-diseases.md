# Prompt 5 — "Infectious Diseases and Their Prevention" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\canva-shared-pipeline.md`.

That file holds:
- §A — hard rules
- §B — colorful brief and richness checklist
- §C — pipeline, builder brief, QA, and report

Deck slug: `infectious-diseases`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Infectious Diseases and Their Prevention"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHQTjfjNNU/ ("Teal and White Modern Kidney Disease Awareness").

- **Borrow the idea:**
  - a clear medical info hierarchy
  - a step/process slide
  - a prevention-habits slide
  - a trustworthy tone
- **Build from scratch.**

**Not a repeat.** This deck must look different from the earlier decks in this project:
- **"Common Diseases":** navy, sky, mint, coral.
- **"Chronic Diseases":** sunrise palette, organ buddies.
- **"Causes, Symptoms & Treatment":** comic Germ Squad.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Medical info hierarchy | A **"Break the Chain" concept**: every slide uses a colorful **chain-link motif**, and prevention slides show the chain snapping |
| Process slide | The process is the **6-link Chain of Infection** drawn as big colorful links, not three teal circles |
| Habits slide | Habits appear as **colorful shield badges** |
| Trustworthy tone | **Flat community illustrations** (neighborhood, school, market, clinic) and cute microbes, **no** stock photos |
| — | **No** teal or white look, **no** curved swoosh corner, **no** cross watermark, **no** hospital mark |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Lemon Cream | `#FFFBEA` | Background |
| Ink | `#1F1B3A` | Text |
| Magenta | `#E0367A` | Accent, "germ" color |
| Cobalt | `#2F5BEA` | Titles, accent |
| Lime | `#7ED957` | Prevention / "safe" color |
| Orange | `#FF8A1F` | Accent, warnings |
| Violet | `#8A4FFF` | Accent |
| Sunny | `#FFD23F` | Highlights, badges |

**Chain links:** the 6 links are always colored in this order — Magenta, Orange, Sunny, Lime, Cobalt, Violet.

**Cards:** card fills rotate through 18 % tints.

### Fonts

| Role | Font | Fallback | Size | Color |
|---|---|---|---|---|
| Titles | Rubik ExtraBold | Montserrat ExtraBold | 70–84 | Cobalt |
| Body | Nunito | — | 26–28 | Ink |
| Eyebrow | Nunito ExtraBold | — | 22, UPPERCASE, letter spacing 200 | Magenta |

### Recurring motifs

1. **Chain-link strip:** a short row of colorful chain links along the top or bottom edge. Use a Canva chain element, recolored.
2. **Shield badges:** colored shield shapes holding icons, used for prevention points.
3. **Cards:** radius 28, 3 px colored outline, tinted fill.
4. **Microbe doodles:** 2–4 cute microbes per slide.
5. **Footer:** page number in a small Cobalt circle.

**Transition:** Push.

### Illustration style

Use **one** flat, bright community illustration set (diverse people, places, health workers), plus **one** cute-microbe set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover**
- Eyebrow: `HEALTH EDUCATION`
- Title, at (120, 240), width 960, 3 lines:
  > Infectious Diseases and Their Prevention
- Highlight pill, Lime:
  > Break the chain, stop the spread.
- Presenter: `Presented by [Your Name] · [Organization]`
- Hero, about 820 wide, right side: a colorful neighborhood scene with people washing hands, a nurse giving a vaccine (no needle in skin), and a broken chain in the sky made of colorful links.
- Decor: microbe doodles and sparkles.

**Slide 2 — What Are Infectious Diseases?**
- Title: `What Are Infectious Diseases?`
- Definition card, Cobalt tint:
  > Illnesses caused by germs — viruses, bacteria, parasites or fungi — that can pass from one person, animal or object to another.
- Four germ cards in a row. Each card has a cute microbe illustration and one example:
  - `Viruses` · flu, measles, hepatitis A
  - `Bacteria` · tuberculosis, typhoid
  - `Parasites` · malaria
  - `Fungi` · ringworm
- Hero: a microscope with a curious student, about 380.

**Slide 3 — The Chain of Infection**
- Title: `The Chain of Infection`
- Six big chain links in an arc across the slide, colored in the order set in §2. Each link has an icon, a title (Rubik 30), and one line (Nunito 22):
  1. `Germ` — The virus, bacteria or parasite.
  2. `Source` — Where it lives: people, animals, water, soil.
  3. `Way Out` — Coughs, blood, stool, bites.
  4. `Spread` — Air, touch, food, water, insects.
  5. `Way In` — Mouth, nose, eyes, skin breaks.
  6. `Next Person` — Someone who can get sick.
- Bottom banner, Lime:
  > Break any one link, and the infection stops spreading.

### Builder B

**Slide 4 — How Germs Spread**
- Title: `How Germs Spread`
- Hero in the center: a flat illustration of a community with dotted paths showing spread, about 640.
- Five route cards around the hero, each with an icon:
  - `Through the air`
  - `Direct contact`
  - `Contaminated food & water`
  - `Insect bites`
  - `Blood & body fluids`

**Slide 5 — Measles**
- Eyebrow: `AIRBORNE`
- Title: `Measles`
- Three cards: `Cause & Spread` · `Signs` · `Prevention`.
  - **Cause & Spread:** Measles virus; spreads very easily through the air when an infected person coughs or sneezes.
  - **Signs:** High fever, cough, runny nose, red eyes, then a red rash spreading from the face down.
  - **Prevention:** Two doses of the MMR vaccine give strong, long-lasting protection.
- Hero: a child resting with a parent nearby (no rash close-ups), plus a vaccine vial icon.

**Slide 6 — Hepatitis A**
- Eyebrow: `FOOD & WATER`
- Title: `Hepatitis A`
- Same 3-card layout:
  - **Cause & Spread:** Hepatitis A virus; spreads through food or water contaminated with stool from an infected person.
  - **Signs:** Tiredness, nausea, stomach pain, dark urine and yellowing of the skin or eyes.
  - **Prevention:** The hepatitis A vaccine, safe drinking water, and handwashing before eating and after using the toilet.
- Hero: a family washing fruit and drinking clean water; a cute liver icon.

### Builder C

**Slide 7 — Malaria**
- Eyebrow: `INSECT-BORNE`
- Title: `Malaria`
- Same 3-card layout:
  - **Cause & Spread:** A parasite spread by the bite of infected Anopheles mosquitoes, mostly at night.
  - **Signs:** Fever, chills, sweating, headache and body aches — it can become serious quickly.
  - **Prevention:** Sleep under treated mosquito nets, use repellent, and get tested early if you have a fever in malaria areas.
- Hero: a family under a mosquito net at night with a cartoon mosquito outside; stars and a moon.

**Slide 8 — HIV**
- Eyebrow: `BLOOD & BODY FLUIDS`
- Title: `HIV`
- Same 3-card layout:
  - **Cause & Spread:** A virus that weakens the immune system; spreads through certain body fluids, such as blood, sexual fluids and breast milk.
  - **Signs:** Often no symptoms for years — testing is the only way to know.
  - **Prevention:** Get tested, use condoms, never share needles, and ask a health worker about prevention medicine (PrEP).
- Fun-fact bubble:
  > HIV does not spread through hugging, sharing food or mosquito bites.
- Hero: friendly people at a community health booth, with a red-ribbon icon.
- **Imagery note:** respectful and stigma-free.

**Slide 9 — How Vaccines Protect Us**
- Title: `How Vaccines Protect Us`
- Three-step horizontal flow. Each step is a colored card with an illustration and a number badge:
  1. `Train` — A vaccine shows your body a harmless piece or copy of the germ.
  2. `Remember` — Your immune system learns and remembers it.
  3. `Defend` — If the real germ comes, your body fights it fast.
- Below: a **community immunity** illustration — many shielded people protecting a few unshielded ones. Caption:
  > When most people are vaccinated, the whole community is better protected.

### Builder D

**Slide 10 — Break the Chain: Everyday Prevention**
- Title: `Break the Chain`
- Hero: a big colorful chain snapping in the middle with a burst, about 520.
- Six shield badges in a 3 × 2 grid, each with a different color, an icon, and a label:
  - `Wash hands with soap`
  - `Get vaccinated`
  - `Cover coughs & sneezes`
  - `Drink safe water`
  - `Cook food well`
  - `Stop mosquito breeding`

**Slide 11 — When to Get Help**
- Title: `When to See a Health Worker`
- Left — card `GET CHECKED IF…`, with ! bullets:
  - A fever lasts more than 3 days
  - Breathing is difficult
  - A rash appears with fever
  - There are signs of dehydration
  - You may have been exposed to a serious infection
- Right — card `STAY HOME WHEN SICK`, with ✓ bullets:
  - ✓ Rest and drink fluids
  - ✓ Wear a mask around others if coughing
  - ✓ Keep your own cup and towel
- Hero: a friendly health worker with a clipboard, about 360.
- Disclaimer:
  > For education only — not a substitute for professional medical advice.

**Slide 12 — Thank You**
- Title: `Thank You!` — Rubik 140, Cobalt, on a Sunny burst.
- Subtitle:
  > Together, we can break the chain.
- Three contact pills (Magenta / Lime / Cobalt):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources:
  > World Health Organization (WHO), U.S. CDC, Kementerian Kesehatan RI
- Hero: a diverse community waving, with a broken chain turning into confetti, about 1300 wide.

## 4. Speaker notes

- **Slides 5–11:**
  > General information only. Verify with current WHO / CDC / Kemenkes guidance before presenting.
- **Slide 8:**
  > Use respectful, non-stigmatizing language. Testing and treatment are available and effective.

## 5. Deck-specific QA

- [ ] Chain-link colors stay in the same order everywhere.
- [ ] Medical text matches §3 word for word. HIV imagery is respectful. No needles in skin, no rash close-ups.
- [ ] No teal/white look. No stock photos. Nothing from the earlier disease decks' identities.
