#!/usr/bin/env python3

import sys

groups = []

answers = {}
for line in sys.stdin:
    if len(line.rstrip()) == 0:
        groups.append(answers)
        answers = {}

    for x in line.rstrip():
        if x not in answers:
            answers[x] = 1
        else:
            answers[x] += 1

groups.append(answers)

answer_count = 0
for g in groups:
    answer_count += len(g.keys())

print(f'Sum of answer counts: {answer_count}')
