import fileinput
from pprint import pprint
from collections import Counter


class Cave:
    def __init__(self, name):
        self.name = name
        self.links = set()

    def linkto(self, other_cave):
        self.links.add(other_cave)
        other_cave.links.add(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def parse_line(line):
    return [x for x in line.strip().split('-')]


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def check_small_cave_occurrences(caves, small_cave_allowed_count):
    '''Checks if the list of caves meets the small cave count requirements.'''

    small_cave_counter = Counter([x for x in caves if x.name.islower()])
    small_cave_occurrences = Counter(small_cave_counter.values())
    for small_cave_count, occurences in small_cave_occurrences.items():
        if small_cave_count not in small_cave_allowed_count:
            return False
        if small_cave_allowed_count[small_cave_count] == 'any':
            continue
        if occurences > small_cave_allowed_count[small_cave_count]:
            return False
    return True


def traverse_path(cave, until, small_cave_allowed_count, caves_traversed):
    '''Traverse all possible paths starting from cave and ending at until.

    Returns a list of paths that were successully traversed.'''

    # list of list of paths traversed
    paths_traversed = []
    # list of paths traversed for current working set
    caves_traversed.append(cave)

    for c in cave.links:
        caves = caves_traversed.copy()

        if c == caves[0]:
            # path back to the start is not allowed.
            continue

        if c == until:
            # We found the end! Better keep this path.
            caves.append(until)
            paths_traversed.append(caves)
            continue

        if c.name.isupper() or check_small_cave_occurrences(caves + [c], small_cave_allowed_count):
            # Recursion ftw
            new_paths = traverse_path(
                c, until, small_cave_allowed_count, caves)
            if new_paths:
                paths_traversed.extend(new_paths)
    return paths_traversed


def main():
    input = load_input(fileinput.input(), func=parse_line)
    all_caves = {}
    for links in input:
        for c in links:
            if c not in all_caves:
                cave = Cave(c)
                all_caves[c] = cave

        all_caves[links[0]].linkto(all_caves[links[1]])

    paths_traversed = traverse_path(
        all_caves['start'], all_caves['end'], {1: 'any'}, [])
    print(f'part 1: {len(paths_traversed)}')

    paths_traversed_2 = traverse_path(
        all_caves['start'], all_caves['end'], {1: 'any', 2: 1}, [])
    print(f'part 2: {len(paths_traversed_2)}')


if __name__ == '__main__':
    main()
