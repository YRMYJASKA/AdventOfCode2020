def part1(data):
    invalids = []
    masterset = set()
    for r in data["ranges"].values():
        masterset = masterset | r
    for ticket in data["nearby"]:
        for v in ticket:
            if v not in masterset:
                invalids.append(v)
    return sum(invalids)


def part2(data):
    masterset = set()
    for r in data["ranges"].values():
        masterset = masterset | r
    # Filter out the invalid tickets
    valids = []
    for ticket in data["nearby"]:
        valid = True
        for v in ticket:
            if v not in masterset:
                valid = False
                break
        if valid:
            valids.append(ticket)

    # Create a map for the possible field locations
    locs = {}
    for k in data["ranges"].keys():
        locs[k] = set(range(len(valids[0])))
    # Now process the valids
    for t in valids:
        for i, v in enumerate(t):
            for n, s in data["ranges"].items():
                if v not in s:
                    # we certainly know that this column is not possible
                    locs[n].remove(i)
    prod = 1
    # Now iterate until there are no singeltons left
    while len(locs.keys()) > 0:
        for k, v in locs.items():
            if len(v) == 1:
                vv = list(v)[0]
                # Before deleting, check if this is a "departure field"
                if "departure" in k:
                    prod *= data["myticket"][vv]
                # Delete this item from every other entry
                for k1 in locs.keys():
                    locs[k1] = locs[k1] - v
                del locs[k]
                break

    return prod


if __name__ == "__main__":
    idata = {}
    idata["nearby"] = []
    idata["ranges"] = {}
    with open("input.txt", "r") as f:
        mytickets = False
        nearby = False
        for l in f:
            if len(l.strip()) == 0:
                continue
            elif "nearby" in l:
                nearby = True
            elif "your" in l:
                mytickets = True
            elif nearby:
                idata["nearby"].append(list((map(int, l.strip().split(",")))))
            elif mytickets:
                idata["myticket"] = list(map(int, l.strip().split(",")))
            else:
                # This is a range
                name = l.strip().split(":")[0]
                f = l.strip().split(" or ")[0].split(": ")[1]
                s = l.strip().split(" or ")[1]
                f1, f2 = map(int, f.split("-"))
                fr = set(range(f1, f2 + 1))
                s1, s2 = map(int, s.split("-"))
                sr = set(range(s1, s2 + 1))
                idata["ranges"][name] = fr | sr

    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
