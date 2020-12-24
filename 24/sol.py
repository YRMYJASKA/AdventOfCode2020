from copy import deepcopy


def part1(data):
    blacks = []
    for d in data:
        coord = [0, 0, 0]
        for m in d:
            if m == "e":
                coord[0] += 1
                coord[1] -= 1
            elif m == "w":
                coord[0] -= 1
                coord[1] += 1
            elif m == "ne":
                coord[0] += 1
                coord[2] -= 1
            elif m == "se":
                coord[1] -= 1
                coord[2] += 1
            elif m == "sw":
                coord[0] -= 1
                coord[2] += 1
            elif m == "nw":
                coord[1] += 1
                coord[2] -= 1
        if coord in blacks:
            blacks.remove(coord)
        else:
            blacks.append(coord)

    return len(blacks)


def part2(data):
    # First figure out initial black tiles
    blacks = set()
    for d in data:
        coord = [0, 0, 0]
        for m in d:
            if m == "e":
                coord[0] += 1
                coord[1] -= 1
            elif m == "w":
                coord[0] -= 1
                coord[1] += 1
            elif m == "ne":
                coord[0] += 1
                coord[2] -= 1
            elif m == "se":
                coord[1] -= 1
                coord[2] += 1
            elif m == "sw":
                coord[0] -= 1
                coord[2] += 1
            elif m == "nw":
                coord[1] += 1
                coord[2] -= 1
        coords = ",".join(map(str, coord))
        if coords in blacks:
            blacks.remove(coords)
        else:
            blacks.add(coords)
    # Iterate 100 days
    for _ in range(100):
        temp_blacks = deepcopy(blacks)
        possible_whites = {}

        for bs in blacks:
            b = list(map(int, bs.split(",")))
            d = [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (0, -1, 1),
                 (-1, 0, 1), (0, 1, -1)]
            ac = 0
            for dx, dy, dz in d:
                sr = ",".join(map(str, [b[0] + dx, b[1] + dy, b[2] + dz]))
                if sr in blacks:
                    ac += 1
                else:
                    if sr in possible_whites.keys():
                        possible_whites[sr] += 1
                    else:
                        possible_whites[sr] = 1

            if ac == 0 or ac > 2:
                temp_blacks.remove(bs)
        # Go over possible whites
        for s, c in possible_whites.items():
            if c == 2:
                temp_blacks.add(s)

        blacks = deepcopy(temp_blacks)
    return len(blacks)


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            c = 0
            ll = []
            while c < len(l.strip()):
                if l[c] == "e" or l[c] == "w":
                    ll.append(l[c])
                    c += 1
                else:
                    ll.append(l[c:c+2])
                    c += 2
            idata.append(ll)
    print(idata)
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
