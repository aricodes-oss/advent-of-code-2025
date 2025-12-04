#!/usr/bin/env python

import argparse
import sys


def _max(bank: list[int]) -> int:
    found = 0

    for start in range(0, len(bank) - 1):
        for end in range(start + 1, len(bank)):
            found = max(found, int(f"{bank[start]}{bank[end]}"))

    return found


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
