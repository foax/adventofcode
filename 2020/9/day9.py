#!/usr/bin/env python3

import sys


def is_sum_of_pair(num, num_list):
    for i, x in enumerate(num_list):
        for y in num_list[(i + 1):]:
            if x + y == num:
                return True
    return False


def sum_list(l):
    answer = 0
    for x in l:
        answer += x
    return answer


numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip()))

numbers_to_check = 25
not_a_sum = None
for i in range(0, len(numbers)):
    if not is_sum_of_pair(numbers[i + numbers_to_check], numbers[i:(i + numbers_to_check)]):
        print(
            f'Number {numbers[i + numbers_to_check]} is not a sum of a pair of the last {numbers_to_check} numbers')
        not_a_sum = numbers[i + numbers_to_check]
        break

sum_numbers = None
for i in range(0, len(numbers)):
    sum = numbers[i]
    for j in range(i + 1, len(numbers)):
        sum += numbers[j]
        # Maybe not the best names for variables...
        if sum == not_a_sum:
            sum_numbers = numbers[i:j + 1]
            print(f'Numbers {sum_numbers} add up to {not_a_sum}')
            sum_numbers.sort()
            print(
                f'Sum of smallest and largest: {sum_numbers[0] + sum_numbers[-1]}')
            break
        elif sum > not_a_sum:
            break
    if sum_numbers:
        break
