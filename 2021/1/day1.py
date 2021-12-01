#!/usr/bin/env python3

import sys


def part_1(numbers):
    increases = 0
    for i, x in enumerate(numbers):
        if i == 0:
            continue
        y = numbers[i - 1]
        if x > y:
            increases += 1

    print(f'Part 1: Increases: {increases}')


def part_2(numbers):
    increases = 0
    last_sum = 0

    for i, x in enumerate(numbers):
        if i < 2:
            continue

        y = numbers[i - 1]
        z = numbers[i - 2]
        window_sum = x + y + z

        if last_sum > 0 and window_sum > last_sum:
            increases += 1

        last_sum = window_sum

    print(f'Part 2: Increases: {increases}')


def main():
    numbers = [int(x.rstrip()) for x in sys.stdin.readlines()]
    part_1(numbers)
    part_2(numbers)


if __name__ == "__main__":
    main()
