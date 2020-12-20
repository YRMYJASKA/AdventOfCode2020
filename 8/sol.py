def part1(data):
    glob = 0
    i = 0
    already_ran = set()
    while i < len(data):
        ins = data[i].split(" ")[0]
        val = int(data[i].split(" ")[1])
        if i in already_ran:
            return glob

        already_ran.add(i)

        if ins == "acc":
            glob += val
            i += 1
        elif ins == "jmp":
            i += val
        elif ins == "nop":
            i += 1
        else:
            print("invalid instruction!")
            return


def part2(data):
    for flip in range(0, len(data)):
        old = ""
        if data[flip][:3] == "jmp":
            data[flip] = "nop" + data[flip][3:]
            old = "jmp" + data[flip][3:]
        elif data[flip][:3] == "nop":
            data[flip] = "jmp" + data[flip][3:]
            old = "nop" + data[flip][3:]
        else:
            continue
        glob = 0
        i = 0
        already_ran = set()
        prev = 0
        while i < len(data):
            ins = data[i].split(" ")[0]
            val = int(data[i].split(" ")[1])
            if i in already_ran:
                if len(already_ran) == prev:
                    break
                prev = len(already_ran)
            already_ran.add(i)
            if ins == "acc":
                i += 1
                glob += val
            elif ins == "jmp":
                i += val
            elif ins == "nop":
                i += 1
            else:
                print("invalid instruction!")
                break
        if i == len(data):
            return glob
        data[flip] = old


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            idata.append(l.strip())
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
