input_list = []
extra = []
with open("input.txt") as f:
    text = f.readline().strip()
    for ch in text:
        input_list.append(int(ch))
        extra.append(int(ch))
    offset = int(text[:7])
#for i in range(10000):
#    input_list.extend(extra)
pat = [0,1,0,-1]

for phases in range(100):
    new = []
    for i in range(1, len(input_list)+1):
        temp = 0
        count = 1
        position = 0
        for num in input_list:
            if (count % i) == 0:
                position += 1
                position = (position % len(pat))
            temp += (num * pat[position])
            count += 1

        temp = abs(temp)%10
        new.append(temp)
    input_list = new
    print("pulse:", phases+1)
print(input_list[offset+1:offset+9])
