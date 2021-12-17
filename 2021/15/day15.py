import fileinput
from math import sqrt


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
    yield (point[0], point[1] + 1)
    yield (point[0] + 1, point[1])
    # yield (point[0] - 1, point[1])
    # yield (point[0], point[1] - 1)


def iter_point(point, point_set, extents):
    '''A generator that yields valid next points to try, in the order
    of S, E, N, W. Excludes next points that would be adjacent to existing
    points.'''

    our_set = point_set.copy()
    # print(
    #     f'iter point - point: {point}; point_set: {point_set}; extents: {extents}')

    for next_point in adjacent_points(point):
        # print(f'Trying adjacent point {next_point}')
        if next_point[0] < 0 or next_point[0] > extents or next_point[1] < 0 or next_point[1] > extents:
            # print(f'Out of bounds')
            continue
        if point_set & {next_point}:
            continue
        if (set(adjacent_points(next_point)) - {point}) & our_set:
            # print(last_point)
            # print(set(adjacent_points(next_point)))
            # print((set(adjacent_points(next_point)) - {point}))
            # print(our_set)
            # print((set(adjacent_points(next_point)) - {point}) & our_set)
            continue
        yield next_point


def main():
    risk_values = load_input(fileinput.input())
    print(risk_values)
    extents = int(sqrt(len(risk_values))) - 1
    coord_set = set()

    # Keep a queue of [ (x, y), iteration_number ]
    queue = [((0, 0), iter_point((0, 0), coord_set, extents))]

    # And a set of (x, y) co-ordinates for easy checking
    coord_set = {(0, 0)}

    # Keep a tab of the lowest risk found so far, no point continuing
    # a path if the current path has more risk than this.
    lowest_risk = None

    risk = 0

    iteration = -1
    while len(queue) > 0:
        iteration += 1
        # print(coord_set)
        # print([x[0] for x in queue])
        cur_point = queue[-1]
        if iteration % 100000 == 0:
            print(
                f'cur_point: {cur_point[0]}; risk: {risk}; lowest_risk: {lowest_risk}; queue length: {len(queue)}')

        if cur_point[0] == (extents, extents):
            if lowest_risk is None or risk < lowest_risk:
                lowest_risk = risk
        elif lowest_risk is not None and risk >= lowest_risk:
            risk -= risk_values[(cur_point[0])]
            coord_set.remove(cur_point[0])
            queue.pop()
            continue

        try:
            next_point = next(cur_point[1])
            # print(f'next point: {next_point}')
            queue.append((next_point, iter_point(
                next_point, coord_set, extents)))
            coord_set.add(next_point)
            risk += risk_values[next_point]
        except StopIteration:
            # print(f'No more next points')
            risk -= risk_values[(cur_point[0])]
            coord_set.remove(cur_point[0])
            queue.pop()

    print(lowest_risk)


if __name__ == '__main__':
    main()
