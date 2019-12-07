class VM():
    def __init__(self, phase, inside, code_file):
        self.phase = phase
        self.code = self.parse_code(code_file)
        self.counter=0
        self.stopped = False
        self.done = False
        self.input = inside
        self.output = None

    def parse_code(self, code_file):
        with open(code_file) as f:
            return f.readline().split(",")

    def get_function(self):
        return self.code[self.counter]

    def get_argument(self, position):
        if position == 1:
            return self.code[self.counter+1]
        elif position == 2:
            return self.code[self.counter+2]
        else:
            return self.code[self.counter+3]

    def inc_counter(self, value):
        self.counter += value

    def get_position(self, position):
        if isinstance(position, str):
            return self.code[int(position)]
        if isinstance(position, int):
            return self.code[position]

    def set_value(self, input):
        self.code[int(self.get_argument(3))] = input

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
                    if first < second:
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
                    self.set_output(self.counter+1)
                else:
                    self.set_output(self.get_position(self.counter+1))
                self.inc_counter(2)
                self.stopped = True
            else:
                self.done = True

def permutations(values):
    if len(values) == 1:
        return [values]
    output = []
    for j in range(len(values)):
        perms = permutations(values[:j]+values[j+1:])
        for i in perms:
            output.append(values[j] + i)
    return output

if __name__ == "__main__":
   vm = VM("18", "18", "test5.txt")
#"../Day5/input.txt")
   while not vm.done:
       vm.run()
       if vm.stopped:
           print(vm.output)
       vm.set_input("18")
   print(vm.output) 
   
"""
maximum = 0
winner = []
vals = "56789"
perms = permutations(vals)
perms = ["98765"] # 9 7 8 5 6 => 18216 ; 98765=>139629729
for perm in perms:
    output = "0"
    paths = {}
    with open("input.txt") as f:
         text = f.readline()
         for val in vals:
             lst = text.split(',')
             paths[val] = (lst, 0, val)
    temp_perm = perm
    count = 0
    while True:
        if not perm:
            break
        for val in perm:
            if count != 0:
                phase = output
            else:
                phase = val
            temp = runner(phase, output, paths[val][0], paths[val][1], paths)
            if temp is None:
                break
            elif temp == "99":
                i = perm.index(val)
                temp_perm = temp_perm[:i] + temp_perm[i+1:]
            else:
                output = temp
        perm = temp_perm
        count = 1
        print(temp)
        if temp is None:
            break
#        if temp == "99":
#            break
    if int(output) > maximum:
        winner = perm
        maximum = int(output)
print(winner, maximum)
"""
