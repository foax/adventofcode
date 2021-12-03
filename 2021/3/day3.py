#!/usr/bin/env python3

import sys


def bit_count(input):
    '''Count the 1's and 0's in each index.'''

    count = {x: 0 for x in range(0, len(input[0]))}
    for line in input:
        for i, x in enumerate(line):
            count[i] += x
    return count


def bit_count_subtract(count, line):
    '''Subtract a line of bits from a bit count.'''

    for i, x in enumerate(line):
        count[i] -= x


def bit_line_to_dec(line):
    '''Convert a bit line do decimal.'''

    value = 0
    line_len = len(line)
    for i in range(0, line_len):
        value += (2 ** (line_len - 1 - i)) * line[i]
    return value


def find_gamma(input):

    input_len = len(input)
    line_len = len(input[0])
    count = bit_count(input)
    gamma_value = 0

    for i in range(0, line_len):
        if count[i] > input_len // 2:
            gamma_value += (2 ** (line_len - 1 - i))
    return gamma_value


def find_oxygen_gen_rating(input):
    our_input = input.copy()
    count = bit_count(our_input)

    i = 0
    while len(our_input) > 1:
        if count[i] >= len(our_input) / 2:
            common_bit = 1
        else:
            common_bit = 0

        new_input = []
        for line in our_input:
            if line[i] == common_bit:
                new_input.append(line)
            else:
                bit_count_subtract(count, line)

        our_input = new_input
        i += 1

    return bit_line_to_dec(our_input[0])


def find_co2_rating(input):
    our_input = input.copy()
    count = bit_count(our_input)

    i = 0
    while len(our_input) > 1:
        common_bit = 0
        half_length = len(our_input) / 2
        if count[i] < half_length:
            common_bit = 1

        new_input = []
        for line in our_input:
            if line[i] == common_bit:
                new_input.append(line)
            else:
                bit_count_subtract(count, line)

        our_input = new_input
        i += 1

    return bit_line_to_dec(our_input[0])


def main():
    input = [[int(x) for x in line.rstrip()] for line in sys.stdin.readlines()]

    gamma = find_gamma(input)
    epsilon = (2 ** len(input[0]) - 1) ^ gamma
    oxygen = find_oxygen_gen_rating(input)
    co2 = find_co2_rating(input)
    print(
        f'gamma value: {gamma}; epsilon value: {epsilon}; multiply: {gamma * epsilon}')
    print(f'oxygen: {oxygen}; co2: {co2}; multiply: {oxygen * co2}')


if __name__ == '__main__':
    main()
