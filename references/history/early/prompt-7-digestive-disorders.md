# Prompt 7 — "Digestive System Disorders" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of:

`%USERPROFILE%\Downloads\Canva-PPT-Prompts\canva-shared-pipeline.md`

That file holds:
- §A — hard rules
- §B — the colorful brief and richness checklist
- §C — the pipeline, builder brief, QA and report

Deck slug: `digestive-disorders`.

---

## 0. Goal

Build a 12-slide Canva presentation, 1920 × 1080, called **"Digestive System Disorders"**. It is an educational health deck for students and the general public.

**Reference (direction only):** https://www.canva.com/templates/EAG84X119Rk/ ("Blue and White Modern Medical Epidemiology").

- **Borrow the idea:**
  - white rounded title pills
  - a numbered list slide
  - big rounded frames for visuals
  - a professional medical structure
- **Build from scratch.**

**Not a repeat:** this deck must look different from the earlier disease decks in this project.

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Rounded title pills | Pills are **colorful**, one per section. The background is a **warm peach cream**, not a blue-teal gradient. |
| Numbered list | Numbers sit on **fruit- and veggie-shaped badges** (apple, pear, carrot, lemon). |
| Rounded frames for visuals | Frames hold **flat illustrations** of cute organ characters and food, **not** stock photos of doctors. |
| Professional structure | A **"Food's Journey" concept**: a winding colorful path shows the route from mouth to intestines, and it appears on the section slides. |
| — | **No** white circles bleeding off the edges, **no** company logo, **no** stethoscope hero. |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Peach Cream | `#FFF3E8` | Background |
| Cocoa Ink | `#2E1F2A` | Text |
| Tangerine | `#FF8A3D` | Titles, accent |
| Raspberry | `#E23E6B` | Warnings, symptoms |
| Leaf | `#4CAF50` | Healthy gut, prevention |
| Banana | `#FFD045` | Highlights |
| Plum | `#7B4FB8` | Accent |
| Aqua | `#2EC5CE` | Water, hydration accent |

**Color rules:**
- Each disorder slide has its own theme color (title pill, cards, organ buddy):

  | Disorder | Theme color |
  |---|---|
  | GERD | Tangerine |
  | Gastritis & Peptic Ulcer | Raspberry |
  | Gastroenteritis | Aqua |
  | Constipation | Leaf |
  | IBS | Plum |

- Every slide has fruit and veggie doodles (Canva) in 3+ colors, plus soft blobs.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Lilita One | Baloo 2 ExtraBold | 70–84 | Cocoa Ink, inside a colored rounded pill |
| Body | Nunito | — | 26–28 | Cocoa Ink |
| Eyebrow | Nunito ExtraBold | — | 22 | Uppercase, letter spacing 200, theme color |

### Recurring motifs

1. **Section title pill:** a colored rounded pill behind each title (theme color, 25 % tint).
2. **Organ buddy:** a cute flat stomach / intestine / liver / esophagus character in a circle badge, placed at the top right.
3. **Food's Journey path:** a colorful dotted, winding path (Canva element).
4. **Fruit badges:** numbers sit on fruit-shaped badges.
5. **Footer:** a wavy line plus the page number.

**Transition:** Push.

### Illustration style

- One flat, cheerful set with cute digestive-organ characters, food, and diverse people eating and drinking.
- One icon set.
- No gross imagery: no vomit or stool depictions. Use symbolic icons only (a toilet icon is OK).

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover**
- Eyebrow: `GUT HEALTH EDUCATION`
- Title at (120, 240), width 940, 2 lines:
  > Digestive System Disorders
- Pill (Leaf):
  > Know your gut, care for your health.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~820, right): a happy stomach character surrounded by colorful fruit, vegetables and a water glass. A cheerful family eats a healthy meal nearby.
- Decor: fruit doodles, sparkles.

**Slide 2 — The Food's Journey**
- Title: `The Food's Journey`
- Center: a flat digestive-system diagram (~640 tall) with a colorful winding path along it.
- Six numbered fruit badges, each with a label and one line:
  1. `Mouth` — Chewing and saliva start breaking food down.
  2. `Esophagus` — A tube that pushes food to the stomach.
  3. `Stomach` — Acid and juices mix and break down food.
  4. `Small Intestine` — Absorbs most nutrients into the blood.
  5. `Large Intestine` — Absorbs water and forms stool.
  6. `Liver & Pancreas` — Make bile and enzymes that help digestion.

**Slide 3 — Common Digestive Disorders**
- Title: `Common Digestive Disorders`
- Five colorful cards in a row, each in its theme color, with an organ-buddy icon and a one-line description:
  - `GERD` — Stomach acid flows back up.
  - `Gastritis & Ulcers` — Irritated or sore stomach lining.
  - `Gastroenteritis` — Stomach and gut infection.
  - `Constipation` — Hard, infrequent stools.
  - `IBS` — A sensitive, irritable bowel.
- Hero: a curious kid looking at a big friendly stomach character (~360).

### Builder B

**Slide 4 — GERD (Acid Reflux)** — theme Tangerine
- Eyebrow `ACID REFLUX`. Title: `GERD (Acid Reflux)`.
- Three cards:
  - **What it is:** Stomach acid flows back into the esophagus.
  - **Signs:** Heartburn, a sour taste in the mouth, and discomfort that's worse after meals or when lying down.
  - **Helpful habits:** Eat smaller meals, avoid lying down 2–3 hours after eating, and limit trigger foods like fatty or spicy meals.
- Hero: a person sitting upright after dinner, with a cute esophagus/stomach buddy (~500).

**Slide 5 — Gastritis & Peptic Ulcer** — theme Raspberry
- Eyebrow `STOMACH LINING`. Title: `Gastritis & Peptic Ulcer`.
- Three cards:
  - **What it is:** Inflammation or sores in the lining of the stomach or upper small intestine.
  - **Common causes:** H. pylori bacteria, frequent use of painkillers like ibuprofen, and heavy alcohol use.
  - **Care:** See a doctor — treatment may include medicine to lower acid or to clear H. pylori.
- Hero: a stomach buddy holding an ice pack, with a doctor (~480).
- Speech bubble:
  > Black, tarry stools or vomiting blood need urgent care.

**Slide 6 — Gastroenteritis** — theme Aqua
- Eyebrow `INFECTION`. Title: `Gastroenteritis (Stomach Flu)`.
- Three cards:
  - **What it is:** An infection of the stomach and intestines caused by viruses, bacteria or parasites.
  - **Signs:** Diarrhea, nausea, vomiting, stomach cramps and sometimes fever.
  - **Care:** Drink oral rehydration solution (ORS), rest, and wash hands well to avoid spreading it.
- Hero: a person sipping from a water glass with an ORS sachet, and water-drop doodles (~480).

### Builder C

**Slide 7 — Constipation** — theme Leaf
- Eyebrow `BOWEL HABITS`. Title: `Constipation`.
- Three cards:
  - **What it is:** Passing stools less often, or stools that are hard and difficult to pass.
  - **Common causes:** Low fiber, not drinking enough water, and little physical activity.
  - **Helpful habits:** Eat more fiber (vegetables, fruit, whole grains), drink water, and stay active.
- Hero: a bowl of colorful fiber foods with a happy intestine buddy (~500).

**Slide 8 — Irritable Bowel Syndrome (IBS)** — theme Plum
- Eyebrow `SENSITIVE GUT`. Title: `Irritable Bowel Syndrome (IBS)`.
- Three cards:
  - **What it is:** A long-term condition where the gut is extra sensitive, without visible damage.
  - **Signs:** Belly pain, bloating, and diarrhea, constipation or both.
  - **Managing it:** Notice trigger foods, manage stress, eat regularly, and talk to a doctor about a plan.
- Hero: a person doing calm yoga or breathing next to a relaxed intestine buddy (~480).

**Slide 9 — Who Is at Risk?**
- Title: `What Raises the Risk?`
- Six colorful fruit-badge tiles in a 3 × 2 grid, each with an icon:
  - `Low-fiber diet`
  - `Not drinking enough water`
  - `Unsafe food & water`
  - `Smoking & heavy alcohol`
  - `Frequent painkiller use`
  - `Stress & irregular meals`
- Hero: a balance scale with a burger on one side and vegetables on the other (~340).

### Builder D

**Slide 10 — Habits for a Happy Gut**
- Title: `Habits for a Happy Gut`
- Hero: a big happy gut buddy giving a thumbs up (~460).
- Six numbered fruit badges with habits:
  1. Eat plenty of fiber
  2. Drink enough water
  3. Eat regular, smaller meals
  4. Wash hands & food well
  5. Stay active every day
  6. Limit alcohol and don't smoke

**Slide 11 — Warning Signs**
- Title: `When to See a Doctor`
- A Raspberry-border card with `!` bullets:
  - ! Severe or constant belly pain — especially in the lower right side
  - ! Blood in stool or black, tarry stools
  - ! Vomiting blood
  - ! Difficulty swallowing
  - ! Unexplained weight loss
  - ! Signs of dehydration
- Hero: a friendly doctor talking with a patient (~400).
- Disclaimer:
  > For education only — not a substitute for professional medical advice.

**Slide 12 — Thank You**
- Title: `Thank You!` — Lilita One 140, on a Banana burst.
- Subtitle:
  > A happy gut makes a happy you.
- Three contact pills (Tangerine / Leaf / Plum):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Sources:
  > World Health Organization (WHO), U.S. NIH (NIDDK), Kementerian Kesehatan RI
- Hero along the bottom (~1300): a picnic scene with people and cute organ buddies, plus fruit confetti.

## 4. Speaker notes

- **Slides 4–11:**
  > General information only. Verify with current WHO / NIDDK / Kemenkes guidance before presenting.
- **Slide 11:**
  > Severe lower-right belly pain can be appendicitis — seek emergency care.

## 5. Deck-specific QA

- [ ] Each disorder slide uses its own theme color and organ buddy.
- [ ] No gross imagery.
- [ ] Medical text matches §3 word for word.
- [ ] Not blue-teal; no doctor stock photos; no white edge circles.
- [ ] Nothing from the earlier disease decks' identities.
