#!/usr/bin/env python3

import sys
import re


class Ship:

    def __init__(self, pos=[0, 0], wpt=[1, 0]):
        self.pos = pos.copy()
        self.wpt = wpt.copy()

    def __str__(self):
        return f'Position: {self.pos}; Waypoint: {self.wpt}'

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

    def move(self, direction, amount):
        match direction:
            case 'N':
                self.pos[1] += amount
            case 'E':
                self.pos[0] += amount
            case 'S':
                self.pos[1] -= amount
            case 'W':
                self.pos[0] -= amount

    def move_forward(self, amount):
        self.pos[0] += self.wpt[0] * amount
        self.pos[1] += self.wpt[1] * amount

    def rotate_waypoint(self, direction):
        if direction == 'R90' or direction == 'L270':
            self.wpt = [self.wpt[1], self.wpt[0] * -1]
        elif direction == 'R270' or direction == 'L90':
            self.wpt = [self.wpt[1] * -1, self.wpt[0]]
        elif direction == 'L180' or direction == 'R180':
            self.wpt = [self.wpt[0] * -1, self.wpt[1] * -1]

    def get_position(self):
        return tuple(self.pos)

    def get_waypoint(self):
        return tuple(self.wpt)


def main():
    instructions = [line.rstrip() for line in sys.stdin.readlines()]
    ships = [Ship(), Ship(wpt=[10, 1])]

    # print(
    #     f'Ship part 1 starting info: {ships[0]}; Ship part 2 starting info: {ships[1]}')
    for i in instructions:
        # print(i)
        match = re.match('^([NSEWLRF])(\d+)$', i)
        action, value = match.group(1, 2)
        value = int(value)

        if action in 'NSEW':
            ships[0].move(action, value)
            ships[1].move_waypoint(action, value)
        elif action in 'LR':
            for s in ships:
                s.rotate_waypoint(i)
        elif action in 'F':
            for s in ships:
                s.move_forward(value)

        # print([str(s) for s in ships])

    for i, s in enumerate(ships):
        (x, y) = s.get_position()
        print(f'ship[{i}] Manhattan distance: {abs(x) + abs(y)}')


if __name__ == '__main__':
    main()
