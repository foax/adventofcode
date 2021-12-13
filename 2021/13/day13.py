import fileinput
import re

def load_input(iterator, func=lambda x: x):
    return [func(line) for line in iterator]

def fold_paper(paper, fold):
    new_paper = set()
    idx = {'x': 0, 'y': 1}[fold[0]]
    for coord in paper:
        if coord[idx] == fold[1]:
            continue
        new_coord = list(coord)
        new_coord[idx] = abs(fold[1] - coord[idx]) - 1
        print(f'{coord} --> {tuple(new_coord)}')
        new_paper.add(tuple(new_coord))
    return new_paper

def paper_str(paper):
    max = [0, 0]
    for coord in paper:
        for i in range(2):
            if coord[i] > max[i]:
                max[i] = coord[i]
    
    s = ''
    for y in range(max[1] + 1):
        for x in range(max[0] + 1):
            if (x, y) in paper:
                s += '#'
            else:
                s += '.'
        s += '\n'
    return s


def main():
    paper = set()
    folds = None


    for line in fileinput.input():
        if folds == None:
            if line.strip() == '':
                folds = []
                continue
            coords = tuple([int(x) for x in line.strip().split(',')])
            paper.add(coords)
        else:
            match = re.match('fold along ([xy])=(\d+)', line.strip())
            folds.append((match.group(1), int(match.group(2))))


    for fold in folds:
        paper = fold_paper(paper, fold)

    print(paper_str(paper))

if __name__ == '__main__':
    main()

