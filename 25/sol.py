def part1(pk1, pk2):
    # Find out the loop size
    x = 1
    c = 0
    while x != pk1:
        x = (x*7) % 20201227
        c += 1
    print("loop size", c)
    x = 1
    for _ in range(c):
        x = (x*pk2) % 20201227
    return x


def part2():
    pass


if __name__ == "__main__":
    public_key1 = 0
    public_key2 = 0
    with open("input.txt", "r") as f:
        public_key1 = int(f.readline().strip())
        public_key2 = int(f.readline().strip())
    print("Part 1:", part1(public_key1, public_key2))
    print("Part 2:", part2())
