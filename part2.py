with open("input.txt") as f:
    text = f.readline().strip()
picture = [[2 for i in range(25)] for j in range(6)]
i = 0
minimum = 150
height = 0
width = 0
while i < len(text):
    if text[i] == "0":
        if picture[height][width] == 2:
            picture[height][width] = 0
    elif text[i] == "1":
        if picture[height][width] == 2:
            picture[height][width] = 1
    width += 1
    if not width % 25:
        height += 1
        width = 0
    if not height % 6:
        height = 0
    i += 1
for line in picture:
    print(line)
