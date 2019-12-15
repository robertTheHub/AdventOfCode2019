wall = set()
valid = set()
floor = []

with open("map.txt") as f:
    spaces = f.readline()
    walls = f.readline()
    walls = walls.strip()[1:-1].split('), (')
    spaces = spaces.strip()[1:-1].split('), (')
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for point in walls:
        x,y = point.split(', ')
        x = int(x)
        y = int(y)
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        wall.add((x,y))
    for space in spaces:
        x,y = space.split(', ')
        x = int(x)
        y = int(y)
        if x < minx:
            minx = x
        if y < miny:
            miny = y
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
        valid.add((x,y))
    floor = [[' ' for i in range(0, (maxx-minx)+2)] for j in range(0, (maxy-miny)+2)]
    for wal in wall:
        x = wal[0]
        y = wal[1]
        floor[y-miny][x-minx] = '#'
    for val in valid:
        x = val[0]
        y = val[1]
        floor[y-miny][x-minx] = '.'
    floor[(-13)-miny][16-minx] = '!'
    floor[(0) - miny][0 - minx] = '!'
    for row in floor:
        print(''.join(row))
