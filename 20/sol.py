from math import sqrt
from copy import deepcopy


# the width and height of individual tiles
TILE_LEN = 10
VISUALISATION = False


def part1(data):
    _, connections = connecttiles(data)
    p = 1
    for k, v in connections.items():
        count = 0
        for _, c in v.items():
            if c == 0:
                count += 1
        if count == 2:
            # this is a corner
            p *= k
    return p


def rotate_tile(tile, rot, hflip, vflip, length=TILE_LEN):
    # Get around pesky immutable strings in python
    tile = [[c for c in t] for t in tile]
    # Rotate the tile
    for i in range(rot//90):
        tile_temp = deepcopy(tile)
        for j in range(length):
            for k in range(length):
                c = tile[j][k]
                tile_temp[k][length - 1 - j] = c
        tile = deepcopy(tile_temp)

    # Horizontal flip
    if hflip:
        tile = tile[::-1]
    # Vertical flip
    if vflip:
        for i in range(length):
            tile[i] = tile[i][::-1]
    return tile


def connecttiles(data):
    # Build dictionary of the edges
    edges = {}
    for k, v in data.items():
        edges[k] = {}
        edges[k]["N"] = v[0]
        edges[k]["S"] = v[-1][::-1]
        east = ""
        west = ""
        for i in range(len(v)):
            west += v[len(v)-1-i][0]
            east += v[i][-1]
        edges[k]["E"] = east
        edges[k]["W"] = west
    # Start pairing
    connections = {}
    for x in data.keys():
        connections[x] = {"N": 0, "W": 0, "S": 0, "E": 0}
    for i1, ed1 in edges.items():
        for i2, ed2 in edges.items():
            if i1 == i2:
                continue
            for d1, e1 in ed1.items():
                for d2, e2 in ed2.items():
                    # Simple check with rotation
                    if e1 == e2[::-1]:
                        # Connect the tiles and rotate
                        connections[i1][d1] = (i2, d2)
                        connections[i2][d2] = (i1, d1)
                        continue
                    # Flipping check
                    if e1 == e2:
                        connections[i1][d1] = (i2, d2)
                        connections[i2][d2] = (i1, d1)
    return edges, connections


def rotate(rot):
    dirs = ['N', 'E', 'S', 'W']
    for _ in range(rot//90):
        dirs.insert(0, dirs.pop())
    return dirs


def determine_orientation(rot, hflip, vflip):
    ''' Determine the new orientation of a block
    '''
    # normal orientation
    dirs = rotate(rot)
    if hflip:
        t = dirs[0]
        dirs[0] = dirs[2]
        dirs[2] = t
    elif vflip:
        t = dirs[1]
        dirs[1] = dirs[3]
        dirs[3] = t
    return dirs


def determine_edge(rot, hflip, vflip, edge):
    ''' Determine how an edge is affected by its orientation,
        output: clockwise string of the current edge
    '''
    if hflip ^ vflip:
        edge = edge[::-1]
    return edge


def check_monsters(picture, y, x):
    deltas = [(0, 0), (1, 1), (4, 1), (5, 0), (6, 0), (7, 1),
              (10, 1), (11, 0), (12, 0), (13, 1), (16, 1),
              (17, 0), (18, 0), (18, -1), (19, 0)]
    c = 0
    for dx, dy in deltas:
        if picture[y+dy][x+dx] == "#":
            c += 1
    if c == len(deltas):
        return True
    return False


def part2(data):
    edges, connections = connecttiles(data)

    # start by assembling the tiles
    dim = int(sqrt(len(connections)))
    # 4-tuple 2D array. (tileid, rotation, hor_flip, ver_flip)
    big_picture = [[(0, 0, False, False) for _ in range(dim)]
                   for _ in range(dim)]

    # Fix one of the corners to the top left
    for k, v in connections.items():
        c = 0
        for vv in v.values():
            if vv == 0:
                c += 1
        if c == 2:
            rot = 0
            hflip = False
            vflip = False
            # Orient the tile such that it has connections to east and south
            if connections[k]["E"] == 0:
                e1 = edges[k]["W"]
                e2 = edges[connections[k]["W"][0]][connections[k]["W"][1]]
                if e1 == e2:
                    # Translation
                    vflip = True
                elif e1 == e2[::-1]:
                    # Rotation
                    rot = 180
            newc = connections[k][determine_orientation(rot, hflip, vflip)[2]]
            if connections[k]["S"] == 0 or newc == 0:
                e1 = edges[k]["N"]
                e2 = edges[connections[k]["N"][0]][connections[k]["N"][1]]
                # This can only be a flip
                if e1 == e2[::-1] or e1 == e2:
                    hflip = True

            big_picture[0][0] = (k, rot, hflip, vflip)
            break

    # Start building from that corner
    # One connection determines the rotation of the next tile
    for y in range(dim):
        for x in range(dim):
            if x == 0 and y == 0:
                continue

            # Determine this tile
            if x == 0:
                # First in row ==> get connection from above
                connid, crot, chflip, cvflip = big_picture[y - 1][0]
                # Get the 'south' of the connecting tile
                direction = determine_orientation(crot, chflip, cvflip)[2]
            else:
                # Not first in row ==> get connection from the west
                connid, crot, chflip, cvflip = big_picture[y][x - 1]
                # Get the 'east' of the connecting tile
                direction = determine_orientation(crot, chflip, cvflip)[1]
            thistile, thisdir = connections[connid][direction]
            thisedge = edges[thistile][thisdir]
            connedge = edges[connid][direction]

            # Find the new oriented edge of the connecting tile
            new_connedge = determine_edge(crot, chflip,
                                          cvflip,  connedge)
            # Find the orientation of this new tile
            # NOTE: This might not work so if it is buggy come here
            rot, hflip, vflip = 0, False, False
            if thisedge[::-1] == new_connedge:
                # This is a rotation
                # Now determine by how much
                if x != 0:
                    i = ['W', 'S', 'E', 'N'].index(thisdir)
                else:
                    i = ['N', 'W', 'S', 'E'].index(thisdir)
                rot = i*90
            elif thisedge == new_connedge:
                # This is a translation
                if x != 0:
                    if thisdir == 'W':
                        hflip = True
                    elif thisdir == 'E':
                        # Simple flip
                        vflip = True
                    elif thisdir == 'N':
                        rot = 90
                        vflip = True
                    else:
                        rot = 90
                        hflip = True
                else:
                    if thisdir == 'N':
                        vflip = True
                    elif thisdir == 'S':
                        hflip = True
                    elif thisdir == 'W':
                        rot = 90
                        vflip = True
                    else:
                        rot = 90
                        hflip = True

            big_picture[y][x] = (thistile, rot, hflip, vflip)
            if VISUALISATION:
                for j in big_picture:
                    tile_row = []
                    for r in j:
                        if r[0] == 0:
                            continue
                        tile_row.append(rotate_tile(data[r[0]], r[1],
                                        r[2], r[3]))
                    if len(tile_row) == 0:
                        break
                    for i in range(TILE_LEN):
                        line = ""
                        for t in tile_row:
                            line += "".join(t[i]) + " "
                        print(line)
                    print()

    # Now that the pieces have been placed on the  board with right
    # orientations, we create the picture from these
    picture = []
    for y in range(dim):
        tile_row = []
        for x in range(dim):
            tileid, rot, hflip, vflip = big_picture[y][x]
            tile = rotate_tile(data[tileid], rot, hflip, vflip)
            tile_row.append(tile[1:-1])
        for i in range(TILE_LEN - 2):
            line = ""
            for t in tile_row:
                line += ("".join(t[i]))[1:-1]
            picture.append(line)
    # Print the whole map formed by the tiles
    if VISUALISATION:
        for l in picture:
            print(l)

    # Now search for the sea monsters
    cc = 0
    # All the possible orientations of the sea
    orientations = []
    for rot in range(0, 360, 90):
        orientations.append((rot, False, False))
        orientations.append((rot, False, True))
        orientations.append((rot, True, False))
        orientations.append((rot, True, True))
    for rot, hflip, vflip in orientations:
        p = rotate_tile(picture, rot, hflip, vflip, length=len(picture[0]))
        for y in range(1, len(p)-1):
            for x in range(len(p[y])-19):
                if check_monsters(p, y, x):
                    cc += 1
        if cc != 0:
            break
    total = 0
    for l in picture:
        total += "".join(l).count("#")

    # Finally, count the number of non-monster '#'
    return total - cc*15


if __name__ == "__main__":
    idata = {}
    with open("input.txt", "r") as f:
        tilen = 0
        for line in f:
            row = []
            line = line.strip()
            if len(line) == 0:
                continue
            elif "Tile" == line[:4]:
                tilen = int(line.split(" ")[1][:-1])
                idata[tilen] = []
            else:
                row = line.split()
                idata[tilen] += row
    print("Part 1:", part1(idata))
    print("Part 2:", part2(idata))
