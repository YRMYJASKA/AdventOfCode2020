import numpy as np
import copy


def adj_num(i, j, data):
    cc = 0
    locs = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1),
            (i+1, j), (i+1, j+1)]
    for row, col in locs:
        if row >= len(data) or row < 0:
            continue
        elif col >= len(data[row]) or col < 0:
            continue
        if data[row][col] == "#":
            cc += 1
    return cc


def part1(data):
    change = True
    current = data
    while change:
        new = copy.deepcopy(current)
        change = False
        for row in range(len(current)):
            for column in range(len(current[row])):
                seat = current[row][column]
                if seat == ".":
                    continue
                count_adj = adj_num(row, column, current)
                if count_adj == 0 and seat == "L":
                    new[row][column] = "#"
                    change = True
                elif count_adj >= 4 and seat == "#":
                    new[row][column] = "L"
                    change = True
        current = copy.deepcopy(new)

    # Count occupied
    cc = 0
    for row in current:
        for e in row:
            if e == "#":
                cc += 1
    return cc


def sight_num(i, j, data):
    cc = 0
    slopes = [(1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1),
              (1, -1), (0, -1), (1, 0)]
    for x, y in slopes:
        ni, nj = i, j
        while True:
            ni += x
            nj += y
            if ni >= len(data) or ni < 0 or nj >= len(data[1]) or nj < 0:
                break
            if data[ni][nj] == "#":
                cc += 1
                break
            if data[ni][nj] == "L":
                break
    return cc


def part2(data):
    change = True
    current = data
    while change:
        new = copy.deepcopy(current)
        change = False
        for row in range(len(current)):
            for column in range(len(current[row])):
                seat = current[row][column]
                if seat == ".":
                    continue
                count_adj = sight_num(row, column, current)
                if count_adj == 0 and seat == "L":
                    new[row][column] = "#"
                    change = True
                elif count_adj >= 5 and seat == "#":
                    new[row][column] = "L"
                    change = True
        current = copy.deepcopy(new)
        # for l in current:
        #     print("".join(l))

    # Count occupied
    cc = 0
    for row in current:
        for e in row:
            if e == "#":
                cc += 1
    return cc
    pass


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            row = []
            for c in l.strip():
                row.append(c)
            idata.append(row)
    idata = np.array(idata)
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
