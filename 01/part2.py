#!/usr/bin/env python

import sys
import argparse

MIN = 0
MAX = 99


def main(args) -> int | None:
    # Our position on the dial
    location = 50

    # The list of moves we are going to make
    moves = []

    # The number of times we have landed on 0
    zeros = 0

    with open(args.file, "r") as f:
        moves = f.read().split("\n")

    moves = [move.rstrip() for move in moves]

    for move in moves:
        if not len(move):
            continue

        direction, distance = move[0], int(move[1:])
        direction = -1 if direction == "L" else 1

        for _ in range(1, distance + 1):
            location += direction
            if location < MIN:
                location += 100
            elif location > MAX:
                location -= 100

            if location == 0:
                zeros += 1

    print(zeros)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
