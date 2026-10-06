"""archive0_deck -- the presentation in this repository, built with python-pptx2.

The deck ("Tuyển sinh lớp 10 năm 2025 tại Việt Nam") is generated from code:
:mod:`archive0_deck.sections` holds the content, :mod:`archive0_deck.layout` the
drawing primitives, :mod:`archive0_deck.animation` the entrance effects, and
:mod:`archive0_deck.validation` / :mod:`archive0_deck.preview` verify the result.

Typical use::

    from archive0_deck import build_deck

    deck = build_deck()
    deck.save("presentation.pptx")
"""

from .builder import DECK_TITLE, build_deck
from .layout import Deck, Slide
from .preview import render_contact_sheet, render_previews, render_slide
from .validation import format_report, is_valid, validate_package

__all__ = [
    "DECK_TITLE",
    "Deck",
    "Slide",
    "build_deck",
    "format_report",
    "is_valid",
    "render_contact_sheet",
    "render_previews",
    "render_slide",
    "validate_package",
]
