import fileinput


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def spawn_lanternfish(seed, days, internal_timer=7, extra_days=2):

    max_size = internal_timer + extra_days
    fish_count = [seed.count(x) for x in range(max_size)]

    for x in range(days):
        new_count = [0] * max_size
        for fish in range(1, max_size):
            new_count[fish - 1] = fish_count[fish]
        new_count[max_size - 1] = fish_count[0]
        new_count[internal_timer - 1] += fish_count[0]
        fish_count = new_count

    return sum(fish_count)


def main():
    numbers = load_input(fileinput.input(), lambda x: [
                         int(x) for x in x.rstrip().split(',')])[0]

    part_1 = spawn_lanternfish(numbers, 18)
    part_2 = spawn_lanternfish(numbers, 256)
    print(f'part 1: {part_1}; part 2: {part_2}')


if __name__ == '__main__':
    main()
