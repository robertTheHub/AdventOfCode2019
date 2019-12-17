input_list = []
extra = []
with open("input.txt") as f:
    text = f.readline().strip()
    for ch in text:
        input_list.append(int(ch))
        extra.append(int(ch))
    offset = int(text[:7])
for i in range(10000-1):
    input_list.extend(extra)
print(len(input_list), offset)
input_list = input_list[offset:]
input_list = input_list[::-1]

for phases in range(100):
    new = []
    temp = 0
    for num in input_list:
        temp += num
        temp1 = temp%10
        new.append(temp1)
    input_list = new
    print("pulse:", phases+1)
print(input_list)
