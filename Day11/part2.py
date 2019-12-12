from Day9.part1 import VM

if __name__ == "__main__":
    def move(x, y, facing):
        if facing == 0:
            return x + 1, y
        elif facing == 1:
            return x, y + 1
        elif facing == 2:
            return x - 1, y
        elif facing == 3:
            return x, y - 1


    phase = "1"
    value = "0"
    vm = VM(phase, value, "input.txt")
    area = {}
    x = 0
    y = 0
    facing = 0  # 0 - Up, 1 Right, 2 Down, 3 Left
    while not vm.is_done():
        vm.run()
        colour = vm.output
        area[(x, y)] = colour
        vm.stopped = False
        vm.run()
        direction = int(vm.output)
        if direction:
            facing = (facing + 1) % 4
        else:
            facing = (facing - 1) % 4
        x, y = move(x, y, facing)
        if not vm.is_done():
            vm.set_input(area.get((x, y), "0"))
    print(len(area.keys()))
    lowestx = 0
    maxx = 0
    maxy = 0
    lowesty = 0
    for set in area.keys():
        if set[0] < lowestx:
            lowestx = set[0]
        elif set[0] > maxx:
            maxx = set[0]
        if set[1] < lowesty:
            lowesty = set[1]
        elif set[1] > maxy:
            maxy = set[1]
    output = [['.' for i in range(lowesty, maxy + 1)] for j in range(lowestx, maxx + 1)]
    for set, value in area.items():
        newx = set[0] - lowestx
        newy = set[1] - lowesty
        if value == '0':
            value = '.'
        else:
            value = "#"
        output[-(newx +1)][newy] = value
    for line in output:
        print(line)