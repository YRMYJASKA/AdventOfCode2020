import numpy as np

data = []

with open("../input.txt", "r") as f:
    for line in f:
        data.append(int(line))

data_i = np.array(data)


def part1(data):

    full = np.array([2020]*len(data))
    full = full - data

    for x in full:
        if x in data:
            return x,(2020-x)


def part2(data):
    data = set(data)
    for x in data:
        for y in data:
            if 2020 - x - y in data:
                return x, y, 2020-x-y

if __name__=="__main__":
    print("part 1:", np.prod(part1(data_i)))
    print("part 2:", np.prod(part2(data_i)))
