#!/usr/bin/env python3

import sys
import re


class Ship:

    headings_to_degrees = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
    degrees_to_headings = {v: k for k, v in headings_to_degrees.items()}

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 'E'

    def move(self, direction, amount):
        match direction:
            case 'N':
                self.y += amount
            case 'E':
                self.x += amount
            case 'S':
                self.y -= amount
            case 'W':
                self.x -= amount

    def move_forward(self, amount):
        self.move(self.heading, amount)

    def change_direction(self, direction, deg):
        lr_direction = {'L': -1, 'R': 1}
        new_degrees = (
            Ship.headings_to_degrees[self.heading] + lr_direction[direction] * deg) % 360
        self.heading = Ship.degrees_to_headings[new_degrees]

    def get_position(self):
        return (self.x, self.y)


class Ship2:

    headings_to_degrees = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
    degrees_to_headings = {v: k for k, v in headings_to_degrees.items()}

    def __init__(self, pos=[0, 0], wpt=[10, 1], hdg='E'):
        self.pos = pos.copy()
        self.wpt = wpt.copy()
        self.heading = hdg

    def __str__(self):
        return f'Position: {self.pos}; Waypoint: {self.wpt}; Heading: {self.heading}'

    def move_waypoint(self, direction, amount):
        match direction:
            case 'N':
                self.wpt[1] += amount
            case 'E':
                self.wpt[0] += amount
            case 'S':
                self.wpt[1] -= amount
            case 'W':
                self.wpt[0] -= amount

    def move_forward(self, amount):
        self.pos[0] += self.wpt[0] * amount
        self.pos[1] += self.wpt[1] * amount

    def change_direction(self, direction):

        if direction == 'R90' or direction == 'L270':
            self.wpt = [self.wpt[1], self.wpt[0] * -1]
        elif direction == 'R270' or direction == 'L90':
            self.wpt = [self.wpt[1] * -1, self.wpt[0]]
        elif direction == 'L180' or direction == 'R180':
            self.wpt = [self.wpt[0] * -1, self.wpt[1] * -1]

    def get_position(self):
        return tuple(self.pos)


def main():
    instructions = [line.rstrip() for line in sys.stdin.readlines()]
    ship = Ship()
    ship2 = Ship2()
    print(f'Ship 2 starting info: {ship2}')
    for i in instructions:
        print(i)
        match = re.match('^([NSEWLRF])(\d+)$', i)
        action, value = match.group(1, 2)
        value = int(value)
        if action in 'NSEW':
            ship.move(action, value)
            ship2.move_waypoint(action, value)
        elif action in 'LR':
            ship.change_direction(action, value)
            ship2.change_direction(i)
        elif action in 'F':
            ship.move_forward(value)
            ship2.move_forward(value)
        (x, y) = ship2.get_position()
        print(ship2)

    (x, y) = ship.get_position()
    print(f'Manhattan distance: {abs(x) + abs(y)}')

    (x, y) = ship2.get_position()
    print(f'Part 2: Manhattan distance: {abs(x) + abs(y)}')


if __name__ == '__main__':
    main()
