"""Helpers for comparing two decks at the level of content we author.

Library boilerplate (templates, themes, package metadata) differs between
python-pptx and python-pptx2, so comparisons look at slides, shapes, text, notes
and entrance effects only.
"""

EMU_PER_INCH = 914400


def _shape_entry(shape):
    return {
        "type": str(shape.shape_type),
        "box": (round(shape.left / EMU_PER_INCH, 4), round(shape.top / EMU_PER_INCH, 4),
                round(shape.width / EMU_PER_INCH, 4), round(shape.height / EMU_PER_INCH, 4)),
        "text": [run.text for paragraph in shape.text_frame.paragraphs
                 for run in paragraph.runs] if shape.has_text_frame else [],
    }


def deck_content(presentation):
    """Per-slide summary of authored content."""
    slides = []
    for slide in presentation.slides:
        xml = slide._element.xml
        slides.append({
            "shapes": [_shape_entry(shape) for shape in slide.shapes],
            "text": [run.text for shape in slide.shapes if shape.has_text_frame
                     for paragraph in shape.text_frame.paragraphs
                     for run in paragraph.runs],
            "notes": (slide.notes_slide.notes_text_frame.text
                      if slide.has_notes_slide else ""),
            "entrance_effects": xml.count('presetClass="entr"'),
            "has_transition": "<p:transition" in xml,
        })
    return slides
