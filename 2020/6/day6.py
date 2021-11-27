#!/usr/bin/env python3

import sys
from pprint import pprint

groups = []
answers = {}
people_count = 0

for line in sys.stdin:
    if len(line.rstrip()) == 0:
        answers['count'] = people_count
        groups.append(answers)
        answers = {}
        people_count = 0
        continue

    for x in line.rstrip():
        if x not in answers:
            answers[x] = 1
        else:
            answers[x] += 1
    people_count += 1

answers['count'] = people_count
groups.append(answers)

answer_count = 0
for g in groups:
    for a in g:
        if a == 'count':
            continue
        if g[a] == g['count']:
            answer_count += 1

print(f'Sum of answer counts: {answer_count}')
