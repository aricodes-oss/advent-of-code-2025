#!/usr/bin/env python

import argparse
import sys


def _max(bank: list[int], k=12) -> int:
    digits = "".join(map(str, bank))
    if k >= len(digits):
        return int(digits)

    result = []
    skippable = len(digits) - k

    for idx, digit in enumerate(digits):
        while result and result[-1] < digit and skippable > 0:
            result.pop()
            skippable -= 1

        result.append(digit)

    return int("".join(result[:12]))


def main(args) -> int | None:
    # All the battery banks - list[list[int]]
    banks = []

    with open(args.file, "r") as f:
        # This could be one fat list comprehension, but it was hard to read
        for line in f.read().split("\n"):
            if not len(line):
                continue

            banks.append([int(ch) for ch in line])

    print(sum([_max(bank) for bank in banks]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
