#!/usr/bin/env python3

import sys
import re

numbers = []
number_re = re.compile('^\d+$')

for line in sys.stdin:
    if number_re.match(line):
        numbers.append(int(line))

for i, a in enumerate(numbers):
    for b in numbers[i + 1:]:
        if a + b == 2020:
            print(f'a = {a}; b = {b}; a x b = {a*b}')
        for c in numbers [i + 2:]:
            if a + b + c == 2020:
                print(f'a = {a}; b = {b}; c = {c}; a x b x c = {a*b*c}')

