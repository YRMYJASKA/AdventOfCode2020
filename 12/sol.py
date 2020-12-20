import numpy as np


def part1(data):
    direction = 0
    x, y = 0, 0
    for cmd, val in data:
        if cmd == "N":
            y += val
        elif cmd == "S":
            y -= val
        elif cmd == "E":
            x += val
        elif cmd == "W":
            x -= val
        elif cmd == "R":
            direction -= val
        elif cmd == "L":
            direction += val
        elif cmd == "F":
            x += np.cos(np.radians(direction))*val
            y += np.sin(np.radians(direction))*val

    return abs(x), abs(y)



def part2(data):
    pos = np.array([0, 0], dtype=np.float64).T
    wpos = np.array([10, 1]).T
    for cmd, val in data:
        if cmd == "N":
            wpos += [0, val]
        elif cmd == "S":
            wpos -= [0, val]
        elif cmd == "E":
            wpos += [val, 0]
        elif cmd == "W":
            wpos -= [val, 0]
        elif cmd == "R":
            rad = np.radians(-val)
            rot = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
            wpos = rot.dot(wpos)
        elif cmd == "L":
            rad = np.radians(val)
            rot = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
            wpos = rot.dot(wpos)
        elif cmd == "F":
            pos += val*wpos

    return pos


if __name__ == "__main__":
    idata = []
    with open("input.txt", "r") as f:
        for l in f:
            cmd = l.strip()[0]
            val = int(l.strip()[1:])
            idata.append((cmd, val))
    print("Part 1:", int(sum(part1(idata))))
    print("Part 2:", int(np.round(sum(abs(part2(idata))))))
