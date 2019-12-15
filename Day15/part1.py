from Day9.part1 import VM

if __name__ == "__main__":
    direction = "1"
    vm = VM(direction, direction, "input.txt")
    moves = {"1":(0,1), "2":(0,-1), "3":(-1,0), "4":(1,0)}
    next_dir = {"1":"3", "3":"2", "2":"4", "4":"1"}
    revert = {"1":"2", "2":"1", "4":"3", "3":"4"}
    results = {"error": 0, "moved": 1, "end":2}
    valid = set()
    valid.add((0,0))
    wall = set()
    o2 = set()
    counts = {}
    x = 0
    y = 0
    count = 0
    flag = False
    reversion = False
    path = []
    while not vm.is_done():
        count += 1
        vm.run()
        out = int(vm.output)
        if out == 0:
            wall.add((x + moves[direction][0], y + moves[direction][1]))
            direction = next_dir[direction]
            i = 0
            while (x + moves[direction][0], y + moves[direction][1]) in valid.union(wall, o2):
                if (x + moves[direction][0], y + moves[direction][1]) in counts:
                    if counts[(x + moves[direction][0], y + moves[direction][1])] > (len(path)+1):
                        counts[(x + moves[direction][0], y + moves[direction][1])] = len(path)+1
                direction = next_dir[direction]
                i+=1
                if i == 4:
                    direction = revert[path.pop()]
                    reversion = True
                    break
        elif out == 1:
            if not reversion:
                path.append(direction)
            else:
                reversion = False
            x += moves[direction][0]
            y += moves[direction][1]
            valid.add((x, y))
            if (x,y) in counts:
                if len(path)+1 < counts[(x,y)]:
                    counts[(x,y)] = len(path)
            else:
                counts[(x,y)] = len(path)
            i = 0
            while (x + moves[direction][0], y + moves[direction][1]) in valid.union(wall, o2):
                if (x + moves[direction][0], y + moves[direction][1]) in counts:
                    if counts[(x + moves[direction][0], y + moves[direction][1])] > (len(path)+1):
                        counts[(x + moves[direction][0], y + moves[direction][1])] = len(path)+1
                direction = next_dir[direction]
                i += 1
                if i == 4:
                    direction = revert[path.pop()]
                    reversion = True
                    break
        else:
            if not reversion:
                path.append(direction)
            else:
                reversion = False
            x += moves[direction][0]
            y += moves[direction][1]
            o2.add((x, y))
            if (x,y) in counts:
                if len(path)+1 < counts[(x,y)]:
                    counts[(x,y)] = len(path)
            else:
                counts[(x,y)] = len(path)
            i = 0
            while (x + moves[direction][0], y + moves[direction][1]) in valid.union(wall, o2):
                if (x + moves[direction][0], y + moves[direction][1]) in counts:
                    if counts[(x + moves[direction][0], y + moves[direction][1])] > (len(path)+1):
                        counts[(x + moves[direction][0], y + moves[direction][1])] = len(path)+1
                direction = next_dir[direction]
                i += 1
                if i == 4:
                    direction = revert[path.pop()]
                    reversion = True
                    break
        vm.stopped = False
        vm.set_input(direction)
        if (count == 2455):
            break
    print(counts[(16, -12)])

