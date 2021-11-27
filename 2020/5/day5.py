#!/usr/bin/env python3
import sys


def decode_seat_line(line):
    rows = 128
    cols = 8

    row = [0, rows-1]
    for i, x in enumerate(line[:7]):
        if x == 'F':
            row[1] -= rows >> (i+1)
        elif x == 'B':
            row[0] += rows >> (i+1)

    col = [0, cols-1]
    for i, x in enumerate(line[7:]):
        if x == 'L':
            col[1] -= cols >> (i+1)
        elif x == 'R':
            col[0] += cols >> (i+1)

    return row[0] * cols + col[0]


max_id = 0
for line in sys.stdin:
    seat_id = decode_seat_line(line.rstrip())
    if seat_id > max_id:
        max_id = seat_id

print(f'Max seat ID: {max_id}')
