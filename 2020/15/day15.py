import fileinput

def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]

def parse_line(line):
    return [int(x) for x in line.strip().split(',')]

def play_memory_game(starting_numbers, until):
    last_pos = {}
    our_starting_numbers = starting_numbers.copy()
    last_number = None

    for x in range(until):
        # print(f'x: {x}; last_number: {last_number}; last_pos: {last_pos}')
        if our_starting_numbers:
            number = our_starting_numbers.pop(0)
        else:
            if last_number in last_pos:
                number = x - last_pos[last_number] - 1
            else:
                number = 0
        if last_number != None:
            last_pos[last_number] = x - 1
        last_number = number
    return last_number

def main():
    starting_numbers = load_input(fileinput.input(), func=parse_line)[0]
    part_1 = play_memory_game(starting_numbers, 2020)
    part_2 = play_memory_game(starting_numbers, 30000000)
    print(f'part 1: {part_1}; part_2: {part_2}')

if __name__ == '__main__':
    main()