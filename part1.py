with open("input.txt") as f:
    text = f.readline().strip()
i = 0
minimum = 150
count_0, count_1, count_2, value = 0,0,0,0
while i < len(text):
    if i % 150 == 0 and i != 0:
        if count_0 < minimum:
           value = count_1 * count_2
           minimum = count_0
        count_0, count_1, count_2 = 0,0,0
    if text[i] == "0":
        count_0 += 1
    elif text[i] == "1":
        count_1 += 1
    elif text[i] == "2":
        count_2 += 1
    i += 1
print(minimum, value)

