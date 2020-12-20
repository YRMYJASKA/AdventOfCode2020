import numpy as np

ROWS = 128
COLUMNS = 8


def seatid(row, column):
    return 8*row + column


def part1(data):
    maxid = 0
    for d in data:
        col_min, row_min = (0, 0)
        col_max, row_max = (COLUMNS, ROWS)
        # Determine row
        for i in range(7):
            c = d[i]
            if c == "B":
                row_min = row_min + (row_max - row_min)//2
            else:
                row_max = row_max - (row_max - row_min)//2

        # determine column
        for i in range(3):
            c = d[7 + i]
            if c == "R":
                col_min = col_min + (col_max - col_min)//2
            else:
                col_max = col_max - (col_max - col_min)//2
        row = row_min
        col = col_min
        maxid = max(maxid, seatid(row, col))

    return maxid


def part2(data):
    punch_card = np.array([True]*(128*8))
    for d in data:
        col_min, row_min = (0, 0)
        col_max, row_max = (COLUMNS, ROWS)
        # Determine row
        for i in range(7):
            c = d[i]
            if c == "B":
                row_min = row_min + (row_max - row_min)//2
            else:
                row_max = row_max - (row_max - row_min)//2

        # determine column
        for i in range(3):
            c = d[7 + i]
            if c == "R":
                col_min = col_min + (col_max - col_min)//2
            else:
                col_max = col_max - (col_max - col_min)//2
        row = row_min
        col = col_min
        punch_card[seatid(row, col)] = False
    rets = []
    for i in range(len(punch_card)):
        if punch_card[i]:
            rets.append(i)
    # find isolated value
    last = rets[0]
    for e in rets[1:]:
        if e != last + 1:
            return e
        last = e


if __name__ == "__main__":
    idata = np.array([])
    with open("input.txt", "r") as f:
        for line in f:
            idata = np.append(idata, line.strip())
    print(part1(idata))
    print(part2(idata))
