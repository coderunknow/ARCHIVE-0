"""Assemble the full deck.

The slide content itself lives in :mod:`archive0_deck.sections`, one module per
topic group, so this module only wires the parts together.
"""

from .layout import Deck
from .sections import build_all

DECK_TITLE = "Tuyển sinh lớp 10 năm 2025 tại Việt Nam"
DECK_SUBJECT = "Thông tin tuyển sinh lớp 10 năm 2025 (kỳ thi 2025)"
DECK_COMMENTS = ("Dữ liệu kỳ thi năm 2025. Nguồn được ghi trên slide 'Nguồn tham khảo' "
                 "và trong ghi chú của từng slide.")
DECK_FOOTER = "Tuyển sinh lớp 10 · Việt Nam · 2025 — số liệu kỳ thi năm 2025"


def build_deck():
    """Build the presentation and return the :class:`~archive0_deck.layout.Deck`."""
    deck = Deck(title=DECK_TITLE, subject=DECK_SUBJECT, comments=DECK_COMMENTS,
                footer=DECK_FOOTER)
    build_all(deck)
    return deck
