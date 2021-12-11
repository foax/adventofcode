import fileinput
import re
from collections import defaultdict
from pprint import pprint


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def parse_mask(mask):
    masks = defaultdict(int)
    for i, x in enumerate(reversed(mask)):
        mask_value = 2 ** i
        if x == '1':
            masks['on'] += mask_value
        elif x == '0':
            masks['off'] += mask_value
        elif x == 'X':
            masks['floating'] += mask_value
    return masks


def apply_mask(value, mask):
    value = value | mask['on']
    value = value & ~ mask['off']
    return value


def apply_memory_mask(value, mask):
    values = set()
    value = value | mask['on']
    values.add(value)

    floating_mask = mask['floating']
    for bit in range(36):
        if floating_mask % 2 == 1:
            m = 2 ** bit
            for v in list(values):
                values.add(v | m)
                values.add(v & ~ m)
        floating_mask = floating_mask >> 1

    return list(values)


def main():
    lines = load_input(fileinput.input(),
                       func=lambda x: x.strip().split(' = '))
    masks = {'on': 0, 'off': 0}
    mem_part1 = defaultdict(int)
    mem_part2 = defaultdict(int)

    for line in lines:
        if line[0] == 'mask':
            masks = parse_mask(line[1])
            continue
        match = re.match('mem\[(\d+)\]', line[0])
        mem_location = int(match.group(1))
        mem_value = int(line[1])
        mem_part1[mem_location] = apply_mask(mem_value, masks)

        mem_locations = apply_memory_mask(mem_location, masks)
        # print(f'line: {line}; mask: {masks}; mem_locations: {mem_locations}')
        for mem_location in mem_locations:
            mem_part2[mem_location] = mem_value

    mem_sum = sum([v for _, v in mem_part1.items()])
    print(f'part 1: {mem_sum}')

    mem_sum = sum([v for _, v in mem_part2.items()])
    print(f'part 2: {mem_sum}')


if __name__ == '__main__':
    main()
