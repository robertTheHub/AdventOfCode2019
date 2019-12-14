from Day9.part1 import VM

if __name__ == "__main__":
    phase = "0"
    value = "0"
    vm = VM(phase, value, "input.txt")
    tiles = {0: ' ', 1:'X', 2: '#', 3:'-', 4:'o'}
    count = 0
    while not vm.is_done():
        vm.run()
        x = int(vm.output)
        vm.stopped = False
        vm.run()
        y = int(vm.output)
        vm.stopped = False
        vm.run()
        id = int(vm.output)
        vm.stopped = False
        if x == 44:
            print(tiles[id])
        else:
            print(tiles[id], end='')
#    print(vm.code)

