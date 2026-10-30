# Prompt set8-11 — "Bone and Joint Diseases" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A = pages 1–3, B = 4–6, C = 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set8-health\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10)

Deck slug: `bone-joint`.

**Ready skeleton (Phase 0A already done):** if this file exists, upload it instead of building a new one:
`%USERPROFILE%\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\scratch-workspaces\dcdc6f97-14f9-43a0-812f-7b344eef061a\12aa8b61-941b-457d-8505-99fb0b2a7c89\scratch-2026-10-22-82e737\pptx\h\bone-joint-skeleton.pptx`
(script: `bone-joint.py` in the same folder).

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Bone and Joint Diseases"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHNwKhxkf8/ ("Blue Beige Informative Bone Cancer Health Presentation").

- **Borrow the idea:**
  1. an informative, well-structured layout: clear title, short labeled sections, one topic per slide;
  2. blue as the lead color.
- **Build from scratch.**
- **Do not** make it about cancer. **Do not** use a blue/beige-only palette.

**Not a repeat.** This deck must look different from every earlier disease deck in this project (see §1).

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Informative, well-structured layout | A **"Body Frame" concept**: the skeleton as the body's building frame. A light **blueprint-paper background with a faint grid**, plus colorful construction accents: rulers, bolts, hinge icons for joints, and building-block cards. |
| Blue as the lead color | A bright **Blueprint Blue `#2D8CFF`** (not cobalt, not navy) leads, shared with Tangerine, Sunflower, Mint, Coral and Lilac. **4+ palette colors on every slide.** No blue/beige-only look. |
| Bone health subject | The deck covers **common bone and joint diseases** (osteoporosis, osteoarthritis, rheumatoid arthritis, gout, back pain). **Nothing about cancer.** |
| Clean medical tone | Heroes are a **cute flat bone / skeleton buddy** and **active, diverse people** (walking, yoga, dancing, older adults exercising). **No** stock photos, **no** X-ray photos, **no** 3D anatomical renders, **no** logos, **no** spooky or Halloween skeletons (no skulls with dark eyes, no tombstones, no bats). |
| — | Nothing from earlier decks: **no** chain links, shield badges, Rubik or cobalt ("Infectious Diseases"); **no** sky clouds, cloud cards, lung buddy or Fredoka ("Respiratory"); **no** peach cream, winding path or fruit badges (earlier "Digestive"); **no** metro map (set8 digestive), ECG line (heart), neuron network (brain) or water flow (kidney). |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Blueprint Paper | `#EEF5FF` | Background (with the faint grid) |
| Grid Line | `#2D8CFF` at 10 % opacity | Blueprint grid lines, every 240 px |
| Ink | `#1A2140` | All text, page-number bolt, disclaimer bar |
| Blueprint Blue | `#2D8CFF` | Lead color: ruler underlines, eyebrows, cover, "Bones" |
| Tangerine | `#FF8A3D` | Osteoarthritis, accents |
| Sunflower | `#FFC93C` | Gout, fact bubbles, footer ruler |
| Mint | `#2EC4A0` | Back pain & posture, healthy habits |
| Coral | `#FF5E6C` | Rheumatoid arthritis, warnings |
| Lilac | `#A178F0` | Osteoporosis, accents |

**Color rules:**
- Each disease slide has its own theme color for its eyebrow, ruler underline, card beams and bone-buddy badge:

  | Slide | Theme color |
  |---|---|
  | 3 Osteoporosis | Lilac |
  | 4 Osteoarthritis | Tangerine |
  | 5 Rheumatoid Arthritis | Coral |
  | 6 Gout | Sunflower |
  | 7 Back Pain & Posture | Mint |
  | 9 When to See a Doctor | Coral |

- Slides 1, 2, 8 and 10 use all six accents (Blueprint Blue leads).
- Text on any colored fill is **Ink**. White text only on Ink. (White on Tangerine / Sunflower / Mint fails contrast.)
- Card fills: white, or a 20–25 % tint of the theme color.

### Fonts

Both fonts are on the shared whitelist (§D). Use only these two families.

| Role | Font | Size / style | Color |
|---|---|---|---|
| Titles | Alfa Slab One | 76–100 (Thank You 130) | Ink, with a theme-color ruler underline |
| Body | Poppins | 26 | Ink |
| Card heads | Poppins + bold flag | 30 | Ink |
| Eyebrow | Poppins + bold flag | 22, UPPERCASE, letter spacing 200 | theme color |

### Recurring motifs

1. **Blueprint grid:** faint Blueprint Blue grid lines on every slide (the skeleton draws them as thin lines). Builders may swap them for a Canva "blueprint grid pattern" element at 85–90 % transparency, behind everything. Never put text on top of busy grid decor.
2. **Bone buddy badge:** a cute flat bone or skeleton character inside a round badge with four "bolt" dots on its ring, top-right (220 px), in the slide's theme color. Each slide gives the buddy a different pose.
3. **Steel-plate cards ("building blocks"):** white rounded cards (radius 16–20) with an 18 px colored "beam" along the top and two bolt dots on the beam. Each card has an icon, a bold head and short body text.
4. **Ruler underline:** a colored bar with tick marks under every title (plain shapes).
5. **Hinge icons:** joints are drawn as hinges — use a hinge icon on the "Joints" card and as small decor on joint-disease slides.
6. **Construction accents:** bolts, nuts, rulers, set squares and small colored building blocks as decor; sparkles in palette colors.
7. **Footer:** a small Sunflower measuring-tape ruler bottom-left and the page number in an Ink **hex-bolt** (hexagon) bottom-right.

**Transition:** Stack ("Tumpuk") on every page. Fallback: Slide ("Meluncur").

### Illustration style

- One flat, friendly, cheerful set with:
  - a cute **bone buddy** (a smiling cartoon bone or a soft, round, friendly skeleton — never scary);
  - **diverse active people**: walking, yoga, dancing, cycling, stretching, older adults exercising, kids playing;
  - simple friendly health scenes (a doctor checking a knee, someone drinking water).
- One consistent icon set (rounded, bold outline or flat colored).
- **Search terms (Canva Elements):**
  - characters: `cute bone character`, `happy bone cartoon`, `cute skeleton medical`, `friendly skeleton flat`, `knee joint cartoon`, `spine character cute`
  - people: `elderly exercise flat`, `people yoga flat illustration`, `people dancing flat`, `walking people flat`, `doctor knee examination flat`, `office posture flat`, `drinking water flat illustration`
  - icons: `bone icon`, `joint icon`, `hinge icon`, `milk icon`, `sun icon`, `dumbbell icon`, `no smoking icon`, `no alcohol icon`, `shoe icon`, `stethoscope icon`, `thermometer icon`, `phone icon`, `mail icon`, `globe icon`
  - decor: `blueprint grid pattern`, `ruler`, `bolt nut`, `set square`, `building blocks`, `sparkle`, `confetti`
- **Skip** anything tagged Halloween, spooky, horror, X-ray, cancer or logo.

## 3. Slide-by-slide spec

Layouts alternate so no two neighboring slides match. Sizes in px.

### Builder A

**Slide 1 — Cover** (text left, hero right)
- Eyebrow (Blueprint Blue): `BONE & JOINT HEALTH`
- Title at (120, 236), width 860, 2 lines, Alfa Slab One 96:
  > Bone and Joint Diseases
- A row of six small colored building blocks (one per accent) under the title.
- Pill (Mint):
  > Your body's frame, built to move.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero, right side (~860): a big happy bone buddy standing on a blueprint sheet, surrounded by diverse people walking, dancing and doing yoga, plus an older adult stretching.
- Decor: ruler, bolts, hinge doodles, mini bones, sparkles.

**Slide 2 — Bones & Joints 101** (center hero, 4 callout cards)
- Eyebrow (Blueprint Blue): `THE BODY FRAME`
- Title: `Bones & Joints 101`
- Center hero (~520 × 640): a friendly full-body skeleton buddy waving, with its knee and elbow joints highlighted. Not spooky.
- Four steel-plate cards (2 left, 2 right), each with an icon:
  - `Bones` (Blueprint Blue) — Support your body and protect organs like the brain, heart and lungs.
  - `Muscles` (Coral) — Pull on bones to move them.
  - `Joints` (Tangerine, hinge icon) — Where two bones meet, letting us bend, twist and turn.
  - `Cartilage` (Mint) — A smooth, rubbery cushion on the ends of bones inside joints.
- Fact bubble (Sunflower):
  > Adults have 206 bones — and bone is living tissue that keeps renewing itself.

**Slide 3 — Osteoporosis** (theme Lilac; hero left, 3 stacked cards right)
- Eyebrow: `WEAK BONES`
- Title: `Osteoporosis`
- Three steel-plate cards:
  - **What it is:** Bones lose density and become thin and fragile, so they break more easily.
  - **Signs:** Often no signs until a bone breaks; over time, loss of height or a stooped back.
  - **Care & prevention:** Get enough calcium and vitamin D, do weight-bearing exercise, and ask a doctor about a bone density test.
- Hero (~520): an older woman lifting light hand weights next to a smiling bone buddy.
- Fact bubble under the hero:
  > Often called a "silent disease" — many people only find out after a bone breaks.
- Bone buddy badge in Lilac (pose: flexing a tiny dumbbell).

### Builder B

**Slide 4 — Osteoarthritis** (theme Tangerine; centered title, hero top center, 3 cards in a row)
- Eyebrow: `WEAR AND TEAR`
- Title: `Osteoarthritis`
- Hero, top center (~520 × 370): an older man doing gentle knee exercises on a stationary bike, with a smiling knee-hinge buddy.
- Fact bubble, top right (Sunflower tint):
  > The most common type of arthritis — often in the knees, hips and hands.
- Decor, top left: blueprint knee-joint sketch, bolts, ruler.
- Three steel-plate cards in a row:
  - **What it is:** The cartilage that cushions the ends of bones slowly wears down, so the joint becomes painful and stiff.
  - **Signs:** Pain that gets worse with use, stiffness after rest, swelling, and a grating or creaking feeling.
  - **Care & prevention:** Stay active, keep a healthy weight, strengthen the muscles around the joint, and ask a doctor about pain relief.
- Bone buddy badge in Tangerine (pose: holding a hinge).

**Slide 5 — Rheumatoid Arthritis** (theme Coral; 3 stacked cards left, hero right)
- Eyebrow: `AUTOIMMUNE CONDITION`
- Title: `Rheumatoid Arthritis`
- Three steel-plate cards:
  - **What it is:** An autoimmune disease: the immune system attacks the lining of the joints by mistake, causing inflammation.
  - **Signs:** Painful, swollen, stiff joints — often on both sides of the body, like both hands — plus tiredness.
  - **Care:** Early diagnosis and treatment help protect the joints. Stay active, and rest when joints flare up.
- Hero (~540): two friends doing gentle hand and wrist stretches on yoga mats.
- Fact bubble under the hero:
  > Stiffness that lasts a long time in the morning is a common sign of RA.
- Bone buddy badge in Coral (pose: doing a wrist stretch).

**Slide 6 — Gout** (theme Sunflower; intro band, hero left, 2 cards right)
- Eyebrow: `INFLAMMATORY ARTHRITIS`
- Title: `Gout`
- Intro band (Sunflower tint), with a bold lead-in:
  > **What it is:** Too much uric acid builds up and forms sharp crystals in a joint — very often the big toe.
- Hero (~520): a person resting on a sofa with one foot raised, drinking water, while a bone buddy offers a water bottle.
- Two steel-plate cards:
  - **Signs:** Sudden, intense joint pain with swelling, redness and heat — often starting at night.
  - **Care & prevention:** See a doctor for treatment, drink plenty of water, and limit alcohol, sugary drinks, red meat and organ meats.
- Fact bubble:
  > Gout can be well controlled with treatment and healthy habits.
- Bone buddy badge in Sunflower (pose: holding a water glass).

### Builder C

**Slide 7 — Back Pain & Posture** (theme Mint; centered title, intro band, hero center, 2 tip cards each side)
- Eyebrow: `EVERYDAY CARE`
- Title: `Back Pain & Posture`
- Intro band (Mint tint):
  > Most back pain comes from strained muscles or poor posture, and it often gets better within a few weeks.
- Hero, center (~520 × 560): a person sitting tall at a desk with the screen at eye level, and a spine buddy giving a thumbs-up.
- Four tip cards, each with an icon and its own color:
  - `Sit tall` (Mint) — Keep your back supported and your feet flat on the floor.
  - `Lift smart` (Tangerine) — Bend your knees, keep the load close, and don't twist.
  - `Move often` (Lilac) — Stand up and stretch every 30–60 minutes.
  - `Stay active` (Blueprint Blue) — Gentle walking and core exercises help support your spine.
- Bone buddy badge in Mint (pose: standing up straight).

**Slide 8 — Build Strong Bones** (2 × 3 building-block grid left, hero right)
- Eyebrow (Blueprint Blue): `PREVENTION`
- Title: `Build Strong Bones`
- Six building-block tiles, each a different palette color, with an icon:
  - `Calcium-rich foods` (Blueprint Blue, milk icon) — Milk, yogurt, tofu, tempeh, small fish with bones and leafy greens.
  - `Vitamin D & sunlight` (Sunflower, sun icon) — Get some safe morning sun, plus eggs and oily fish.
  - `Weight-bearing exercise` (Mint, walking/dumbbell icon) — Walk, dance, climb stairs or lift light weights.
  - `No smoking` (Coral, no-smoking icon) — Smoking weakens bones and slows healing.
  - `Limit alcohol` (Lilac, no-alcohol icon) — Too much alcohol weakens bones and raises the risk of falls.
  - `Prevent falls` (Tangerine, shoe icon) — Clear clutter, use good lighting and wear non-slip shoes.
- Hero, right (~480 × 620): an older adult and a kid stacking colorful building blocks into a giant happy bone, with people walking and dancing around them.
- Decor, top right: building blocks, bolts, sparkles.

**Slide 9 — When to See a Doctor** (theme Coral; hero left, warning card right, disclaimer bar)
- Eyebrow: `WARNING SIGNS`
- Title: `When to See a Doctor`
- Hero, left (~540): a friendly doctor checking a patient's knee, with a bone buddy holding a clipboard.
- Supporting icons under the hero: stethoscope, thermometer, knee joint, bolts.
- A white card with a Coral border and beam, and Coral ! bullets:
  - ! A swollen, red or hot joint with fever
  - ! Pain or trouble moving after a fall or injury
  - ! Sudden, severe joint pain
  - ! Morning joint stiffness lasting more than 30 minutes
  - ! Loss of movement in a joint
  - ! Numbness or tingling in your arms or legs
- Disclaimer bar (Ink, white text):
  > For education only — not a substitute for professional medical advice.

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Alfa Slab One 130, with a wide Blueprint Blue ruler underline.
- Subtitle:
  > Keep moving, stay strong.
- Three contact pills (Mint / Sunflower / Lilac), Ink text, each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources card:
  > Sources: World Health Organization (WHO) · U.S. NIH (NIAMS) · Kementerian Kesehatan RI
- Hero along the bottom (~1400): a long row of diverse active people (walking, yoga, dancing, an older couple stretching) with the bone buddy waving.
- Decor: building blocks, bolts, sparkles, confetti in all six accents.

## 4. Speaker notes

- Slide 2:
  > Think of the body as a building: bones are the frame, muscles move it, joints are the hinges and cartilage is the cushion.
- Slides 3–9:
  > General information only. Verify with current WHO / NIH (NIAMS) / Kemenkes guidance before presenting.

## 5. Deck-specific QA

- [ ] 10 pages; slides 3–7 and 9 use their theme color; slides 3–7 have the bone buddy badge.
- [ ] Every slide has the blueprint grid, a ruler underline (or ruler accent), and at least 4 palette colors.
- [ ] Cards look like steel plates / building blocks (colored beam + bolt dots); hinge icons appear on joint content.
- [ ] Medical text matches §3 word for word; disclaimer present on slide 9.
- [ ] Only Alfa Slab One and Poppins.
- [ ] No stock photos, no X-ray photos, no 3D anatomy, no logos, no cancer content, no spooky/Halloween skeletons.
- [ ] Not blue/beige-only; nothing from the earlier decks' identities (§1).
- [ ] Transition Stack (or Slide) on every page.
