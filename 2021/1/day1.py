#!/usr/bin/env python3

import sys


def count_increases(numbers):
    '''Counts the number of times a list of integers increases.'''

    increases = [1 for (x, y) in zip(numbers[0:-1], numbers[1:]) if y > x]
    return sum(increases)


def part_2(numbers):
    sums = [sum(x) for x in zip(numbers[0:-2], numbers[1:-1], numbers[2:])]
    return count_increases(sums)


def main():
    numbers = [int(x.rstrip()) for x in sys.stdin.readlines()]
    answers = (count_increases(numbers), part_2(numbers))
    print(f'Part 1: {answers[0]}; Part 2: {answers[1]}')


if __name__ == "__main__":
    main()
