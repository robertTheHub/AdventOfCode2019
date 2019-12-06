dic = {}
count = 0
with open("input.txt") as f:
    for line in f:
        count += 1
        inner, outer =  line.strip().split(')')
        dic[inner] = dic.get(inner, []) + [outer]
queue = dic["COM"]
i = 0
while queue:
    nxt = []
    for val in queue:
        count += i
        if val in dic:
             nxt.extend(dic[val])
    queue = nxt
    i += 1
print(count)
