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


def count_lowers(path):
    return Counter([x for x in path if x.name.islower()])


def traverse_path(cave, until, caves_traversed):
    # list of list of paths traversed
    paths_traversed = []
    # list of paths traversed for current working set
    caves_traversed.append(cave)
    for c in cave.links:
        caves = caves_traversed.copy()
        if c == until:
            caves.append(until)
            paths_traversed.append(caves)
        if c.name.isupper() or c not in caves:
            new_paths = traverse_path(c, until, caves)
            if new_paths:
                paths_traversed.extend(new_paths)
    return paths_traversed


def traverse_path_2(cave, until, caves_traversed):
    # list of list of paths traversed
    paths_traversed = []
    # list of paths traversed for current working set
    caves_traversed.append(cave)
    for c in cave.links:
        caves = caves_traversed.copy()
        if c == caves[0]:
            continue
        if c == until:
            caves.append(until)
            paths_traversed.append(caves)
            continue
        lower_cave_count = count_lowers(caves[1:] + [c])
        lower_cave_occurences = Counter(lower_cave_count.values())
        # print(f'caves: {caves}')
        # print(f'lower_cave_count: {lower_cave_count}')
        # print(f'lower_caves_occurences: {lower_cave_occurences}')

        if c.name.isupper() or (lower_cave_occurences[3] == 0 and lower_cave_occurences[2] <= 1):
            new_paths = traverse_path_2(c, until, caves)
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

    # list of list of cave names
    paths_traversed = traverse_path(all_caves['start'], all_caves['end'], [])
    # pprint(paths_traversed)
    print(f'part 1: {len(paths_traversed)}')

    paths_traversed_2 = traverse_path_2(
        all_caves['start'], all_caves['end'], [])
    # pprint(paths_traversed_2)
    print(f'part 2: {len(paths_traversed_2)}')


if __name__ == '__main__':
    main()
