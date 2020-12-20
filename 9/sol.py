import numpy as np


def part1(data):
    for i in range(25, len(data)):
        preample = set(data[i-25:i])
        curr = data[i]
        valid = False
        for x in preample:
            if curr - x in preample:
                valid = True
                break
        if not valid:
            return int(curr)


def part2(data):
    invalid = part1(data)
    # sliding window tactic
    low, high = 0, 1
    while True:
        r = data[low:high]
        ss = np.sum(r)
        if ss == invalid:
            return int(np.max(r) + np.min(r))
        elif ss > invalid:
            low += 1
        else:
            high += 1


if __name__ == "__main__":
    idata = np.array([])
    with open("input.txt", "r") as f:
        for l in f:
            idata = np.append(idata, np.array([int(l.strip())]))

    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
