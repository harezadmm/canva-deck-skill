r"""Phase 0A skeleton for table-tournament (10 slides, 1920x1080).

Spec: %USERPROFILE%\Downloads\Canva-PPT-Prompts\set9-newyear-business-gamenight\prompt-set9-8-game-night-table-tournament.md
"""
import os
import math
from contextlib import contextmanager
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree
from PIL import ImageFont

PLACEHOLDERS = []  # (slide, label, x, y, w, h)
REG = []           # lint registry: (kind, slide, x, y, w, h, label, back)
WARN = []
CUR = [0]
TILT = None        # (pivot_cx, pivot_cy, degrees) while inside tilt()


# ----------------------------------------------------------------- units / colors
def px(v):
    return Emu(int(round(v * 9525)))


def fpt(pxsize):
    return Pt(pxsize * 0.75)


def rgb(h):
    return RGBColor.from_string(h)


def tint(h, pct=0.2):
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    f = lambda c: int(round(c * pct + 255 * (1 - pct)))
    return "%02X%02X%02X" % (f(r), f(g), f(b))


# ----------------------------------------------------------------- text measuring (lint only)
_PIL = {}


def _pil(bold, size):
    k = (bold, int(round(size)))
    if k not in _PIL:
        _PIL[k] = ImageFont.truetype(r"C:\Windows\Fonts\%s.ttf" % ("arialbd" if bold else "arial"),
                                     max(8, int(round(size))))
    return _PIL[k]


# font -> (width factor vs Arial, natural line-height in em, measured as Arial Bold?)  (conservative)
FM = {
    "Shrikhand": (1.12, 1.35, True), "Chewy": (0.95, 1.25, True),
    "Nunito SemiBold": (1.08, 1.364, False), "Nunito ExtraBold": (1.03, 1.364, True),
    "Poppins": (1.12, 1.5, False), "Poppins#b": (1.08, 1.5, True),
}


def _fm(font, bold):
    return FM["Poppins#b"] if (font == "Poppins" and bold) else FM[font]


def tw(t, size, font=None, bold=False):
    font = font or BODY_F
    f, lh, b = _fm(font, bold)
    return _pil(b, size).getlength(t) * f


def _para_segs(para, font, bold):
    return para if isinstance(para, list) else [(para, font, bold)]


def count_lines(segs, size, width):
    toks = []
    for t, f, b in segs:
        for j, w in enumerate(t.split(" ")):
            toks.append((w, f, b, j > 0))
    lines, cur, widest = 1, 0.0, 0.0
    for w, f, b, sb in toks:
        sp = tw(" ", size, f, b) if sb else 0
        ww = tw(w, size, f, b)
        widest = max(widest, ww)
        if cur > 0 and cur + sp + ww > width:
            lines += 1
            cur = ww
        else:
            cur += sp + ww
    return lines, widest


# ----------------------------------------------------------------- tilt (scrapbook cards)
def _place(x, y, w, h, rot=0, rotate=True):
    if TILT is None:
        return x, y, rot
    cx, cy, deg = TILT
    mx, my = x + w / 2.0, y + h / 2.0
    a = math.radians(deg)
    dx, dy = mx - cx, my - cy
    nx = cx + dx * math.cos(a) - dy * math.sin(a)
    ny = cy + dx * math.sin(a) + dy * math.cos(a)
    return nx - w / 2.0, ny - h / 2.0, (rot + deg) if rotate else rot


@contextmanager
def tilt(cx, cy, deg):
    global TILT
    old = TILT
    TILT = (cx, cy, deg)
    try:
        yield
    finally:
        TILT = old


# ----------------------------------------------------------------- primitives
def _alpha(sp, alpha):
    clr = sp.fill._xPr.find(qn("a:solidFill")).find(qn("a:srgbClr"))
    a = etree.SubElement(clr, qn("a:alpha"))
    a.set("val", str(int(alpha * 100000)))


def shape(slide, kind, x, y, w, h, fill=None, line=None, line_w=0, radius=None, alpha=None,
          name=None, rot=0, dash=False):
    ox, oy, orot = _place(x, y, w, h, rot)
    sp = slide.shapes.add_shape(kind, px(ox), px(oy), px(w), px(h))
    if name:
        sp.name = name
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
        if alpha is not None:
            _alpha(sp, alpha)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line)
        sp.line.width = px(line_w)
        if dash:
            sp.line.dash_style = MSO_LINE.DASH
    else:
        sp.line.fill.background()
    sp.shadow.inherit = False
    if radius is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sp.adjustments[0] = min(0.5, radius / float(min(w, h)))
    if orot:
        sp.rotation = orot
    if sp.has_text_frame:
        sp.text_frame.text = ""
    return sp


def rrect(slide, x, y, w, h, fill, radius=28, **kw):
    return shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, radius=radius, **kw)


def rect(slide, x, y, w, h, fill, **kw):
    return shape(slide, MSO_SHAPE.RECTANGLE, x, y, w, h, fill=fill, **kw)


def circle(slide, x, y, d, fill, **kw):
    return shape(slide, MSO_SHAPE.OVAL, x, y, d, d, fill=fill, **kw)


def _shadow_fx(run, color, dist_px):
    """Hard extruded text shadow (no blur) at 45 degrees."""
    rPr = run._r.get_or_add_rPr()
    eff = etree.Element(qn("a:effectLst"))
    sh = etree.SubElement(eff, qn("a:outerShdw"), blurRad="0", dist=str(int(dist_px * 9525)),
                          dir="2700000", algn="tl", rotWithShape="0")
    etree.SubElement(sh, qn("a:srgbClr"), val=color)
    rPr.find(qn("a:solidFill")).addnext(eff)


def text(slide, x, y, w, h, runs, size, color, font=None, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, spacing=None, line_spacing=None, shadow=None, name=None,
         nolint=False):
    """runs: str, or list of paragraphs; each paragraph a str or list of (text, font, bold)."""
    font = font or BODY_F
    ox, oy, orot = _place(x, y, w, h)
    tb = slide.shapes.add_textbox(px(ox), px(oy), px(w), px(h))
    if name:
        tb.name = name
    if orot:
        tb.rotation = orot
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    paras = runs if isinstance(runs, list) else [runs]
    total_h, snippet = 0.0, ""
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if line_spacing:
            p.line_spacing = line_spacing
        segs = _para_segs(para, font, bold)
        for t, f, b in segs:
            r = p.add_run()
            r.text = t
            r.font.name = f
            r.font.size = fpt(size)
            r.font.bold = b
            r.font.color.rgb = rgb(color)
            if spacing is not None:
                r._r.get_or_add_rPr().set("spc", str(int(spacing)))
            if shadow:
                _shadow_fx(r, shadow[0], shadow[1])
        sp_extra = (spacing or 0) / 100.0 / 0.75  # letter spacing, px per char
        ln, widest = count_lines(segs, size, w)
        if sp_extra:
            nch = sum(len(t) for t, _, _ in segs)
            ln = max(ln, int(math.ceil((sum(tw(t, size, f, b) for t, f, b in segs) + nch * sp_extra) / w)))
        lh = _fm(segs[0][1], segs[0][2])[1]
        total_h += ln * size * lh * (line_spacing or 1.0)
        if widest > w + 1:
            WARN.append("S%d WORD-OVERFLOW %r (word %.0f > box %.0f)" % (CUR[0], segs[0][0][:30], widest, w))
        snippet += segs[0][0][:24] + " "
    if not nolint and total_h > h * 1.04 + 2:
        WARN.append("S%d TEXT-FIT %r est_h %.0f > box_h %.0f" % (CUR[0], snippet.strip(), total_h, h))
    REG.append(("text", CUR[0], x, y, w, h, snippet.strip(), False))
    return tb


def ph(slide, idx, label, x, y, w, h, back=False, fill="E6D6F0", ink="2B1A14", rot=0, alpha=0.8,
       lab_size=None, lab_color=None, anchor=None, align=None):
    """Labeled placeholder rectangle, 20% transparent fill (alpha 0.8), dashed outline."""
    sp = shape(slide, MSO_SHAPE.RECTANGLE, x, y, w, h, fill=fill, alpha=alpha, line=ink, line_w=2,
               name=label, rot=rot, dash=True)
    # shape() applied tilt rotation to rectangle; keep placeholders upright unless rot is explicit
    if TILT is not None:
        sp.rotation = rot
    tf = sp.text_frame
    tf.word_wrap = True
    # keep the label inside the visible part of the slide when the box bleeds off an edge
    tf.margin_left = px(max(0, -x) + 8)
    tf.margin_right = px(max(0, x + w - 1920) + 8)
    tf.margin_top = px(max(0, -y) + 6)
    tf.margin_bottom = px(max(0, y + h - 1080) + 6)
    if anchor is None:
        anchor = MSO_ANCHOR.MIDDLE
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    if align is None:
        align = PP_ALIGN.CENTER
    p.alignment = align
    r = p.add_run()
    r.text = label
    r.font.name = BOLD_PH
    r.font.bold = PH_BOLD
    r.font.size = fpt(lab_size or (11 if min(w, h) <= 72 else 14 if min(w, h) < 110 else 16))
    r.font.color.rgb = rgb(lab_color or ink)
    PLACEHOLDERS.append((idx, label, x, y, w, h))
    REG.append(("ph", CUR[0], x, y, w, h, label, back))
    return sp


def notes(slide, t):
    slide.notes_slide.notes_text_frame.text = t


def lint_report():
    """Print text-vs-placeholder / text-vs-text overlaps (box level) and fit warnings."""
    out = []
    per = {}
    for r in REG:
        per.setdefault(r[1], []).append(r)
    for sl, items in sorted(per.items()):
        txt = [r for r in items if r[0] == "text"]
        phs = [r for r in items if r[0] == "ph" and not r[7]]
        def inter(a, b):
            ix = min(a[2] + a[4], b[2] + b[4]) - max(a[2], b[2])
            iy = min(a[3] + a[5], b[3] + b[5]) - max(a[3], b[3])
            return ix, iy
        for t in txt:
            for p_ in phs:
                ix, iy = inter(t, p_)
                if ix > 6 and iy > 6:
                    out.append("S%d TEXT~PH  %r  x  %r  (%.0fx%.0f)" % (sl, t[6][:28], p_[6][:34], ix, iy))
        for i in range(len(txt)):
            for j in range(i + 1, len(txt)):
                ix, iy = inter(txt[i], txt[j])
                if ix > 6 and iy > 6:
                    out.append("S%d TEXT~TEXT %r x %r (%.0fx%.0f)" % (sl, txt[i][6][:28], txt[j][6][:28], ix, iy))
        SOFT = ("DECOR: washi tape", "DECOR: paper clip", "DECOR: Mustard squiggle")
        for i in range(len(phs)):
            for j in range(i + 1, len(phs)):
                if phs[i][6].startswith(SOFT) or phs[j][6].startswith(SOFT):
                    continue
                ix, iy = inter(phs[i], phs[j])
                if ix > 12 and iy > 12:
                    out.append("S%d PH~PH    %r x %r (%.0fx%.0f)" % (sl, phs[i][6][:30], phs[j][6][:30], ix, iy))
    return WARN + out


# =====================================================================================
# DECK: Table Tournament Night: Roll, Stack and Win   (slug table-tournament)
# Concept "Scrapbook Tournament": solid earthy backgrounds + grid-paper texture, cream
# notebook-paper cards (spiral holes, tilt, washi tape), hanging points tags, die footer.
# =====================================================================================
SLUG = "table-tournament"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), SLUG + "-skeleton.pptx")

C = dict(forest="2E6B4B", cocoa="5A2F1E", brick="C23B33", cream="FFF8E8", ink="2B1810",
         mustard="F2B63D", pink="F58CB0", sky="8ED0EA", lime="9BD35A", peach="FFA36B",
         white="FFFFFF")
TITLE_F = "Chewy"
BODY_F = "Poppins"       # Poppins Medium -> "Poppins" (whitelist name), bold off
BOLD_F = "Poppins"       # Poppins Bold   -> "Poppins" + bold on
BOLD_PH = "Poppins"
PH_BOLD = True
DARK = (C["forest"], C["cocoa"], C["brick"])
PASTELS = [C["mustard"], C["pink"], C["sky"], C["lime"], C["peach"]]
CNAME = {C["cream"]: "Cream", C["mustard"]: "Mustard", C["pink"]: "Pink", C["sky"]: "Sky", C["lime"]: "Lime",
         C["peach"]: "Peach"}
BG = [None]

prs = Presentation()
prs.slide_width = Emu(18288000)
prs.slide_height = Emu(10287000)
BLANK = prs.slide_layouts[6]


def on(color):
    """Cream on the dark earth tones, Ink Brown on every pastel."""
    return C["cream"] if color in DARK else C["ink"]


def lighten(h, pct):
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    f = lambda c: int(round(c + (255 - c) * pct))
    return "%02X%02X%02X" % (f(r), f(g), f(b))


def new(n, bgc):
    CUR[0] = n
    BG[0] = bgc
    s = prs.slides.add_slide(BLANK)
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = rgb(bgc)
    ph(s, n, "DECOR: faint grid-paper texture (lines ~6% lighter, 48px apart) full-bleed, back layer",
       0, 0, 1920, 1080, back=True, fill=lighten(bgc, 0.1), ink=C["cream"],
       anchor=MSO_ANCHOR.BOTTOM, align=PP_ALIGN.CENTER, lab_size=14, lab_color=C["cream"])
    return s


def T(s, x, y, w, h, txt, size=26, color=None, bold=False, **kw):
    """Poppins text helper (Medium = regular weight, Bold = bold on)."""
    return text(s, x, y, w, h, txt, size, color or C["ink"], font=BOLD_F if bold else BODY_F,
                bold=bold, **kw)


def eyebrow(s, x, y, t, color, center=False):
    """Game-color chip + Poppins Bold 22 UPPERCASE, letter spacing 200 (spc 330), Ink text."""
    cw = int(tw(t, 22, BOLD_F, True) + len(t) * 4.4 + 56)
    if center:
        x = (1920 - cw) // 2
    rrect(s, x, y, cw, 40, color, radius=20, line=C["ink"], line_w=2)
    text(s, x, y, cw, 40, t, 22, C["ink"], font=BOLD_F, bold=True, spacing=330,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, nolint=True)
    return cw


def title(s, x, y, w, h, t, size=84, align=PP_ALIGN.LEFT, ls=0.95):
    """Chewy, Cream Paper, no pill or highlight behind it."""
    return text(s, x, y, w, h, t, size, C["cream"], font=TITLE_F, align=align,
                anchor=MSO_ANCHOR.MIDDLE, line_spacing=ls)


def squiggle(s, idx, x, y, w, center=False):
    if center:
        x = (1920 - w) // 2
    ph(s, idx, "DECOR: Mustard squiggle underline (hand-drawn) %dw" % w, x, y, w, 34, lab_size=13)


def die(s, n, pip):
    """Bottom-right die footer: white rounded square, page number, pip dot in the game color."""
    rrect(s, 1798, 972, 76, 76, C["white"], radius=16, line=C["ink"], line_w=3, name="DIE")
    circle(s, 1809, 983, 14, pip, line=C["ink"], line_w=2, name="DIE PIP")
    text(s, 1798, 990, 76, 52, str(n), 26, C["ink"], font=BOLD_F, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, nolint=True)


def tape(s, idx, cx, cy, color, rot=-35, w=120, h=34):
    """Washi-tape placeholder (diagonal strip, centered on cx,cy)."""
    ph(s, idx, "DECOR: washi tape (%s)" % CNAME.get(color, "Mustard"), cx - w / 2.0, cy - h / 2.0,
       w, h, rot=rot, lab_size=12)


def clip(s, idx, x, y, w=56, h=120, label="DECOR: paper clip"):
    ph(s, idx, label, x, y, w, h, lab_size=12)


def doodle(s, idx, x, y, w, h, what="squiggle doodles (6 palette colors)"):
    ph(s, idx, "DECOR: " + what, x, y, w, h)


@contextmanager
def card(s, x, y, w, h, color=None, hdr=None, deg=0.0, strip=72, holes=True, hole_from=34,
         hole_to=34):
    """Notebook-paper card: radius 20, 3px Ink outline, soft shadow, header strip in game color,
    row of 8 spiral holes along the top edge, optional tilt (everything drawn inside tilts too)."""
    with tilt(x + w / 2.0, y + h / 2.0, deg):
        rrect(s, x + 6, y + 10, w, h, "000000", radius=20, alpha=0.28, name="CARD SHADOW")
        rrect(s, x, y, w, h, C["cream"], radius=20, line=C["ink"], line_w=3, name="NOTEBOOK CARD")
        if color:
            rrect(s, x + 3, y + 3, w - 6, strip, color, radius=17, name="HEADER STRIP")
            rect(s, x + 3, y + 3 + strip // 2, w - 6, strip - strip // 2, color, name="HEADER STRIP")
            rect(s, x + 3, y + 2 + strip, w - 6, 3, C["ink"], name="STRIP RULE")
        if holes:
            n = 8
            span = w - hole_from - hole_to
            hy = (y + 9) if color else (y + 12)
            for i in range(n):
                circle(s, x + hole_from + i * span / (n - 1.0) - 7, hy, 14, BG[0], line=C["ink"],
                       line_w=2, name="SPIRAL HOLE")
        if hdr:
            T(s, x + 24, y + 30, w - 48, 38, hdr, 26, bold=True, anchor=MSO_ANCHOR.MIDDLE,
              nolint=True)
        yield


def numdot(s, x, y, d, n, fill=None):
    circle(s, x, y, d, fill or C["cream"], line=C["ink"], line_w=3, name="STEP NUMBER")
    text(s, x, y, d, d, str(n), 24 if d < 60 else 26, C["ink"], font=BOLD_F, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, nolint=True)


def chip(s, x, y, t, fill, size=26, h=60, pad=32, bold=True, icon=None, idx=None, w=None,
         center=False, outline=True, text_color=None):
    """Auto-width pill/chip. Returns its width."""
    lead = 62 if icon else 0
    cw = w or int(tw(t, size, BOLD_F if bold else BODY_F, bold) + 2 * pad + lead)
    if center:
        x = (1920 - cw) // 2
    rrect(s, x, y, cw, h, fill, radius=h // 2, line=C["ink"] if outline else None,
          line_w=3 if outline else 0)
    if icon:
        ph(s, idx, "ICON: " + icon, x + 18, y + (h - 44) // 2, 44, 44)
    T(s, x + pad + lead - (0 if icon else 14), y, cw - 2 * pad - lead + (14 if icon else 28), h, t,
      size, text_color or on(fill), bold=bold, align=PP_ALIGN.LEFT if icon else PP_ALIGN.CENTER,
      anchor=MSO_ANCHOR.MIDDLE)
    return cw


def ptag(s, x, y, w, h, color, t):
    """Luggage-style hanging points tag: string from the top edge, hole, game color."""
    rect(s, x + w // 2 - 3, 0, 6, y + 22, C["cream"], name="TAG STRING")
    sp = shape(s, MSO_SHAPE.SNIP_2_SAME_RECTANGLE, x, y, w, h, fill=color, line=C["ink"],
               line_w=3, name="POINTS TAG")
    sp.adjustments[0] = 0.3
    sp.adjustments[1] = 0.0
    circle(s, x + w // 2 - 12, y + 12, 24, BG[0], line=C["ink"], line_w=3, name="TAG HOLE")
    T(s, x + 18, y + 46, w - 36, h - 56, t, 24, bold=True, align=PP_ALIGN.CENTER,
      anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)


def step_card(s, idx, x, y, w, h, color, n, body, deg=0.0, tape_at=True):
    """Notebook card with a 56px game-color strip holding the number circle, text below."""
    with card(s, x, y, w, h, color=color, deg=deg, strip=56, hole_from=96):
        numdot(s, x + 18, y + 8, 40, n)
        T(s, x + 26, y + 70, w - 52, h - 70 - 16, body, 26, anchor=MSO_ANCHOR.MIDDLE,
          line_spacing=1.0)
        if tape_at:
            tape(s, idx, x + w - 22, y + 6, color, rot=38)


# ---------------- Slide 1: Cover (title left, hero right) ----------------
s = new(1, C["forest"])
doodle(s, 1, 30, 24, 400, 100, "squiggle doodles (spirals, zigzags, stars) TL corner")
eyebrow(s, 110, 140, "GAME NIGHT PLAYBOOK", C["mustard"])
title(s, 110, 220, 860, 390, ["Table", "Tournament", "Night"], size=110)
squiggle(s, 1, 110, 618, 340)
chip(s, 110, 672, "Roll. Stack. Win.", C["brick"], size=32, h=72, pad=44)
T(s, 110, 764, 860, 40, "Hosted by [Your Name] · [Organization]", 26, C["cream"],
  anchor=MSO_ANCHOR.MIDDLE)
for i, (col, ic) in enumerate([(C["mustard"], "dice"), (C["pink"], "playing cards"),
                               (C["sky"], "stacking blocks")]):
    cx = 110 + i * 130
    circle(s, cx, 826, 104, col, line=C["cream"], line_w=3)
    ph(s, 1, "ICON: " + ic, cx + 22, 848, 60, 60)
ph(s, 1, "HERO: scrapbook collage on a tilted notebook-paper sheet - stack of dice, fan of playing "
         "cards, small block tower, a few bingo balls, held with washi tape + paper clip, two "
         "laughing friends peeking from behind 780w", 1040, 110, 780, 760)
tape(s, 1, 1050, 130, C["mustard"], rot=-38, w=190, h=44)
clip(s, 1, 880, 990, 110, 140, "DECOR: paper clip (half-hidden at bottom edge)")
doodle(s, 1, 1100, 900, 620, 80, "squiggle doodles + stars (6 colors)")
die(s, 1, C["mustard"])
notes(s, "Welcome everyone. Explain that teams will play four short games, collect tournament "
         "points, and the top four teams will meet in a final bracket. Gather a die, a deck of "
         "cards, stacking blocks, paper and pens before you start.")

# ---------------- Slide 2: Tonight's Menu (row of 4 cards, banner + hero below) ----------------
s = new(2, C["cocoa"])
doodle(s, 2, 30, 24, 300, 100, "squiggle doodles TL")
doodle(s, 2, 1590, 24, 300, 100, "squiggle doodles TR")
eyebrow(s, 0, 30, "TONIGHT'S MENU", C["pink"], center=True)
title(s, 340, 76, 1240, 120, "Four Games, One Champion", size=84, align=PP_ALIGN.CENTER)
squiggle(s, 2, 0, 198, 520, center=True)
menu = [
    ("GAME 1", C["mustard"], "dice", "Dice Duel", "Push your luck and bank your points."),
    ("GAME 2", C["pink"], "playing cards", "Card Climb", "Guess higher or lower up the ladder."),
    ("GAME 3", C["sky"], "stacking blocks", "Tower Stack", "Pull a block. Keep the tower standing."),
    ("GAME 4", C["lime"], "bingo ball", "Party Bingo", "Mingle and find someone who…"),
]
for i, (g, col, ic, name, tag) in enumerate(menu):
    x, y, w, h = 115 + i * 430, 256, 400, 372
    with card(s, x, y, w, h, color=col, hdr=g, deg=1.2 if i % 2 == 0 else -1.2):
        ph(s, 2, "ICON: " + ic + " (hero icon)", x + 140, y + 86, 120, 120)
        T(s, x + 20, y + 214, w - 40, 40, name, 26, bold=True, align=PP_ALIGN.CENTER,
          anchor=MSO_ANCHOR.MIDDLE)
        T(s, x + 24, y + 260, w - 48, 88, tag, 26, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP,
          line_spacing=1.0)
        tape(s, 2, x + w - 24, y + 6, col, rot=38)
rrect(s, 115, 668, 1060, 96, C["mustard"], radius=28, line=C["ink"], line_w=3)
ph(s, 2, "ICON: trophy", 139, 686, 60, 60)
T(s, 219, 668, 930, 96, [[("Tournament points per game:", BOLD_F, True)],
                         [("1st place = 3 · 2nd place = 2 · everyone else = 1", BODY_F, False)]],
  26, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
rrect(s, 115, 788, 1060, 64, C["cream"], radius=32, line=C["ink"], line_w=3)
T(s, 143, 788, 1010, 64, "After four games, the top four teams play the Cup Bracket.", 26,
  anchor=MSO_ANCHOR.MIDDLE)
ph(s, 2, "HERO: spread of dice, cards and a bingo ball on paper with a stopwatch, a cheering friend "
         "and doodles 600w", 1220, 660, 590, 310)
clip(s, 2, 1150, 640, 50, 110)
doodle(s, 2, 115, 880, 560, 90, "squiggle doodles + stars")
die(s, 2, C["pink"])
notes(s, "Explain the scoring: 1st place = 3 tournament points, 2nd = 2, everyone else = 1. Write "
         "the points on the scoreboard (slide 9) after every game.")

# ---------------- Slide 3: House Rules (hero left, 5 sticky notes right) ----------------
s = new(3, C["brick"])
clip(s, 3, 30, 20, 60, 150)
eyebrow(s, 760, 40, "HOUSE RULES", C["sky"])
title(s, 760, 88, 1100, 120, "Play Fair, Have Fun", size=84)
squiggle(s, 3, 760, 210, 460)
ph(s, 3, "HERO: group of diverse friends high-fiving around a small table with dice and cards, "
         "scrapbook style 520w", 80, 200, 520, 640)
rules = ["Cheer for every team, not just yours.", "The host's call is final.",
         "Keep it quick: 30 seconds per turn.", "Phones down, eyes up, snacks welcome.",
         "Winning is fun. Laughing is better."]
icons = ["megaphone", "whistle", "stopwatch", "phone face down", "smiley"]
for i, body in enumerate(rules):
    col = PASTELS[i]
    x, y, w, h = (770 if i % 2 == 0 else 830), 266 + i * 122, 980, 100
    with tilt(x + w / 2.0, y + h / 2.0, 1.4 if i % 2 == 0 else -1.4):
        rrect(s, x + 5, y + 8, w, h, "000000", radius=14, alpha=0.25, name="NOTE SHADOW")
        rrect(s, x, y, w, h, col, radius=14, line=C["ink"], line_w=3, name="STICKY NOTE")
        numdot(s, x + 22, y + 20, 60, i + 1)
        T(s, x + 106, y + 18, w - 106 - 110, h - 22, body, 26, anchor=MSO_ANCHOR.MIDDLE)
        ph(s, 3, "ICON: " + icons[i], x + w - 82, y + 24, 52, 52)
        tape(s, 3, x + w / 2.0, y - 2, PASTELS[(i + 2) % 5], rot=-4, w=130, h=32)
rrect(s, 760, 878, 1020, 92, C["cream"], radius=28, line=C["ink"], line_w=3)
ph(s, 3, "ICON: clipboard", 784, 902, 44, 44)
T(s, 848, 878, 906, 92, "You will need: a die, a deck of cards, stacking blocks, paper and pens", 26,
  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
doodle(s, 3, 80, 870, 600, 110, "squiggle doodles + stars")
die(s, 3, C["lime"])
notes(s, "Read the five rules aloud. Pick one person as the timer and one as the scorekeeper.")

# ---------------- Slide 4: Game 1 Dice Duel (rules card left, hero right) ----------------
s = new(4, C["forest"])
eyebrow(s, 110, 40, "GAME 1 · PUSH YOUR LUCK", C["mustard"])
title(s, 110, 88, 700, 140, "Dice Duel", size=96)
squiggle(s, 4, 110, 232, 360)
ptag(s, 1500, 46, 330, 140, C["mustard"], "Win = 3 points")
with card(s, 110, 296, 1020, 482, color=C["mustard"], hdr="How to play", deg=-0.8):
    steps = ["Teams take turns rolling one die as many times as they like.",
             "Add up your rolls. Say \"Bank!\" to lock in your points.",
             "Roll a 1 and you lose that turn's points. Your turn ends.",
             "The first team to bank 30 points wins."]
    for i, st in enumerate(steps):
        ry = 296 + 90 + i * 94
        numdot(s, 110 + 30, ry + 16, 56, i + 1, fill=C["mustard"])
        T(s, 110 + 110, ry, 1020 - 110 - 36, 90, st, 26, anchor=MSO_ANCHOR.MIDDLE,
          line_spacing=1.0)
    tape(s, 4, 128, 300, C["mustard"], rot=-40, w=170, h=40)
rrect(s, 110, 802, 1020, 100, C["cream"], radius=32, line=C["ink"], line_w=3)
ph(s, 4, "ICON: lightbulb", 134, 828, 48, 48)
T(s, 206, 802, 896, 100, "Example: roll 4, 6, 3 and bank = 13 points. Roll 4, 6, 1 = zero.", 26,
  anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0)
ph(s, 4, "HERO: huge hand-drawn die mid-roll with smaller dice, a pencil and a score pad, one "
         "friend cheering and one friend covering their eyes 540w", 1240, 220, 560, 730)
doodle(s, 4, 840, 40, 560, 150, "squiggle doodles (spirals, zigzags, stars)")
clip(s, 4, 1112, 270, 56, 120)
die(s, 4, C["mustard"])
notes(s, "Dice Duel: a quick game. Pass one die between teams. Remind players that rolling a 1 "
         "wipes out the points of that turn only; banked points are safe. For a shorter game, "
         "play to 20.")

# ---------------- Slide 5: Game 2 Card Climb (ladder hero top, 2x2 steps below) ----------------
s = new(5, C["cocoa"])
eyebrow(s, 110, 36, "GAME 2 · HIGHER OR LOWER", C["pink"])
title(s, 110, 84, 600, 140, "Card Climb", size=96)
squiggle(s, 5, 110, 230, 330)
ptag(s, 1500, 24, 330, 130, C["pink"], "Win = 3 points")
ph(s, 5, "HERO: row of six playing cards rising like stair steps (first face up, rest face down) "
         "with a small friend climbing the steps, scrapbook style 1100w", 720, 170, 1100, 330)
rrect(s, 110, 306, 560, 96, C["cream"], radius=30, line=C["ink"], line_w=3)
T(s, 138, 306, 504, 96, "A tie? One sudden-death flip decides.", 26, anchor=MSO_ANCHOR.MIDDLE,
  line_spacing=1.0)
doodle(s, 5, 110, 414, 540, 90, "squiggle doodles + stars")
steps = ["Shuffle a deck and lay out a ladder of six cards, face down.",
         "Flip the first card. Guess if the next card is higher or lower. Ace is high.",
         "Right guess: flip it and keep climbing. Wrong guess or a tie: your turn ends.",
         "Each team gets two turns. The team that climbs the most cards wins."]
for i, st in enumerate(steps):
    step_card(s, 5, 110 + (i % 2) * 865, 530 + (i // 2) * 225, 835, 205, C["pink"], i + 1, st,
              deg=1.0 if (i % 2 == 0) else -1.0)
clip(s, 5, 66, 505, 50, 110)
die(s, 5, C["pink"])
notes(s, "Card Climb: use a standard deck without jokers. Count each correct guess as one step "
         "climbed. Let teams shuffle for each other. Ace is high; the lowest card is 2.")

# ---------------- Slide 6: Game 3 Tower Stack (tower center, 2 step cards each side) -----------
s = new(6, C["brick"])
doodle(s, 6, 30, 24, 300, 130, "squiggle doodles TL")
eyebrow(s, 0, 36, "GAME 3 · STEADY HANDS", C["sky"], center=True)
title(s, 460, 84, 1000, 140, "Tower Stack", size=96, align=PP_ALIGN.CENTER)
squiggle(s, 6, 0, 230, 360, center=True)
ptag(s, 1500, 28, 330, 150, C["sky"], "Last team standing = 3 points")
ph(s, 6, "HERO: tall wooden block tower, slightly wobbly, one block half-pulled with a hand "
         "reaching in, stopwatch beside it, nervous friends watching 520h", 710, 300, 500, 640)
steps = ["Build the tower: stack the blocks three across, level by level.",
         "On your turn, pull one block with one hand from any level below the top.",
         "Place it on top. You have 30 seconds.",
         "If the tower falls on your turn, your team is out. The last team standing wins."]
for i, st in enumerate(steps):
    cx = 110 if i < 2 else 1270
    cy = 310 + (i % 2) * 290
    step_card(s, 6, cx, cy, 540, 240, C["sky"], i + 1, st, deg=1.0 if i % 2 == 0 else -1.0)
    # short connector line to the tower (plain bar)
    if i < 2:
        rect(s, 652, cy + 118, 58, 5, C["cream"], name="CONNECTOR")
    else:
        rect(s, 1210, cy + 118, 60, 5, C["cream"], name="CONNECTOR")
clip(s, 6, 840, 285, 56, 110)
die(s, 6, C["sky"])
notes(s, "Tower Stack: use any stacking blocks. Ask players to keep their other hand behind their "
         "back. Play on a stable, flat table. Stop the game if someone feels unsafe.")

# ---------------- Slide 7: Game 4 Party Bingo (bingo card left, rules right) ----------------
s = new(7, C["forest"])
eyebrow(s, 110, 36, "GAME 4 · MINGLE", C["lime"])
title(s, 110, 84, 620, 140, "Party Bingo", size=96)
squiggle(s, 7, 110, 230, 400)
ptag(s, 1410, 28, 430, 130, C["lime"], "First to Bingo = 3 points")
doodle(s, 7, 740, 40, 560, 160, "squiggle doodles (spirals, zigzags, stars)")
prompts = ["Has a pet", "Plays an instrument", "Loves spicy food", "Can whistle",
           "Speaks two languages", "Has a birthday this month", "Is wearing green",
           "Has traveled by plane", "Likes pineapple on pizza", "Can juggle", "Has a sibling",
           "Plays chess", "Loves karaoke", "Is left-handed", "Has a nickname", "Reads comics"]
with card(s, 110, 270, 1000, 662, color=C["lime"], hdr="Find someone who…"):
    for i, pr in enumerate(prompts):
        r, c = divmod(i, 4)
        gx, gy = 110 + 28 + c * 238, 270 + 94 + r * 134
        rrect(s, gx, gy, 228, 124, lighten(PASTELS[(r + c) % 5], 0.15), radius=14, line=C["ink"],
              line_w=2.5, name="BINGO CELL")
        T(s, gx + 10, gy + 6, 208, 112, pr, 22, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
          line_spacing=1.0)
    tape(s, 7, 128, 276, C["lime"], rot=-40, w=170, h=40)
with card(s, 1180, 270, 650, 400, color=C["lime"], deg=0.0, strip=56):
    T(s, 1206, 346, 598, 124, "Walk around and ask a question. If the answer is \"yes,\" that "
      "person signs the square.", 26, line_spacing=1.0)
    T(s, 1206, 482, 598, 44, "One signature per person.", 26, line_spacing=1.0)
    T(s, 1206, 538, 598, 86, "First to complete a row, column or diagonal shouts \"Bingo!\"", 26,
      line_spacing=1.0)
    tape(s, 7, 1808, 276, C["lime"], rot=38)
ph(s, 7, "HERO: cluster of bingo balls, a marker pen and a cheering friend shouting \"Bingo!\" in a "
         "speech bubble 480w", 1230, 690, 580, 270)
clip(s, 7, 1085, 250, 56, 120)
die(s, 7, C["lime"])
notes(s, "Party Bingo: hand out a copy of the card (print it, or let players copy it onto paper). "
         "Feel free to swap prompts to suit your group. Stop after 10 minutes if nobody has a "
         "Bingo.")

# ---------------- Slide 8: The Cup Bracket (bracket center, rules chip + hero bottom) ----------
s = new(8, C["cocoa"])
eyebrow(s, 0, 30, "THE FINAL FACE-OFF", C["peach"], center=True)
title(s, 410, 76, 1100, 120, "The Cup Bracket", size=84, align=PP_ALIGN.CENTER)
squiggle(s, 8, 0, 198, 520, center=True)
doodle(s, 8, 30, 24, 300, 100, "squiggle doodles TL")
doodle(s, 8, 1530, 40, 350, 340, "lightning + squiggle doodles, stars")
seeds = [  # (label, y_label, [(seed, color, y_card)])
    ("SEMI-FINAL 1", 264, [("#1 seed", C["peach"], 308), ("#4 seed", C["mustard"], 444)]),
    ("SEMI-FINAL 2", 570, [("#2 seed", C["sky"], 614), ("#3 seed", C["pink"], 750)]),
]
mids = []
for lab, ly, cards in seeds:
    chip(s, 110, ly, lab, C["cream"], size=22, h=36, pad=24)
    for seed, col, cy in cards:
        with card(s, 110, cy, 470, 100, color=col, strip=48, hole_from=210, hole_to=24):
            T(s, 110 + 24, cy + 6, 170, 38, seed, 26, bold=True, anchor=MSO_ANCHOR.MIDDLE,
              nolint=True)
            T(s, 110 + 24, cy + 52, 420, 44, "Team name: ______", 26, anchor=MSO_ANCHOR.MIDDLE,
              nolint=True)
    T(s, 110, cards[0][2] + 104, 470, 32, "vs", 22, bold=True, color=C["cream"],
      align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, nolint=True)
    c1, c2 = cards[0][2] + 50, cards[1][2] + 50
    mids.append((c1 + c2) // 2)
    # bracket lines (plain bars)
    for c_ in (c1, c2):
        rect(s, 580, c_ - 2, 26, 5, C["cream"], name="BRACKET LINE")
    rect(s, 604, c1 - 2, 5, c2 - c1 + 5, C["cream"], name="BRACKET LINE")
    rect(s, 604, (c1 + c2) // 2 - 2, 46, 5, C["cream"], name="BRACKET LINE")
rect(s, 648, mids[0] - 2, 5, mids[1] - mids[0] + 5, C["cream"], name="BRACKET LINE")
fy = (mids[0] + mids[1]) // 2
rect(s, 648, fy - 2, 44, 5, C["cream"], name="BRACKET LINE")
with card(s, 692, fy - 125, 430, 250, color=C["mustard"], hdr="FINAL"):
    for k in range(2):
        rrect(s, 692 + 26, fy - 125 + 88 + k * 80, 430 - 52, 64, C["white"], radius=18,
              line=C["ink"], line_w=2.5, dash=True, name="EMPTY SLOT")
    tape(s, 8, 692 + 430 - 24, fy - 125 + 6, C["mustard"], rot=38)
rect(s, 1122, fy - 2, 40, 5, C["cream"], name="BRACKET LINE")
ph(s, 8, "ICON: golden trophy cup 190w", 1166, fy - 120, 190, 200)
chip(s, 1146, fy + 90, "CHAMPION", C["cream"], size=26, h=56, w=230)
chip(s, 110, 880, "Seed the top four teams by tournament points. Every match is a quick Dice Duel to "
     "15 points.", C["mustard"], size=26, h=88, icon="dice", idx=8, w=1220, bold=False)
ph(s, 8, "HERO: two big dice facing each other like a face-off, lightning doodles, two friends "
         "rooting on either side 500w", 1390, 430, 480, 530)
clip(s, 8, 1106, 440, 50, 110)
die(s, 8, C["peach"])
notes(s, "Seed the teams from the scoreboard. Break ties with a single Dice Duel roll-off. "
         "Matches are Dice Duel to 15 points.")

# ---------------- Slide 9: Scoreboard and Awards (table left, awards + hero right) -------------
s = new(9, C["brick"])
eyebrow(s, 110, 36, "SCOREBOARD", C["mustard"])
title(s, 110, 84, 1000, 120, "Points and Prizes", size=84)
squiggle(s, 9, 110, 208, 480)
with card(s, 110, 270, 1100, 478, color=None, holes=True):
    heads = [("Team", C["mustard"], 170), ("Dice Duel", C["pink"], 170),
             ("Card Climb", C["sky"], 170), ("Tower Stack", C["lime"], 170),
             ("Party Bingo", C["peach"], 170), ("Total", C["mustard"], 140)]
    hx = 134
    xs = []
    for lab, col, cw_ in heads:
        rrect(s, hx, 310, cw_, 52, col, radius=26, line=C["ink"], line_w=2.5, name="HEADER PILL")
        T(s, hx, 310, cw_, 52, lab, 22, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        xs.append((hx, cw_))
        hx += cw_ + 8
    for r in range(5):
        ry = 372 + r * 72
        for ci, (cx_, cw_) in enumerate(xs):
            fill = tint(PASTELS[r % 5], 0.35) if ci == 0 else C["white"]
            rect(s, cx_, ry, cw_, 64, fill, line=C["ink"], line_w=2, name="TABLE CELL")
            T(s, cx_, ry, cw_, 64, ("Team %d" % (r + 1)) if ci == 0 else "—", 26,
              bold=(ci == 0), align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, nolint=True)
    tape(s, 9, 128, 276, C["mustard"], rot=-40, w=170, h=40)
rrect(s, 110, 772, 1100, 64, C["cream"], radius=32, line=C["ink"], line_w=3)
T(s, 140, 772, 1040, 64, "1st = 3 points · 2nd = 2 points · everyone else = 1 point", 26,
  anchor=MSO_ANCHOR.MIDDLE)
awards = [("Lucky Roller", "Best Dice Duel run", C["mustard"], "dice"),
          ("Steady Hands", "Last tower standing", C["sky"], "stacking blocks"),
          ("Best Sport", "Cheered the loudest", C["lime"], "megaphone")]
for i, (nm, ds, col, ic) in enumerate(awards):
    x, y, w, h = 1250, 50 + i * 170, 580, 150
    with tilt(x + w / 2.0, y + h / 2.0, 2.0 if i % 2 == 0 else -2.0):
        rrect(s, x + 6, y + 10, w, h, "000000", radius=24, alpha=0.28, name="RIBBON SHADOW")
        rrect(s, x, y, w, h, C["cream"], radius=24, line=C["ink"], line_w=3, name="AWARD RIBBON")
        circle(s, x + 22, y + 27, 96, col, line=C["ink"], line_w=3, name="ROSETTE")
        ph(s, 9, "ICON: " + ic, x + 42, y + 47, 56, 56)
        T(s, x + 136, y + 28, w - 160, 44, nm, 26, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        T(s, x + 136, y + 78, w - 160, 44, ds, 26, anchor=MSO_ANCHOR.MIDDLE)
        tape(s, 9, x + w - 24, y + 6, col, rot=36)
ph(s, 9, "HERO: shiny cartoon trophy cup with confetti and a podium (1-2-3) 580w", 1250, 585, 580,
   375)
doodle(s, 9, 110, 860, 700, 100, "squiggle doodles + stars")
clip(s, 9, 1182, 290, 56, 120)
die(s, 9, C["lime"])
notes(s, "Add up each team's tournament points from the games. Hand out the three fun awards, "
         "then crown the champion from the bracket.")

# ---------------- Slide 10: Thank You (centered, hero along bottom) ----------------
s = new(10, C["forest"])
doodle(s, 10, 30, 30, 300, 230, "squiggle confetti TL (6 colors)")
doodle(s, 10, 1590, 30, 300, 230, "squiggle confetti TR (6 colors)")
title(s, 360, 40, 1200, 190, "Thank You!", size=140, align=PP_ALIGN.CENTER)
squiggle(s, 10, 0, 234, 560, center=True)
T(s, 360, 282, 1200, 48, "Thanks for playing! Same table, same time next week?", 30, C["cream"],
  align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
pw0 = chip(s, 0, 360, "The champions take home the Golden Dice!", C["mustard"], size=26, h=72, bold=False,
           icon="trophy", idx=10, center=True)
tape(s, 10, (1920 - pw0) / 2.0 + 10, 428, C["pink"], rot=38)
tape(s, 10, (1920 + pw0) / 2.0 + 2, 430, C["sky"], rot=-38)
pills = [("123-456-7890", C["pink"], "phone"), ("hello@yourwebsite.com", C["sky"], "mail"),
         ("www.yourwebsite.com", C["lime"], "web")]
widths = [int(tw(t, 26, BOLD_F, True) + 64 + 62) for t, _, _ in pills]
x0 = (1920 - (sum(widths) + 2 * 36)) // 2
for (lab, col, ic), pw in zip(pills, widths):
    chip(s, x0, 478, lab, col, size=26, h=76, icon=ic, idx=10, w=pw)
    x0 += pw + 36
ph(s, 10, "HERO: diverse friends and a family cheering around a small table covered in dice, "
          "cards, blocks and bingo balls, confetti squiggles flying 1400w", 260, 584, 1400, 376)
clip(s, 10, 160, 500, 60, 130)
die(s, 10, C["mustard"])
notes(s, "Thank everyone, hand over the prize, and invite the group to host the next tournament. "
         "Replace the contact details with your own.")

assert len(prs.slides) == 10
prs.save(OUT)
print("saved", OUT)
print("placeholders:", len(PLACEHOLDERS))
for row in PLACEHOLDERS:
    print("S%d | %s | %d,%d,%d,%d" % row)
print("---- LINT ----")
for w in lint_report():
    print(w)
