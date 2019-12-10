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
for loc in asteroids:
    count_left = set()
    count_right = set()
    for spot in asteroids:
        if loc == spot:
            continue
        elif loc[0] == spot[0]:
            if loc[1] > spot[1]:
                count_left.add("inf")
            else:
                count_right.add("inf")
        else:
            slope = (loc[1]-spot[1])/(loc[0] - spot[0])
            if loc[0] < spot[0]:
                count_right.add(slope)
            else:
                count_left.add(slope)
    total = len(count_left) + len(count_right)
    if total > maximum:
        maximum = total
        winner = loc
print(maximum, winner)
