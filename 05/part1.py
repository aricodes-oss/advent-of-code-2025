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
    ids = []

    with open(args.file, "r") as f:
        raw_ranges, raw_ids = f.read().split("\n\n")

        for raw_range in raw_ranges.split("\n"):
            if len(raw_range) == 0:
                continue
            low, high = map(int, raw_range.split("-"))
            ranges.append(range(low, high + 1))

        ids = [int(id) for id in raw_ids.split("\n") if len(id) != 0]

    fresh = sum(1 for id in ids if _in_ranges(id, ranges))
    print(fresh)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
