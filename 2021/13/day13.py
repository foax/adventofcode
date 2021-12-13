import fileinput
import re

def fold_paper(paper, axis, fold_pos):
    new_paper = set()
    idx = {'x': 0, 'y': 1}[axis]
    for coord in paper:
        if coord[idx] == fold_pos:
            continue
        new_coord = list(coord)
        new_coord[idx] = abs(fold_pos - coord[idx]) - 1
        # print(f'{coord} --> {tuple(new_coord)}')
        new_paper.add(tuple(new_coord))
    return new_paper

def paper_str(paper):
    extents = []
    for i in (0,1):
        extents.append(max([x[i] for x in paper]))

    s = [['.' for x in range(extents[0] + 1)] for y in range(extents[1] + 1)]
    for coord in paper:
        s[coord[1]][coord[0]] = '#'
    return '\n'.join([''.join(x) for x in s])


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
        paper = fold_paper(paper, *fold)

    print(paper_str(paper))

if __name__ == '__main__':
    main()

