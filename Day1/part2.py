total = 0
with open("input.txt") as file: # Find fuel for the luggage
    for line in file:
        value = int(line)
        while value: #Find fuel for module and the fuel for its fuel
            value = max(0, (value // 3) - 2)
            total += value
print(total)
