"""Text measurement and fitting.

One implementation is shared by the deck builder (to size text boxes) and by the
preview renderer (to draw them), so both always agree on how text wraps.

Measurement uses DejaVu Sans, whose glyphs are wider than Arial/Calibri. A box
sized with these metrics therefore also fits in PowerPoint.
"""

from pathlib import Path

from PIL import ImageFont

_FONT_DIRS = (
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/usr/share/fonts/dejavu"),
)
_REGULAR_NAME = "DejaVuSans.ttf"
_BOLD_NAME = "DejaVuSans-Bold.ttf"

_SUBPIXEL = 4          # measurement oversampling, keeps wrap decisions stable
_LINE_HEIGHT = 1.26    # line box as a multiple of the font size

_font_cache: dict[tuple[int, bool], ImageFont.FreeTypeFont] = {}


def _font_path(bold):
    name = _BOLD_NAME if bold else _REGULAR_NAME
    for directory in _FONT_DIRS:
        candidate = directory / name
        if candidate.is_file():
            return candidate
    raise RuntimeError(
        f"{name} not found in {[str(d) for d in _FONT_DIRS]}; install the DejaVu "
        "fonts or update archive0_deck.typography._FONT_DIRS"
    )


def measurement_font(size_pt, bold=False):
    """A PIL font for *size_pt* rounded up to the measurement grid."""
    key = (round(size_pt * _SUBPIXEL), bool(bold))
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(str(_font_path(bold)), key[0])
    return _font_cache[key]


def render_font(size_px, bold=False):
    """A PIL font at an exact pixel size, for drawing previews."""
    key = ("render", int(size_px), bool(bold))
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(str(_font_path(bold)), int(size_px))
    return _font_cache[key]


def text_width_in(text, size_pt, bold=False):
    """Rendered width of *text* on a single line, in inches."""
    font = measurement_font(size_pt, bold)
    return font.getlength(str(text)) / _SUBPIXEL / 72.0


def wrap(text, size_pt, bold, width_in):
    """Greedy word wrap; returns the list of lines."""
    font = measurement_font(size_pt, bold)
    max_px = max(width_in, 0.2) * 72.0 * _SUBPIXEL
    lines, current = [], ""
    for word in str(text).split():
        trial = f"{current} {word}" if current else word
        if font.getlength(trial) <= max_px:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def line_height_in(size_pt):
    """Height of one line of text at *size_pt*, in inches."""
    return size_pt * _LINE_HEIGHT / 72.0


def measure(paragraphs, size_pt, bold, width_in):
    """Return ``(line_count, height_in)`` for *paragraphs* wrapped in *width_in*."""
    line_count = sum(len(wrap(p, size_pt, bold, width_in)) for p in paragraphs)
    return line_count, line_count * line_height_in(size_pt)


def fit_size(paragraphs, width_in, height_in, base_pt, bold=False,
             floor_pt=8.0, extra_gap_pt=0.0):
    """Largest size at or below *base_pt* (0.5 pt steps) that fits the box."""
    size = base_pt
    while size > floor_pt:
        lines, height = measure(paragraphs, size, bold, width_in)
        if height + (lines - 1) * extra_gap_pt / 72.0 <= height_in:
            return size
        size -= 0.5
    return floor_pt
