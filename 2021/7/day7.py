import fileinput
from collections import Counter


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def crab_fuel(chosen_crab, crab_count, fuel_factor=lambda x: x):
    fuel = 0
    for crab in crab_count:
        fuel += fuel_factor(abs(crab - chosen_crab)) * crab_count[crab]
    return fuel


def triangular_number(x):
    # 1 = 1; 2 = 3; 3 = 6; 4 = 10...
    return ((x ** 2) + x) // 2


def part_1(crabs):
    fuel_used = Counter(
        {crab: crab_fuel(crab, crabs) for crab in range(0, max(crabs) + 1)})
    return fuel_used.most_common()[-1]


def part_2(crabs):
    fuel_used = Counter(
        {crab: crab_fuel(crab, crabs, fuel_factor=triangular_number) for crab in range(0, max(crabs) + 1)})
    return fuel_used.most_common()[-1]


def main():
    input = load_input(fileinput.input(), lambda x: [
                       int(y) for y in x.rstrip().split(',')])[0]
    crabs = Counter(input)
    fuel_used = Counter({crab: crab_fuel(crab, crabs) for crab in crabs})

    part_1_answer = part_1(crabs)
    part_2_answer = part_2(crabs)

    print(f'Part 1: {part_1_answer}; part 2: {part_2_answer}')


if __name__ == '__main__':
    main()
