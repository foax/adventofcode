#!/usr/bin/env python3

import fileinput


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

    def do_commands(self, commands):
        for cmd in commands:
            getattr(self, cmd[0])(int(cmd[1]))


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


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def main():

    commands = load_input(fileinput.input(), lambda x: x.rstrip().split(' '))
    subs = [Sub('part 1'), Collins('part 2')]

    for sub in subs:
        sub.do_commands(commands)
        print(
            f'Sub name: {sub.name}; position: {sub.position} depth: {sub.depth}; Multiply: {sub.position * sub.depth}')


if __name__ == '__main__':
    main()
