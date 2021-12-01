#!/usr/bin/env python3

import sys
import copy


def adjacent_occupied_count(floor, seat_row, seat_col):
    '''Returns how many adjacent seats are occupied on a floor, given a co-ordinate.'''

    seat_count = 0
    for x in range(seat_row - 1, seat_row + 2):
        if x < 0 or x > len(floor) - 1:
            continue
        for y in range(seat_col - 1, seat_col + 2):
            if y < 0 or y > len(floor[x]) - 1 or (x == seat_row and y == seat_col):
                continue
            if floor[x][y] == '#':
                seat_count += 1

    return seat_count


def in_range(floor, x, y):
    return x >= 0 and x < len(floor) and y >= 0 and y < len(floor[0])


def check_seat_in_direction(floor, seat_row, seat_col, direction_row, direction_col):
    seat_found = False
    x = seat_row + direction_row
    y = seat_col + direction_col
    while in_range(floor, x, y):
        if floor[x][y] == 'L':
            break
        if floor[x][y] == '#':
            seat_found = True
            break
        x += direction_row
        y += direction_col
    return seat_found


def line_of_sight_occupied_count(floor, seat_row, seat_col):
    seat_count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if check_seat_in_direction(floor, seat_row, seat_col, x, y):
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


def change_seats_part_2(floor):
    '''Update seat occupancy based on day 11 ruleset part 2.'''

    changes = 0
    orig_floor = copy.deepcopy(floor)
    for x, row in enumerate(orig_floor):
        for y, seat in enumerate(row):
            # print(f'row: {x}, col: {y}, seat: {seat}')
            if seat == '.':
                continue
            count = line_of_sight_occupied_count(orig_floor, x, y)
            # print(f'adjacent filled seats: {count}')
            if seat == 'L' and count == 0:
                floor[x][y] = '#'
                changes += 1
            elif seat == '#' and count >= 5:
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

    part_1_floor = copy.deepcopy(floor)
    x = 0
    while True:
        # print(f'Iteration {x}\n')
        # print_floor(floor)

        if change_seats(part_1_floor) == 0:
            break
        x += 1

    print(
        f'Part 1: number of occupied seats: {count_occupied_seats(part_1_floor)}')

    part_2_floor = copy.deepcopy(floor)
    x = 0
    while True:
        # print(f'Iteration {x}\n')
        # print_floor(floor)

        if change_seats_part_2(part_2_floor) == 0:
            break
        x += 1

    print(
        f'Part 2: number of occupied seats: {count_occupied_seats(part_2_floor)}')


if __name__ == '__main__':
    main()
