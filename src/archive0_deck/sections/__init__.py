"""Slide content, one module per topic group.

Each module exposes ``build(deck)``, which appends its slides in order. The order
of :data:`SECTION_BUILDERS` is the order of the deck, and slide numbers follow
from it, so nothing here hard-codes a page number.
"""

from . import closing, localities, national, opening, rules, scoring

SECTION_BUILDERS = (
    opening,
    rules,
    national,
    localities,
    scoring,
    closing,
)


def build_all(deck):
    """Append every section's slides to *deck*, in order."""
    for section in SECTION_BUILDERS:
        section.build(deck)
    return deck
