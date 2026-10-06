"""The deck's content contract: what the presentation must contain."""

from pptx2 import Presentation

from tests.compare import deck_content

SLIDE_COUNT = 18
SECTION_KICKERS = ("NỘI DUNG", "PHẦN 01", "PHẦN 02", "PHẦN 03", "PHẦN 04",
                   "PHẦN 05", "GIẢI LAO", "MINH BẠCH")
JOKE_PLACEHOLDER = "[Dán câu joke của bạn vào đây]"
# slides that state rules or figures; each must say where the fact comes from
FACT_SLIDES = tuple(range(3, 15)) + (16, 17)
SOURCE_MARKERS = ("Nguồn", "Điều ", "Thông tư", "Sở GD")


def slide_texts(deck_file):
    presentation = Presentation(str(deck_file))
    return [[run.text for shape in slide.shapes if shape.has_text_frame
             for paragraph in shape.text_frame.paragraphs for run in paragraph.runs]
            for slide in presentation.slides]


def test_slide_count(deck_path):
    assert len(Presentation(str(deck_path)).slides) == SLIDE_COUNT


def test_slide_numbers_are_sequential(deck):
    assert [slide.number for slide in deck.slides] == list(range(1, SLIDE_COUNT + 1))


def test_every_slide_has_notes(deck_path):
    presentation = Presentation(str(deck_path))
    without = [number for number, slide in enumerate(presentation.slides, start=1)
               if not slide.notes_slide.notes_text_frame.text.strip()]
    assert without == [], f"slides without speaker notes: {without}"


def test_page_numbers_on_every_slide_except_the_title(deck_path):
    texts = slide_texts(deck_path)
    assert "01" not in texts[0], "the title slide shows no page number"
    for number, runs in enumerate(texts[1:], start=2):
        assert f"{number:02d}" in runs, f"slide {number} has no page number"


def test_all_section_kickers_present(deck_path):
    joined = "\n".join(run for runs in slide_texts(deck_path) for run in runs)
    for kicker in SECTION_KICKERS:
        assert kicker in joined, f"missing kicker {kicker!r}"


def test_joke_slide_keeps_an_editable_placeholder(deck_path):
    assert any(JOKE_PLACEHOLDER in runs for runs in slide_texts(deck_path))


def test_sources_slide_lists_sources(deck_path):
    joined = "\n".join(slide_texts(deck_path)[16])
    for expected in ("Thông tư 30/2024/TT-BGDĐT", "VnExpress", "Tuổi Trẻ"):
        assert expected in joined, f"{expected!r} missing from the sources slide"


def test_facts_carry_sources(deck_path):
    texts = slide_texts(deck_path)
    for number in FACT_SLIDES:
        joined = "\n".join(texts[number - 1])
        assert any(marker in joined for marker in SOURCE_MARKERS), \
            f"slide {number} cites no source"


def test_unfilled_personal_fields_stay_bracketed(deck_path):
    """The user never supplied a name, class or date, so none is invented."""
    title_slide = "\n".join(slide_texts(deck_path)[0])
    for placeholder in ("[Tên của bạn]", "[Lớp]", "[Ngày]"):
        assert placeholder in title_slide


def test_deck_covers_only_the_2025_cycle(deck_path):
    joined = "\n".join(run for runs in slide_texts(deck_path) for run in runs)
    for next_cycle_fact in ("năm học 2026", "2026-2027", "2026–2027", "năm 2026"):
        assert next_cycle_fact not in joined


def test_regenerated_deck_matches_the_committed_artifact(deck_path, committed_deck):
    """The committed .pptx is exactly what this code produces (no drift)."""
    committed = deck_content(Presentation(str(committed_deck)))
    regenerated = deck_content(Presentation(str(deck_path)))
    assert len(committed) == len(regenerated)
    for number, (expected, actual) in enumerate(zip(committed, regenerated), start=1):
        assert actual["text"] == expected["text"], f"slide {number}: text differs"
        assert actual["notes"] == expected["notes"], f"slide {number}: notes differ"
        assert actual["shapes"] == expected["shapes"], f"slide {number}: shapes differ"
        assert actual["entrance_effects"] == expected["entrance_effects"], \
            f"slide {number}: entrance effects differ"
        assert actual["has_transition"] == expected["has_transition"], \
            f"slide {number}: transition differs"


def test_core_properties_match_the_committed_artifact(deck_path, committed_deck):
    """File properties are part of the artifact (title, subject, comments)."""
    regenerated = Presentation(str(deck_path)).core_properties
    committed = Presentation(str(committed_deck)).core_properties
    for field in ("title", "subject", "comments", "author", "last_modified_by"):
        assert getattr(regenerated, field) == getattr(committed, field), field
