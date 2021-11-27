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


seat_ids = []
for line in sys.stdin:
    seat_id = decode_seat_line(line.rstrip())
    seat_ids.append(seat_id)

seat_ids.sort()
print(f'Max seat ID: {seat_ids[-1]}')

last_seat = seat_ids[0]
for seat in seat_ids[1:]:
    if seat != last_seat + 1:
        print(f'Found free seat: {seat - 1}')
        break
    last_seat = seat
