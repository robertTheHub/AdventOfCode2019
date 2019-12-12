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

for i in range(1000):
    for j in range(4):
        for moon in count[:j] + count[j+1:]:
            for axis in range(3):
                if moons[j][0][axis] < moons[moon][0][axis]:
                    moons[j][1][axis] += 1
                elif moons[j][0][axis] > moons[moon][0][axis]:
                    moons[j][1][axis] -= 1
    for j in range(4):
        for axis in range(3):
            moons[j][0][axis] += moons[j][1][axis]
energy = 0
for pair in moons:
    kin = 0
    pot = 0
    for val in pair[0]:
        pot += abs(val)
    for val in pair[1]:
        kin += abs(val)
    energy += kin * pot
print(energy)
