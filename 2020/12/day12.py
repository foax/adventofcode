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


def main():
    instructions = [line.rstrip() for line in sys.stdin.readlines()]
    ship = Ship()
    for i in instructions:
        match = re.match('^([NSEWLRF])(\d+)$', i)
        action, value = match.group(1, 2)
        value = int(value)
        if action in 'NSEW':
            ship.move(action, value)
        elif action in 'LR':
            ship.change_direction(action, value)
        elif action in 'F':
            ship.move_forward(value)

    (x, y) = ship.get_position()
    print(f'Manhattan distance: {abs(x) + abs(y)}')


if __name__ == '__main__':
    main()
