from copy import deepcopy


def part1(data):
    state = deepcopy(data)
    for i in range(6):
        curr = deepcopy(state)
        # get bounds
        themin = min([min(list(p)) for p in state]) - 1
        themax = max([max(list(p)) for p in state]) + 1
        for x in range(themin, themax+1):
            for y in range(themin, themax+1):
                for z in range(themin, themax+1):
                    s = 0
                    for x0 in range(-1, 2):
                        for y0 in range(-1, 2):
                            for z0 in range(-1, 2):
                                if x0 == 0 and y0 == 0 and z0 == 0:
                                    continue
                                if (x+x0, y+y0, z+z0) in state:
                                    s += 1
                    if (x, y, z) in state:
                        if s not in [2, 3]:
                            curr.remove((x, y, z))
                    else:
                        if s == 3:
                            curr.add((x, y, z))
        state = deepcopy(curr)

    return len(state)


def part2(data):
    # Prep the data

    state = set()
    for (x, y, z) in data:
        state.add((x, y, z, 0))

    for i in range(6):
        curr = deepcopy(state)
        # get bounds
        themin = min([min(list(p)) for p in state]) - 1
        themax = max([max(list(p)) for p in state]) + 1
        for x in range(themin, themax+1):
            for y in range(themin, themax+1):
                for z in range(themin, themax+1):
                    for w in range(themin, themax+1):
                        s = 0
                        # Sum
                        for x0 in range(-1, 2):
                            for y0 in range(-1, 2):
                                for z0 in range(-1, 2):
                                    for w0 in range(-1, 2):
                                        if x0 == 0 and y0 == 0 and z0 == 0 and w0 == 0:
                                            continue
                                        if (x+x0, y+y0, z+z0, w+w0) in state:
                                            s += 1
                        if (x, y, z, w) in state:
                            if s not in [2, 3]:
                                curr.remove((x, y, z, w))
                        else:
                            if s == 3:
                                curr.add((x, y, z, w))
        state = deepcopy(curr)

    return len(state)


if __name__ == "__main__":
    idata = set()
    with open("input.txt", "r") as f:
        y = 0
        for l in f:
            dim = len(l.strip())
            for x in range(dim):
                if l.strip()[x] == "#":
                    idata.add((x, y, 0))
            y += 1
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
