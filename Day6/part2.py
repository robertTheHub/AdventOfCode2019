dic = {}
count = 0
with open("input.txt") as f:
    for line in f:
        inner, outer =  line.strip().split(')')
        dic[outer] = dic.get(outer, []) + [inner]
if dic["SAN"] == dic["YOU"]:
    print(count)
else:
    san_path = dic["SAN"]
    nxt =  dic["SAN"][0]
    while nxt != "COM":
        nxt = dic[nxt][0]
        san_path.append(nxt)
    nxt = dic["YOU"][0]
    while nxt != "COM":
        nxt = dic[nxt][0]
        if nxt in san_path:
            count += 1
            count += san_path.index(nxt)
            break
        else:
            count += 1    
print(count)
