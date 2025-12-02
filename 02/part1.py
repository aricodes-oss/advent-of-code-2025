#!/usr/bin/env python

import argparse
import sys


def _invalid_id(id: int) -> bool:
    s = str(id)
    if len(s) < 2 or len(s) % 2 != 0:
        return False

    return s[0 : len(s) // 2] == s[len(s) // 2 :]


def main(args) -> int | None:
    sum = 0
    ranges = []

    with open(args.file, "r") as f:
        data = f.read().split(",")
        for pair in data:
            low, high = pair.split("-")
            ranges.append([int(low), int(high)])

    for low, high in ranges:
        for id in range(low, high + 1):
            if _invalid_id(id):
                sum += id

    print(sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
