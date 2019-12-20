from Day17.part2 import VM

if __name__ == "__main__":
    puzzle = [['' for i in range(50)] for j in range(50)]
    count = 0
    for i in range(50):
        for j in range(50):
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
                    puzzle[j][i] = "#"
                    count += 1
                else:
                    puzzle[j][i] = "."
            vm.run()
    for line in puzzle:
        print(''.join(line))
    print(count)
