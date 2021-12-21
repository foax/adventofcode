import fileinput
import re

def process_pair(input):
    pair = None
    num = None
    j = None

    for i, x in enumerate(input):
        if j is not None and i <= j:
            continue
        if x == '[':
            if pair is None:
                pair = []
            else:
                sub_pair, j = process_pair(input[i:])
                j += i
                pair.append(sub_pair)
        elif re.match('\d', x):
            if num is None:
                num = int(x)
            else:
                num = num * 10 + int(x)
        elif x == ',' or x == ']':
            if num is not None:
                pair.append(num)
            num = None
            if x == ']':
                return pair, i

    # If we get here, we have a mismatching bracket
    return None

def load_input(iterator):
    snailfishes = []
    for line in iterator:
        snailfish, _ = process_pair(line.strip())
        snailfishes.append(snailfish)
    return snailfishes

def add_to_rightmost(pair, num):
    if type(pair[1]) == int:
        pair[1] += num
    else:
        add_to_rightmost(pair[1], num)

def explode_snailfish(snailfish):
    queue = []
    pair = snailfish
    depth = 0
    i = 0
    exploded_pair = None
    while True:
        if depth == 4 and exploded_pair is None:
            exploded_pair = pair.copy()
            for q, j in reversed(queue):
                if j == 1:
                    if type(q[0]) == int:
                        q[0] += exploded_pair[0]
                    else:
                        add_to_rightmost(q[0], exploded_pair[0])
                    break
            pair, i = queue.pop()
            pair[i] = 0
            i += 1
            depth -= 1
        elif i > 1:
            if queue:
                pair, i = queue.pop()
                i += 1
                depth -= 1
            else:
                break
        elif type(pair[i]) == list:
            depth += 1
            queue.append((pair, i))
            pair = pair[i]
            i = 0
        else:
            if exploded_pair:
                pair[i] += exploded_pair[1]
                break
            i += 1
    return bool(exploded_pair)

def split_snailfish(snailfish):
    for i, x in enumerate(snailfish):
        if type(x) == int:
            if x >= 10:
                y = x // 2
                snailfish[i] = [y, x-y]
                return True
        else:
            if split_snailfish(x):
                return True
    return False

def reduce_snailfish(snailfish):
    result = True
    while result:
        result = explode_snailfish(snailfish)
        if not result:
            result = split_snailfish(snailfish)

def magnitude(snailfish):
    result = 0
    factor = {0: 3, 1: 2}
    for i, x in enumerate(snailfish):
        if type(x) == int:
            result += factor[i] * x
        else:
            result += factor[i] * magnitude(x)
    return result


def main():
    snailfishes = load_input(fileinput.input())
    a = snailfishes[0]
    for b in snailfishes[1:]:
        a = [a, b]
        reduce_snailfish(a)
    print(f'Magnitude: {magnitude(a)}')


if __name__ == '__main__':
    main()