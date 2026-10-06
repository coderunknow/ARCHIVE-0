"""Text measurement and fitting."""

import pytest

from archive0_deck import typography


def test_measure_counts_wrapped_lines():
    lines, height = typography.measure(["word " * 40], 12, False, 2.0)
    assert lines > 1
    assert height == pytest.approx(lines * 12 * 1.26 / 72.0)


def test_long_words_are_not_split():
    assert typography.wrap("a" * 200, 12, False, 3.0) == ["a" * 200]


def test_empty_text_still_occupies_one_line():
    assert typography.wrap("", 12, False, 3.0) == [""]


def test_more_text_never_measures_shorter():
    short = typography.measure(["một hai ba"], 12, False, 3.0)[1]
    long = typography.measure(["một hai ba " * 20], 12, False, 3.0)[1]
    assert long >= short


def test_fit_size_shrinks_to_fit_and_never_below_the_base():
    assert typography.fit_size(["x"], 4.0, 1.0, 14) == 14
    fitted = typography.fit_size(["nhiều chữ " * 40], 2.0, 0.5, 14)
    assert fitted < 14


def test_fit_size_never_exceeds_the_box():
    paragraphs = ["một đoạn văn bản dài để buộc phải thu nhỏ " * 6]
    width, height = 3.0, 1.2
    size = typography.fit_size(paragraphs, width, height, 16)
    assert typography.measure(paragraphs, size, False, width)[1] <= height + 1e-9


def test_text_width_grows_with_content_and_size():
    narrow = typography.text_width_in("abc", 12, True)
    assert typography.text_width_in("abcdef", 12, True) > narrow
    assert typography.text_width_in("abc", 24, True) > narrow


def test_bold_text_is_wider_than_regular():
    assert typography.text_width_in("Điểm xét tuyển", 12, True) > \
        typography.text_width_in("Điểm xét tuyển", 12, False)
