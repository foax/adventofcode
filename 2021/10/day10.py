import fileinput

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
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for x in stack:
        score = score * 5 + points[x]
    return score


def main():
    lines = load_input(fileinput.input(), lambda x: x.strip())

    syntax_error_score = 0
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

            # found illegal character
            syntax_error_score += chunk_points[x]
            chunk_stack = None
            break

        if chunk_stack:
            chunk_stack.reverse()
            incomplete_stacks.append(incomplete_chunk_score(chunk_stack))

    print(f'Syntax error score: {syntax_error_score}')

    middle_score = sorted(incomplete_stacks)[len(incomplete_stacks) // 2]
    print(
        f'Incomplete middle score: {middle_score}')


if __name__ == '__main__':
    main()
