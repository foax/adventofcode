#!/usr/bin/env python3

import fileinput
from pprint import pprint


def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]


def blank_bingo_card_marks():
    blank_card = {'rows': [0] * 5,
                  'cols': [0] * 5,
                  'numbers': [],
                  'marks': [],
                  'won': False}

    for row in range(0, 5):
        blank_card['marks'].append([])
        for col in range(0, 5):
            blank_card['marks'][row].append(False)
    return blank_card


def mark_cards(bingo_cards, numbers_dict):
    for number, coords in numbers_dict.items():
        if not bingo_cards[number]['won']:
            bingo_cards[number]['rows'][coords[0]] += 1
            bingo_cards[number]['cols'][coords[1]] += 1
            bingo_cards[number]['marks'][coords[0]][coords[1]] = True


def check_card(bingo_card):
    return (max(bingo_card['rows'] + bingo_card['cols']) == 5)


def count_unmarked_numbers(bingo_card):
    count = 0
    for row in range(0, 5):
        for col in range(0, 5):
            if not bingo_card['marks'][row][col]:
                count += bingo_card['numbers'][row][col]
    return count


def main():

    bingo_numbers = None
    bingo_cards = []
    already_won = []
    bingo_line_count = 0

    # {
    #   bingo_card_number:
    #     {
    #        board_num: (x, y),
    #        ...
    #     },
    #   ...
    # }

    bingo_card_numbers = {}

    for line in fileinput.input():
        if not bingo_numbers:
            bingo_numbers = [int(x) for x in line.rstrip().split(',')]
        elif line.rstrip() == '':
            continue
        else:
            if bingo_line_count == 0:
                bingo_card = blank_bingo_card_marks()
                bingo_cards.append(bingo_card)
                board_count = len(bingo_cards) - 1
            bingo_line = [int(x) for x in line.rstrip().split(' ') if x != '']

            for row, number in enumerate(bingo_line):
                if number not in bingo_card_numbers:
                    bingo_card_numbers[number] = {}
                bingo_card_numbers[number][board_count] = (
                    bingo_line_count, row)

            bingo_card['numbers'].append(bingo_line)
            bingo_line_count = (bingo_line_count + 1) % 5

    bingo = False
    for number in bingo_numbers:
        if number not in bingo_card_numbers:
            continue
        mark_cards(bingo_cards, bingo_card_numbers[number])
        for card_num in bingo_card_numbers[number].keys():
            if bingo_cards[card_num]['won']:
                continue
            bingo = check_card(bingo_cards[card_num])
            sum = count_unmarked_numbers(bingo_cards[card_num])
            if bingo:
                if len(already_won) == 0:
                    print(f'BINGO! Number {number}; Card number {card_num}')
                    print(
                        f'Unmarked numbers: {sum}')
                    print(f'Multiply: {number * sum}')
                print(f'BINGO! Number {number}; Card number {card_num}')
                already_won.append((card_num, number))
                bingo_cards[card_num]['won'] = True

    pprint(already_won)
    (card_num, bingo_number) = already_won[-1]
    sum = count_unmarked_numbers(bingo_cards[card_num])
    print(
        f'The last winning card was {card_num}; bingo number was {bingo_number}; unmarked numbers sum: {sum}; multiply: {bingo_number * sum}')
    # pprint(bingo_numbers)
    # pprint(bingo_cards)
    # pprint(bingo_card_numbers)
    # pprint(bingo_card_marks)


if __name__ == '__main__':
    main()
