import re


def part1(data):
    valids = {}
    for i, v in data.items():
        kk = set(v.keys())
        if len(kk) == 8 or (len(kk) == 7 and "cid" not in kk):
            valids[i] = v

    return valids


def part2(data):
    valids = part1(data)
    cc = 0
    for k, v in valids.items():
        try:
            byr = int(v["byr"])
            iyr = int(v["iyr"])
            eyr = int(v["eyr"])
            _ = int(v["pid"])
            hgt, hgt_suff = int(v["hgt"][:-2]), v["hgt"][-2:]
        except:
            continue
        if not (byr >= 1920 and byr <= 2002 and iyr >= 2010 and iyr <= 2020 and eyr >= 2020 and
                eyr <= 2030):
            continue

        if hgt_suff == "cm":
            if not (hgt >= 150 and hgt <= 193):
                continue
        elif hgt_suff == "in":
            if not (hgt >= 59 and hgt <= 76):
                continue
        else:
            continue
        if (len(v["hcl"]) != 7) or (v["hcl"][0] != "#") or (not bool(re.match('^[a-z0-9]+$', v["hcl"][1:]))):
            continue
        if v["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        if len(v["pid"]) != 9:
            continue
        # passed all checks
        cc += 1
    return cc


if __name__ == "__main__":
    idata = {}
    with open("input.txt", "r") as f:
        counter = 0
        idata[counter] = {}
        for line in f:
            if line == "\n":
                # new crediental
                counter += 1
                idata[counter] = {}
                continue
            args = [x.split(":") for x in line.strip().split(" ")]
            # create mapping
            for name, val in args:
                fval = val
                idata[counter][name] = fval
    print("Part 1:", len(part1(idata)))
    print("Part 2:", part2(idata))
