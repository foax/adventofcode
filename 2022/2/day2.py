import fileinput
from pprint import pprint

rps_map = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

rps_score = {
    'R': 1,
    'P': 2,
    'S': 3
}

rps_beats = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}

def load_input():
    games = []
    for line in fileinput.input():
        games.append(tuple(line.rstrip().split()))
    return games


def rps(turn):
    '''Return the result of a game of rock, paper, scissors.
    
    0 if player 1 wins, 1 if player 2 wins, -1 if a draw.'''

    if turn[0] == turn[1]:
        return -1
    elif turn[1] == rps_beats[turn[0]]:
        return 0
    else:
        return 1

def part1(game):
    score = rps_score[rps_map[game[1]]]
    winner = rps(list(map(lambda x: rps_map[x], game)))
    if winner == 1:
        score = score + 6
    elif winner == -1:
        score = score + 3
    
    return score

def part2(game):
    their_choice = rps_map[game[0]]
    my_choice = ''
    if game[1] == 'X':
        my_choice = rps_beats[their_choice]
    elif game[1] == 'Z':
        (my_choice,) = {'R', 'P', 'S'} - set(their_choice) - set(rps_beats[their_choice])
    else:
        my_choice = their_choice
    
    score = rps_score[my_choice]
    winner = rps((their_choice, my_choice))
    if winner == 1:
        score = score + 6
    elif winner == -1:
        score = score + 3
    
    return score

def main():
    games = load_input()
    score = [0, 0]
    for game in games:
        score[0] = score[0] + part1(game)
        score[1] = score[1] + part2(game)

#    pprint(games)
    print(f'Part 1: {score[0]}')
    print(f'Part 2: {score[1]}')

if __name__ == "__main__":
    main()
