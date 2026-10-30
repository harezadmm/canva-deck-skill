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

## C. Pipeline (target 40–50 min)

### Skills (main agent, load first)

- `anthropic-skills:pptx`
- `elite-powerpoint-designer`
- `ppt-visual`
- `presentation-design`

### Phase 0A — main agent: build the skeleton .pptx (~5 min)

1. Use python-pptx.
   - Slide size: **20 in × 11.25 in** (18288000 × 10287000 EMU), so Canva imports it at 1920 × 1080.
   - Convert px to EMU with `px * 9525`.
2. For every slide, create:
   - the background (solid or 2-stop gradient);
   - all text, with exact copy, font names, sizes, colors, and letter spacing;
   - the plain layout shapes.
3. For every visual, place a **labeled placeholder rectangle** at its exact position.
   - Fill: 20 % transparent.
   - Label format: `HERO: … 600w`, `ICON: …`, `DECOR: …`.
4. Add the speaker notes from the deck spec.
5. Save the file as `<deck-slug>-skeleton.pptx`.
6. If LibreOffice is available, render one slide to PNG as a sanity check.

### Phase 0B — asset scout subagent, in parallel with 0A (~10–12 min)

1. Search Canva Elements for every visual in the deck spec.
2. Pick **one consistent illustration set** for heroes and characters, and **one icon set**.
3. Write `<deck-slug>-assets.md` with these columns:

   | Slide | Item | Exact keyword | Creator | Result (row, col) | Pro/free |

4. Insert nothing into the design.

### Phase 0C — main agent: import (~3 min)

1. Upload the skeleton with the `file_upload` tool (Buat desain → Impor file, or the Unggahan panel).
   - If that fails, ask the user to drag the file into Canva once.
2. Rename the design to the deck title.
3. Spot-check 2–3 slides:
   - Fonts mapped correctly. Re-set any substituted font on the affected text boxes.
   - Gradients, radii, and transparency survived.
4. **Fallback:** if the import is badly broken, build one representative slide by hand as a "kit page", duplicate it, and let builders swap content. Report which path you used.
5. Put the edit URL into each builder brief.

### Phase 1 — 4 builder subagents in parallel (~20–25 min)

| Builder | Slides |
|---|---|
| A | 1–3 |
| B | 4–6 |
| C | 7–9 |
| D | 10–12 |

**Builder brief** (give each builder §A, §B, the deck's design system, its own slides, and the asset sheet):

> Open your **own** Chrome tab with `<EDIT URL>`. Edit only slides `<X–Y>`.
>
> For each slide:
> 1. Place the decor first: background blobs/patterns, title highlight, doodles, footer.
> 2. Then place the hero, characters, and icons, using the exact keyword and result from the asset sheet.
> 3. Lock the aspect ratio. Match each placeholder's size and position via Posisi (Lebar / Tinggi / X / Y). Delete the placeholders.
> 4. Recolor decor to the palette where Canva allows it.
> 5. Run the §B richness checklist and the colorful check. Add fitting Canva elements if anything is missing.
> 6. Fix only real problems: overlap, clipping, unreadable text.
> 7. Take a zoom screenshot of the slide.
>
> The Canva UI is in Indonesian. Never use Tanya Canva, AI Canva, Bagikan, Unduh, or "Ubah semua". Never copy/paste. If your tab's screenshots time out twice, stop and report "BLOCKED".
>
> **Report:** per slide (done / issues / richness result), and the assets used (keyword + creator + Pro/free).

### Phase 2 — main agent: QA and report (~5 min)

**QA, common to every deck** (run with `presentation-design`, plus the deck's own checklist):

- [ ] 12 pages in order; every placeholder deleted.
- [ ] §B richness checklist and colorful check pass on every slide.
- [ ] Consistent illustration and icon sets.
- [ ] Every visual comes from Canva Elements; no Canva AI assets.
- [ ] Only the deck's 2 font families (or their fallbacks); body text ≥ 22 px; contrast ≥ 4.5:1.
- [ ] Copy matches the spec word for word.
- [ ] No overlap, clipping, or stray elements. Check each page's Lapisan list once.
- [ ] Nothing shared, downloaded, or published.

**Final report to the user** (in Indonesian):

1. The edit link.
2. One line per slide.
3. Assets per slide: keyword + creator + Pro/free.
4. What was deliberately done differently from the reference.
5. Which path was used, the time per phase, and anything not achieved.
6. A list of the placeholders the user or client must fill in.
