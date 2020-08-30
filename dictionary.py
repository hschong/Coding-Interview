from collections import defaultdict
# import collections

dic = defaultdict(int)
dic['A'] = 90
dic['B'] = 80
dic['C'] += 1

for key, val in dic.items():
    print(key, val)

lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dic = defaultdict(list)
for k, v in lst:
    dic[k].append(v)

sorted(dic.items())
