total = 0
with open("input.txt") as file:
    for line in file:
        value = int(line)
        total += max(0, (value // 3) - 2)
print(total)
