#!/usr/bin/env python

import argparse
import sys


def _in_ranges(id: int, ranges: list[range]) -> bool:
    for r in ranges:
        if id in r:
            return True

    return False


def main(args) -> int | None:
    ranges = []

    with open(args.file, "r") as f:
        raw_ranges, raw_ids = f.read().split("\n\n")

        for raw_range in raw_ranges.split("\n"):
            if len(raw_range) == 0:
                continue
            low, high = map(int, raw_range.split("-"))
            ranges.append(range(low, high + 1))

    # Sort ranges by start position
    sorted_ranges = sorted(ranges, key=lambda r: r.start)

    merged = []
    for r in sorted_ranges:
        if merged and r.start <= merged[-1].stop:
            last = merged.pop()
            merged.append(range(last.start, max(last.stop, r.stop)))
        else:
            merged.append(r)

    # Count total unique numbers
    total = sum(len(r) for r in merged)
    print(total)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
