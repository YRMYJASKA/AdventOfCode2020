import numpy as np

def part1(data):
    x, y = (0,0)
    cc = 0
    width =  len(data[0])
    while y < len(data):
        loc = data[y][x % width]
        #print(x,y, loc)
        if loc == "#":
            cc += 1
        y += 1
        x += 3
    return cc

def part2(data):
    deltas = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    res = []
    for d in deltas:
        x, y = (0,0)
        cc = 0
        width =  len(data[0])
        while y < len(data) + 1 - d[0]:
            loc = data[y][x % width]
            #print(x,y, loc)
            if loc == "#":
                cc += 1
            y += d[0]
            x += d[1]
        res.append(cc)
    return np.prod(res)

if __name__ == "__main__":
    data = []
    with open("input.txt") as f:
        for line in f:
            data.append(line.strip())
    data = np.array(data)
    print(part1(data))
    print(part2(data))
