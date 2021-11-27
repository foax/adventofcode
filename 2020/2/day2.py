#!/usr/bin/env python3

import sys
import re

DEBUG = False

line_re = re.compile('^(\d+)-(\d+) (\w): (\w+)$')
valid = 0
part_two_valid = 0

for line in sys.stdin:
    re_result = line_re.match(line)
    if not re_result:
        continue

    if DEBUG:
        print(line)
    min_len = int(re_result.group(1))
    max_len = int(re_result.group(2))
    pwd_letter = re_result.group(3)
    passwd = re_result.group(4)

    letter_count = passwd.count(pwd_letter)
    if letter_count >= min_len and letter_count <= max_len:
        if DEBUG:
            print(f'password {passwd} is valid')
        valid += 1

    if (
        (passwd[min_len - 1] == pwd_letter or passwd[max_len - 1] == pwd_letter)
        and
            (passwd[min_len - 1] != passwd[max_len - 1])):
        if DEBUG:
            print(f'password {passwd} is valid for part two')
        part_two_valid += 1

print(f'Valid passwords: part 1 {valid}; part 2 {part_two_valid}')
