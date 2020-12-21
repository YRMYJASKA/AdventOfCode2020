def part1(allergenset, counts):
    for k, v in allergenset.items():
        for i in v:
            if i in counts.keys():
                del counts[i]
    return sum(counts.values())


def part2(allergenset):
    canonicals = {}
    change = True
    while change:
        change = False
        for k, v in allergenset.items():
            if len(v) == 1:
                change = True
                # Delete this from all others
                for k1 in allergenset.keys():
                    if k1 == k:
                        continue
                    allergenset[k1] -= v
                elem = v.pop()
                canonicals[k] = elem
    ret = ""
    allergens = list(allergenset.keys())
    allergens.sort()
    for a in allergens:
        ret += canonicals[a] + ","
    return ret[:-1]


if __name__ == "__main__":
    idata = {}
    counts = {}
    with open("input.txt", "r") as f:
        for l in f:
            ll = l.strip().split(" (contains ")
            for ingredient in ll[0].split(" "):
                if ingredient in counts.keys():
                    counts[ingredient] += 1
                else:
                    counts[ingredient] = 1
            for allergen in set(ll[1][:-1].split(", ")):
                if allergen in idata.keys():
                    idata[allergen] &= set(ll[0].split(" "))
                else:
                    idata[allergen] = set(ll[0].split(" "))
    print("Part 1:", part1(idata, counts))
    print("Part 2:", part2(idata))
