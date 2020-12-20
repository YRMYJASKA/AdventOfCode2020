import numpy as np


def part1(target, lines):
    mods = [target]*len(lines) % lines
    i = 0
    while True:
        if 0 in mods:
            return i*lines[np.where(mods == 0)]
        i += 1
        mods = (mods + 1) % lines


def part2(lines):
    mods = [int(x) for x in lines if x != 'x']
    res = []
    counter = 0
    for i in range(0, len(lines)):
        if lines[i] != 'x':
            res.append((mods[counter] - i) % int(lines[i]))
            counter += 1

    # CRT
    while len(res) > 1:
        r1, r2 = res[0], res[1]
        m1, m2 = mods[0], mods[1]
        # find Bezout coefficients
        r_prev, r = m1, m2
        s_prev, s = 1, 0
        t_prev, t = 0, 1
        while r != 0:
            q = r_prev // r
            r_prev, r = r, r_prev - q*r
            s_prev, s = s, s_prev - q*s
            t_prev, t = t, t_prev - q*t
        b1, b2 = s_prev, t_prev
        x = r1*m2*b2 + r2*m1*b1
        res.pop(0)
        mods.pop(0)
        res[0] = x % (m1*m2)
        mods[0] = m1*m2
    return(int(res[0]))


if __name__ == "__main__":
    lines1 = []
    lines2 = []
    target = 0
    with open("input.txt", "r") as f:
        target = int(f.readline().strip())
        line = f.readline().strip()
        line = line.split(",")
        lines1 = [int(x) for x in line if x != "x"]
        lines2 = [x for x in line]
    lines1 = np.array(lines1)
    print("Part 1:", part1(target, lines1)[0])
    print("Part 2:", part2(lines2))
