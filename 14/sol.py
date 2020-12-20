def part1(data):
    mem = {}
    for mask, ins in data.items():
        for loc, val in ins:
            val = bin(val)[2:]
            val = list('0'*(36-len(val)) + val)
            for c in range(len(mask)):
                if mask[c] == "0":
                    val[c] = "0"
                elif mask[c] == "1":
                    val[c] = "1"
            mem[loc] = int("".join(val), 2)
    return sum(mem.values())


def mask_addresses(mask, add):
    add = bin(add)[2:]
    add = '0'*(36-len(add)) + add
    addresses = ['']
    for c in range(len(mask)):
        if mask[c] == "1":
            for a in range(len(addresses)):
                addresses[a] += '1'
        elif mask[c] == "X":
            buff = []
            for a in addresses:
                buff.append(str(a) + '1')
                buff.append(str(a) + '0')
            addresses = buff
        else:
            for a in range(len(addresses)):
                addresses[a] += add[c]
    addresses = [int(x, 2) for x in addresses]
    return addresses


def part2(data):
    mem = {}
    for mask, ins in data.items():
        for loc, val in ins:
            adds = mask_addresses(mask, loc)
            for a in adds:
                mem[a] = val
    return sum(mem.values())


if __name__ == "__main__":
    idata = {}
    with open("input.txt", "r") as f:
        ins = []
        mask = f.readline().split(" ")[2].strip()
        for l in f:
            if l.split(" ")[0] == "mask":
                idata[mask] = ins
                mask = l.split(" ")[2].strip()
                ins = []
            else:
                ins.append([int(l.split("[")[1].split(" =")[0][:-1]), int(l.split("= ")[1])])
        idata[mask] = ins
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
