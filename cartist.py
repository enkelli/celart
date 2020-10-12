#!/usr/bin/env python3

import argparse
import sys

from cartist import Artist
from cartist.cli import CLIArtist
from cartist.rules import DEFAULT_RULE_SET
from cartist.rules import get_rule_set_from_csv


def parse_args(args):
    """Parses input arguments."""

    parser = argparse.ArgumentParser(description='Draws amazing cellular automata.')
    parser.add_argument(
        '-r',
        '--rule-set',
        metavar='FILE',
        nargs=1,
        dest='rule_set',
        help='CSV file with rule set.',
    )
    parser.add_argument(
        metavar='NUMBER',
        dest='number',
        type=int,
        nargs='?',
        default=25,
        help='Number to be squared (default: %(default)s)',
    )

    run_type = parser.add_mutually_exclusive_group()
    run_type.add_argument(
        '-c', '--cli', action='store_true', dest='cli', help='Run CLI version only.'
    )
    run_type.add_argument(
        '-s',
        '--sqrt-only',
        action='store_true',
        dest='sqrt_only',
        help='Prints only sqrt of the given number (computed with the given rule set)',
    )

    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args if args else sys.argv[1:])
    rule_set = DEFAULT_RULE_SET
    try:
        if args.rule_set:
            rule_set = get_rule_set_from_csv(args.rule_set[0])
    except Exception as ex:
        print(ex)
        sys.exit(1)

    if args.sqrt_only:
        artist = Artist(args.number, rule_set)
    elif args.cli:
        artist = CLIArtist(args.number, rule_set)
    else:
        try:
            from cartist.gui import GUIArtist
            artist = GUIArtist(args.number, rule_set)
        except ImportError:
            print('tkinter not installed, falling back to CLI...\n')
            artist = CLIArtist(args.number, rule_set)

    artist.paint()


if __name__ == '__main__':
    main()
