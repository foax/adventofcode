import fileinput
from collections import Counter


class ListItem():
    def __init__(self, value):
        self.value = value
        self.next = None


def insert_elements(start, rules):
    cur = start
    while cur.next:
        pair = cur.value + cur.next.value
        if pair in rules:
            p = ListItem(rules[pair])
            p.next = cur.next
            cur.next = p
            cur = cur.next
        cur = cur.next


def convert_to_list(start):
    l = []
    cur = start
    while cur:
        l.append(cur.value)
        cur = cur.next
    return l


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

    start = None
    last = None
    for p in polymer_template:
        polymer = ListItem(p)
        if not start:
            start = polymer
        else:
            last.next = polymer
        last = polymer

    print(convert_to_list(start))
    for x in range(10):
        print(x)
        insert_elements(start, insertion_rules)

    count = Counter(convert_to_list(start)).most_common()
    print(
        f'Most common: {count[0]}; Least common: {count[-1]}; Difference: {count[0][1] - count[-1][1]}')


if __name__ == '__main__':
    main()
