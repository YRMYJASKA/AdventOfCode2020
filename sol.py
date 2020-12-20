def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            idata.append(l.strip())
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
