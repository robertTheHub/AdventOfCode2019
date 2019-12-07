def runner(phase, input_signal):
    with open("input.txt") as f:
         lst = f.readline().split(',')
    io = phase
    i = 0
    valid = {'1', '2', '5', '6', '7', '8'}
    while i < len(lst):
        if lst[i][-1] in valid:
            try:
                second = lst[int(lst[i+2])]
            except Exception:
                pass
            try:
                first = lst[int(lst[i+1])]
            except Exception:
                pass
            if len(lst[i]) >= 4:
                if lst[i][-4] == '1':
                    second = lst[i+2]
            if len(lst[i]) >= 3:
                if lst[i][-3] == '1':
                    first = lst[i+1]
            if lst[i][-1] == '1':
                lst[int(lst[i+3])] = str(int(first) + int(second))
                i += 4
            elif lst[i][-1] == '2':
                lst[int(lst[i+3])] = str(int(first) * int(second))
                i += 4
            elif lst[i][-1] == '5':
                if int(first):
                     i = int(second)
                else:
                     i += 3
            elif lst[i][-1] == '6':
                if not int(first):
                     i = int(second)
                else:
                     i += 3
            elif lst[i][-1] == '7':
                if first < second:
                     lst[int(lst[i+3])] = 1
                else:
                     lst[int(lst[i+3])] = 0
                i += 4
            elif lst[i][-1] == '8':
                if first == second:
                     lst[int(lst[i+3])] = 1
                else:
                     lst[int(lst[i+3])] = 0
                i += 4
        elif lst[i][-1] == '3':
            lst[int(lst[i+1])] = io
            io = input_signal
            i += 2
        elif lst[i][-1] == '4':
            if lst[i][0] == '1':
                 return(lst[i+1])
            else:
                 return(lst[int(lst[i+1])])
            i += 2
        else:
            return(lst[i])
def permutations(values):
    if len(values) == 1:
        return [values]
    output = []
    for j in range(len(values)):
        perms = permutations(values[:j]+values[j+1:])
        for i in perms:
            output.append(values[j] + i)
    return output
            
maximum = 0
winner = []
vals = "01234"
perms = permutations(vals)
for perm in perms:
    output = "0"
    for val in perm:
        output = runner(val, output) 
    if int(output) > maximum:
        winner = perm
        maximum = int(output)
print(winner, maximum)
