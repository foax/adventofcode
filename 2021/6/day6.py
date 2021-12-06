import fileinput


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def spawn_lanternfish(seed, max_days, internal_timer=7, extra_days=2):

    fish_count = {x: seed.count(x) for x in set(seed)}

    for x in range(0, max_days):
        new_count = {}
        for fish, count in fish_count.items():
            if fish >= internal_timer:
                new_fish = fish - 1
            else:
                new_fish = (fish - 1) % internal_timer

            if new_fish == internal_timer - 1 and fish != internal_timer:
                new_count[internal_timer + extra_days - 1] = count
            if new_fish in new_count:
                new_count[new_fish] += count
            else:
                new_count[new_fish] = count
        fish_count = new_count

    return sum([x for _, x in fish_count.items()])


def main():
    numbers = load_input(fileinput.input(), lambda x: [
                         int(x) for x in x.rstrip().split(',')])[0]

    part_1 = spawn_lanternfish(numbers, 18)
    part_2 = spawn_lanternfish(numbers, 256)
    print(f'part 1: {part_1}; part 2: {part_2}')


if __name__ == '__main__':
    main()
