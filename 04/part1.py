#!/usr/bin/env python

import argparse
import sys

type Grid = list[list[str]]

ROLL = "@"


def _inbounds(grid: Grid, x: int, y: int) -> bool:
    return (y >= 0 and x >= 0) and (y < len(grid[0]) and x < len(grid))


def _neighbors(grid: Grid, x: int, y: int) -> int:
    found = 0

    for tx in range(x - 1, x + 2):
        for ty in range(y - 1, y + 2):
            if ty == y and tx == x:
                continue

            if _inbounds(grid, tx, ty) and grid[tx][ty] == ROLL:
                found += 1

    return found


def main(args) -> int | None:
    grid = []

    with open(args.file, "r") as f:
        for line in f.read().split("\n"):
            if len(line) == 0:
                continue
            grid.append(list(line.strip()))

    count = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            assert _inbounds(grid, x, y)
            if grid[x][y] == ROLL and _neighbors(grid, x, y) < 4:
                count += 1

    print(count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
