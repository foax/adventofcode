import fileinput
from collections import defaultdict
from pprint import pprint
import time

digits = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg')
}

digits_by_length = defaultdict(list)
for x in digits:
    digits_by_length[len(digits[x])].append(x)


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def parse_line(line):
    digit_list = []
    # for x in line.strip().split(' | '):
    #     digit_list.append(sorted([''.join(sorted(y))
    #                       for y in x.split(' ')], key=lambda z: len(z)))

    for x in line.strip().split(' | '):
        digit_list.append([set(y) for y in x.split(' ')])
    return digit_list


def solve_line(line):
    signal_wires = {wire: set('abcdefg') for wire in 'abcdefg'}
    for digit_str in sorted(line[0], key=lambda x: len(x)):
        for digit in digits_by_length[len(digit_str)]:
            remaining_wires = digits[digit].copy()
            new_signal_wires = signal_wires.copy()
            matched_sets = []
            for wire in sorted(digit_str, key=lambda x: len(signal_wires[x])):
                new_signal_wires[wire] = new_signal_wires[wire] & remaining_wires
                new_set = new_signal_wires[wire]
                matched_sets.append(new_set)
                if len(new_set) == matched_sets.count(new_set):
                    remaining_wires -= new_signal_wires[wire]
                elif len(new_signal_wires[wire]) == 0:
                    # something has gone wrong, abort loop
                    new_signal_wires = signal_wires
                    break
                # print(
                #     f'digit_str: {digit_str}; digit: {digits[digit]}; wire: {wire}; new_signal_wires: {new_signal_wires}')
                # time.sleep()
            signal_wires = new_signal_wires
            if max([len(x) for x in signal_wires.values()]) == 1:
                break
    #         print()
    # pprint(signal_wires)

    value_map = {k: list(v)[0] for k, v in signal_wires.items()}
    # pprint(value_map)

    result = 0
    for digit in line[1]:
        # print(digit)
        new_digit = set([value_map[x] for x in digit])
        for k, v in digits.items():
            if v == new_digit:
                result = result * 10 + k
                break

    return result


def main():
    input = load_input(fileinput.input(), parse_line)
    unique_segments = [2, 3, 4, 7]
    count = 0
    for x in input:
        for y in x[1]:
            if len(y) in unique_segments:
                count += 1

    print(count)

    print(sum([solve_line(line) for line in input]))
    # solve_line(input[0])
    # for line in input:
    #     signal_wires = {wire: set() for wire in 'abcdefg'}
    #     for digit_str in line[0]:
    #         for digit in digits_by_length(len(digit_str)):
    #             for x in digit_str:


if __name__ == '__main__':
    main()
