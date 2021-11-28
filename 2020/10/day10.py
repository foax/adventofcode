#!/usr/bin/env python3

import sys
from pprint import pprint

adapters = []
for line in sys.stdin:
    adapters.append(int(line.rstrip()))

adapters.sort()
adapters.append(adapters[-1] + 3)

last = 0
diff_counts = {}
while adapters:
    adapter = adapters.pop(0)
    diff = adapter - last
    if diff not in diff_counts:
        diff_counts[diff] = 0
    diff_counts[diff] += 1
    last = adapter

print('Diff distributions')
pprint(diff_counts)
print(
    f'Multiply 1 jolt and 3 jolt differences: {diff_counts[1] * diff_counts[3]}')
