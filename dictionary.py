import collections

# Default dictionary
dic = collections.defaultdict(int)
dic['A'] = 90
dic['B'] = 80
dic['C'] += 1

for key, val in dic.items():
    print(key, val)

lst = [('white', 1), ('blue', 2), ('white', 3), ('blue', 4), ('red', 1)]
dic = collections.defaultdict(list)
for k, v in lst:
    dic[k].append(v)

sorted(dic.items(), reverse=True)


# Counter object
lst = [1, 2, 3, 4, 5, 5, 6, 6, 5]
count_dic = collections.Counter(lst)
# Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
