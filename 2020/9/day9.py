#!/usr/bin/env python3

import sys


def is_sum_of_pair(num, num_list):
    for i, x in enumerate(num_list):
        for y in num_list[(i + 1):]:
            if x + y == num:
                return True
    return False


numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip()))

numbers_to_check = 25
for i in range(0, len(numbers)):
    if not is_sum_of_pair(numbers[i + numbers_to_check], numbers[i:(i + numbers_to_check)]):
        print(
            f'Number {numbers[i + numbers_to_check]} is not a sum of a pair of the last {numbers_to_check} numbers')
        break
