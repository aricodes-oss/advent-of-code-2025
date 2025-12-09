#!/usr/bin/env python

import argparse
import sys


def main(args) -> int | None:
    lines = []
    with open(args.file, "r") as f:
        lines = f.read().rstrip().split("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    sys.exit(main(args) or 0)
