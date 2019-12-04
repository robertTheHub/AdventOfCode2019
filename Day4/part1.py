low = 245182
up = 790572
count = 0
i = low + 1
while i < up:
    digits = str(i)
    valid = True
    double = False
    repeated = digits[0]
    rep_count = 1
    for j in range(5):
        if digits[j] == digits[j+1]:
            double = True
        elif digits[j] > digits[j+1]:
            i = int(digits[:j+1] + (digits[j] * (5-j)))
            valid = False
            break
    if valid:
        i += 1
        if double:
            count += 1
print(count)


