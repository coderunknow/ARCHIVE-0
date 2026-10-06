# ARCHIVE-0

The presentation in this repository — **“Tuyển sinh lớp 10 năm 2025 tại Việt Nam”**
(18 slides) — is generated from code, and this code is also how the deck is
verified. The PowerPoint work is done with
[**python-pptx2**](https://pypi.org/project/python-pptx2/) (import name `pptx2`),
the maintained fork of `python-pptx`.

`presentation.pptx` is the committed artifact produced by this code.

## Requirements

* Python 3.9 or newer (matching the supported versions of python-pptx2)
* `python-pptx2>=3.2.0`, `Pillow`, `lxml` — installed automatically with the package
* the DejaVu fonts, used for text measurement (`fonts-dejavu-core`)

## Install and build

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'

python -m archive0_deck build --out presentation.pptx
```

Optional extras while building:

```bash
python -m archive0_deck build \
    --preview-dir build/preview --contact-sheet build/contact_sheet.png
```

## Verify

```bash
python -m archive0_deck verify presentation.pptx     # structure (+ schema, if available)
python -m pytest                                     # test suite
```

`verify` always checks zip integrity, relationship targets, content-type coverage,
slide element order, unique animation time-node ids and animation targets that
resolve to real shapes. Schema validation against the ISO/IEC 29500-4
presentationML schemas runs when a schema directory is supplied:

```bash
ARCHIVE0_OOXML_XSD=/path/to/schemas python -m archive0_deck verify presentation.pptx
```

The directory must contain `pml.xsd` and the `dml-*.xsd` / `shared-*.xsd` files it
imports. Validation is Markup-Compatibility aware, because python-pptx2 writes
`mc:Ignorable` on every slide part and those attributes are not part of the ISO
schemas.

## Project layout

| Path | Responsibility |
| --- | --- |
| `src/archive0_deck/theme.py` | palette, fonts, slide geometry (pure data) |
| `src/archive0_deck/typography.py` | text measurement and fitting (one implementation, shared with the preview) |
| `src/archive0_deck/animation.py` | entrance-animation timing XML and slide transitions |
| `src/archive0_deck/layout.py` | `Deck` and `Slide` — drawing primitives and sealing a slide |
| `src/archive0_deck/sections/` | slide content, one module per topic group |
| `src/archive0_deck/builder.py` | assembles the deck from its sections |
| `src/archive0_deck/preview.py` | geometry preview renderer (PNG per slide, contact sheet) |
| `src/archive0_deck/validation.py` | package validation (structural and schema) |
| `tests/` | content contract, animation, typography, validation, preview |

Slide numbers come from the insertion order of `sections.SECTION_BUILDERS`, so no
section hard-codes a page number.

## Content notes

The deck reports the **2025** admission cycle (exam year 2025, school year
2025–2026) and deliberately excludes later cycles. Every figure and rule is
attributed on the slide it appears on, and the full list with URLs is on the
sources slide (slide 17) and in the speaker notes of each slide.

Name, class and date on the title slide are left as bracketed placeholders, and
slide 16 is an empty frame for the presenter's own joke: the user did not supply
those, so nothing was invented.

`preview.py` is a geometry mock — it uses the deck's own boxes, colours, font
sizes and wrapping code — so previews are a layout check, not a PowerPoint render.
