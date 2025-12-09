#!/usr/bin/env python

import argparse
import sys

BEAM = "|"
SPLITTER = "^"
START = "S"
EMPTY = "."

paths = set()


def _fall(trace: list[str], line_no: int, lines: list[str]) -> None:
    # Base case -
    if line_no == len(lines) - 1:
        paths.add(" ".join(map(str, trace)))
        return

    line = lines[line_no]
    pos = trace[-1]
    ch = line[trace[-1]]

    if ch == SPLITTER:
        for origin in [pos - 1, pos + 1]:
            _fall(trace + [origin], line_no + 1, lines)
    elif ch in [START, EMPTY]:
        _fall(trace, line_no + 1, lines)


def main(args) -> int | None:
    lines = []
    with open(args.file, "r") as f:
        lines = f.read().rstrip().split("\n")

    start = lines[0].index(START)
    _fall([start], 0, lines)
    print(len(list(paths)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
