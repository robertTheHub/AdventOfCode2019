class VM():
    def __init__(self, phase, inside, code_file):
        self.phase = phase
        self.code = self.parse_code(code_file)
        self.counter = 0
        self.stopped = False
        self.done = False
        self.input = inside
        self.output = None

    def parse_code(self, code_file):
        with open(code_file) as f:
            return f.readline().strip().split(",")

    def get_function(self):
        return self.code[self.counter]

    def get_argument(self, position):
        if position == 1:
            return self.code[self.counter + 1]
        elif position == 2:
            return self.code[self.counter + 2]
        else:
            return self.code[self.counter + 3]

    def inc_counter(self, value):
        self.counter += value

    def get_position(self, position):
        if isinstance(position, str):
            return self.code[int(position)]
        if isinstance(position, int):
            return self.code[position]

    def set_value(self, input):
        self.code[int(self.get_argument(3))] = str(input)

    def set_counter(self, value):
        self.counter = value

    def set_input(self, value):
        self.input = value
        self.stopped = False

    def set_output(self, position):
        self.output = self.get_position(position)
        self.stopped = True

    def use_input(self):
        if self.phase:
            self.code[int(self.code[self.counter + 1])] = self.phase
            self.phase = None
        else:
            self.code[int(self.code[self.counter + 1])] = self.input

    def run(self):
        valid = {'1', '2', '5', '6', '7', '8'}
        while self.counter < len(self.code) and not self.stopped and not self.done:
            function = self.get_function()
            if function[-1] in valid:
                try:
                    second = self.get_position(self.get_argument(2))
                except Exception:
                    pass
                try:
                    first = self.get_position(self.get_argument(1))
                except Exception as e:
                    pass
                if len(function) >= 4:
                    if function[-4] == '1':
                        second = self.get_argument(2)
                if len(function) >= 3:
                    if function[-3] == '1':
                        first = self.get_argument(1)
                if function[-1] == '1':
                    self.set_value(str(int(first) + int(second)))
                    self.inc_counter(4)
                elif function[-1] == '2':
                    self.set_value(str(int(first) * int(second)))
                    self.inc_counter(4)
                elif function[-1] == '5':
                    if int(first):
                        self.set_counter(int(second))
                    else:
                        self.inc_counter(3)
                elif function[-1] == '6':
                    if not int(first):
                        self.set_counter(int(second))
                    else:
                        self.inc_counter(3)
                elif function[-1] == '7':
                    if int(first) < int(second):
                        self.set_value(1)
                    else:
                        self.set_value(0)
                    self.inc_counter(4)
                elif function[-1] == '8':
                    if first == second:
                        self.set_value(1)
                    else:
                        self.set_value(0)
                    self.inc_counter(4)
            elif function[-1] == '3':
                self.use_input()
                self.inc_counter(2)
            elif function[-1] == '4':
                if function[0] == '1':
                    self.set_output(self.counter + 1)
                else:
                    self.set_output(self.get_position(self.counter + 1))
                self.inc_counter(2)
                self.stopped = True
            else:
                self.done = True


def permutations(values):
    if len(values) == 1:
        return [values]
    output = []
    for j in range(len(values)):
        perms = permutations(values[:j] + values[j + 1:])
        for i in perms:
            output.append(values[j] + i)
    return output


if __name__ == "__main__":
    maximum = 0
    winner = []
    vals = "56789"
    perms = permutations(vals)
    for perm in perms:
        output = "0"
        vms = {}
        for val in perm:
            vms[val] = VM(val, output, "input1.txt")
            vms[val].run()
            output = vms[val].output
        while len(vms.keys()):
            for val in perm:
                vms[val].set_input(output)
                vms[val].run()
                output = vms[val].output
                if vms[val].done:
                    vms.pop(val)
        if int(output) > maximum:
            winner = perm
            maximum = int(output)
    print(winner, maximum)

