import fileinput

def load_input():
    calories = []
    x = 0
    for line in fileinput.input():
        line = line.rstrip()
        if line == "":
            calories.append(x)
            x = 0
            continue
        x = x + int(line)
    if x:
        calories.append(x)
    return calories

def main():
    calories = load_input()
    print(f"Part 1: {max(calories)}")
    print(f"Part 2: {sum(sorted(calories)[-3:])}")

if __name__ == '__main__':
    main()
