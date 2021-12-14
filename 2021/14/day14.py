import fileinput
from collections import Counter


class ListItem():
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_elements(polymer, rules):
    i = 0
    while i < len(polymer) - 1:
        pair = ''.join(polymer[i:i+2])
        if pair in rules:
            polymer.insert(i+1, rules[pair])
            i += 1
        i += 1


def main():
    polymer_template = None
    insertion_rules = {}

    for line in fileinput.input():
        if line == '\n':
            continue
        if polymer_template == None:
            polymer_template = list(line.strip())
        else:
            rule = line.strip().split(' -> ')
            insertion_rules[rule[0]] = rule[1]

    # print(polymer_template)
    # print(insertion_rules)
    # insert_elements(polymer_template, insertion_rules)
    print(polymer_template)

    for x in range(40):
        insert_elements(polymer_template, insertion_rules)
        print(x, len(polymer_template))

    count = Counter(polymer_template).most_common()
    print(
        f'Most common: {count[0]}; Least common: {count[-1]}; Difference: {count[0][1] - count[-1][1]}')


if __name__ == '__main__':
    main()
