# Prompt set8-9 — "Brain and Nervous System Disorders" (colorful)

> Copy everything below into a new task.
> Team: one main agent + one asset scout + three builder subagents (A pages 1–3, B 4–6, C 7–10).

**FIRST:** read and follow every section of this file:
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set8-health\canva-shared-pipeline.md`

It contains:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report
- §D — lessons learned, including the **font whitelist** and the **10-slide rule** (builders A = 1–3, B = 4–6, C = 7–10). Where §C still says 12 slides / 4 builders, §D wins.

Deck slug: `brain-nervous-system`.

---

## 0. Goal

Build a 10-slide Canva presentation (1920 × 1080) called **"Brain and Nervous System Disorders"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAHJlKiGb20/ ("Purple and Orange Modern Nervous System Presentation").

- **Borrow the idea:**
  1. **purple + orange** as the two lead colors;
  2. a **modern, clean layout** with generous white space and clear card blocks;
  3. a simple flow: how the system works → one disorder per slide → healthy habits → when to see a doctor.
- **Build from scratch.**

**Not a repeat.** This deck must look different from every earlier health deck in this project:

| Earlier deck | Its identity (do **not** reuse) |
|---|---|
| Infectious Diseases | chain links, shield badges, Rubik |
| Respiratory | sky clouds, cloud cards, lung buddy, Fredoka |
| Digestive (earlier) | peach cream, winding path, fruit badges |
| set8 Digestive | metro / subway map |
| set8 Heart | ECG heartbeat line |
| set8 Kidney | water flow |
| set8 Bone | blueprint grid |

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Purple + orange as lead colors | A **"Neuron Network" concept**: colorful nerve-connection lines with **glowing dot nodes** link the cards on every slide, like a constellation. The reference's flat purple panels are not used. |
| Modern, clean layout | **Light Lavender Mist background** with 4+ bright colors per slide. Not dark, not navy, no glossy gradient. |
| Clear card blocks for each topic | Cards are **white "neuron cards"** with a colored outline and a colored **icon node** (circle) on their top-left corner; wires run from node to node. **No** photo cards. |
| Medical subject | Heroes are a **cute flat brain buddy** character and flat diverse people. **No** stock photos, **no** realistic brain / anatomy photos or 3D renders, **no** logos. |
| — | **No** chain links, shields, clouds, winding paths, metro maps, ECG lines, water waves or blueprint grids. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Lavender Mist | `#F3F0FF` | Background (solid) |
| Ink | `#221A3F` | Text |
| Neuron Purple | `#6C3CF0` | Titles, lead accent, Alzheimer's theme |
| Spark Orange | `#FF8A2B` | Lead accent, title underline, Stroke theme |
| Synapse Teal | `#14B8A6` | Accent, Epilepsy theme |
| Zesty Lime | `#9BE15D` | Accent, Parkinson's theme |
| Pop Pink | `#FF5FA2` | Accent, Migraine theme |
| Sunny Yellow | `#FFD23F` | Fun-fact bubbles, sparks, Thank-you burst |
| White | `#FFFFFF` | Card fill |

**Color rules:**
- Each disorder slide has its own theme color for its eyebrow pill, card outlines and brain-buddy ring:

  | Disorder | Theme color |
  |---|---|
  | Migraine | Pop Pink |
  | Epilepsy | Synapse Teal |
  | Stroke | Spark Orange |
  | Alzheimer's Disease & Dementia | Neuron Purple |
  | Parkinson's Disease | Zesty Lime |

- Text on a Neuron Purple fill is White. Text on every other colored fill (orange, teal, lime, pink, yellow) is **Ink** — white fails contrast there.
- Every slide shows **at least 4 palette colors**: wires and icon nodes use 2–3 colors that are different from the theme.

### Fonts

Both fonts are on the §D whitelist. Set weights as family **"Nunito"** plus the bold flag (SemiBold = regular weight in pptx, ExtraBold = bold); in Canva use **Cetak Tebal**, never Ctrl+B on SemiBold.

| Role | Font | Fallback | Size / style | Color |
|---|---|---|---|---|
| Titles | Luckiest Guy | Lilita One | 72–96 (Thank You 140) | Neuron Purple |
| Card heads | Nunito ExtraBold | — | 28 | Ink |
| Body | Nunito SemiBold | — | 26 | Ink |
| Eyebrow | Nunito ExtraBold | — | 22, UPPERCASE, letter spacing 200, inside a theme-color pill | Ink (White on purple) |

Max 4 font sizes per slide: title, 28, 26, 22.

### Recurring motifs

1. **Neuron network:** thin (5 px) colored wire lines that connect cards, icons and the hero, with **glowing dot nodes** (a solid 18 px dot inside a 40 px 30 %-transparent halo) at each joint. In Canva, add organic neuron / nerve-line graphics on top of the skeleton's straight wires.
2. **Brain buddy:** a cute flat brain character (pink-purple, big eyes, small arms). On disorder slides it sits in a **200 px ring node** top-right (6 px theme-color ring, light theme tint fill) — a node of the network, not a plain badge.
3. **Signal sparks:** small spark / lightning-burst / star stickers riding along the wires, in Sunny Yellow and Spark Orange.
4. **Axon underline:** under every title, an 8 px Spark Orange rounded bar with a glowing node on each end.
5. **Neuron cards:** white rounded cards (radius 28, 3 px outline) with a 64 px colored icon node on the top-left corner.
6. **Footer:** a short axon wire ending in the page number inside a 64 px colored node, bottom-right.

**Transition:** Circle wipe (**"Sapuan lingkaran"**), applied to all pages with "Terapkan ke semua halaman". Fallback if missing: Dissolve (**"Larut"**).

### Illustration style

- One flat, cheerful, rounded set with:
  - the brain buddy character (same creator on every slide);
  - diverse people of all ages (reading, cycling, chatting, resting, exercising, helping);
  - simple health scenes (doctor, phone call, photo album, tai chi).
- One consistent icon set (bold rounded line icons with a color fill).
- Search terms to try first:
  - `cute brain character`, `brain mascot flat`, `happy brain cartoon`
  - `neuron network line`, `nerve cell illustration flat`, `neural connection dots`
  - `spark doodle`, `lightning burst sticker`, `glowing dots`
  - `nervous system flat illustration` (friendly body outline — no realistic anatomy)
  - `headache woman resting flat`, `first aid recovery position flat`, `calling ambulance flat`
  - `grandparent grandchild photo album flat`, `elderly tai chi flat`, `doctor patient talking flat`
  - icons: `brain icon`, `spine icon`, `neuron icon`, `moon sleep icon`, `dumbbell icon`, `helmet icon`, `phone icon`

## 3. Slide-by-slide spec

Coordinates are px on 1920 × 1080. Keep all content above y 960; the footer sits below.

### Builder A

**Slide 1 — Cover** (title left, hero right)
- Eyebrow pill (Spark Orange) at (100, 230):
  > BRAIN HEALTH EDUCATION
- Title at (100, 290), width 960, Luckiest Guy 84, 2 lines:
  > Brain and Nervous
  > System Disorders
- Axon underline at (100, 524).
- Pill (Spark Orange, Ink text) at (100, 580):
  > Stay sharp, stay connected.
- Presenter line at (100, 690):
  > Presented by [Your Name] · [Organization]
- Three small icon nodes (book, bicycle, chat bubble) at y 780, joined by wires.
- Hero, right side (1100, 120), ~720 × 800: a big happy brain buddy at the center of a glowing neuron network, with diverse people (reading, cycling, chatting) sitting at the nodes.
- Decor: neuron lines + glow dots top-left; signal sparks along the bottom.

**Slide 2 — How Your Nervous System Works** (center hero, 4 cards around)
- Title, centered, Luckiest Guy 72:
  > How Your Nervous System Works
- Center hero (700, 220), 520 × 700: a friendly flat body outline showing the brain, spinal cord and branching nerves. No realistic anatomy.
- Four neuron cards, each wired to the hero with a node at the hero's edge:
  - Left top (Neuron Purple) `Brain` — The control center: it thinks, remembers and controls your body.
  - Right top (Spark Orange) `Spinal Cord` — The main pathway carrying messages between the brain and the body.
  - Left bottom (Synapse Teal) `Nerves` — Cables that carry signals to and from every part of your body.
  - Right bottom (Pop Pink) `Neurons` — Billions of nerve cells that send tiny electrical and chemical signals.
- Fun-fact bubble (Sunny Yellow), bottom-right:
  > Your brain has about 86 billion neurons.
- Decor bottom-left: signal sparks + glow dots.

**Slide 3 — Migraine** (theme Pop Pink; cards stacked left on a vertical nerve spine, hero right)
- Eyebrow pill: `HEADACHE DISORDER`
- Title: `Migraine`
- Three neuron cards, x 180, width 1000, linked by a vertical wire at x 132:
  - **What it is:** A brain condition that causes repeated, often severe headaches that can last from hours to days.
  - **Signs:** Throbbing pain, often on one side of the head, with nausea and sensitivity to light and sound. Some people see flashing lights (aura) first.
  - **Care:** Rest in a dark, quiet room, note and avoid your triggers, and see a doctor if headaches are frequent or severe.
- Hero (1260, 300), 520 × 520: a person resting in a dim, quiet room with an eye mask and a glass of water.
- Tip bubble (Sunny Yellow) under the hero:
  > Common triggers: stress, poor sleep, skipped meals and bright lights.
- Brain buddy ring in Pop Pink.

### Builder B

**Slide 4 — Epilepsy** (theme Synapse Teal; 3 cards across the top, first-aid panel bottom-left, hero bottom-right)
- Eyebrow pill: `SEIZURE DISORDER`
- Title: `Epilepsy`
- Three neuron cards in a row (y 270), linked by one horizontal wire with nodes in the gaps:
  - **What it is:** A brain condition that causes repeated seizures — sudden bursts of electrical activity in the brain.
  - **Signs:** Staring spells, jerking movements, stiffness, or a brief loss of awareness.
  - **Care:** Many people become seizure-free with the right medicine, taken every day as prescribed.
- First-aid panel (100, 556), 1180 × 400, light teal tint, head `Seizure First Aid`, five numbered steps in two columns (numbers in teal nodes joined by wires):
  1. Stay calm and stay with the person.
  2. Time the seizure.
  3. Protect the head with something soft.
  4. Turn them gently onto their side.
  5. Put nothing in their mouth.
- Banner inside the panel (Spark Orange, Ink text, phone icon):
  > Call emergency services if a seizure lasts more than 5 minutes.
- Hero (1340, 556), 480 × 400: a helper gently turning a person onto their side, with a cushion under the head.
- Brain buddy ring in Synapse Teal.

**Slide 5 — Stroke — Act F.A.S.T.** (theme Spark Orange; hero left, What-it-is card + 2 × 2 F.A.S.T. tiles + Care banner right)
- Eyebrow pill: `MEDICAL EMERGENCY`
- Title: `Stroke — Act F.A.S.T.`
- Hero (100, 280), 520 × 600: a person calling emergency services on a phone while helping someone sit down.
- Card **What it is:** A stroke happens when blood flow to part of the brain is blocked or a blood vessel bursts. Brain cells start to die within minutes.
- Four F.A.S.T. tiles (2 × 2). Each has a 120 px letter node (Luckiest Guy 84), a small icon, a head and one line. Wires join F → A → S → T:
  - **F** (Neuron Purple node) `Face` — Is one side of the face drooping?
  - **A** (Synapse Teal node) `Arms` — Can they raise both arms? Does one drift down?
  - **S** (Pop Pink node) `Speech` — Is speech slurred or strange?
  - **T** (Spark Orange node) `Time` — Call emergency services right away.
- Care banner (light orange tint):
  > **Care:** Note the time symptoms started. Fast hospital treatment saves brain cells and lives.
- Brain buddy ring in Spark Orange.

**Slide 6 — Alzheimer's Disease & Dementia** (theme Neuron Purple; hero top center, 3 cards in a row at the bottom)
- Eyebrow pill (White text): `MEMORY & THINKING`
- Title (Luckiest Guy 72): `Alzheimer's Disease & Dementia`
- Hero (700, 250), 520 × 360: an older adult and a grandchild looking at a photo album together.
- Fun-fact bubble (Sunny Yellow), left of the hero:
  > Dementia is not a normal part of aging.
- Decor right of the hero: floating photo frames, small hearts and glow dots.
- Three neuron cards in a row (y 640), purple outlines, icon nodes in orange / teal / pink:
  - **What it is:** Dementia is a decline in memory and thinking that affects daily life. Alzheimer's disease is its most common cause.
  - **Signs:** Forgetting recent events, repeating questions, getting lost in familiar places, and mood changes.
  - **Care:** There is no cure yet, but early diagnosis, medicines, routines and family support can help.
- Brain buddy ring in Neuron Purple.

### Builder C

**Slide 7 — Parkinson's Disease** (theme Zesty Lime; hero left, 3 cards in a zigzag constellation right)
- Eyebrow pill: `MOVEMENT DISORDER`
- Title: `Parkinson's Disease`
- Hero (100, 270), 520 × 520: an older adult doing tai chi with a friendly physiotherapist.
- Fun-fact bubble (Sunny Yellow) under the hero:
  > Exercise like walking, dancing or tai chi can help with balance and movement.
- Three neuron cards, zigzag (x 700 / 820 / 700), joined by diagonal wires:
  - **What it is:** A condition in which brain cells that make dopamine slowly stop working, affecting movement.
  - **Signs:** Shaking (tremor) at rest, slow movement, stiff muscles and balance problems.
  - **Care:** Medicines, physiotherapy and regular exercise help manage the symptoms.
- Brain buddy ring in Zesty Lime.

**Slide 8 — Brain-Healthy Habits** (3 tiles left, hero center, 3 tiles right)
- Title, centered: `Brain-Healthy Habits`
- Hero center (700, 260), 520 × 560: a big happy brain buddy lifting tiny dumbbells, with signal sparks around it.
- Pill under the hero (Neuron Purple, White text):
  > Small habits, strong signals.
- Six tiles, each a different palette color (light tint fill + colored outline + icon node), each wired to the hero:
  - (Neuron Purple, moon icon) `Get enough sleep` — Adults need 7–9 hours a night.
  - (Spark Orange, running icon) `Exercise regularly` — Move at least 150 minutes a week.
  - (Zesty Lime, salad icon) `Eat a balanced diet` — Fruits, vegetables, whole grains and fish.
  - (Synapse Teal, book icon) `Keep learning` — Read, play music or learn a new skill.
  - (Pop Pink, chat icon) `Stay social` — Talk, laugh and spend time with others.
  - (Sunny Yellow, helmet icon) `Wear a helmet & seatbelt` — Protect your head from injury.

**Slide 9 — When to See a Doctor** (warning card left, hero right)
- Title: `When to See a Doctor`
- A white card with a 4 px Spark Orange border, head `Get medical help if you notice:`, and orange ! nodes joined by a vertical wire:
  - ! Sudden, severe headache — the worst you've ever had
  - ! Sudden weakness, numbness or trouble speaking
  - ! A first-ever seizure
  - ! Memory problems that get worse or affect daily life
  - ! A new tremor, numbness or tingling that doesn't go away
  - ! A head injury followed by vomiting, confusion or drowsiness
- Banner (Pop Pink, Ink text):
  > Signs of a stroke? Call emergency services now — don't wait.
- Hero (1300, 260), 520 × 560: a friendly doctor talking with a smiling patient.
- Disclaimer pill:
  > For education only — not a substitute for professional medical advice.

**Slide 10 — Thank You** (centered, hero along the bottom)
- Title: `Thank You!` in Luckiest Guy 140, Neuron Purple, on a Sunny Yellow spark burst.
- Subtitle:
  > Keep your brain happy and your signals strong.
- Three contact pills (Neuron Purple / Spark Orange / Synapse Teal), each with an icon:
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources:
  > Sources: World Health Organization (WHO), U.S. NIH (NINDS), Kementerian Kesehatan RI
- Hero along the bottom (~1300 × 450): diverse people and a waving brain buddy linked by glowing neuron lines, with sparks in every palette color.

## 4. Speaker notes

- Slide 1:
  > Welcome. Today we look at how the brain and nerves work, five common disorders, and simple habits that protect the brain.
- Slide 2:
  > The brain, spinal cord and nerves work together like a messaging network made of billions of neurons.
- Slides 3–9:
  > General information only. Verify with current WHO / NINDS / Kemenkes guidance before presenting.
- Slide 4 (add):
  > Never hold the person down or put anything in their mouth.
- Slide 5 (add):
  > Tell the audience their local emergency number (for example, 112 or 119 in Indonesia).
- Slide 10:
  > Thank the audience and invite questions.

## 5. Deck-specific QA

- [ ] 10 pages; consecutive slides use different layouts.
- [ ] Every slide shows the neuron network (wires + glowing nodes) linking its cards, plus signal sparks.
- [ ] Each disorder slide (3–7) uses its theme color, has What it is / Signs / Care, and has the brain buddy ring.
- [ ] Medical text matches §3 word for word, including the seizure first-aid steps and F.A.S.T.
- [ ] Only Luckiest Guy and Nunito (or Lilita One fallback); White text only on Neuron Purple.
- [ ] Background is light Lavender Mist; no dark / navy, no stock photos, no realistic brain anatomy, no logos.
- [ ] Nothing from the earlier decks' identities (chain links, shields, clouds, winding path, metro map, ECG line, water flow, blueprint).
- [ ] Transition is Circle wipe ("Sapuan lingkaran") on all pages, or Dissolve ("Larut") if it is missing.
