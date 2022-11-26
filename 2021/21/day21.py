import fileinput

def load_input(iterator):
    return [int(line.strip().split(': ')[1]) for line in iterator]

def deterministic_dice(sides):
    x = 1
    while True:
        yield x
        x = (x % sides) + 1 

def play_dirac(start_pos, dice, limit=1000):
    scores = [0, 0]
    pos = start_pos.copy()
    player = 0
    roll_count = 0
    while max(scores) < limit:
        roll = 0
        for _ in range(3):
            roll += next(dice)
        roll_count += 3
        pos[player] = (pos[player] - 1 + roll) % 10 + 1
        scores[player] += pos[player]
        player = (player + 1) % 2
    return scores, roll_count

def main():
    start_pos = load_input(fileinput.input())
    scores, roll_count = play_dirac(start_pos, deterministic_dice(100))
    print(f'Part 1: {min(scores) * roll_count}')

if __name__ == '__main__':
    main()