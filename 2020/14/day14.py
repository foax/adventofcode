import fileinput
import re
from collections import defaultdict
from pprint import pprint


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def parse_mask(mask):
    masks = {'on': 0, 'off': 0}
    for i, x in enumerate(reversed(mask)):
        if x == '1':
            masks['on'] += 2 ** i
        elif x == '0':
            masks['off'] += 2 ** i
    return masks


def apply_mask(value, mask):
    value = value | mask['on']
    value = value & ~ mask['off']
    return value


def main():
    lines = load_input(fileinput.input(),
                       func=lambda x: x.strip().split(' = '))
    masks = {'on': 0, 'off': 0}
    mem = defaultdict(int)

    for line in lines:
        if line[0] == 'mask':
            masks = parse_mask(line[1])
            continue
        match = re.match('mem\[(\d+)\]', line[0])
        mem_location = match.group(1)
        mem_value = int(line[1])
        mem[mem_location] = apply_mask(mem_value, masks)

    pprint(mem)
    mem_sum = sum([v for _, v in mem.items()])
    print(mem_sum)


if __name__ == '__main__':
    main()
