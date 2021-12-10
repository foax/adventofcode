import fileinput
from collections import Counter

starting_chunks = '([{<'
ending_chunks = ')]}>'

chunks = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

chunk_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def incomplete_chunk_score(stack):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    score = 0
    for x in stack:
        score = score * 5 + points[x]
    return score


def main():
    lines = load_input(fileinput.input(), lambda x: x.strip())

    illegal_chars = []
    incomplete_stacks = []
    for line in lines:
        chunk_stack = []
        for x in line:
            if x in chunks:
                chunk_stack.append(x)
                continue
            start_chunk = chunk_stack.pop()
            if x == chunks[start_chunk]:
                # found matching chunk
                continue
            else:
                # found illegal character
                illegal_chars.append(x)
                chunk_stack = []
                break

        if chunk_stack:
            # print(f'line {line} is incomplete. Stack: {chunk_stack}')
            incomplete_stacks.append(reversed(chunk_stack))

    illegal_char_count = Counter(illegal_chars)
    syntax_error_score = sum([chunk_points[chunk] * count for chunk,
                              count in illegal_char_count.items()])
    print(f'Syntax error score: {syntax_error_score}')

    scores = sorted([incomplete_chunk_score(stack)
                    for stack in incomplete_stacks])
    # print(scores)
    print(f'Incomplete middle score: {scores[len(scores) // 2]}')


if __name__ == '__main__':
    main()
