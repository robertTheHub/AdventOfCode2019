class VM:
    def __init__(self, code_file):
        self.code = self.parse_code(code_file)
        self.counter = 0
        self.stopped = False
        self.done = False
        self.input = ""
        self.output = None
        self.base = 0
        self.size = len(self.code)
        self.input_spent = True
        self.has_output = False

    def parse_code(self, code_file):
        with open(code_file) as f:
            return f.readline().strip().split(",")

    def get_from_code(self, position):
        position = int(position)
        if position >= self.size:
            expand = (position - self.size) + 1
            self.code.extend(["0" for i in range(expand)])
            self.size = len(self.code)
        return self.code[position]

    def get_function(self):
        return self.get_from_code(self.counter)

    def put_in_code(self, position, value):
        position = int(position)
        if position >= self.size:
            expand = (position - self.size) + 1
            self.code.extend(["0" for i in range(expand)])
            self.size = len(self.code)
        self.code[position] = value

    def get_argument(self, position):
        if position == 1:
            return self.get_from_code(self.counter + 1)
        elif position == 2:
            return self.get_from_code(self.counter + 2)
        else:
            return self.get_from_code(self.counter + 3)

    def get_positionly(self, param):
        return self.get_from_code(self.get_argument(param))

    def inc_counter(self, value):
        self.counter += value

    def set_counter(self, value):
        self.counter = value

    def set_input(self, value):
        self.input_spent = False
        self.stopped = False
        self.input = value

    def set_base(self, value):
        value = int(value)
        self.base += value

    def set_output(self, value):
        self.output = value
        self.stopped = True
        self.has_output = True

    def use_input(self, position):
        arg = int(position)
        self.put_in_code(arg, self.input)
        self.stopped = True
        self.input_spent = True

    def get_relatively(self, param):
        arg = int(self.get_argument(param))
        return self.get_from_code(arg + self.base)

    def get_output(self):
        self.has_output = False
        self.stopped = False
        return self.output

    def get_relative_position(self, param):
        arg = int(self.get_argument(param))
        return arg + self.base

    def is_runnable(self):
        if self.is_done():
            return False
        elif self.stopped:
            return False
        else:
            return True

    def is_done(self):
        if self.get_from_code(self.counter)[-2:] == "99":
            self.done = True
        if self.done:
            return True
        else:
            return False

    def run(self):
        valid = {'1', '2', '5', '6', '7', '8'}
        while self.is_runnable():
            function = self.get_function()
            counter = self.counter
            if function[-1] in valid:
                if len(function) >= 5:
                    if function[-5] == '1':
                        third = self.get_argument(3)
                        debug_third = str(third)
                    elif function[-5] == '2':
                        third = self.get_relative_position(3)
                        debug_third = "(" + self.get_argument(3) + ")"
                else:
                    third = self.get_argument(3)
                    debug_third = "[" + str(third) + "]"
                if len(function) >= 4:
                    if function[-4] == '1':
                        second = self.get_argument(2)
                        debug_second = str(second)
                    elif function[-4] == '2':
                        second = self.get_relatively(2)
                        debug_second = "(" + str(self.get_argument(2)) + ")"
                    elif function[-4] == '0':
                        second = self.get_positionly(2)
                        debug_second = "[" + str(self.get_argument(2)) + "]"
                else:
                    second = self.get_positionly(2)
                    debug_second = "[" + str(self.get_argument(2)) + "]"
                if len(function) >= 3:
                    if function[-3] == '1':
                        first = self.get_argument(1)
                        debug_first = str(first)
                    elif function[-3] == '2':
                        first = self.get_relatively(1)
                        debug_first = "(" + str(self.get_argument(1)) + ")"
                    elif function[-3] == '0':
                        first = self.get_positionly(1)
                        debug_first = "[" + str(self.get_argument(1)) + "]"
                else:
                    first = self.get_positionly(1)
                    debug_first = "[" + str(self.get_argument(1)) + "]"
                if function[-1] == '1':
                    self.put_in_code(third, str(int(first) + int(second)))
                    self.inc_counter(4)
                    name = 'add'
                elif function[-1] == '2':
                    self.put_in_code(third, str(int(first) * int(second)))
                    self.inc_counter(4)
                    name = 'mul'
                elif function[-1] == '5':
                    if int(first):
                        self.set_counter(int(second))
                    else:
                        self.inc_counter(3)
                    name = 'jmpnz'
                    debug_third = ''
                elif function[-1] == '6':
                    if not int(first):
                        self.set_counter(int(second))
                    else:
                        self.inc_counter(3)
                    name = 'jmpz'
                    debug_third = ''
                elif function[-1] == '7':
                    if int(first) < int(second):
                        self.put_in_code(third, "1")
                    else:
                        self.put_in_code(third, "0")
                    self.inc_counter(4)
                    name = 'slt'
                elif function[-1] == '8':
                    if first == second:
                        self.put_in_code(third, "1")
                    else:
                        self.put_in_code(third, "0")
                    self.inc_counter(4)
                    name = 'seq'
                #print(counter, " : ", name, debug_first, debug_second, debug_third)
            else:
                if function[-1] == '3':
                    if function[0] == '2':
                        self.use_input(self.get_relative_position(1))
                        debug_first = "(" + str(self.get_argument(1)) + ")"
                    else:
                        self.use_input(self.get_argument(1))
                        debug_first = self.get_argument(1)
                    self.inc_counter(2)
                    name = 'in'
                elif function[-1] == '4':
                    if function[0] == '1':
                        self.set_output(self.get_argument(1))
                        debug_first = self.get_argument(1)
                    elif function[0] == '2':
                        self.set_output(self.get_relatively(1))
                        debug_first = "(" + str(self.get_argument(1)) + ")"
                    else:
                        self.set_output(self.get_positionly(1))
                        debug_first = "[" + str(self.get_argument(1)) + "]"
                    self.inc_counter(2)
                    name = 'out'
                    self.stopped = True
                elif function[-2:] == '99':
                    self.done = True
                    name = 'halt'
                elif function[-1] == '9':
                    if function[0] == '1':
                        self.set_base(self.get_argument(1))
                        debug_first = self.get_argument(1)
                    elif function[0] == '2':
                        self.set_base(self.get_relatively(1))
                        debug_first = "(" + str(self.get_relative_position(1)) + ")"
                    else:
                        self.set_base(self.get_positionly(1))
                        debug_first = "[" + str(self.get_argument(1)) + "]"
                    self.inc_counter(2)
                    name = 'arb'
                else:
                    raise ValueError
                #print(counter, ": ", name, debug_first)
            self.is_done()


if __name__ == "__main__":
    answer = "A,B,A,C,B,A,C,B,A,C\nL,6,L,4,R,9,3\nL,6,R,9,3,R,9,3,L,8\nL,6,L,9,1,L,9,1,L,6\nn\n"
    answer = [ord(x) for x in answer]
    vm = VM("input.txt")
    vm.set_input(str(answer[0]))
    i = 1
    while not vm.is_done():
        vm.run()
        if vm.has_output:
            print(chr(int(vm.get_output())), end='')
        if vm.input_spent:
            if i < len(answer):
                vm.set_input(str(answer[i]))
                i += 1
            else:
                vm.set_input(answer[-1])
    print(vm.get_output())