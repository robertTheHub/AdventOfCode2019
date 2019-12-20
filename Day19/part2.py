from Day17.part2 import VM

if __name__ == "__main__":
    puzzle = [['' for i in range(250)] for j in range(200)]
    count = 0
    for i in range(750,1000):
        row = 0
        for j in range(1000,1200):
            vm = VM("input.txt")
            if vm.input_spent:
                vm.set_input(i)
            vm.run()
            if vm.input_spent:
                vm.set_input(j)
            vm.run()
            vm.stopped = False
            vm.run()
            if vm.has_output:
                if int(vm.get_output()):
                    puzzle[j-1000][i-750] = "#"
                else:
                    puzzle[j-1000][i-750] = "."
            vm.run()
    for line in puzzle:
        print(''.join(line))
    print(count)