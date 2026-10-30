# Prompt 2/5: "The Merry Cookie Workshop" (colorful)

> Copy everything below into a new task.
> Team: one main agent, one asset scout, and four builder subagents.

**FIRST:** read and follow every section of
`%USERPROFILE%\Downloads\Canva-PPT-Prompts\set7-christmas-gamenight\canva-shared-pipeline.md`.

That file holds:
- §A: hard rules
- §B: colorful brief and richness checklist
- §C: pipeline, builder brief, QA, and report
- §D: lessons learned from earlier runs

Deck slug: `christmas-cookie-workshop`.

---

## 0. Goal

Build a 12-slide Canva presentation (1920 × 1080) called **"The Merry Cookie Workshop: Bake, Decorate & Share"**. It is a playful holiday baking class for families, schools, and community groups:
- why bake together
- safety
- a simple sugar-cookie recipe
- icing and decorating tricks
- cookies around the world
- gifting
- a cookie swap and a decorating challenge

**Reference (direction only):** https://www.canva.com/templates/EAG12C6c_sk/ ("Red and White Playful Merry Christmas Presentation").

- **Borrow the idea:**
  - a red-and-white playful energy
  - bouncy, friendly titles
  - playful hand-drawn Christmas doodles
  - generous white space
- **Build from scratch.** Do not copy any layout, illustration, or text from the reference.

**Must also differ from the earlier Christmas decks in this project:**
- Eco-Friendly Christmas
- Christmas Around the World (world-tour stop tags, dashed travel path, globe)
- Family Fun Guide (mint background, scrapbook polaroids, washi tape)
- Season's Greetings (midnight-blue sky, penguins, frosted-glass panels)
- Christmas Through the Senses (papercraft layers, emerald and berry, sense badges)
- The Magic of Christmas (storybook pages, chapter ribbons, dusk gradient)
- The other two Christmas decks in this set:
  - set7-1 Carol Stories: vinyl tracks, music staff
  - set7-3 Dear North Pole: postal stamps, envelopes

## 1. Borrow vs. must differ

| Borrow | Must differ |
|---|---|
| Red-and-white playful | Red and white appear only as **candy-cane stripe ribbons and frames**. The content uses **bright icing colors** (mint, bubblegum, lemon, blueberry, lilac), so every slide shows 4+ colors |
| Bouncy titles | Titles sit on a **candy-stripe title tab** with an **icing-drip edge** |
| Playful doodles | A **"frosting party" concept**: cookie-cutter-shaped cards (star, tree, round, gingerbread person), sprinkle confetti, piping-bag swirls, recipe cards with checkboxes |
| — | **No** Santa face, **no** reindeer, **no** stockings or fireplace scenes, **no** photo-realistic food photos, **no** polaroids or washi tape, **no** globe or travel path |

## 2. Design system

### Colors

| Token | Hex | Use |
|---|---|---|
| Sugar White | `#FFFBF6` | Background A |
| Mint Milk | `#E3F8EF` | Background B |
| Lemon Milk | `#FFF6D6` | Background C |
| Cocoa Ink | `#3B2420` | Text |
| Candy Red | `#E8333C` | Titles, stripes |
| Mint Icing | `#36C9A0` | Accent |
| Bubblegum | `#FF7BB0` | Accent |
| Lemon Drop | `#FFD23F` | Accent |
| Blueberry | `#4C8DFF` | Accent |
| Lilac Sugar | `#A47BF2` | Accent |
| Gingerbread | `#C47A3D` | Cookies, mascot details |

**Background rotation** (slide 1 → 12): Sugar White → Mint Milk → Lemon Milk → repeat.

Every slide has sprinkle confetti (tiny rounded bars and dots) in 3+ palette colors and at least one candy-stripe element.

### Fonts

| Role | Font | Fallback | Size | Color / style |
|---|---|---|---|---|
| Titles | Shrikhand | Lilita One | 74–88 | Candy Red, on a white tab with a candy-stripe border |
| Body | Nunito SemiBold | Quicksand SemiBold | 26–28 | Cocoa Ink |
| Eyebrow | Nunito ExtraBold | Quicksand Bold | 22 | UPPERCASE, letter spacing 200, palette color |

### Recurring motifs

1. **Candy-stripe title tab:** a white rounded tab with a red-and-white striped border and a small icing drip.
2. **Cookie-cutter cards:** cards shaped like a star, tree, circle, or gingerbread person (Canva shapes or frames), each filled with a light icing tint and a 3 px outline in a palette color.
3. **Recipe card:** a white card with a ruled header, checkbox ingredient rows, and an icing-drip top edge.
4. **Step badges:** numbers on round cookie badges with colorful icing tops.
5. **Ginger the mascot:** a friendly gingerbread person who appears small on most slides (pointing, waving, or holding a spoon).
6. **Footer:** a tiny rolling pin with the page number on a cookie circle.

**Transition:** Stack ("Tumpuk"). If it is not available, use Slide ("Meluncur").

### Illustration style

- **One** flat, cute, bright baking set:
  - diverse kids and grown-ups in aprons
  - mixing bowls, rolling pins, cookie cutters, and piping bags
  - colorful decorated cookies, a gingerbread person, and gift boxes
- The asset scout searches terms like:
  - "christmas baking flat illustration"
  - "kids baking cookies"
  - "gingerbread man cute"
  - "decorated christmas cookies"
  - "sprinkles"
- **One** cute filled icon set.

## 3. Slide-by-slide spec

### Builder A

**Slide 1: Cover** (Sugar White)
- Eyebrow: `A HOLIDAY BAKING CLASS`
- Title at (120, 220), width 960, 2 lines:
  > The Merry Cookie Workshop
- Pill (Mint Icing, white text):
  > Bake, decorate & share the joy.
- Presenter line:
  > Presented by [Your Name] · [Organization]
- Hero (~860, right): diverse kids and grown-ups decorating cookies at a table, with piping bags, a tray of colorful cookies, and Ginger waving.
- Decor: sprinkles, candy-stripe ribbon, piping swirls.

**Slide 2: Why Bake Together?** (Mint Milk)
- Title: `Why Bake Together?`
- Four cookie-cutter cards (star, tree, circle, gingerbread), each a different color, with an icon:
  - `Teamwork` — Everyone gets a job, from mixing to sprinkling.
  - `Creativity` — No two cookies look the same.
  - `Math in action` — Measuring and timing make numbers fun.
  - `Sharing` — Cookies make sweet gifts for friends and neighbors.
- Hero (~400, bottom right): a grandparent and a child rolling dough together.

**Slide 3: Before You Start** (Lemon Milk)
- Title: `Before You Start`
- Six checklist tickets (2 columns), each with a colored check circle:
  - `Wash your hands`
  - `Tie back long hair`
  - `Read the whole recipe first`
  - `Set out all the ingredients`
  - `Grown-ups handle the oven`
  - `Check for food allergies`
- Hero (~440): a kid in an apron and chef hat holding measuring cups.

### Builder B

**Slide 4: Simple Sugar Cookies** (Sugar White)
- Eyebrow `THE RECIPE` · Title `Simple Sugar Cookies`
- Recipe card with checkbox rows:
  - 2¾ cups (345 g) all-purpose flour
  - 1 tsp baking powder
  - ½ tsp salt
  - 1 cup (225 g) butter, softened
  - 1 cup (200 g) sugar
  - 1 egg
  - 1 tsp vanilla extract
- Three info chips:
  - `Makes: about 24 cookies`
  - `Oven: 180 °C / 350 °F`
  - `Bake: 8–10 min`
- Hero (~520, right): a big mixing bowl with flour, eggs, butter, and a whisk.

**Slide 5: Mix, Roll & Cut** (Mint Milk)
- Title: `Mix, Roll & Cut`
- Four numbered steps on cookie badges, in a horizontal path:
  1. Beat the butter and sugar until fluffy, then add the egg and vanilla.
  2. Mix in the flour, baking powder and salt to make a soft dough.
  3. Chill the dough for 1 hour, then roll it about 5 mm thick.
  4. Cut fun shapes and bake until the edges are just golden.
- Hero (~480, top): hands with a rolling pin and colorful cookie cutters on dough.

**Slide 6: Icing 101** (Lemon Milk)
- Title: `Icing 101`
- Mini recipe card `Simple Icing`:
  > 2 cups (250 g) powdered sugar + 2–3 tbsp milk + a few drops of food coloring.
- Tip bubble (Bubblegum tint):
  > Use thick icing for outlines and thinner icing to fill.
- Four small bowls of icing in Mint, Bubblegum, Lemon and Blueberry, each with a color label.
- Hero (~500): colorful piping bags squeezing icing swirls.

### Builder C

**Slide 7: Three Decorating Tricks** (Sugar White)
- Title: `Three Decorating Tricks`
- Three cookie-cutter cards, each with a small decorated-cookie illustration:
  - `Outline & Flood` — Pipe a border with thick icing, then fill the middle with thinner icing.
  - `Sprinkle Magic` — Add sprinkles while the icing is still wet so they stick.
  - `Wet-on-Wet Dots` — Drop dots of a second color into wet icing to make polka dots and hearts.
- Decor: Ginger holding a piping bag.

**Slide 8: Cookies Around the World** (Mint Milk)
- Title: `Cookies Around the World`
- Four plate-shaped round cards in a 2 × 2 grid, each with a cookie illustration (no globe, no flags, no travel path):
  - `Germany · Lebkuchen` — Spiced honey cookies, often sold at Christmas markets.
  - `Sweden · Pepparkakor` — Thin, crispy ginger cookies shaped like hearts and stars.
  - `Italy · Pizzelle` — Crisp waffle cookies pressed with pretty patterns.
  - `Mexico · Polvorones` — Crumbly cookies rolled in powdered sugar.
- Decor: sprinkles, a small Ginger peeking from a corner.

**Slide 9: Wrap It Up** (Lemon Milk)
- Title: `Wrap It Up: Cookie Gifts`
- Three gift-tag cards, each a different color:
  - `Cookie Jar` — Layer cookies in a clear jar and tie a ribbon on top.
  - `Paper Bag Pals` — Decorate brown paper bags with stamps and stickers.
  - `Cookie Box` — Line a box with paper and add a handwritten tag.
- Hero (~500): colorful gift boxes and a jar of cookies with ribbons.

### Builder D

**Slide 10: Host a Cookie Swap** (Sugar White)
- Title: `Host a Cookie Swap`
- Four numbered steps on cookie badges:
  1. Invite 6–10 bakers.
  2. Each person bakes a batch of one kind.
  3. Lay all the cookies out on a big table.
  4. Everyone fills a box with a mix to take home.
- Tip banner (Lilac Sugar, white text):
  > Ask everyone to bring a card listing the ingredients — helpful for allergies!
- Hero (~480): friends trading cookie boxes around a party table.

**Slide 11: Decorate-Off Challenge** (Mint Milk)
- Title: `Decorate-Off Challenge`
- Rule pill:
  > 15 minutes · 1 cookie each · everyone votes!
- Four award badges (ribbon rosettes), each a different color:
  - `Most Colorful`
  - `Funniest Face`
  - `Best Snowflake`
  - `Silliest Sweater`
- Hero (~460): kids proudly holding up decorated cookies, with a wooden-spoon trophy.

**Slide 12: Sweet Holidays!** (Lemon Milk)
- Title centered, Shrikhand 130, Candy Red:
  > Sweet Holidays!
- Subtitle:
  > Thanks for baking with us — now go share the cookies!
- Three contact pills (Mint / Bubblegum / Blueberry, white text):
  - `123-456-7890`
  - `hello@yourwebsite.com`
  - `www.yourwebsite.com`
- Hero along the bottom (~1400): a long table of colorful cookies with several gingerbread people waving, plus sprinkle confetti.

## 4. Speaker notes

- **Slides 3–6 and 10:** Always check for food allergies (wheat, egg, milk, nuts). Adults handle the oven and hot trays.
- **Slide 4:** Oven times vary. Check the cookies from 8 minutes.

## 5. Deck-specific QA

- [ ] Backgrounds rotate Sugar White → Mint Milk → Lemon Milk as listed.
- [ ] Red and white are used only as stripes and title color; content cards use the icing colors.
- [ ] Recipe numbers match §3 exactly (amounts, °C/°F, minutes).
- [ ] Ginger the mascot looks the same on every slide (one asset).
- [ ] No Santa face, reindeer, stockings, polaroids, washi tape, or globe.
- [ ] Text matches §3 word for word.
- [ ] Nothing copied from the reference; nothing from the earlier Christmas decks (§0).
