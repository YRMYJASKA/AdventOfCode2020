def part1(data):
    ss = 0
    for stmt in data:
        ss += evalexpr(stmt)
    return ss


def readexpr(stmt):
    buff = []
    i = 0
    while i < len(stmt):
        if stmt[i] == ' ':
            i += 1
            continue
        elif stmt[i] in '+*':
            buff += stmt[i]
            i += 1
        elif stmt[i] == '(':
            lvl = 1
            x = 1
            ns = ""
            while lvl > 0:
                c = stmt[i+x]
                ns += c
                if c == '(':
                    lvl += 1
                elif c == ')':
                    lvl -= 1
                x += 1
            buff.append(readexpr(ns[:-1]))
            i += x + 1
        elif stmt[i] in "+*":
            buff.append(stmt[i])
            i += 1
        else:
            buff.append(int(stmt[i]))
            i += 1
    return buff


def evalexpr(expr):
    if type(expr) == int:
        return expr
    curr = evalexpr(expr[0])
    t = 1
    while t < len(expr):
        if expr[t] == '*':
            curr *= evalexpr(expr[t+1])
        elif expr[t] == '+':
            curr += evalexpr(expr[t+1])
        t += 2
    return curr


def formatexpr2(expr):
    if type(expr) == int or expr == "*":
        return expr
    t = 0
    while t < len(expr):
        if expr[t] == '+':
            expr[t-1] = [formatexpr2(expr[t-1]), '+', formatexpr2(expr[t+1])]
            del expr[t]
            del expr[t]
        else:
            expr[t] = formatexpr2(expr[t])
            t += 1
    return expr


def part2(data):
    ss = 0
    for d in idata:
        e = formatexpr2(d)
        s = evalexpr(e)
        ss += s
    return ss


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            idata.append(readexpr(l.strip()))

    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
