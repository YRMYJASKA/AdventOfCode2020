import re


def part1(rules, data):
    r = set(buildrulestrings(rules))
    ss = 0
    for d in data:
        if d in r:
            ss += 1
    return ss


def part2(rules, data):
    # Oh no...
    res = part2expr(rules)
    p = re.compile('^' + res + '$')
    ss = 0
    for d in data:
        if p.match(d):
            ss += 1
    return ss


memo = {}


def part2expr(rules, k=0):
    if k in memo.keys():
        return memo[k]
    if type(rules[k]) == str:
        return rules[k]

    expr = []
    for r in rules[k]:
        ss = []
        for s in r:
            ss.append(part2expr(rules, k=s))
        expr.append(''.join(ss))

    memo[k] = "(" + '|'.join(expr) + ")"
    return memo[k]


def buildrulestrings(rules, r=0):
    if type(rules[r]) == str:
        return [rules[r]]

    strings = []

    for s in rules[r]:
        ss = [""]
        for k in s:
            kr = buildrulestrings(rules, r=k)
            sn = []
            for ks in kr:
                sn += [x + ks for x in ss]
            ss = sn
        strings += ss
    return strings


if __name__ == "__main__":
    idata = []
    rules = {}
    with open("input.txt", "r") as f:
        rul = True
        for l in f:
            if len(l.strip()) == 0:
                rul = False
                continue
            if rul:
                i, r = l.strip().split(": ")
                i = int(i)
                if r[0] == "\"":
                    # Terminal rule
                    rules[i] = r[1:-1]
                    continue
                rules[i] = []
                r = r.split(" | ")
                for rr in r:
                    rules[i].append(list(map(int, rr.split(" "))))
            else:
                idata.append(l.strip())

    print("Part 1:", part1(rules, idata))
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    # Screw it
    rules[8] = [[42]*i for i in range(1, 10)]
    rules[11] = [[42]*i + [31]*i for i in range(1,5)]
    print("Part 2:", part2(rules, idata))
