# AGENTS.md

Instructions for AI agents working in this repository. Read this file, then
`DESIGN_LOG.md`, before changing anything.

## Start here

1. Read `DESIGN_LOG.md`. It is the source of truth for design intent, constraints and
   what was actually verified, and it is **append-only**: add new entries at the bottom,
   never rewrite or reorder old ones.
2. Verify repository state instead of trusting it — `git status`, `git log`, and the
   files themselves. A log entry records the state at the time it was written; if it
   contradicts what you observe, stop and ask before acting (that is what entry #6 did).
3. Read `README.md` for what the deck is, the package layout and the commands.

## Ground rules

- Never invent, assume, infer or fabricate information. Only confirmed information is
  fact (DESIGN_LOG.md, Constraints & Decisions).
- Do not guess requirements the repository does not establish, and do not add unrelated
  changes. If a missing answer materially affects the result, stop and ask.
- Keep the change set scoped to the requested task.
- Preserve existing behaviour and conventions unless the task explicitly changes them.
- Report results that were actually produced: quote real command output, state which
  checks ran and which did not, and keep limitations visible. Never claim a check passed
  unverified.

## Project facts

- `presentation.pptx` (18 slides, Vietnamese) is **generated, not hand-edited**. Change
  `src/archive0_deck/` and rebuild; `tests/test_deck.py` fails if the committed artifact
  drifts from the code, so code and artifact are committed together.
- Deck text is authored content. When code is rewritten or generated, string literals
  must stay exactly as they are and be checked against the original (DESIGN_LOG.md #10,
  #13: a rename that reached inside string literals corrupted Vietnamese slide text and
  was caught only by comparing the built deck with the committed one).
- PowerPoint work uses **`python-pptx2`** (import name `pptx2`); `python-pptx` is not a
  dependency. Deprecation warnings are errors (`pyproject.toml`), so pptx2 deprecations
  must be fixed, not silenced.
- Conventions that keep the package coherent: page numbers and slide order come from
  `sections.SECTION_BUILDERS`; deck metadata strings live in `builder.py`; palette and
  geometry in `theme.py`; text measurement has exactly one implementation,
  `typography.py`, shared by the builder and the preview renderer.
- `preview.py` is a geometry mock, not a renderer. Never describe its output as a
  PowerPoint render, and do not claim render-level verification: no PowerPoint engine is
  available in this environment (DESIGN_LOG.md #5, #10).
- The deck reports the 2025 admission cycle only, and keeps name/class/date and the joke
  as marked placeholders because the user did not supply them. Do not fill these in.
- The ISO/IEC 29500-4 schemas are **not vendored**; schema validation is opt-in through
  the `ARCHIVE0_OOXML_XSD` environment variable.

## Checks to run before reporting work complete

See `README.md` for environment setup. From the repository root:

```bash
python -m pytest                                     # full suite
python -m archive0_deck build --out presentation.pptx  # regenerate the tracked artifact
python -m archive0_deck verify presentation.pptx       # structure always, schema if enabled
ARCHIVE0_OOXML_XSD=<schema-dir> python -m archive0_deck verify presentation.pptx
```

- `verify` always performs the structural checks (zip, relationships, content types,
  slide element order, time-node ids, animation targets) and adds schema validation when
  a schema directory containing `pml.xsd` is supplied. Without it, the schema test skips.
- There is no CI, no configured linter and no formatter in this repository; checks are
  run locally by hand. Match the surrounding code: module docstrings, docstrings on
  public functions, and lines wrapped near 100 columns (long string literals excepted).
- Changes are delivered as a pull request against `main`.

## Keep the design log current

Append a `DESIGN_LOG.md` entry (next number, dated, typed `INTENT` / `DECISION` / `DONE` /
`NOTE` / `CONTRADICTION`) when a task introduces a material decision, constraint,
limitation or verified change in project state. `INTENT` quotes the user's own words;
the other types record what was checked and how, not what was hoped for. Keep it short,
and never edit an existing entry.
