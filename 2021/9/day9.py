import fileinput
from collections import Counter
from pprint import pprint


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def find_high_neighbours(i, j, input, find_basins=False, basin_threshold=9):
    '''Returns a list of neighbours that are greater in value than the current point.
    Returns a list of sets of (neighbour_value, x, y)'''

    line_len = len(input[0])
    line_count = len(input)
    neighbours = set()
    self = input[i][j]

    for x, y in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
        if x < 0 or x >= line_count:
            continue
        if y < 0 or y >= line_len:
            continue
        neighbour = input[x][y]
        if find_basins and neighbour >= basin_threshold:
            continue
        if neighbour > self:
            new_neighbour = (neighbour, x, y)
            neighbours.add(new_neighbour)
            if find_basins:
                neighbours |= find_high_neighbours(
                    x, y, input, find_basins, basin_threshold)
    return neighbours


def main():
    input = load_input(fileinput.input(), lambda x: [
                       int(y) for y in x.strip()])
    # print(input)

    line_len = len(input[0])
    line_count = len(input)

    # Part 1
    low_points = []
    for i, line in enumerate(input):
        for j, num in enumerate(line):
            neighbours = find_high_neighbours(i, j, input)
            # print(i, j, input[i][j], neighbours)
            num_neighbours = 4
            for x, y in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
                if x < 0 or x >= line_count:
                    num_neighbours -= 1
                if y < 0 or y >= line_len:
                    num_neighbours -= 1

            if len(neighbours) == num_neighbours:
                # print('found lower number')
                low_points.append((num, (i, j)))

    # print(low_points)
    print(f'risk level sum: {sum([x[0]+1 for x in low_points])}')

    # Part 2
    basins = []
    for num, coords in low_points:
        basins.append((num, coords, find_high_neighbours(
            coords[0], coords[1], input, find_basins=True)))

    basins.sort(key=lambda x: len(x[2]))
    basin_sizes = [len(x[2]) + 1 for x in basins]

    # pprint(basins)
    # print(basin_sizes)
    print(
        f'3 largest basin sizes multiplied: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}')


if __name__ == '__main__':
    main()
