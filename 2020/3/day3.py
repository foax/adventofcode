#!/usr/bin/env python3
import sys

DEBUG = True

lines = []
width = None
tree_count = 0


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


for line in sys.stdin:
    if not width:
        width = len(line) - 1
        if DEBUG:
            print(f'width: {width}')
    lines.append(line_to_int(line))

x = 0
y = 0

while y < len(lines):
    if DEBUG:
        print(f'x: {x}; y: {y}; line_int: {lines[y]}')
    if lines[y] & (2 ** x):
        if DEBUG:
            print('hit a tree jim')
        tree_count += 1

    x = (x + 3) % width
    y += 1

print(f'trees hit: {tree_count}')
