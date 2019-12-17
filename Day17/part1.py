from Day9.part1 import VM

if __name__ == "__main__":
    direction = "1"
    vm = VM(direction, direction, "input.txt")
    my_puzzle = []
    temp = []
    while not vm.is_done():
        vm.run()
        out = (chr(int(vm.output)))
        print(out, end="")
        if out == "\n":
            if len(temp):
                my_puzzle.append(temp)
                temp = []
        else:
            temp.append(out)
        vm.stopped = False
        vm.set_input(direction)
    count = 0
    width = len(my_puzzle[0])
    height = len(my_puzzle)
    for y in range(height):
        for x in range(width):
            if my_puzzle[y][x] == "#":
                if 0 < y < (height-2):
                    if 0 < x < (width-2):
                        if my_puzzle[y][x+1] == "#":
                            if my_puzzle[y][x-1] == "#":
                                if my_puzzle[y+1][x] == "#":
                                    if my_puzzle[y-1][x] == "#":
                                        count += x*y
    print(count)
