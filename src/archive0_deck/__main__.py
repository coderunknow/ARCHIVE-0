"""Command line entry points: ``python -m archive0_deck``.

    build   write presentation.pptx (and optionally slide previews)
    verify  validate an existing .pptx (structure, and schema when available)
"""

import argparse
import sys
from pathlib import Path

from .builder import build_deck
from .preview import render_contact_sheet, render_previews
from .validation import SCHEMA_ENV_VAR, format_report, is_valid, validate_package

DEFAULT_OUT = Path("presentation.pptx")


def _build(args):
    deck = build_deck()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    deck.save(args.out)
    print(f"wrote {args.out} ({len(deck.slides)} slides)")

    if args.preview_dir or args.contact_sheet:
        paths, issues = render_previews(deck.manifest, args.preview_dir or "build/preview")
        print(f"wrote {len(paths)} previews to {args.preview_dir or 'build/preview'}")
        if args.contact_sheet:
            render_contact_sheet(paths, args.contact_sheet)
            print(f"wrote contact sheet {args.contact_sheet}")
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        if issues:
            return 1
    return 0


def _verify(args):
    report = validate_package(args.deck, args.xsd)
    print(format_report(report))
    return 0 if is_valid(report) else 1


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m archive0_deck",
                                     description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="build presentation.pptx")
    build.add_argument("--out", type=Path, default=DEFAULT_OUT,
                       help="output .pptx path (default: %(default)s)")
    build.add_argument("--preview-dir", type=Path, default=None,
                       help="also write one PNG per slide into this directory")
    build.add_argument("--contact-sheet", type=Path, default=None,
                       help="also write a contact sheet of all slides")
    build.set_defaults(func=_build)

    verify = subparsers.add_parser("verify", help="validate a .pptx")
    verify.add_argument("deck", type=Path, nargs="?", default=DEFAULT_OUT)
    verify.add_argument("--xsd", type=Path, default=None,
                        help=f"schema directory containing pml.xsd "
                             f"(default: ${SCHEMA_ENV_VAR})")
    verify.set_defaults(func=_verify)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
