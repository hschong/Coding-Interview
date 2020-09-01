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
lst = ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'f', 'e']
string = 'abcdeabcdabcaba'

most_common_lst = collections.Counter(string).most_common(2)
# print(count_dic)
# Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
count_dic = collections.Counter(lst)
# print(lst)
# Counter({'e': 3, 'f': 2, 'a': 1, 'b': 1, 'c': 1, 'd': 1})
