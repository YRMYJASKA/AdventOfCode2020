import numpy as np


def part1(data):
    j1 = 0
    j3 = 1
    curr = 0
    while True:
        # print(curr)
        # print("j1, j3 =", j1, j3)
        d = data - np.array([curr]*len(data))
        # print(d)
        positives = np.array([e for e in d if (e > 0)])
        if len(positives) == 0:
            break
        m = np.min(positives)
        if m > 3:
            break
        curr += m
        if m == 1:
            j1 += 1
        elif m == 3:
            j3 += 1

    return j1*j3


memo = {}
def part2(data, curr=0):
    if curr in memo.keys():
        return memo[curr]
    d = data - np.array([curr]*len(data))
    positives = np.array([e for e in d if (e > 0)])
    if len(positives) == 0:
        memo[curr] = 1
        return 1
    cc = 0
    if 1 in d:
        cc += part2(data, curr + 1)
    if 2 in d:
        cc += part2(data, curr + 2)
    if 3 in d:
        cc += part2(data, curr + 3)
    memo[curr] = cc
    return cc


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            idata.append(int(l.strip()))
    idata = np.array(idata)
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
