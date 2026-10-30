# Skeleton brief (one subagent per deck)

You turn one deck prompt into a `.pptx` skeleton that Canva imports at 1920 × 1080. Builders later swap every placeholder for real Canva Elements, so the skeleton holds **only text, plain shapes and labeled placeholders**.

Your task message gives you the deck prompt path and the set folder.

## Steps
1. Read the deck prompt (§2 design system, §3 slides, §4 notes) and `references/pipeline.md` §C Phase 2 and §D (font whitelist).
2. Copy `scripts/table-tournament.py` to `<set folder>\skeletons\<deck-slug>.py`. It is self-contained: units (`px`, `fpt`), shapes (`rrect`, `circle`, `rect`), `text` with a fit lint, `ph` placeholders, `notes`, `tilt`. `idea-to-plan.py` is a second example (business style).
3. Keep the helpers. Replace the colors, fonts, `SLUG`, and the 10 slide blocks with your deck's spec:
   - backgrounds, every text word for word (exact font, size in px, color, letter spacing);
   - cards, pills, chips, bars, grids, step circles;
   - one `ph(...)` per visual with a clear label: `HERO: <scene description> <width>w`, `ICON: <what>`, `DECOR: <what>`, at the exact position and size;
   - speaker notes from §4.
4. Run it with plain `python <deck-slug>.py` (not `python -I`). It saves `<deck-slug>-skeleton.pptx` next to the script and prints the placeholder list and a LINT list.
5. Fix every LINT warning (text overflowing its box, overlaps) by adjusting boxes, never by changing the spec text. Run again until LINT is clean.
6. Check: `len(prs.slides) == 10`, slide size 18288000 × 10287000 EMU.

## Rules
- Fonts: only the deck's 2 families, both on the whitelist.
- No images, no icons drawn from many shapes, no clip art. Visuals come later from Canva Elements.
- On Windows keep the full path under 260 characters.

## Report (short)
Skeleton path, placeholder count, LINT status, anything in the spec you had to bend.
