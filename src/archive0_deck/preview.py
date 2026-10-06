"""Preview renderer.

Draws every slide from the deck manifest so the composition can be eyeballed and
text overflow detected without a PowerPoint installation. It is a geometry mock,
not a PowerPoint engine render: it uses the same boxes, colours and font sizes as
the deck, and the same wrapping code as the builder
(:mod:`archive0_deck.typography`).
"""

from pathlib import Path

from PIL import Image, ImageDraw

from . import theme, typography

SCALE = 140          # pixels per inch
_MARGIN = 4          # padding between thumbnails in the contact sheet


def _px(value):
    return int(round(value * SCALE))


def _draw_rect(draw, shape):
    x, y, w, h = shape["x"], shape["y"], shape["w"], shape["h"]
    radius = min(_px(w), _px(h)) // 2 if shape.get("radius") else 0
    radius = min(radius, _px(min(w, h)) // 2)
    draw.rounded_rectangle([_px(x), _px(y), _px(x + w), _px(y + h)],
                           radius=radius, fill="#" + shape["fill"])


def _draw_text(draw, shape):
    margin = shape.get("margin", 0.06)
    inner_width = _px(shape["w"] - 2 * margin)
    line_gap = shape.get("space_after", 6) / 72.0 * SCALE

    blocks = []
    total_height = 0.0
    for paragraph in shape["paras"]:
        size_pt, bold = paragraph["size"], paragraph["bold"]
        lines = typography.wrap(paragraph["text"], size_pt, bold,
                                max(inner_width, 1) / SCALE)
        line_height = typography.line_height_in(size_pt) * SCALE
        blocks.append((lines, size_pt, bold, paragraph["color"], line_height))
        total_height += len(lines) * line_height + line_gap
    if blocks:
        total_height -= line_gap

    cursor_y = _px(shape["y"]) + _px(0.02)
    if shape["anchor"] == "middle":
        cursor_y = _px(shape["y"]) + (_px(shape["h"]) - total_height) / 2
    elif shape["anchor"] == "bottom":
        cursor_y = _px(shape["y"]) + _px(shape["h"]) - total_height

    for lines, size_pt, bold, color, line_height in blocks:
        font = typography.render_font(round(size_pt * SCALE / 72.0), bold)
        for line in lines:
            width = draw.textlength(line, font=font)
            if shape["align"] == "center":
                x = _px(shape["x"]) + (_px(shape["w"]) - width) / 2
            elif shape["align"] == "right":
                x = _px(shape["x"] + shape["w"] - margin) - width
            else:
                x = _px(shape["x"] + margin)
            draw.text((x, cursor_y), line, font=font, fill="#" + color)
            cursor_y += line_height
        cursor_y += line_gap

    overflow = total_height - _px(shape["h"]) > 2
    return overflow


def render_slide(slide):
    """Render one manifest entry; returns ``(image, issues)``."""
    image = Image.new("RGB", (_px(theme.SLIDE_WIDTH), _px(theme.SLIDE_HEIGHT)),
                      "#" + str(theme.BG))
    draw = ImageDraw.Draw(image)
    issues = []
    for shape in slide["shapes"]:
        if shape["type"] == "rect":
            _draw_rect(draw, shape)
        else:
            if _draw_text(draw, shape):
                first = shape["paras"][0]["text"] if shape["paras"] else ""
                issues.append(
                    f"slide {slide['page']:02d}: text overflows its box "
                    f"({shape['h']:.2f}in) :: {first[:60]!r}")
    return image, issues


def render_previews(manifest, out_dir):
    """Write one PNG per slide into *out_dir*; returns ``(paths, issues)``."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths, issues = [], []
    for slide in manifest:
        image, slide_issues = render_slide(slide)
        path = out_dir / f"slide{slide['page']:02d}.png"
        image.save(path)
        paths.append(path)
        issues.extend(slide_issues)
    return paths, issues


def render_contact_sheet(paths, out_path, columns=3):
    """Tile slide previews into a single contact sheet."""
    thumbnails = []
    for path in paths:
        image = Image.open(path)
        thumbnails.append(image.resize((image.width // 4, image.height // 4)))
    if not thumbnails:
        raise ValueError("no previews to tile")
    width, height = thumbnails[0].size
    rows = (len(thumbnails) + columns - 1) // columns
    sheet = Image.new("RGB",
                      (columns * (width + _MARGIN) + _MARGIN,
                       rows * (height + _MARGIN) + _MARGIN),
                      "#222222")
    for index, thumbnail in enumerate(thumbnails):
        row, column = divmod(index, columns)
        sheet.paste(thumbnail, (_MARGIN + column * (width + _MARGIN),
                                _MARGIN + row * (height + _MARGIN)))
    sheet.save(out_path)
    return Path(out_path)
