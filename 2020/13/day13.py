#!/usr/bin/env python3

import sys


def find_bus(start_time, buses):
    current_time = start_time
    while True:
        for bus in buses:
            if current_time % bus == 0:
                return (current_time - start_time, bus)
        current_time += 1


def main():
    start_time = int(sys.stdin.readline().rstrip())
    buses = [int(bus)
             for bus in sys.stdin.readline().rstrip().split(',') if bus != 'x']

    time, bus = find_bus(start_time, buses)
    print(f'Waited {time} minutes for bus {bus}. Multiply: {bus * time}')


if __name__ == '__main__':
    main()
