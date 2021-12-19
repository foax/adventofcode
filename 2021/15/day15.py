import fileinput
from math import sqrt
from pprint import pprint, pformat


def load_input(source):
    grid = {}
    y = 0
    for line in source:
        x = 0
        for v in line.strip():
            grid[(x, y)] = int(v)
            x += 1
        y += 1
    return grid


def adjacent_points(point):
    '''Generator that yields possible adjacent points to the given point.'''

    for adj in (point[0], point[1] + 1), (point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] - 1):
        yield adj


def next_point(path_cost, visited):
    '''Returns the next point to evaluate that has the lowest path cost and is not yet visited.'''

    low_cost_paths = sorted(path_cost.items(), key=lambda x: x[1])
    for point in low_cost_paths:
        if point[0] not in visited:
            return point[0]
    return False


def lookup_risk(point, risk_values, extents):
    '''Lookup the risk of a point.'''

    lookup_point = (point[0] % extents, point[1] % extents)
    return (risk_values[lookup_point] + (point[0] // extents + point[1] // extents) - 1) % 9 + 1


def find_lowest_risk_path(risk_values, multiplier=1):

    # Assume input is a square
    input_size = int(sqrt(len(risk_values)))
    # The largest x or y co-ordinate on our grid
    extent = (input_size * multiplier) - 1
    visited = set()
    path_cost = {(0, 0): 0}

    while True:
        point = next_point(path_cost, visited)
        # print(
        #     f'point: {point}; len(visited): {len(visited)}; path_cost: \n{pformat(path_cost)}')
        if not point:
            break
        visited.add(point)

        for adj in adjacent_points(point):
            if adj[0] < 0 or adj[0] > extent or adj[1] < 0 or adj[1] > extent:
                continue
            if adj in visited:
                continue
            cost = path_cost[point] + lookup_risk(adj, risk_values, input_size)
            if adj in path_cost and cost >= path_cost[adj]:
                continue
            path_cost[adj] = cost
        if point != (extent, extent):
            del(path_cost[point])

    return path_cost[(extent, extent)]


def main():
    risk_values = load_input(fileinput.input())
    # Assuming the input is a square

    part_1 = find_lowest_risk_path(risk_values)
    print(f'Part 1 lowest total risk: {part_1}')
    part_2 = find_lowest_risk_path(risk_values, 5)
    print(f'Part 2 lowest total risk: {part_2}')


if __name__ == '__main__':
    main()
