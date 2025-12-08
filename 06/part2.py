#!/usr/bin/env python

import operator
import argparse
import sys


def main(args) -> int | None:
    with open(args.file, "r") as f:
        lines = f.read().rstrip("\n").split("\n")

    # Pad all lines to same length
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    # Transpose character-by-character to read columns
    columns = ["".join(chars) for chars in zip(*lines)]

    # Group columns into problems (separated by all-space columns)
    problems = []
    current_problem = []
    for col in columns:
        if col.strip() == "":
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    if current_problem:
        problems.append(current_problem)

    results = []
    for problem_cols in problems:
        # Find which column has the operator
        op_char = None
        for col in problem_cols:
            if col[-1] in "*+":
                op_char = col[-1]
                break

        if not op_char:
            continue

        # Extract numbers from each column (top-to-bottom), excluding operator row
        numbers = []
        for col in problem_cols:
            number_str = col[:-1].strip()  # Exclude operator row
            if number_str:
                numbers.append(int(number_str))

        # Reverse to read right-to-left
        numbers = numbers[::-1]

        # Apply operation
        op = operator.mul if op_char == "*" else operator.add
        result = numbers[0]
        for num in numbers[1:]:
            result = op(result, num)
        results.append(result)

    print(sum(results))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    sys.exit(main(parser.parse_args()) or 0)
