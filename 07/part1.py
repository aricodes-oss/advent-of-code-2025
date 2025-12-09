#!/usr/bin/env python

import argparse
import sys

BEAM = "|"
SPLITTER = "^"
START = "S"
EMPTY = "."


def main(args) -> int | None:
    lines = []
    with open(args.file, "r") as f:
        lines = f.read().rstrip().split("\n")

    beams = []
    splits = 0
    for line in lines:
        new_beams = set()
        # If we're not tracking any beams
        if not beams:
            beams.append(line.index(START))
            continue

        # Check the target space the beam is trying to move into
        for beam in beams:
            ch = line[beam]
            if ch == SPLITTER:
                # Generate two new beams, terminate current one
                new_beams.update([beam - 1, beam + 1])
                splits += 1
            elif ch == EMPTY:
                # Propagate the current one
                new_beams.add(beam)
        beams = list(new_beams)

    print(splits)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
