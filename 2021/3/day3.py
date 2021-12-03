#!/usr/bin/env python3

import fileinput


def bit_count(input):
    '''Count how many occurences a bit is present in a list of numbers.

    Returns a dict of { bitmask: count }'''

    count = {}
    for x in input:
        mask = 1
        while mask <= x:
            if x & mask:
                if mask not in count:
                    count[mask] = 1
                else:
                    count[mask] += 1
            mask = mask << 1
    return count


def bit_count_subtract(count, x):
    '''Subtract bits from a bit count.'''

    mask = 1
    while mask <= x:
        if x & mask:
            count[mask] -= 1
        mask = mask << 1


def find_gamma(input):
    input_len = len(input)
    count = bit_count(input)
    max_bit = max(count.keys())
    gamma_value = 0

    x = 1
    while x <= max_bit:
        if count[x] > input_len / 2:
            gamma_value += x
        x = x << 1

    return gamma_value


def find_rating(input, invert=False):
    our_input = input.copy()
    count = bit_count(our_input)

    mask = max(count.keys())
    while len(our_input) > 1:
        count_bit = (count[mask] >= len(our_input) / 2) != invert
        new_input = []
        for x in our_input:
            if (x & mask > 0) == count_bit:
                new_input.append(x)
            else:
                bit_count_subtract(count, x)

        our_input = new_input
        mask = mask >> 1

    return our_input[0]


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def main():

    # input is a list of integers, converted from binary strings
    input = load_input(fileinput.input(), lambda x: int(x.rstrip(), 2))

    gamma = find_gamma(input)
    # epsilon is just the inverse of gamma, so do a bitwise xor against
    # the mask that covers the highest number of bits in our input
    epsilon = (2 ** (max(input) - 1).bit_length() - 1) ^ gamma
    oxygen = find_rating(input)
    co2 = find_rating(input, invert=True)
    print(
        f'gamma value: {gamma}; epsilon value: {epsilon}; multiply: {gamma * epsilon}')
    print(f'oxygen: {oxygen}; co2: {co2}; multiply: {oxygen * co2}')


if __name__ == '__main__':
    main()
