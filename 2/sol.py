
idata = []
with open("input.txt", "r") as f:
    for line in f:
        linef = line.strip().split(" ")
        idata.append([int(linef[0].split("-")[0]), int(linef[0].split("-")[1]),linef[1][0], linef[-1]])

def part1(data):
    summa = 0
    for d in data:
        cc = d[3].count(d[2])
        if d[0] <= cc and cc <= d[1]:
            summa += 1
    return summa

def part2(data):
    summa = 0
    for d in data:
        c = d[2]
        if (c == d[3][d[0]-1])^(c == d[3][d[1]-1]): 
            summa += 1
    return summa


if __name__ == "__main__":
    print("part 1:", part1(idata))
    print("part 2:", part2(idata))
