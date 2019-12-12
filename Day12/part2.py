moons = [[[] for i in range(2)] for j in range(4)]
i = 0
count = []
with open("input.txt") as f:
    for line in f:
        count.append(i)
        for word in line.strip()[1:-1].split(', '):
            value = word.split('=')[1]
            moons[i][0].append(int(value))
            moons[i][1].append(0)
        i += 1
output = []
for axis in range(3):
    seen = {}
    vals = []
    for j in range(4):
        vals.append(moons[j][0][axis])
        vals.append(moons[j][1][axis])
    seen[tuple(vals)] = 1
    i = 1
    while True:
        for j in range(4):
            for moon in count[:j] + count[j + 1:]:
                if moons[j][0][axis] < moons[moon][0][axis]:
                    moons[j][1][axis] += 1
                elif moons[j][0][axis] > moons[moon][0][axis]:
                    moons[j][1][axis] -= 1
        vals = []
        for j in range(4):
            moons[j][0][axis] += moons[j][1][axis]
            vals.append(moons[j][0][axis])
            vals.append(moons[j][1][axis])
        vals = tuple(vals)
        if vals in seen:
            break
        else:
            seen[vals] = 1
            i+= 1
    output.append(i)
print(output)

