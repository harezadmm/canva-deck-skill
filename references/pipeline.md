# Shared rules and pipeline for every colorful Canva deck prompt

> Every deck prompt in this folder tells the main agent to **read this whole file first**.
> The main agent copies §A, §C, and the deck's own slides into each builder's brief.
> The user's own Chrome (Claude in Chrome) is already logged in to Canva **Premium**.

---

## A. Hard rules (all agents)

1. **Built from scratch; all assets come from Canva Elements.** This is a project rule.
   - Never click "Use this template" on the reference. Never copy its pages or elements.
   - The code skeleton may contain only **text** and **plain layout shapes**: background, cards, pills, circles, lines, and simple bars or grids.
   - **Everything visual comes from Canva Elements** (Elemen → Grafis / Stiker / Bentuk / Bingkai / Foto). That includes illustrations, characters, icons, frames, patterns, blobs, bursts, doodles, and sparkles.
   - Pro elements are allowed.
2. **No Canva AI.**
   - Not allowed: Magic Media, Dream Lab, Magic Design, Magic Write, Magic Edit/Grab/Expand, "Tanya Canva", "AI Canva", "Buat Animasi".
   - Skip any asset whose creator is "Canva AI Elements Lab".
3. **Nothing outward.**
   - No sharing, publishing, or downloading.
   - No changes to sharing, access, or account settings.
   - Never log in for the user.
4. **Stay in your lane.**
   - Builders edit only their own pages.
   - Only the main agent adds, deletes, or reorders pages.
   - Never click "Ubah semua".
5. **No copy/paste.** All agents share one clipboard. Insert every asset fresh from the Elements panel.
6. **Copy is exact.**
   - Text must match the deck's slide spec word for word.
   - Bracketed items like `[Your Name]` stay visible as placeholders.
7. **No real logos, brands, or trademarked characters.** No real people's names either, except those in quotes the spec attributes.
8. **Language.**
   - Deck content is in **English**.
   - The final report to the user is in **Indonesian**.

## B. Colorful brief (applies to every deck)

The client wants **colorful, illustration-rich, not-too-simple** slides.

### Richness checklist

Every slide must have **all** of these:

1. 1 hero illustration or scene, at least 480 px.
2. 3–6 supporting icons, characters, or small illustrations.
3. At least 2 decorative layers: blobs, pattern, doodles, sparkles, confetti, bursts.
4. Text inside cards, pills, badges, or bubbles — never a bare paragraph on its own.
5. **At least 4 palette colors clearly visible.**

### Layout and readability rules

- Never use the same layout on two consecutive slides.
- Keep text readable:
  - Contrast ≥ 4.5:1.
  - Body text ≥ 22 px.
  - No text on top of busy decoration.

### Design rules (from elite-powerpoint-designer)

- One idea per slide.
- Max 6 lines of body text per card.
- Max 4 font sizes per slide.
- Max 2 font families per deck.
- Max 3 animated elements per slide.
- One transition type for the whole deck.

## C. Pipeline (current since set9: one builder per deck)

### Skills (main agent, load first)

- `anthropic-skills:pptx`
- `elite-powerpoint-designer`
- `ppt-visual`
- `presentation-design`

### Phase 1: prompts (main agent + writer subagents)

- Follow `references/prompt-writer-brief.md`. One prompt file per reference template.
- Save the set in `%USERPROFILE%\Downloads\Canva-PPT-Prompts\setN-<themes>\` with a copy of this file.
- The main agent cross-checks the whole set before any skeleton is built: no shared concept, font pair or reference look; transitions spread out.

### Phase 2: skeleton .pptx (one subagent per deck, all in parallel)

1. Follow `references/skeleton-brief.md`. Adapt `scripts/table-tournament.py`.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU), so Canva imports it at 1920 × 1080.
   - Convert px to EMU with `px * 9525`. Font size in pt = spec px × 0.75.
2. For every slide, create:
   - the background (solid or 2-stop gradient);
   - all text, with exact copy, font names, sizes, colors, and letter spacing;
   - the plain layout shapes (cards, pills, chips, bars, grids).
3. For every visual, place a **labeled placeholder rectangle** at its exact position, 20 % transparent, labeled `HERO: … 600w`, `ICON: …` or `DECOR: …`.
4. Add the speaker notes from the deck spec.
5. Save as `<set folder>\skeletons\<deck-slug>-skeleton.pptx`. The main agent validates: 10 slides, 18288000 × 10287000 EMU.

### Phase 3: build in Canva (one builder subagent owns one whole deck)

- Each builder follows `references/builder-brief.md`: import the skeleton, style lock, replace every placeholder with Canva Elements on all 10 pages, apply the transition, read-design check, report.
- There is **no separate asset scout**: the builder picks the style lock itself.
- Run **at most 4 builders at once** in one Chrome (6 worked once, but Chrome slows down and the account hits its usage limit sooner). Start the next deck when one finishes.
- Task message per builder: absolute path of the deck prompt, absolute path of the skeleton, deck title, transition (and its fallback).
- **Progress:** use the Canva connector `search-designs` (sort `modified_descending`, compare `updated_at`) and `ListAgents`. Do not read agent output files through the shell.
- **Usage limit (HTTP 429):** wait for the reset time, then resume each stopped builder with `SendMessage`. Never spawn a duplicate builder for a deck that already exists.

### Phase 4: main agent QA and report

**QA, common to every deck** (run with `presentation-design`, plus the deck's own checklist):

- [ ] 10 pages in order; every placeholder deleted (`read-design`: no `HERO:`, `ICON:`, `DECOR:`).
- [ ] §B richness checklist and colorful check pass on every slide.
- [ ] Consistent illustration and icon sets (style lock in page-1 notes).
- [ ] Every visual comes from Canva Elements; no Canva AI assets.
- [ ] Only the deck's 2 font families; body text ≥ 22 px; contrast ≥ 4.5:1.
- [ ] Copy matches the spec word for word.
- [ ] No overlap, clipping, or stray elements.
- [ ] Nothing shared, downloaded, or published.

**Final report to the user** (in Indonesian, short):

1. Every deck's edit link and its transition.
2. Known gaps per deck (from the builder reports, honestly).
3. The placeholders the user or client must fill in (`[Your Name] · [Organization]`, contact lines).
4. Scratch designs or leftover tabs the user should clean up by hand (agents never delete designs).
5. Confirmation that nothing was shared, downloaded or published.

## D. Lessons learned from earlier runs (all agents)

### Running several decks at once
- Run at most **3–4 Canva agents at the same time** in one Chrome. With 7 or more tabs open, Chrome stalls.
- Each agent opens and keeps its **own tab**. Tab groups can reset when several agents share Chrome; if yours is gone, reopen your edit URL in a new tab.
- The Canva editor only renders in a **visible, foreground tab**. Bring your tab to the front before taking screenshots.
- If the Chrome extension disconnects (`list_connected_browsers` returns `[]`), retry once. If it is still down, stop and report `BLOCKED`. Never try to log in.
- Close your own tabs when you finish.

### Import
- `file_upload` only accepts files from a folder the session can read. Save the skeleton in the scratchpad and upload it from there, not from `%TEMP%`.
- Canva shows imported text sizes at **spec × 0.75**: body 26 appears as 19.5, and title 140 appears as 105. That is correct. Do not "fix" it.

### Canva UI tips (Indonesian UI)
- **Gaya** sits next to **Posisi** in the toolbar.
- In the Posisi fields, press Ctrl+A, then type the value.
- **To set a hex color:** color swatch → the rainbow **"+"** → type the hex in the field. Clicking a hex search result does not apply the color.
- **Do not use Ctrl+B on Semibold text.** It switches the weight off. Use the font panel's **Cetak Tebal** instead.
- Transition names:
  - Larut = Dissolve
  - Meluncur = Slide
  - Some transitions, such as Pop or Geser, may be missing. Use the deck's fallback.
- **"Terapkan ke semua halaman"** for a transition is allowed. It is not "Ubah semua".
- Never apply an animation to a whole page by mistake. If you do, remove it with **Hapus semua animasi** on that page only.

### Style lock
- The builder picks **one illustration creator or set** and **one icon set**, and writes them into the page-1 speaker notes as the **style lock**, for example:
  - illustrations: creator X
  - icons: "<topic> icon bold outline"
- The builder searches with that style lock first. Use another creator only when the lock has nothing that fits, and report each exception.

### QA traps
- `read-design` thumbnails are often **stale**. The live editor is the truth; confirm any problem there before fixing or reporting it.
- **Placeholder sweep:** before reporting done, run `read-design` (design_content) and search for `HERO:`, `ICON:`, `DECOR:` and lone `ICON` text. Any hit means a placeholder is still on the page. Delete it or replace it.
- Also check for **empty icon circles or empty frames**, which are shapes that were meant to hold an icon.
- A line break inside a title can read as a missing space in `read-design` ("Thanks forPlaying!"). Check in the editor before editing.
- Name any scratch design the asset scout creates `ZZ scratch – <deck-slug>` so the user can find it and delete it themselves. Agents never delete designs.

### Fonts that survive pptx import into this Canva account
- **Use only these:** Alfa Slab One, Shrikhand, Lilita One, Press Start 2P, Poppins, Nunito (SemiBold / ExtraBold), Rubik, Chewy, Quicksand, Luckiest Guy, Archivo Black, DM Sans, Fredoka.
- **Missing, do not use:** Boogaloo, Pixelify Sans, Outfit, Lexend. They fall back to Arimo, Cinema Outfit or Lexend Mega.

### Deck length
- The user wants **10 slides** per deck for speed.
- Prompt files split the slides into Builder A (1–3), B (4–6) and C (7–10) sections for readability. One builder builds all three sections.

### More lessons (set9)
- **Never type on the canvas.** Typing triggers shortcuts and creates stray shapes (for example "L" draws a line). Click the Elements search box first.
- Canva allows at most **5 3D elements per page**. Over that, the page stops saving. Use flat items for the rest.
- On Windows, keep paths short (under 260 characters). Upload skeletons from a short folder such as Downloads.
- Run the skeleton scripts with plain `python` (not `python -I`, which hides the user site-packages where lxml lives).
