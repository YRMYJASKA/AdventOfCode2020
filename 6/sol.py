def part1(filename):
    cc = 0
    with open(filename, "r") as f:
        buff = ""
        for line in f:
            if line.strip() == "":
                cc += len(set(buff))
                buff = ""
                continue
            buff += line.strip()
    cc += len(set(buff))
    return cc


def whole_intersection(sets):
    s = sets[0]
    for d in sets:
        s = s.intersection(d)
    return s


def part2(filename):
    cc = 0
    sets = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                cc += len(whole_intersection(sets))
                sets = []
                continue
            sets.append(set(line.strip()))
    cc += len(whole_intersection(sets))
    return cc


if __name__ == "__main__":
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))
