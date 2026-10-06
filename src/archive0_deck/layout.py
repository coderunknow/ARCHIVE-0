"""Slide construction: the :class:`Deck` under construction and the drawing
primitives used by the section modules.

Responsibilities are deliberately small -- this module knows how to draw shapes
and text and how to seal a slide (transition, animation, notes). It knows nothing
about the deck's subject matter (see :mod:`archive0_deck.sections`) and nothing
about validating or previewing the result.
"""

from pptx2 import Presentation
from pptx2.enum.shapes import MSO_SHAPE
from pptx2.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx2.util import Inches, Pt

from . import animation, theme
from .typography import fit_size, text_width_in

BLANK_LAYOUT = 6

_ALIGN_NAMES = {PP_ALIGN.LEFT: "left", PP_ALIGN.CENTER: "center", PP_ALIGN.RIGHT: "right"}
_ANCHOR_NAMES = {MSO_ANCHOR.TOP: "top", MSO_ANCHOR.MIDDLE: "middle",
                 MSO_ANCHOR.BOTTOM: "bottom"}


class Deck:
    """A presentation under construction.

    Owns the pptx2 presentation, the ordered slide sequence and the preview
    manifest. Slide numbers come from the insertion order, so sections never
    hard-code them.
    """

    def __init__(self, title="", subject="", comments="", footer=""):
        self._presentation = Presentation()
        self._presentation.slide_width = Inches(theme.SLIDE_WIDTH)
        self._presentation.slide_height = Inches(theme.SLIDE_HEIGHT)
        self._footer = footer
        properties = self._presentation.core_properties
        properties.title = title
        properties.subject = subject
        properties.author = ""
        properties.last_modified_by = ""
        properties.comments = comments
        self._slides = []

    def add_slide(self, kicker=None, title=None, notes="", label=None):
        """Append a slide and return it. *label* names the slide in the manifest."""
        number = len(self._slides) + 1
        slide = Slide(self._presentation, kicker, title, number, notes,
                      label or title or f"slide {number}", self._footer)
        self._slides.append(slide)
        return slide

    def save(self, path):
        """Seal any unfinished slides and write the .pptx to *path*."""
        for slide in self._slides:
            slide.finish()
        self._presentation.save(str(path))
        return path

    @property
    def slides(self):
        return tuple(self._slides)

    @property
    def manifest(self):
        """Per-slide geometry used by the preview renderer (fresh list each call)."""
        return [slide.manifest_entry() for slide in self._slides]


class Slide:
    """One slide plus the primitives used to draw it."""

    def __init__(self, presentation, kicker, title, number, notes, label, footer=""):
        self._slide = presentation.slides.add_slide(presentation.slide_layouts[BLANK_LAYOUT])
        self.number = number
        self.label = label
        self._notes = notes
        self._footer = footer
        self._effects = []          # (shape_id, preset) in reveal order
        self._shapes = []           # manifest entries for the preview renderer
        self._sealed = False
        self._draw_background()
        if kicker or title:
            self._draw_header(kicker, title)

    # ------------------------------------------------------------------ internals
    def _register(self, shape, kind=None):
        if kind is not None:
            self._effects.append((shape.shape_id, kind))
        return shape

    def _draw_background(self):
        self.rect(0, 0, theme.SLIDE_WIDTH, theme.SLIDE_HEIGHT, theme.BG, radius=0)
        self.rect(theme.SLIDE_WIDTH - 3.1, 0, 3.1, 0.16, theme.PANEL2, radius=0)

    def _draw_header(self, kicker, title):
        if kicker:
            self.text(theme.CONTENT_LEFT, 0.42, theme.CONTENT_WIDTH, 0.32, [kicker],
                      size=11.5, color=theme.LIME, bold=True, anim_kind=animation.FADE,
                      spacing=1.0)
        self.text(theme.CONTENT_LEFT - 0.02, 0.72, theme.CONTENT_WIDTH, 0.82, [title],
                  size=30, color=theme.WHITE, bold=True, anim_kind=animation.FADE,
                  spacing=0.95, font=theme.FONT_HEAD)
        self.rect(theme.CONTENT_LEFT + 0.02, 1.62, 1.15, 0.065, theme.LIME,
                  kind=animation.WIPE_UP)

    # ------------------------------------------------------------------ primitives
    def rect(self, x, y, w, h, fill, kind=None, radius=0.09, line=None, line_w=1.0):
        """Add a (rounded) rectangle. *kind* is an entrance preset, or ``None``."""
        shape = self._slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
            Inches(x), Inches(y), Inches(w), Inches(h))
        if radius:
            try:
                shape.adjustments[0] = radius
            except (IndexError, ValueError):
                pass                       # rectangle has no adjustment handle
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
        if line is not None:
            shape.line.color.rgb = line
            shape.line.width = Pt(line_w)
        else:
            shape.line.fill.background()
        shape.shadow.clear()
        self._shapes.append({"type": "rect", "x": x, "y": y, "w": w, "h": h,
                             "fill": str(fill), "radius": radius})
        return self._register(shape, kind)

    def text(self, x, y, w, h, paragraphs, size=14, color=theme.BODY, bold=False,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, anim_kind=None, spacing=1.15,
             space_after=6, font=theme.FONT_BODY, margin=0.06, italic=False,
             sizes=None, colors=None, bolds=None, shrink=True):
        """Add a text box.

        *paragraphs* is a list of strings; *sizes*/*colors*/*bolds* override the
        per-paragraph defaults. With *shrink* the largest size that fits the box is
        chosen automatically (see :mod:`archive0_deck.typography`).
        """
        count = len(paragraphs)
        sizes = sizes or [size] * count
        colors = colors or [color] * count
        bolds = bolds or [bold] * count
        scale = 1.0
        if shrink:
            fitted = fit_size(paragraphs, w - 2 * margin, h - 0.06, size, bold,
                              extra_gap_pt=space_after)
            scale = fitted / float(size)

        box = self._slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        frame = box.text_frame
        frame.word_wrap = True
        frame.margin_left = frame.margin_right = Inches(margin)
        frame.margin_top = frame.margin_bottom = Inches(0.02)
        frame.vertical_anchor = anchor

        manifest_paragraphs = []
        for index, text in enumerate(paragraphs):
            paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            paragraph.alignment = align
            paragraph.line_spacing = spacing
            if index < count - 1:
                paragraph.space_after = Pt(space_after)
            run = paragraph.add_run()
            run.text = str(text)
            run.font.name = font
            run.font.size = Pt(round(sizes[index] * scale, 1))
            run.font.bold = bolds[index]
            run.font.italic = italic
            run.font.color.rgb = colors[index]
            manifest_paragraphs.append({"text": str(text),
                                        "size": round(sizes[index] * scale, 1),
                                        "bold": bolds[index], "color": str(colors[index]),
                                        "font": font})

        self._shapes.append({"type": "text", "x": x, "y": y, "w": w, "h": h,
                             "align": _ALIGN_NAMES.get(align, "left"),
                             "anchor": _ANCHOR_NAMES.get(anchor, "top"),
                             "spacing": spacing, "space_after": space_after,
                             "margin": margin, "paras": manifest_paragraphs})
        return self._register(box, anim_kind)

    # ------------------------------------------------------------------ components
    def card(self, x, y, w, h, title, lines, accent=theme.LIME, title_size=15.5,
             body_size=13, source=None, fill=theme.PANEL, kind_title=animation.FADE,
             kind_body=animation.FADE, body_spacing=1.2, source_size=9.5):
        """A bordered panel with a title, body lines and an optional source note."""
        self.rect(x, y, w, h, fill, radius=0.06, line=theme.EDGE)
        pad = 0.24
        inner_width = w - 2 * pad
        top = y + 0.2
        if title:
            size = (fit_size([title], inner_width, 0.75, title_size, True)
                    if len(title) > 18 else title_size)
            self.text(x + pad, top, inner_width, 0.42, [title], size=size, color=accent,
                      bold=True, anim_kind=kind_title, spacing=1.0, font=theme.FONT_HEAD,
                      shrink=False)
            top += 0.48
        source_height = 0.34 if source else 0.0
        available_height = (y + h - pad - source_height) - top
        if lines:
            self.text(x + pad, top, inner_width, available_height, lines, size=body_size,
                      color=theme.BODY, anim_kind=kind_body, spacing=body_spacing,
                      space_after=5)
        if source:
            self.text(x + pad, y + h - pad - 0.26, inner_width, 0.3, [source],
                      size=source_size, color=theme.MUTED2, spacing=1.0, italic=True)

    def kpi(self, x, y, w, h, value, label, accent=theme.LIME, value_size=30):
        """A big number with a caption underneath."""
        self.rect(x, y, w, h, theme.PANEL2, radius=0.07, line=theme.EDGE)
        self.text(x + 0.18, y + 0.14, w - 0.36, h * 0.48, [value], size=value_size,
                  color=accent, bold=True, anim_kind=animation.WIPE_UP, spacing=0.95,
                  font=theme.FONT_HEAD)
        self.text(x + 0.18, y + h * 0.5, w - 0.36, h * 0.46, [label], size=11.5,
                  color=theme.BODY, anim_kind=animation.FADE, spacing=1.12)

    def chip(self, x, y, text, accent=theme.LIME, size=11.5, h=0.42):
        """A small pill sized to fit *text*; returns its width in inches."""
        pad = 0.22
        width = max(0.9, min(text_width_in(text, size, bold=True) + 2 * pad, 4.6))
        self.rect(x, y, width, h, theme.PANEL2, radius=0.5, line=accent, line_w=1.0,
                  kind=animation.WIPE_UP)
        self.text(x + 0.04, y + 0.02, width - 0.08, h - 0.04, [text], size=size,
                  color=accent, bold=True, align=PP_ALIGN.CENTER,
                  anchor=MSO_ANCHOR.MIDDLE, anim_kind=animation.FADE, spacing=1.0)
        return width

    def row(self, x, y, w, h, left, right, accent=theme.LIME, left_w=None,
            right_color=None, size=13, left_bold=True):
        """A single label/value row."""
        self.rect(x, y, w, h, theme.PANEL, radius=0.06, line=theme.EDGE)
        label_width = left_w or (w * 0.6)
        self.text(x + 0.22, y + 0.02, label_width, h - 0.04, [left], size=size,
                  color=theme.WHITE if left_bold else theme.BODY, bold=left_bold,
                  anim_kind=animation.FADE, spacing=1.05, anchor=MSO_ANCHOR.MIDDLE)
        if right:
            self.text(x + 0.22 + label_width, y + 0.02, w - 0.44 - label_width, h - 0.04,
                      [right], size=size, color=right_color or accent, bold=True,
                      align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE,
                      anim_kind=animation.FADE, spacing=1.05)

    def footer(self, show_page=True):
        if self._footer:
            self.text(theme.CONTENT_LEFT, 6.98, 8.0, 0.3, [self._footer],
                      size=9, color=theme.MUTED2, spacing=1.0)
        if show_page:
            self.text(theme.CONTENT_RIGHT - 1.2, 6.98, 1.2, 0.3, [f"{self.number:02d}"],
                      size=10.5, color=theme.LIME, bold=True, align=PP_ALIGN.RIGHT,
                      spacing=1.0, font=theme.FONT_HEAD, shrink=False)

    # ------------------------------------------------------------------ sealing
    def finish(self):
        """Apply transition, entrance animation and notes. Safe to call twice."""
        if self._sealed:
            return
        self._sealed = True
        self._slide._element.append(animation.build_transition_xml())
        timing = animation.build_timing_xml(self._effects)
        if timing is not None:
            self._slide._element.append(timing)
        if self._notes:
            self._slide.notes_slide.notes_text_frame.text = self._notes

    def manifest_entry(self):
        """Geometry of this slide for the preview renderer."""
        return {"page": self.number, "label": self.label, "shapes": list(self._shapes)}
