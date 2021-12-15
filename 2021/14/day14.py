import fileinput
from collections import Counter, defaultdict


def polymer_step(count, rules):
    new_counts = Counter()
    for pair, pair_count in count.items():
        if pair in rules:
            for new_pair in rules[pair]:
                new_counts[new_pair] += pair_count
    return new_counts


def solve_part(polymer, rules, steps):
    pair_counts = Counter()
    for i in range(len(polymer) - 1):
        pair_counts[polymer[i:i+2]] += 1

    for i in range(steps):
        pair_counts = polymer_step(pair_counts, rules)

    letter_count = Counter()
    for pair, count in pair_counts.items():
        letter_count[pair[0]] += count
    letter_count[polymer[-1]] += 1
    most_common = letter_count.most_common()[0]
    least_common = letter_count.most_common()[-1]

    print(
        f'After {steps} steps - Most common: {most_common} Least common: {least_common} Diff: {most_common[1] - least_common[1]}')


def main():
    polymer = None
    insertion_pairs = {}

    for line in fileinput.input():
        if line == '\n':
            continue
        if polymer == None:
            polymer = line.strip()
        else:
            rule = line.strip().split(' -> ')
            insertion_pairs[rule[0]] = (
                rule[0][0] + rule[1], rule[1] + rule[0][1])

    solve_part(polymer, insertion_pairs, 10)
    solve_part(polymer, insertion_pairs, 40)


if __name__ == '__main__':
    main()
