#!/usr/bin/env python3

import fileinput
from pprint import pprint


def blank_bingo_card():
    '''Returns a blank bingo card.'''

    blank_card = {'rows': [0] * 5,
                  'cols': [0] * 5,
                  'numbers': [],
                  'marks': [],
                  'won': False}

    # 'marks': [[False] * 5] * 5 gives 5 copies of the same list object
    # rather than 5 distinct list objects.
    for row in range(0, 5):
        blank_card['marks'].append([])
        for col in range(0, 5):
            blank_card['marks'][row].append(False)
    return blank_card


def mark_cards(bingo_cards, card_coords):
    '''Mark all the bingo cards listed in card_coords'''

    for card_number, coords in card_coords.items():
        if not bingo_cards[card_number]['won']:
            bingo_cards[card_number]['rows'][coords[0]] += 1
            bingo_cards[card_number]['cols'][coords[1]] += 1
            bingo_cards[card_number]['marks'][coords[0]][coords[1]] = True


def check_card(bingo_card):
    '''Returns true if a card has either a full row or column marked.'''

    return (max(bingo_card['rows'] + bingo_card['cols']) == 5)


def sum_unmarked_numbers(bingo_card):
    '''Returns the sum of all unmarked numbers on a bingo card.'''

    count = 0
    for row in range(0, 5):
        for col in range(0, 5):
            if not bingo_card['marks'][row][col]:
                count += bingo_card['numbers'][row][col]
    return count


def load_bingo_input(bingo_numbers, bingo_cards, bingo_card_numbers, input_file=None):

    bingo_line_count = 0
    for line in fileinput.input(input_file):
        if not bingo_numbers:
            bingo_numbers.extend([int(x) for x in line.rstrip().split(',')])
        elif line.rstrip() == '':
            continue
        else:
            if bingo_line_count == 0:
                bingo_cards.append(blank_bingo_card())
                card_count = len(bingo_cards) - 1

            bingo_line = [int(x) for x in line.rstrip().split(' ') if x != '']

            for col, number in enumerate(bingo_line):
                if number not in bingo_card_numbers:
                    bingo_card_numbers[number] = {}
                bingo_card_numbers[number][card_count] = (
                    bingo_line_count, col)

            bingo_cards[-1]['numbers'].append(bingo_line)
            bingo_line_count = (bingo_line_count + 1) % 5


def find_winners(bingo_numbers, bingo_cards, bingo_card_numbers):

    winners = []
    # last_winning_card = None
    bingo = False
    for number in bingo_numbers:
        if number not in bingo_card_numbers:
            continue

        mark_cards(bingo_cards, bingo_card_numbers[number])
        for card_num in bingo_card_numbers[number].keys():
            if bingo_cards[card_num]['won']:
                continue
            bingo = check_card(bingo_cards[card_num])
            sum = sum_unmarked_numbers(bingo_cards[card_num])

            if bingo:
                # if not last_winning_card:
                #     print(f'BINGO! Number {number}; card number {card_num}')
                #     print(
                #         f'Unmarked numbers: {sum} Multiply: {number * sum}')
                winners.append((card_num, number))
                bingo_cards[card_num]['won'] = True
    return winners


def main():

    # List of bingo numbers given by first line of input
    bingo_numbers = []
    # List of bingo cards, populated when reading input
    bingo_cards = []
    # A dict to track which cards have a given bingo number for quick lookup.
    # bingo_card_numbers[bingo_number][card_num] = (x, y)
    bingo_card_numbers = {}

    load_bingo_input(bingo_numbers, bingo_cards, bingo_card_numbers)
    winners = find_winners(bingo_numbers, bingo_cards, bingo_card_numbers)

    for x in (1, len(winners)):
        sum = sum_unmarked_numbers(bingo_cards[winners[x-1][0]])
        print(
            f'Winner {x}: Bingo number {winners[x-1][1]}; sum of unmarked numbers: {sum}; multiply: {winners[x-1][1] * sum}')


if __name__ == '__main__':
    main()
