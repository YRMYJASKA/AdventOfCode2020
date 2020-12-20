def part1(data):
    cc = 0
    for k, v in data.items():
        if contains_gold(k, data):
            cc += 1
    return cc


# Memoization
contain_dict = {}


def contains_gold(bag, data):
    if bag in contain_dict.keys():
        return contain_dict[bag]
    elif len(data[bag]) == 0:
        contain_dict[bag] = False
        return False
    elif "shiny gold" in data[bag].keys():
        return True
        contain_dict[bag] = True
    else:
        for k, _ in data[bag].items():
            if contains_gold(k, data):
                contain_dict[bag] = True
                return True
        return False


def bag_sum(bag, data):
    cc = 0
    if len(data[bag]) == 0:
        return 0
    for k, v in data[bag].items():
        cc += v + v*bag_sum(k, data)
    return cc


def part2(data):
    return bag_sum("shiny gold", data)


if __name__ == "__main__":
    idata = {}
    with open("input.txt") as f:
        for line in f:
            ff = line.strip()
            colour = ff.split(" bags ")[0]
            ll = ff[:-1].split(" contain ")[1].split(", ")
            if "no other bags" in ll:
                # empty bag
                idata[colour] = {}
            else:
                for l in ll:
                    num = int(l[0])
                    if num == 1:
                        c = l[2:-4]
                    else:
                        c = l[2:-5]
                    if colour in idata.keys():
                        idata[colour][c] = num
                    else:
                        idata[colour] = {c: num}
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
