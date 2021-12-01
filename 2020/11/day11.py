#!/usr/bin/env python3

import sys
import copy


def adjacent_occupied_count(floor, seat_row, seat_col):
    '''Returns how many adjacent seats are occupied on a floor, given a co-ordinate.'''

    seat_count = 0
    # print(f'seat_row: {seat_row}; seat_y: {seat_col}')
    for x in range(seat_row - 1, seat_row + 2):
        # print(f'x: {x}')
        if x < 0 or x > len(floor) - 1:
            continue
        for y in range(seat_col - 1, seat_col + 2):
            # print(f'y: {y}')
            if y < 0 or y > len(floor[x]) - 1 or (x == seat_row and y == seat_col):
                continue
            # print(f'x: {x}; y: {y}; seat: {floor[x][y]}')
            if floor[x][y] == '#':
                seat_count += 1

    return seat_count


def change_seats(floor):
    '''Update seat occupancy based on day 11 ruleset.'''

    changes = 0
    orig_floor = copy.deepcopy(floor)
    for x, row in enumerate(orig_floor):
        for y, seat in enumerate(row):
            # print(f'row: {x}, col: {y}, seat: {seat}')
            if seat == '.':
                continue
            count = adjacent_occupied_count(orig_floor, x, y)
            # print(f'adjacent filled seats: {count}')
            if seat == 'L' and count == 0:
                floor[x][y] = '#'
                changes += 1
            elif seat == '#' and count >= 4:
                floor[x][y] = 'L'
                changes += 1
    return changes


def count_occupied_seats(floor):
    count = 0
    for row in floor:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def print_floor(floor):
    for line in floor:
        print(''.join(line))
    print


def main():
    floor = []
    floor = [list(line.rstrip()) for line in sys.stdin.readlines()]

    x = 0
    while True:
        # print(f'Iteration {x}\n')
        # print_floor(floor)

        if change_seats(floor) == 0:
            break
        x += 1

    print(f'Number of occupied seats: {count_occupied_seats(floor)}')


if __name__ == '__main__':
    main()
