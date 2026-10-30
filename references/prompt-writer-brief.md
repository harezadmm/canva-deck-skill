# Prompt-writer brief (one writer subagent per theme group)

You write **deck prompt files**. Each prompt is the full spec for one colorful 10-slide Canva deck, built later by the skeleton script and one builder agent.

Your task message gives you:
- the set folder, for example `%USERPROFILE%\Downloads\Canva-PPT-Prompts\set10-<themes>\`
- your theme and its reference template URLs (one prompt per URL)
- the prompt numbers to use, for example `set10-4` to `set10-6`

## Read first
1. `references/pipeline.md`: all of it (§A hard rules, §B richness, §D lessons, **font whitelist**).
2. `references/examples/`: three finished prompts. Match their structure, depth and tone **exactly**. They are the quality bar.
3. Earlier decks on the same theme, in the skill's `references/history/` and in `%USERPROFILE%\Downloads\Canva-PPT-Prompts\` (grep the theme word, for example `game night`, `new year`, `business plan`). Your deck must differ from all of them.

## Reference templates
- Open the reference URL to read its title and look. If the browser cannot reach it, use the title words in the URL and say so in your report. Never retry through another tool or route.
- References are for **direction only**: mood, palette family, kind of content. Never copy a layout, illustration or text.

## One prompt file per reference
File name: `prompt-<setN>-<n>-<theme>-<slug>.md`, saved in the set folder.

Sections (same order as the examples):

| Section | Content |
|---|---|
| Header | Deck title, `FIRST: read …canva-shared-pipeline.md` with the **absolute path** of the set folder's copy, deck slug |
| §0 Goal | What the deck is for, the 10-slide flow, the reference URL with "borrow the idea" (4 points) and "build from scratch" |
| Must also differ from | Earlier same-theme decks by file name, plus the other decks of this set |
| §1 Borrow vs. must differ | Table. A named concept (for example "Scrapbook Tournament"), what is new in backgrounds, heroes, titles, structure, decor, and an explicit **No** list |
| §2 Design system | Color token table (8–10 colors, hex, use), background rotation (no two consecutive slides alike), color rules with contrast, font table, recurring motifs (5–6), transition + fallback, illustration style, **asset search terms** (Canva Elements keywords, English) |
| §3 Slide-by-slide spec | Builder A (1–3), B (4–6), C (7–10). Per slide: layout name and background, every text **word for word** in backticks or quotes, positions and sizes in px for titles and heroes, the hero described as a scene with ~width, supporting icons, decor, footer |
| §4 Speaker notes | One short note per slide |
| §5 Deck-specific QA | Checklist on top of the shared QA |

## Content rules
- **10 slides.** Slide 1 cover, slide 10 thank-you with the contact pills `123-456-7890`, `hello@yourwebsite.com`, `www.yourwebsite.com`. Cover shows `[Your Name] · [Organization]`.
- Real, useful content: real rules for games, real steps for plans, real numbers in a worked example. No lorem ipsum.
- English. Max 6 lines of body text per card. Body ≥ 26 px spec (shows as 19.5 after import, which is correct).
- Every slide passes §B: 1 hero ≥ 480 px, 3–6 supporting items, ≥ 2 decor layers, ≥ 4 palette colors visible, no bare paragraph.
- Never the same layout on two consecutive slides.
- **Fonts:** exactly 2 families, both from the §D whitelist. Never Boogaloo, Pixelify Sans, Outfit or Lexend.
- No real brands, logos, trademarked games or characters, real people.

## Set-level uniqueness (the main agent checks this after all writers finish)
- No two decks in the set share a concept or hero idea (for example two board-game tournaments).
- No two decks share the same font pair. Do not reuse a title font more than twice in a set.
- Transitions are spread out. Names in the Canva UI: Larut, Meluncur, Tumpuk, Usap Warna, Usap Garis, Usap Lingkaran. Give each deck a fallback.

## Report (short)
Per prompt: file path, deck title, concept in one line, font pair, transition, and anything you could not check (for example a reference you could not open).
