# Builder brief: set9 (ONE builder owns ONE whole deck)

You are the **only** builder of one deck. Your task message gives you:
- the deck prompt file (full spec) and the deck title
- the skeleton .pptx to import (absolute path)
- the transition to apply

You will: import the skeleton into Canva, replace **every** placeholder on all 10 pages with real Canva Elements graphics, apply the transition, verify, and report. Quality bar: **bright, colorful, illustration-rich, exactly as rich as the earlier decks in this project. No shortcuts, no thinner pages.**

The skeleton already has, on every page: the exact spec text, plain layout shapes (cards, pills, chips, bars), and labeled placeholder boxes `HERO: …`, `ICON: …`, `DECOR: …`. Each placeholder shows the size and position its graphic must take.

## Read first
1. Your deck prompt: §1 (borrow vs must differ), §2 (design system, motifs, illustration style, asset search terms), §3 (your 10 slides), §5 (deck QA).
2. `%USERPROFILE%\Downloads\Canva-PPT-Prompts\set9-newyear-business-gamenight\canva-shared-pipeline.md`: §A hard rules, §B richness checklist, §D lessons.

## Parallel work
- Other builders are building OTHER decks in other tabs of the same Chrome at the same time. Use only your own tab(s) (`tabs_create_mcp`). Never close, navigate or reuse a tab you did not create.
- The editor only renders in the visible, foreground tab. Keep your tab active; a screenshot on your tabId usually fronts it.
- If the extension disconnects (`list_connected_browsers` returns `[]`), retry a few times. **BLOCKED** (report what is done and what is left) only if the editor stays stuck for more than 10 minutes or the extension stays down for more than about 5 minutes. Never sign in.
- Canva may sync the active page across tabs of the same design: use ONE tab for your design.

## Step 1: import the skeleton
1. Open `https://www.canva.com/` in your tab. Click **Buat desain** → **Unggah** / **Impor file** (or open the Unggahan panel) and upload the skeleton with the `file_upload` tool (find the file input with `find` / `read_page`). Wait for the conversion; click **Buka** on the toast to open the design.
2. Rename the design to the deck title (click the title at the top, Ctrl+A, type, Enter).
3. Confirm **10 pages** and spot-check fonts. Imported text shows at spec × 0.75 (for example 26 shows as 19.5). That is correct. If a font is substituted (fallback), report it; do not use "Ubah semua".
4. Import only **once**. If it fails twice, report BLOCKED. Never delete designs.

## Step 2: style lock (one illustration set per deck)
1. Search Elements with the deck §2 keywords. Pick **one illustration creator** whose flat, bright style fits and who has many items, and **one icon set**.
2. Use that creator for every hero and character, and the icon set for every icon. Use another creator only when the lock has nothing that fits; report every exception.
3. Write `STYLE LOCK: <creator>; icons: <keyword>` into the speaker notes of page 1 (append, keep the existing notes).
4. To browse a creator: select one of their items → "…" → Info → "Lihat karya <creator>". Skip items made by "Canva AI Elements Lab".

## Per page (all 10, in order; finish each page fully before the next)
1. Place the decor first: background layers, title highlight, doodles, footer.
2. Then place the hero, characters and icons.
3. Lock the aspect ratio. Match each placeholder's size and position via **Posisi**: click the element, then enter Lebar / Tinggi / X / Y (Ctrl+A, then type).
4. Delete the placeholder box, including its label text.
5. Recolor decor to the deck palette where Canva allows it.
6. Run the §B richness check, **all five**:
   - 1 hero, at least 480 px
   - 3-6 supporting items
   - at least 2 decor layers
   - at least 4 palette colors visible
   - no bare paragraph of text
7. Fix only real problems: overlap, clipping, unreadable text. Never retype or restyle spec text.
8. Zoom screenshot of the page.

## Step 3: transition
Apply the transition named in your task to **all pages** (**Terapkan ke semua halaman** is allowed). Names in the UI: Larut = Dissolve, Meluncur = Slide, Tumpuk = Stack, Usap Warna, Usap Garis, Usap Lingkaran. If it is missing, use the fallback in the deck prompt and report it. If your deck prompt asks for one on-click animation, add exactly that one.

## Canva tips (the UI is in Indonesian)
- The **Gaya** button sits next to **Posisi**. Screenshot before clicking.
- **Hex color:** swatch → rainbow **"+"** → hex field.
- Do not use Ctrl+B on Semibold text. Use the font panel's **Cetak Tebal**.
- **Never type on the canvas.** Typing triggers shortcuts and creates stray shapes (for example "L" makes a line). Always click the Elements search box first, then type.
- Clicks in the Elements panel can insert stray items. Check for them and delete them.
- Do not add, delete or reorder pages.

## Hard rules
- Canva Elements only (Pro is OK). **Never** Canva AI, Magic Media, Dream Lab, Tanya Canva or any generate feature.
- Never sign in. Never use Bagikan/Share, Unduh/Download or Publish. Never change access.
- No copy/paste (shared clipboard). Insert each asset fresh, or duplicate on the canvas with Ctrl+D.
- Never click "Ubah semua".
- Keep spec text word for word. Bracket placeholders (`[Your Name] · [Organization]`, contact lines) stay as they are.
- Do not copy the reference template. No real logos, brands, or famous characters.

## Tools
- **Chrome** (load in ONE ToolSearch call): `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__find,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__form_input`
- **read-design (read-only):** `select:mcp__d5cfe195-efd4-4037-bb29-1fb256afd51c__read-design`. Never use edit-design.

## Speed rules (same quality, fewer round trips)
- **Batch actions** with `browser_batch`: insert flow = click search box → type keyword → Enter → wait 2 s → screenshot. Placement flow = click element → Posisi → set W / X / Y (Ctrl+A, type, Tab) → Delete the placeholder.
- Scaled screenshots (scale 0.5) while working; full or zoomed only for each page's final check. Use `find` / `read_page` refs instead of hunting by screenshot.
- Decide what you need before searching. Reuse with Ctrl+D. At most 2 result pages per asset, then take the best fit.
- Run read-design once at the end, not after every page.

## Finish
1. `read-design` with `design_content` for all pages. Confirm **no** `HERO:`, `ICON:`, `DECOR:` or stray `ICON` text remains and the spec text is intact. Thumbnails can be stale: the live editor is the truth.
2. In the live editor confirm no empty circle or frame is left where an icon belongs, and no stray shapes.
3. Close your tab.
4. Report tersely:
   - the design edit URL
   - per page: PASS/FAIL, what you placed, the creator used
   - style lock (creator, icon set)
   - transition applied
   - gaps, exceptions, any BLOCKED
