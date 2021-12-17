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
    for adj in (point[0], point[1] + 1), (point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] - 1):
        yield adj

# def valid_adj_points(point, visited, extents):


def next_point(path_cost, visited):
    low_cost_paths = sorted(path_cost.items(), key=lambda x: x[1])
    for point in low_cost_paths:
        if point[0] not in visited:
            return point[0]
    return False


def lookup_risk(point, risk_values, extents):
    lookup_point = (point[0] % extents, point[1] % extents)
    return (risk_values[lookup_point] + (point[0] // extents + point[1] // extents) - 1) % 9 + 1


def main():
    risk_values = load_input(fileinput.input())
    # print(risk_values)
    input_size = int(sqrt(len(risk_values)))
    extent = (input_size * 5) - 1
    visited = set()
    path_cost = {(0, 0): 0}

    while True:
        point = next_point(path_cost, visited)
        # print(
        #     f'point: {point}; len(visited): {len(visited)}; path_cost: {pformat(path_cost)}')
        if not point:
            break
        visited.add(point)
        for adj in adjacent_points(point):
            if adj[0] < 0 or adj[0] > extent or adj[1] < 0 or adj[1] > extent:
                continue
            if adj in visited:
                continue
            # if {adjacent_points(adj)} & visited:
            #     continue
            cost = path_cost[point] + lookup_risk(adj, risk_values, input_size)
            if adj in path_cost and cost >= path_cost[adj]:
                continue
            path_cost[adj] = cost
        if point != (extent, extent):
            del(path_cost[point])

    print(path_cost[(extent, extent)])


if __name__ == '__main__':
    main()
