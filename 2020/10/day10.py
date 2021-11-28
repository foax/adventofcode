#!/usr/bin/env python3

import sys
from pprint import pprint


def inc_diff_count(diff_counts, index, amount):
    '''Helper function for incrementing a counter in a dict.'''
    if index not in diff_counts:
        diff_counts[index] = 0
    diff_counts[index] += amount


adapters = []
for line in sys.stdin:
    adapters.append(int(line.rstrip()))

adapters.sort()
adapters.append(adapters[-1] + 3)

# Used to keep track of the different ways to get to a certain
# index in the adapters list
diff_counts = {}

# map adapter numbers to their list index for easy lookup
adapter_indexes = {k: v for v, k in enumerate(adapters)}

for i, adapter in enumerate(adapters):
    for j in range(1, 4):
        adapter_to_check = adapter - j

        # Don't go back past 0
        if adapter_to_check == 0:
            inc_diff_count(diff_counts, i, 1)
            break

        # If the adapter number we are checking is already in our list...
        if adapter_to_check in adapter_indexes:
            # Add the number of ways to get to that adapter number to the
            # number of ways to get to the adapter we are checking
            inc_diff_count(
                diff_counts, i, diff_counts[adapter_indexes[adapter_to_check]])

print(f'Number of ways to connect adapter: {diff_counts[len(adapters) - 1]}')
