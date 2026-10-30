# Prompt 5/5 — "New Year 2027: Goals & Fresh Starts" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\scratch-workspaces\dcdc6f97-14f9-43a0-812f-7b344eef061a\12aa8b61-941b-457d-8505-99fb0b2a7c89\scratch-2026-10-22-82e737\canva-shared-pipeline.md`.

That file holds the hard rules (§A), the colorful brief (§B), and the pipeline, builder brief, QA and report (§C).

Deck slug: `new-year-goals`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"Happy New Year 2027 – Goals & Fresh Starts"**.

It is an upbeat New Year goal-setting workshop deck: reflect on 2026, then plan 2027.

**Reference (direction only):** https://www.canva.com/templates/EAG2mCV_j3Y/ ("Blue and Yellow Textured Happy New Year").

- **Borrow the idea:**
  - flat festive illustrations (stars, fireworks, confetti, streamers)
  - bold chunky titles
  - split layouts with a big illustration on one side
  - a celebratory tone
- **Build from scratch.**
- **Must also differ** from the earlier "New Year's Eve 2027 – Party Deck" prompt (navy + champagne art deco, party run-sheet).

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Flat festive illustrations | **Confetti-sunrise palette**: hot pink, electric violet, turquoise, sunshine and tangerine on a soft lilac-cream background. **Not** navy + mustard. |
| Bold titles | Rounded retro titles (Righteous) with a colored drop shadow, **not** slab serif |
| Split layouts | Layouts use **Memphis / confetti shapes** and rounded colored panels. **No** navy/yellow half-and-half split panels |
| Celebration tone | Heroes are **people setting goals** (writing lists, climbing steps, planting seeds, vision boards). **No** clock at 12, **no** "January 1" calendar hero, **no** title on a box stage, **no** bottles or disco balls |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Lilac Cream | `#F6F1FF` | Background |
| Ink Plum | `#2B1B4A` | Text |
| Hot Pink | `#FF3E8A` | Accent |
| Electric Violet | `#7B2FF7` | Titles |
| Turquoise | `#14C8C2` | Accent |
| Sunshine | `#FFC93C` | Highlights, stars |
| Tangerine | `#FF7F3F` | Accent |
| White | `#FFFFFF` | Cards |

**Color rules**
- Every slide has **confetti and streamer clusters** (Canva) in all 5 accent colors at two corners.
- Card fills rotate through the 18 % tints of the accent colors.
- Slide 1, slide 7 and slide 12 use a **multi-color gradient** background (Violet → Pink → Tangerine) for impact.

### Fonts

- **Titles:** Righteous (fallback: Lilita One), 76–90, Electric Violet. Add a Hot Pink drop shadow (Canva Efek → Bayangan, offset 6, 0 % blur).
- **Body:** Poppins (fallback: Nunito), 26–28, Ink Plum.
- **Eyebrow:** Poppins Bold 22, UPPERCASE, letter spacing 200, Turquoise.

### Recurring motifs

1. **"2027" mini-badge** on every slide: a Sunshine starburst (Canva) with "2027" in Righteous 28.
2. **Rounded panels:** radius 32, white or tinted, with a 3 px colored outline.
3. **Number stickers:** colored circles, 80 px.
4. **Confetti and streamers** in corners, plus sparkles.
5. **Footer:** a wavy multi-color line and the page number.

**Transition:** Push.

### Illustration style

One flat, vibrant set of diverse people doing goal-related actions: writing in a planner, climbing stairs to a flag, watering a plant, high-fiving, making a vision board, running, reading. Use a consistent style throughout.

## 3. Slide-by-slide spec

### Builder A

**Slide 1 — Cover (gradient background)**
- Eyebrow, White: `NEW YEAR WORKSHOP`.
- Title, White, Pink shadow, Righteous 130, 2 lines:
  > Happy New Year
  > 2027!
- Subtitle, White:
  > Goals, habits and fresh starts.
- Pill, Sunshine, Ink text: `Hosted by [Your Name]`.
- Hero (~820), right: a group of people cheering with confetti, and a big "2027" built from stars and streamers (no balloon numerals).
- Decor: confetti and fireworks in 5 colors.

**Slide 2 — Welcome**
- Title: `Welcome to a Fresh Start`.
- Left panel (White):
  > A new year is a blank page. Today we'll look back with kindness, then plan forward with purpose.
- Right: hero (~600) of a person opening a door into a bright, colorful landscape.
- Three small stickers below:
  - `Reflect`
  - `Plan`
  - `Act`

**Slide 3 — Looking Back at 2026**
- Title: `Looking Back at 2026`.
- Three tinted panels in a row (Pink / Turquoise / Sunshine), each with an icon and a prompt:
  - `Wins` — What am I proud of this year?
  - `Lessons` — What did I learn the hard way?
  - `Gratitude` — Who or what am I thankful for?
- Each panel has 3 empty lines for writing.
- Hero (~360): a person looking at a photo album.

### Builder B

**Slide 4 — My Word of the Year**
- Title: `Pick Your Word of the Year`.
- Center: a big Sunshine starburst with the placeholder `[YOUR WORD]` in Righteous 96.
- Around it, 8 example word stickers in different colors:
  - `Grow`
  - `Balance`
  - `Brave`
  - `Focus`
  - `Joy`
  - `Health`
  - `Create`
  - `Connect`
- Hero (~320): a person holding up a sign.

**Slide 5 — Six Areas of Life**
- Title: `Six Areas of Life`.
- A colorful **life wheel** built from 6 pie-slice shapes (plain shapes), each slice a different accent color, with an icon and a label:
  - `Health`
  - `Career / Study`
  - `Money`
  - `Relationships`
  - `Growth`
  - `Fun`
- Side panel:
  > Rate each area from 1 to 10. Where do you want the biggest change?
- Hero (~300): a person balancing on a beam.

**Slide 6 — Set SMART Goals**
- Title: `Set SMART Goals`.
- Five tall colored cards, one per letter (S / M / A / R / T), each with a big letter (Righteous 96), a word and a line:

| Letter | Word | Line |
|---|---|---|
| S | Specific | Clear and well defined. |
| M | Measurable | You can track progress. |
| A | Achievable | Realistic for you. |
| R | Relevant | Matters to your bigger life. |
| T | Time-bound | Has a deadline. |

- Bottom example strip:
  > Example: "Read 12 books by December 2027 — one each month."

### Builder C

**Slide 7 — Vision Board (gradient background)**
- Title, White: `Build Your Vision Board`.
- A collage of 6 colorful frames (Canva frames), tilted, each with an illustration placeholder:
  - travel
  - fitness
  - learning
  - home
  - friends
  - career
- Washi tape and stickers on the frames.
- Tip panel:
  > Use pictures and words that make you feel excited, then place it where you'll see it every day.

**Slide 8 — Small Habits, Big Results**
- Title: `Small Habits, Big Results`.
- Hero (~520): a person climbing colorful stairs toward a flag.
- Each step is labeled with a habit:
  - `Drink water`
  - `Move 20 minutes`
  - `Read 10 pages`
  - `Save a little`
  - `Sleep on time`
- Side panel:
  > Tip: stack a new habit onto one you already do — like reading right after breakfast.

**Slide 9 — My 2027 Roadmap**
- Title: `My 2027 Roadmap`.
- A 4 × 3 grid of 12 month cards (`JAN` … `DEC`). Each card is a different tint (cycling the accents), with the month in Righteous 32 and one empty line.
- Four quarter badges above the columns:
  - `Q1 Start`
  - `Q2 Build`
  - `Q3 Grow`
  - `Q4 Celebrate`
- Small doodles: a rocket, a seedling, a trophy.

### Builder D

**Slide 10 — Stay on Track**
- Title: `Stay on Track`.
- Four panels, each with an icon and a sticker number:
  1. `Write it down` — Goals on paper are easier to remember.
  2. `Find a buddy` — Share goals and check in monthly.
  3. `Track progress` — Use a habit tracker or calendar.
  4. `Celebrate wins` — Reward small steps along the way.
- Hero (~380): two friends high-fiving.

**Slide 11 — Words to Carry Forward**
- A centered quote on a big White panel with a Turquoise outline:
  > "The secret of getting ahead is getting started."
- Attribution, Pink: `— ATTRIBUTED TO MARK TWAIN`.
- Decor: fireworks and confetti in all colors around the panel; a person running toward a sunrise (~420).

**Slide 12 — Happy New Year! (gradient background)**
- Title, White, Pink shadow, Righteous 140:
  > Cheers to 2027!
- Subtitle, White:
  > Your fresh start begins now.
- Three contact pills (White / Sunshine / Turquoise):
  - `[email]`
  - `@yourhandle`
  - `www.yourwebsite.com`
- Hero along the bottom (~1300 wide): diverse people celebrating with confetti, streamers and fireworks.

## 4. Speaker notes

- **Slide 11:** `This quote is widely attributed to Mark Twain, but the attribution is uncertain.`

## 5. Deck-specific QA

- [ ] Writing prompts (slides 3, 4, 9) have clear empty space.
- [ ] The SMART letters are correct.
- [ ] Nothing from the reference: no navy/mustard split, no clock 12, no Jan 1 calendar, no box-stage title, no bottles or disco balls.
- [ ] Nothing from the earlier art-deco party deck.
