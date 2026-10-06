"""The animation timing written into each slide."""

import re
import zipfile

from lxml import etree

from archive0_deck import animation

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


def slide_xml(deck_path, number):
    with zipfile.ZipFile(deck_path) as archive:
        return archive.read(f"ppt/slides/slide{number}.xml").decode()


def test_no_effects_and_no_timing_when_a_slide_is_empty():
    assert animation.build_timing_xml([]) is None


def test_timing_has_a_single_reveal_group():
    xml = etree.tostring(animation.build_timing_xml(
        [(2, animation.FADE), (3, animation.WIPE_UP)]), encoding="unicode")
    assert animation.build_timing_xml([(2, animation.FADE)]).tag == P + "timing"
    delays = re.findall(r'presetClass="entr"[^>]*>\s*<p:stCondLst><p:cond delay="(\d+)"', xml)
    assert delays == ["0", str(animation.STAGGER_MS)]


def test_time_node_ids_are_unique():
    xml = etree.tostring(animation.build_timing_xml(
        [(n, animation.FADE) for n in range(2, 30)]), encoding="unicode")
    ids = re.findall(r'<p:cTn id="(\d+)"', xml)
    assert len(ids) == len(set(ids))


def test_delays_are_capped():
    count = 60
    xml = etree.tostring(animation.build_timing_xml(
        [(n, animation.FADE) for n in range(2, 2 + count)]), encoding="unicode")
    delays = [int(d) for d in re.findall(r'<p:cond delay="(\d+)"/>', xml)]
    assert max(delays) == animation.MAX_DELAY_MS


def test_every_slide_has_effects_and_a_fade_transition(deck_path):
    for number in range(1, 19):
        xml = slide_xml(deck_path, number)
        assert "<p:transition" in xml and "<p:fade/>" in xml, f"slide {number}: no transition"
        assert xml.count('presetClass="entr"') > 0, f"slide {number}: no entrance effects"


def test_animation_targets_resolve_to_real_shapes(deck_path):
    for number in range(1, 19):
        xml = slide_xml(deck_path, number)
        shape_ids = set(re.findall(r'<p:cNvPr id="(\d+)"', xml))
        targets = set(re.findall(r'<p:spTgt spid="(\d+)"/>', xml))
        assert targets, f"slide {number}: animation without targets"
        assert targets <= shape_ids, f"slide {number}: unknown targets {targets - shape_ids}"
