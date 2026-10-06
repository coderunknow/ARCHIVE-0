"""Shared fixtures: the deck is built once per session, not per test."""

import os
from pathlib import Path

import pytest

from archive0_deck import build_deck

REPO_ROOT = Path(__file__).resolve().parents[1]
COMMITTED_DECK = REPO_ROOT / "presentation.pptx"


@pytest.fixture(scope="session")
def deck():
    return build_deck()


@pytest.fixture(scope="session")
def deck_path(deck, tmp_path_factory):
    """The deck under test, written to a temporary file."""
    path = tmp_path_factory.mktemp("deck") / "presentation.pptx"
    deck.save(path)
    return path


@pytest.fixture(scope="session")
def schema_dir():
    """Directory with the ISO/IEC 29500-4 schemas, or None when unavailable.

    Set ``ARCHIVE0_OOXML_XSD`` to a directory containing ``pml.xsd`` (and the
    ``dml-*.xsd`` / ``shared-*.xsd`` files it imports) to enable schema checks.
    """
    directory = os.environ.get("ARCHIVE0_OOXML_XSD")
    if not directory:
        return None
    path = Path(directory)
    return path if (path / "pml.xsd").is_file() else None


@pytest.fixture(scope="session")
def committed_deck():
    if not COMMITTED_DECK.is_file():        # pragma: no cover - repo invariant
        pytest.skip("presentation.pptx is not present")
    return COMMITTED_DECK
