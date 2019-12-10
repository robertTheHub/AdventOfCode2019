asteroids = set()
y = 0
with open("input.txt") as f:
    for line in f:
        x = 0
        for ch in line:
            if ch == "#":
                asteroids.add((x,y))
            x += 1
        y += 1
winner = 0
maximum = 0
loc = (26,29)
count_left = {}
count_right = {}
for spot in asteroids:
    if loc == spot:
        continue
    else:
        distance = (loc[0]-spot[0])**2 + (loc[1]-spot[1])**2
        spot = (spot[0], spot[1], distance)
        if loc[0] == spot[0]:
            if loc[1] < spot[1]:
                count_left["inf"] = count_left.get("inf", []) + [spot]
            else:
                count_right["inf"] = count_right.get("inf", []) + [spot]
        else:
            slope = (loc[1]-spot[1])/(loc[0] - spot[0])
            if loc[0] < spot[0]:
                count_right[slope] = count_right.get(slope, []) + [spot]
            else:
                count_left[slope] = count_left.get(slope, []) + [spot]
left = []
right = []
for i in count_left.keys():
    if i != "inf":
        left.append(i)
    count_left[i].sort(key=lambda tup: tup[2], reverse=True)
for i in count_right.keys():
    if i != "inf":
        right.append(i)
    count_right[i].sort(key=lambda tup: tup[2], reverse=True)
left.sort()
right.sort()
count = 0
winner = ()
order = []
while count < 200:
    if len(count_right["inf"]):
        count += 1
        val = count_right["inf"].pop()
        if count == 200:
            winner = val
            break
    new = []
    for i in right:
        count += 1
        val = count_right[i].pop()
        if count == 200:
            winner = val
            break
        if len(count_right[i]):
            new.append(i)
    right = new
    if len(count_left["inf"]):
        count += 1
        val = count_left["inf"].pop()
        if count == 200:
            winner = val
            break
    new = []
    for i in left:
        count += 1
        val = count_left[i].pop()
        if count == 200:
            winner = val
            break
        if not len(count_left[i]):
            new.append(i)
    left = new
print(count, val)
