---
name: canva-deck
description: End-to-end factory for colorful, illustration-rich 10-slide Canva presentations built from scratch with Canva Elements. It covers writing deck prompts from Canva template references, generating python-pptx skeletons, and having one builder subagent per deck build it in Canva through Claude in Chrome, then reporting the links. Use this skill whenever the user pastes Canva template URLs and asks for prompts ("buatkan prompt", "promt ppt", "REFF"), asks to build or continue Canva decks ("kerjakan semua deck", "bangun ppt di canva", "/goal … multiple subagent"), or asks for deck progress or links ("sudah jadi semua?", "link nya mana"). Use it even when the user does not say "skill" or "Canva", as long as the topic is these presentation decks.
---

# Canva deck factory

You make **colorful, illustration-rich, not-too-simple** 10-slide Canva presentations for the user's clients. The user is a Canva Premium designer who sells these decks, so visual richness is the product. Deck content is in English. The user writes short Indonesian; answer in short Indonesian.

All paths below are relative to this skill's base directory (shown when the skill loads). Subagents do not see this skill, so always give them **absolute paths**.

## Files

| Path | Read when |
|---|---|
| `references/pipeline.md` | **Always, before any deck work.** §A hard rules, §B richness checklist, §C pipeline, §D lessons and the font whitelist |
| `references/prompt-writer-brief.md` | Phase 1, handed to each prompt-writer subagent |
| `references/skeleton-brief.md` | Phase 2, handed to each skeleton subagent |
| `references/builder-brief.md` | Phase 3, handed to each builder subagent |
| `references/examples/` | Three finished prompts (new year, business plan, game night). They are the quality bar |
| `references/history/` | Every earlier prompt (sets 5–9). New decks must not repeat their concepts |
| `scripts/table-tournament.py`, `scripts/idea-to-plan.py` | Working skeleton generators to adapt |
| `references/setup-id.md` | Indonesian setup guide; point the user to it when a tool below is missing |

**Work folder:** new sets go in `%USERPROFILE%\Downloads\Canva-PPT-Prompts\setN-<themes>\`.
- Find N by taking the highest set number in that folder and in `references/history/`, plus 1. The last set built with this skill's history was set9.
- Copy `references/pipeline.md` into each new set folder as `canva-shared-pipeline.md`. Each set then carries its own rules, and the prompts point at that copy.

## Before starting

Check that these tools exist:
- **Claude in Chrome** (`mcp__claude-in-chrome__*`), with the user already logged in to Canva Premium in that Chrome;
- the **Canva connector** (`search-designs`, `read-design`);
- Python with `python-pptx`, `lxml` and `Pillow`.

If one is missing, say so in one line, point to `references/setup-id.md`, and stop before that phase. Never log in for the user.

## Phase 1: prompts ("buatkan prompt … + URLs")

1. Create the set folder and copy the pipeline into it.
2. Group the reference URLs by theme. Run **one writer subagent per theme group, in parallel**, with `references/prompt-writer-brief.md`. Tell each writer:
   - its URLs;
   - its prompt numbers;
   - the set folder;
   - the other decks in the set, so the writers do not collide.
3. When all writers are done, check the whole set yourself:
   - No two decks share a concept or hero idea.
   - No two decks share a font pair, and no title font is used more than twice.
   - Transitions are spread out.
   - All fonts are on the whitelist.
   - Send fixes back to the writer with SendMessage.

   Overlaps happen often: in set9, two decks were both board-game tournaments, and one title font appeared three times.
4. Report each deck in one line: title, concept, font pair and transition.

## Phase 2: skeletons

1. Run **one skeleton subagent per deck, all in parallel**, with `references/skeleton-brief.md`.
2. Validate every `.pptx` yourself with python-pptx: 10 slides, 18288000 × 10287000 EMU.

## Phase 3: build in Canva ("kerjakan semua", "/goal …")

- Run **one builder subagent per whole deck** with `references/builder-brief.md`. Splitting one deck across agents was slower, because Canva syncs the active page across tabs and the agents collided.
- Run at most **4 builders at once**. Six worked once but strained Chrome and hit the usage limit. When one finishes, start the next deck.
- Each builder's task message holds:
  - absolute paths to the deck prompt, the skeleton, `references/builder-brief.md` and the set's `canva-shared-pipeline.md`;
  - the deck title;
  - the transition and its fallback.
- **Progress:** use `search-designs` (sort `modified_descending`, compare `updated_at` to the current UTC time) and `ListAgents`. Do not read agent output files through the shell.
- **Placeholder sweep:** use `read-design` with `design_content`. Any remaining `HERO:`, `ICON:` or `DECOR:` text means the deck is not finished.
- **Usage limit (HTTP 429):** wait for the reset, then resume each stopped builder with SendMessage. Never spawn a second builder for a deck that already exists in Canva; that creates duplicate designs.
- A deck takes about 1.5–2.5 h. When the user asks "sudah jadi?", answer with the finished links and what is still running.

## Final report (Indonesian, short)

1. Every deck's edit link and its transition.
2. Honest gaps per deck, taken from the builder reports. The user prefers knowing to being surprised.
3. Placeholders to fill: `[Your Name] · [Organization]` on the cover, and the contact lines on slide 10.
4. Scratch designs or leftover tabs to clean up by hand. Agents never delete designs.
5. Confirmation that nothing was shared, downloaded or published.

## Hard rules (full list in pipeline §A)

These protect the user's client work and Canva account:
- **Build from scratch.** Every visual comes from **Canva Elements**; Pro elements are OK. References are for direction only: never "Use this template", never copy a layout.
- **No Canva AI:** no Magic Media, Dream Lab, Magic Design or Write, or Tanya Canva. Skip assets made by "Canva AI Elements Lab".
- **Nothing outward:** never Bagikan/Share, Unduh/Download or Publish. Never change access, never log in, never delete designs.
- **Never click "Ubah semua"**, which restyles every page at once. No copy/paste, because agents share one clipboard.
- **Spec text is word for word.** Bracket placeholders stay as they are.
- **Fonts only from the whitelist** in pipeline §D. Missing fonts fall back silently on import, and Canva has no safe global font swap.
- No real logos, brands, trademarked characters or real people.

## Speed vs. quality

The user's target is **10 decks per day without any drop in richness**. Speed up the process, never the output:
- no thinner pages;
- no decor moved into the skeleton;
- no cheaper builder models.

Parallelize every independent piece. Builders batch Chrome steps with `browser_batch` and use scaled screenshots while working.
