path = "input.txt"

bad_reactions = {}
reactions = {}
with open(path) as f:
    for line in f:
        line = line.strip()
        items, product = line.split('=>')
        val, prod = product.strip().split(' ')
        reactions[prod] = {}
        reactions[prod]["OUT"] = int(val)
        bad_reactions[prod] = {}
        for item in items.strip().split(', '):
            subval, subprod = item.split(' ')
            bad_reactions[prod][subprod] = float(subval)/float(val)
            reactions[prod][subprod] = int(subval)

count = 0
priority = [['ORE']]
check = set()
check.add('ORE')
while count < len(bad_reactions.keys()):
    new_set = set()
    new_list = []
    for key, value in bad_reactions.items():
        if key in check:
            continue
        else:
            add = True
            for subkey in value.keys():
                if subkey not in check:
                    add = False
                    break
            if add:
                new_set.add(key)
                new_list.append(key)
                count += 1
    check.update(new_set)
    priority.append(new_list)

need = {"FUEL": 1}
extra = {}
for chunk in priority[::-1]:
    if chunk == ["ORE"]:
        continue
    for prod in chunk:
        need_amt = need[prod]
        extra_amt = extra.get(prod, 0)
        ratio = reactions[prod]["OUT"]
        if extra_amt >= need_amt:
            extra[prod] -= need_amt
        else:
            additional = need_amt - extra_amt
            mult = -(-additional//ratio)
            extra[prod] = (ratio*mult) - additional
            for key,value in reactions[prod].items():
                if key == "OUT":
                    continue
                else:
                    need[key] = need.get(key, 0) + (value*mult)
print(need['ORE'])


