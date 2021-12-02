#!/usr/bin/env python3

import sys


class Sub:

    def __init__(self):
        self.depth = 0
        self.position = 0

    def forward(self, amount):
        self.position += amount

    def down(self, amount):
        self.depth += amount

    def up(self, amount):
        self.depth -= amount

    def get_depth(self):
        return self.depth

    def get_position(self):
        return self.position


def main():
    commands = [line.rstrip().split(' ') for line in sys.stdin.readlines()]
    sub = Sub()
    for c in commands:
        getattr(sub, c[0])(int(c[1]))

    pos = sub.get_position()
    depth = sub.get_depth()
    print(f'Sub position: {pos}; Sub depth: {depth}; Multiply: {pos * depth}')


if __name__ == '__main__':
    main()
