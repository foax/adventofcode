#!/usr/bin/env python3

import fileinput


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def parse_line(line):
    return tuple([tuple([int(x) for x in coord.split(',')]) for coord in line.rstrip().split(' -> ')])


def load_lines(input_file=None):
    lines = load_input(fileinput.input(input_file), func=parse_line)
    return lines


def find_extents(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        for coord in line:
            if coord[0] > max_x:
                max_x = coord[0]
            if coord[1] > max_y:
                max_y = coord[1]
    return (max_x, max_y)


def empty_space(lines):
    space = []
    max_x, max_y = find_extents(lines)
    for y in range(0, max_y + 1):
        row = [0] * (max_x + 1)
        space.append(row)
    return space


def space_as_str(space):
    output = ''
    for line in space:
        for x in line:
            if x == 0:
                output += '.'
            else:
                output += str(x)
        output += '\n'
    return output


def count_points(space, threshold):
    count = 0
    for line in space:
        for x in line:
            if x >= threshold:
                count += 1
    return count


def mark_lines(lines, space, check_diagonals=False):
    for start, end in lines:
        step = [0, 0]
        for x in (0, 1):
            if start[x] < end[x]:
                step[x] = 1
            elif start[x] > end[x]:
                step[x] = -1
            else:
                step[x] = 0
        if 0 not in step and not check_diagonals:
            continue

        pos = list(start)
        while True:
            space[pos[1]][pos[0]] += 1
            if pos == list(end):
                break
            pos = [x + y for x, y in zip(step, pos)]


def check_overlapping_lines(lines, check_diagonals=False, min_overlap=2):
    space = empty_space(lines)
    mark_lines(lines, space, check_diagonals)
    count = count_points(space, min_overlap)
    return count


def main():
    lines = load_lines()
    part_1 = check_overlapping_lines(lines)
    part_2 = check_overlapping_lines(lines, check_diagonals=True)
    print(f'Part 1: {part_1}; Part 2: {part_2}')


if __name__ == '__main__':
    main()
