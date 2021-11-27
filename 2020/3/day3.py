#!/usr/bin/env python3
import sys

DEBUG = False

lines = []
width = None
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_hit_multiple = 1


def line_to_int(line):
    '''Converts a line of "..#..#..." to an integer.'''

    line_int = 0
    for i, x in enumerate(line):
        if DEBUG:
            print(f'i: {i}; x: {x}')
        if x == '#':
            line_int += 2 ** i
            if DEBUG:
                print(f'line_int: {line_int}')
    return line_int


def count_trees_hit(slope, lines, width):
    '''Counts the number of trees hit down a slope.'''

    x = 0
    y = 0
    tree_count = 0

    while y < len(lines):
        if lines[y] & (2 ** x):
            if DEBUG:
                print('hit a tree jim')
            tree_count += 1
        else:
            if DEBUG:
                print('missed that tree jim')

        x = (x + slope[0]) % width
        y += slope[1]
    return tree_count


for line in sys.stdin:
    if not width:
        width = len(line) - 1
        if DEBUG:
            print(f'width: {width}')
    lines.append(line_to_int(line))

for slope in slopes:
    if DEBUG:
        print(f'slope x: {slope[0]}; slope y: {slope[1]}')
    trees_hit = count_trees_hit(slope, lines, width)
    print(f'Right {slope[0]}, down {slope[1]}; trees hit: {trees_hit}')
    trees_hit_multiple *= trees_hit

print(f'multiply trees hit: {trees_hit_multiple}')
