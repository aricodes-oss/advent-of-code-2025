#!/usr/bin/env python

import argparse
import sys


def _chunk(id: str, size: int) -> list[str]:
    return [id[i : i + size] for i in range(0, len(id), size)]


def _invalid_id(id: int) -> bool:
    string = str(id)
    for chunk_size in range(1, (len(string) // 2) + 1):
        chunks = _chunk(string, chunk_size)
        if all([chunk == chunks[0] for chunk in chunks]):
            return True


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
