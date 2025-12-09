#!/usr/bin/env python

import argparse
import sys

BEAM = "|"
SPLITTER = "^"
START = "S"
EMPTY = "."


def _fall(pos: int, line_no: int, lines: list[str]) -> int:
    # Base case
    if line_no == len(lines):
        return 1

    line = lines[line_no]
    ch = line[pos]

    if ch == SPLITTER:
        return _fall(pos - 1, line_no + 1, lines) + _fall(pos + 1, line_no + 1, lines)

    return _fall(pos, line_no + 1, lines)


def main(args) -> int | None:
    lines = []
    with open(args.file, "r") as f:
        lines = f.read().rstrip().split("\n")

    start = lines[0].index(START)
    print(_fall(start, 1, lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
