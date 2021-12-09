import fileinput


class Point:
    def __init__(self, height, up=None, down=None, left=None, right=None):
        self.height = height
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.height)

    def neighbours(self):
        n = set()
        for dir in ('up', 'down', 'left', 'right'):
            if getattr(self, dir):
                n.add(getattr(self, dir))
        return n

    def high_neighbours(self):
        return set([p for p in self.neighbours() if p.height > self.height])

    def get_basin(self, threshold=9):
        basin = set()
        if self.height < threshold:
            basin.add(self)
        for point in self.high_neighbours():
            basin |= point.get_basin(threshold=threshold)
        return basin


class Heightmap:
    def __init__(self, lines):
        self.points = []
        for x, line in enumerate(lines):
            self.points.append([])
            for y, height in enumerate(line):
                p = Point(int(height))
                self.points[-1].append(p)
                if y > 0:
                    p.left = self.points[x][y - 1]
                    p.left.right = p
                if x > 0:
                    p.up = self.points[x - 1][y]
                    p.up.down = p

    def __str__(self):
        x = ''
        for line in self.points:
            for point in line:
                x += str(point)
            x += '\n'
        return x

    def __iter__(self):
        for line in self.points:
            for point in line:
                yield point


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def main():
    input = load_input(fileinput.input(), lambda x: [
                       int(y) for y in x.strip()])

    heightmap = Heightmap(input)
    low_points = []
    for point in heightmap:
        if len(point.neighbours()) == len(point.high_neighbours()):
            low_points.append(point)

    print(f'Sum of risk levels: {sum([x.height + 1 for x in low_points])}')

    basins = [p.get_basin() for p in low_points]
    basin_sizes = sorted([len(x) for x in basins])
    print(
        f'3 largest basin sizes multiplied: {basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]}')


if __name__ == '__main__':
    main()
