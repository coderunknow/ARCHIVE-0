# DESIGN_LOG

> Source of truth for design intent + append-only work log.
> Rules: read before every task; verify against the real project; append new entries, avoid editing old ones.

## Design Intent
(Exact ideas from the user, in their own words. Add bullets; do not silently reword.)

- "you should have file powerpoint can be imported instantly in power point."
- Task given by the user: create a complete PowerPoint presentation "based **only on verified requirements and available project context**", validate it, commit the changes, push the branch, and open a Pull Request.
- Presentation topic: (not yet specified)
- Target audience: (not yet specified)
- Presentation duration / required number of slides: (not yet specified)
- Required slide structure or mandatory content: (not yet specified)
- Visual style / template: (not yet specified)
- Language of the presentation: (not yet specified)
- Required output filename and location: (not yet specified)

## Constraints & Decisions

- User (verbatim): "Never invent, assume, infer, or fabricate information that has not been explicitly provided or verified."
- Do not assume topic, audience, duration, slide count, grading criteria, teacher expectations, visual style, facts, filenames, branch names, directory structure, PR requirements or presentation structure.
- If important information is missing: stop the dependent work and ask a specific, concise question.
- Only confirmed information may be treated as fact.
- Keep the change set scoped to the task; do not modify unrelated files.
- Repository: `coderunknow/ARCHIVE-0`; working branch `arena/5f5c7ee0-archive-0` (this session is fixed to it); base branch `main`.
- This log is append-only.

## Log
<!-- Append new entries below. Do not edit old entries. -->

### #1 — 2026-10-06 — NOTE
Log created (it did not exist). Project state at creation, verified:
- Working tree clean on branch `arena/5f5c7ee0-archive-0` (branched from `main`).
- Single commit: `f106c1e` "Initial commit" — contains only `README.md` (content: `# ARCHIVE-0`), 1 file, 1 line.
- `git ls-files` and a full `find` of the working tree show no other files: no assets, templates, docs, requirements, presentation files, contribution guide, workflows or PR templates.
- Remote: `https://github.com/coderunknow/ARCHIVE-0.git`; only remote branch is `main` at `f106c1e`; no existing pull requests or issues.
- Conclusion: the repository provides no verified information about the presentation (no topic, audience, slide count, style, filename or structure). Those items must be obtained from the user before a presentation is generated.

### #2 — 2026-10-06 — INTENT
User answered the six blocking questions (repository had no presentation context at all):
- Topic (verbatim): "2025 Grade 10 Admissions Information in Vietnam."
- Audience: school track chosen — "School / university class".
- Length: "16+ slides / as many as needed".
- Language (verbatim): "Vietnam and Common English words used by young people (do not overuse english)."
- Output (verbatim): "root" and "you should have file powerpoint can be imported instantly in power point."
- Style (verbatim): "fun, badass and I can add my own joke without edit the construction too much. Many clean and smooth animation, high quality."

### #3 — 2026-10-06 — DECISION
- Facts are limited to the 2025 admission cycle (exam year 2025 / school year 2025–2026); every fact carries a source, and 2026-cycle articles were deliberately excluded even when they appeared in search results.
- Because the user did not provide a name/class/date or a joke, those appear as clearly marked placeholders: "[Tên của bạn] · [Lớp] · [Ngày]" on slide 1, and "[Dán câu joke của bạn vào đây]" on slide 16. No personal data was invented.
- "Fun/badass" style implemented as a dark electric theme; "can add my own joke without edit the construction too much" implemented as a dedicated joke slide with a ready-made, directly editable text box.
- Animations: one reveal group per slide, auto-start, 380 ms entrance effects (Fade for text, Wipe-up for bars/KPI numbers), 90 ms stagger capped at 2.2 s.

### #4 — 2026-10-06 — DONE
Created `presentation.pptx` (18 slides, 16:9, Vietnamese with light English; speaker notes on all 18 slides; content sources slide + per-slide source footnotes).
Verified:
- Schema validation: all 18 `ppt/slides/slideN.xml` + `ppt/presentation.xml` validate against the official ISO/IEC 29500-4 (Transitional) presentationML schema (`pml.xsd` etc., fetched via GitHub API), including the hand-authored `<p:timing>` animation XML and `<p:transition>`.
- Structural checks: zip integrity OK; element order (`cSld` → `clrMapOvr` → `transition` → `timing`); no duplicate `timeNode` ids; every animation target resolves to an existing shape id; all relationship targets and content-type overrides resolve.
- Text fitting: conservative DejaVu-based measurement for every text box -> 0 overflow flags across all 18 slides.
- Visual check: per-slide previews rendered from the build manifest (geometry/colour/font-size faithful) and inspected, plus a contact sheet of all 18 slides; text was corrected where it was too dense (e.g. slide 13).
- Terminology/number consistency cross-checked between slides (Hà Nội 79.740/127.000+/7–8/6; TP.HCM 70.070/76.435/6–7/6; Cần Thơ 11.057/5–6/6).

### #5 — 2026-10-06 — NOTE
Limitations, stated honestly:
- No PowerPoint or LibreOffice engine was available in this sandbox (apt mirrors and LibreOffice download hosts are blocked; Aspose.Slides requires libgdiplus, which is unavailable), so the deck was NOT rendered by a PowerPoint-compatible engine. Visual verification used a geometry mock render + ISO schema validation + package integrity checks instead.
- Animation preset *labels* in PowerPoint's Animation Pane may differ slightly from PowerPoint's own defaults (the entrance filter strings and structure follow a PowerPoint-authored reference; presetID/presetSubtype values were chosen to match the same effects).
- Facts are accurate as published for the 2025 cycle; later cycles (e.g. 2026) differ and were intentionally excluded.

### #6 — 2026-10-06 — CONTRADICTION
Task premise vs. verified repository state.
- Task statement says: "You are working on an existing repository that currently contains or is based on `python-pptx`", and asks to transform it into `python-pptx2` with a substantial internal refactor.
- What the repository actually contains (verified): `README.md` (12 bytes: `# ARCHIVE-0`), `DESIGN_LOG.md` and `presentation.pptx` (both added by entry #4). Full history across all refs is 2 commits / 3 files. There is **no Python code at all**: no modules, no `setup.py`/`pyproject.toml`, no package layout, no tests, no docs, no tooling config.
- GitHub metadata (verified): `coderunknow/ARCHIVE-0` is **not a fork**, `parent: null`, no description, `diskUsage: 0`; branches are only `main` and `arena/5f5c7ee0-archive-0`; the only PR is #1 (the presentation deck).
- `python-pptx` exists in this environment only as an installed third-party package in `/tmp/pptxenv` (`python-pptx 1.0.2`), used as a build dependency for entry #4. Upstream `scanny/python-pptx` is a different repository (default branch `master`).
- Conclusion: there is nothing in this repository to rename or refactor, and the repository contains no evidence that can answer the refactor's architectural questions (base version/commit, history policy, supported Python versions, compatibility promise, module boundaries to change).
- Action taken: stopped before making any architectural decision and asked the user (per the task's rule 1 and the "stop and ask" conditions). No files other than this log entry were touched.

### #7 — 2026-10-06 — INTENT
User's answer to the contradiction raised in #6 (verbatim, custom response):
"The project currently uses the existing `python-pptx` library.  Migrate the project to the existing `python-pptx2` library and refactor the project's PowerPoint-related code to use it cleanly.  Use the existing `python-pptx2` package rather than creating your own version of the library. Refactor the current code as needed to work naturally with `python-pptx2`, while preserving the project's existing behavior where practical.  Do not add unrelated changes or make assumptions about requirements that are not clear from the repository.  Add or update tests where appropriate, run the relevant checks, perform a final verification, and update the pull request with the actual results before considering the work complete."
- Also chosen: reuse PR #1 for this work (no new PR).
- Consequence: the project's own package is NOT called python-pptx2 — `python-pptx2` is the library we depend on (PyPI `python-pptx2` 3.2.0, import name `pptx2`). This project's package is `archive0_deck` (distribution `archive0-deck`).

### #8 — 2026-10-06 — DONE
Migrated the project's PowerPoint code (the deck builder from #4, which had never been committed) into a structured package that uses `python-pptx2` 3.2.0, and regenerated the artifact.
- New package `src/archive0_deck/`: `theme` (palette/fonts/geometry), `typography` (single measurement implementation), `animation` (timing + transition XML), `layout` (`Deck`/`Slide` primitives), `sections/` (6 content modules, 18 slides), `builder`, `preview`, `validation`, `__main__` CLI (`build` / `verify`).
- Structural fixes: the 815-line top-level script became focused modules; the global mutable `manifest` and the file-based `manifest.json` contract replaced by `Deck.manifest`; `Slide._text` private API renamed to `text`; `theme._font` leak replaced by `typography.text_width_in`/`render_font`; duplicated wrap/font code in the preview renderer removed (it now shares `typography`); page numbers derived from insertion order instead of hard-coded; dead `fmt_pt`, unused `Emu` import and unused `FLOAT_UP` preset removed; 85 ignored `delay=`/`dur=` arguments dropped from sections and from the primitive signatures (the timing builder derives stagger from reveal order).
- pptx2 specifics: `shadow.inherit = False` (deprecated in pptx2) replaced by `shadow.clear()`; validation made Markup-Compatibility aware because pptx2 writes `mc:Ignorable` on every slide part (plain XSD validation reports those parts as invalid).
- Added `pyproject.toml` (package metadata, `python-pptx2>=3.2.0` dependency, pytest config with `filterwarnings = error::DeprecationWarning`), `.gitignore`, tests and a README describing the layout and commands.

### #9 — 2026-10-06 — DONE
Verification actually performed (all commands run after the refactor):
- `pip install -e .` succeeds; `python -m archive0_deck build` writes 18 slides.
- Content equivalence vs the artifact committed in #4 (built with python-pptx 1.0.2): 0 differences across all 18 slides — same shapes, geometry, text, font sizes/bold/colours, notes.
- Animation equivalence vs that same artifact: identical per-slide delay sequences and filters, 262 entrance effects in both, transitions on all 18 slides.
- Schema validation: 19/19 parts valid (18 slides + presentation.xml) against the ISO/IEC 29500-4 schemas, with MC attributes stripped (18 stripped).
- Structural checks: zip integrity OK, no broken relationships, no uncovered parts, no duplicate time-node ids, no dangling animation targets (111 parts).
- `python -m pytest`: 33 passed (content contract incl. drift test against the committed artifact, animation, typography, validation, preview).
- `pyflakes src/archive0_deck tests`: clean.
- Preview render of the regenerated deck: 18 PNGs + contact sheet, 0 overflow flags, visually inspected and identical to the #4 deck.
- `presentation.pptx` regenerated with python-pptx2 and committed (117,849 bytes, was 116,276 bytes built with python-pptx 1.0.2).

### #10 — 2026-10-06 — NOTE
Limitations and deliberate non-changes:
- Still no PowerPoint-compatible renderer in this sandbox (apt mirrors and LibreOffice download hosts blocked), so the deck is not engine-rendered; verification uses the geometry preview plus schema/package checks and content/timing comparison against the previously committed artifact.
- Deliberately unchanged: slide content, wording, figures, geometry, colours, fonts, animation timings, the placeholder text (name/class/date, joke frame) and the append-only history in this log. The section modules were generated from the #4 code and every string literal was checked to be preserved (the generator asserted literal preservation; the only two dropped literals are the old `s.title = "Title"` / `s.title = "Cảm ơn"` manifest labels, replaced by the `label=` argument).
- Citation text was left as content rather than being refactored into a citation registry: the notes and the sources slide use different wording per entry, so unifying them would have changed the user-visible text.
- `preview.py` remains a geometry mock, not a renderer; the ISO schemas are not vendored into the repository (validation uses `ARCHIVE0_OOXML_XSD` when provided).

### #11 — 2026-10-06 — INTENT
User request (verbatim): "Add an `AGENTS.md` file at the repository root to provide persistent instructions for AI agents working on this project." — with the requirements that it be based only on information explicitly present or verified in the repository, stay concise and practical, not duplicate `README.md`/`DESIGN_LOG.md`, not become an implementation plan, and be reviewed against the real repository afterwards. Same message (verbatim, closing): "update the PR again (required, merge and tag release v0.1.0."

### #12 — 2026-10-06 — DONE
`AGENTS.md` added at the repository root and reviewed against the working tree.
- Checked before writing: no existing agent instructions in the repository (no `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/`, `.github/` or `CONTRIBUTING.md`); the only standing rules were the header and Constraints section of this log, which `AGENTS.md` references instead of restating.
- Every statement in the file was verified against the repository or this log: the build/test commands (run: 32 passed + 1 skipped without schemas, 33 passed with them), `pyflakes src tests` clean, the artifact regenerated byte-identically, the absence of CI/linter/formatter/pre-commit configuration, `python-pptx2` as the only PowerPoint dependency, the drift tests in `tests/test_deck.py`, and the `ARCHIVE0_OOXML_XSD` opt-in.
- One draft claim was corrected during the review: it cited #10 for a string-literal corruption that #10 does not record, so the lesson is recorded here instead (below) and the citation fixed.

### #13 — 2026-10-06 — NOTE
Lesson recorded for future agents, verified in this session's migration: rewriting code with an automated identifier rename that reaches inside string literals silently changes authored deck text (`TP.HCM` → `FADE.HCM`, `TP Cần Thơ` → `FADE Cần Thơ`; 11 differences across slides 9–11 and 17). It was caught only by comparing a freshly built deck against the committed one. The reliable practice is to rewrite `tokenize` NAME tokens only (never `STRING` tokens) and to assert that the set of string literals is preserved; any content difference other than 0 blocks a commit.
