"""Package validation and the preview renderer."""

import zipfile

import pytest

from archive0_deck import preview, validation


def test_package_is_structurally_valid(deck_path):
    report = validation.validate_package(deck_path)
    assert report["zip_ok"]
    assert report["bad_relationships"] == []
    assert report["uncovered_parts"] == []
    assert report["duplicate_time_node_ids"] == []
    assert report["dangling_animation_targets"] == []
    assert all(report["element_order"].values())
    assert validation.is_valid(report)


def test_slides_carry_markup_compatibility_attributes(deck_path):
    """python-pptx2 writes mc:Ignorable, so validation has to be MC-aware."""
    with zipfile.ZipFile(deck_path) as archive:
        assert "mc:Ignorable" in archive.read("ppt/slides/slide1.xml").decode()
    report = validation.validate_package(deck_path)
    assert report["mc_attributes_stripped"] >= 1


def test_schema_validation_when_schemas_are_available(deck_path, schema_dir):
    if schema_dir is None:
        pytest.skip(f"set {validation.SCHEMA_ENV_VAR} to validate against the ISO schemas")
    report = validation.validate_package(deck_path, schema_dir)
    assert report["schema_checked"]
    assert validation.is_valid(report), validation.format_report(report)


def test_strip_mc_attributes_is_idempotent(deck_path):
    from lxml import etree
    with zipfile.ZipFile(deck_path) as archive:
        document = etree.fromstring(archive.read("ppt/slides/slide1.xml"))
    assert validation.strip_mc_attributes(document) >= 1
    assert validation.strip_mc_attributes(document) == 0


def test_previews_render_without_overflow(deck):
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as directory:
        paths, issues = preview.render_previews(deck.manifest, Path(directory))
        assert len(paths) == len(deck.slides)
        assert issues == [], "text overflows its box:\n" + "\n".join(issues)
        assert all(path.is_file() for path in paths)

        sheet = preview.render_contact_sheet(paths, Path(directory) / "sheet.png")
        assert sheet.is_file()


def test_manifest_matches_the_slide_count(deck):
    manifest = deck.manifest
    assert [entry["page"] for entry in manifest] == [slide.number for slide in deck.slides]
    assert all(entry["shapes"] for entry in manifest), "every slide draws something"


def test_element_order_check_rejects_wrong_order():
    assert validation._ordered(["cSld", "clrMapOvr", "transition", "timing"])
    assert not validation._ordered(["cSld", "timing", "transition"])
    assert not validation._ordered(["clrMapOvr", "cSld"])
