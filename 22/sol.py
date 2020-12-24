from copy import deepcopy


def part1(decks):
    while len(decks[1]) > 0 and len(decks[2]) > 0:
        p1 = decks[1].pop(0)
        p2 = decks[2].pop(0)
        if p1 > p2:
            decks[1] += [p1, p2]
        else:
            decks[2] += [p2, p1]
    winner = 1
    if len(decks[1]) == 0:
        winner = 2
    return calcscore(decks[winner])


def calcscore(deck):
    return sum((i+1)*v for i, v in enumerate(deck[::-1]))


def part2(decks):
    states = {0: {1: 0, 2: 0}}
    i = 1
    while len(decks[1]) > 0 and len(decks[2]) > 0:
        # check if in previous states
        ds1 = calcscore(decks[1])
        ds2 = calcscore(decks[2])
        for _, v in states.items():
            if v[1] == ds1 and v[2] == ds2:
                # Player 1 wins
                return ds1, 1

        states[i] = {1: ds1, 2: ds2}
        i += 1

        p1 = decks[1].pop(0)
        p2 = decks[2].pop(0)
        if len(decks[1]) >= p1 and len(decks[2]) >= p2:
            ndecks = deepcopy(decks)
            ndecks[1] = ndecks[1][:p1]
            ndecks[2] = ndecks[2][:p2]
            _, winner = part2(ndecks)
            if winner == 1:
                decks[1] += [p1, p2]
            else:
                decks[2] += [p2, p1]
            continue

        # Regular comparison
        if p1 > p2:
            decks[1] += [p1, p2]
        else:
            decks[2] += [p2, p1]
    winner = 1
    if len(decks[1]) == 0:
        winner = 2
    return calcscore(decks[winner]), winner


if __name__ == "__main__":
    idecks = {}
    idecks[1] = []
    idecks[2] = []
    with open("input.txt", "r") as f:
        playerswitch = 1
        for l in f:
            ll = l.strip()
            if "Player 2" in ll:
                playerswitch = 2
            if len(ll) == 0 or "Player" in ll:
                continue
            else:
                idecks[playerswitch].append(int(ll))
    print("Part 1:", part1(deepcopy(idecks)))
    print("Part 2:", part2(deepcopy(idecks))[0])
