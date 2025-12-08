#!/usr/bin/env python

import operator
import argparse
import sys
import re

type Worksheet = list[list[int | str]]


def main(args) -> int | None:
    worksheet: Worksheet = []
    with open(args.file, "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            if len(line) == 0:
                continue
            worksheet.append(re.split(r"\s+", line.strip()))

    # Transpose the matrix into lists of columns
    worksheet = list(zip(*worksheet))
    results = []
    for problem in worksheet:
        problem = list(problem)
        operand = problem.pop()
        op = operator.mul if operand == "*" else operator.add

        problem = list(map(int, problem))
        result = problem.pop()
        for elem in problem:
            result = op(result, elem)
        results.append(result)

    print(sum(results))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    sys.exit(main(parser.parse_args()) or 0)
