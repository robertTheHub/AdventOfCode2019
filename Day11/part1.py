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


    phase = "0"
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

