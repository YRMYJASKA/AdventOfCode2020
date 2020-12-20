def part1(data, lim=2020):
    locations = {}
    # first pass through the data
    for i in range(len(data)-1):
        locations[data[i]] = i

    # Then start iterating
    curr = data[-1]
    for i in range(len(data)-1, lim):
        prev = curr
        if curr in locations.keys():
            curr = i - locations[curr]
        else:
            curr = 0
        locations[prev] = i
    return prev


if __name__ == "__main__":
    example = [0, 3, 6]
    idata = [0, 14, 1, 3, 7, 9]
    print("Part 1:", part1(idata))
    print("Part 2:", part1(idata, 30000000))
