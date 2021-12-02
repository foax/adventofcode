#!/usr/bin/env python3

import sys


class Sub:
    '''Your run of the mill submarine.'''

    def __init__(self, name):
        self.name = name
        self.depth = 0
        self.position = 0
        self.aim = 0

    def forward(self, amount):
        self.position += amount

    def down(self, amount):
        self.depth += amount

    def up(self, amount):
        self.depth -= amount


class Collins(Sub):
    '''Cutting edge technology, for its day. Now supports aiming.'''

    def __init__(self, name):
        super().__init__(name)
        self.aim = 0

    def forward(self, amount):
        super().forward(amount)
        self.depth += self.aim * amount

    def down(self, amount):
        self.aim += amount

    def up(self, amount):
        self.aim -= amount


def main():
    commands = [line.rstrip().split(' ') for line in sys.stdin.readlines()]
    subs = [Sub('part 1'), Collins('part 2')]

    for sub in subs:
        for cmd in commands:
            getattr(sub, cmd[0])(int(cmd[1]))
        pos = sub.position
        depth = sub.depth
        print(
            f'Sub name: {sub.name}; position: {sub.position} depth: {sub.depth}; Multiply: {sub.position * sub.depth}')


if __name__ == '__main__':
    main()
