import fileinput


class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.nearby = set()

    def add_nearby(self, o):
        self.nearby.add(o)
        o.nearby.add(self)

    def incr(self):
        self.energy += 1
        return (self.energy == 10)

    def __str__(self):
        return str(self.energy)


class OctopusMap:
    def __init__(self, grid):
        self.grid = []

        for x, line in enumerate(grid):
            new_line = []
            self.grid.append(new_line)
            for y, energy in enumerate(line):
                octopus = Octopus(energy)
                new_line.append(octopus)
                for i, j in ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1)):
                    if i < 0 or j < 0 or j >= len(self.grid[i]):
                        continue
                    self.grid[i][j].add_nearby(octopus)

    def __str__(self):
        return '\n'.join(' '.join(str(s) for s in line) for line in self.grid)

    def __iter__(self):
        for line in self.grid:
            for octopus in line:
                yield octopus

    def __len__(self):
        return sum([len(x) for x in self.grid])

    def energy_step(self, limit=None):

        i = 0
        while limit == None or i < limit:

            flashing = set()
            for o in self:
                if o.incr():
                    flashing.add(o)

            iter_flashing = flashing.copy()
            while iter_flashing:
                new_flashing = set()
                for o in iter_flashing:
                    for nearby in o.nearby:
                        if nearby.incr():
                            new_flashing.add(nearby)
                flashing |= new_flashing
                iter_flashing = new_flashing.copy()

            flashes = len(flashing)
            for o in flashing:
                o.energy = 0

            yield len(flashing)
            i += 1


def parse_line(line):
    return [int(x) for x in line.strip()]


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def main():
    input = load_input(fileinput.input(), parse_line)
    o = OctopusMap(input)

    flash_sum = 0
    sizeof_o = len(o)
    all_flash_step = 0
    step = 1

    for flashes in o.energy_step():
        if step <= 100:
            flash_sum += flashes
        if flashes == sizeof_o:
            all_flash_step = step
        if step > 100 and all_flash_step:
            break
        step += 1

    print(f'part 1: {flash_sum}')
    print(f'part 2: {all_flash_step}')


if __name__ == '__main__':
    main()
