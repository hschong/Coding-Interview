import collections

dic = dict(x=10, y=11)  # {'x': 10, 'y': 11}
dic = dict()
dic['a'] = 1
dic['b'] = 2
dic.setdefault('c', 3)

dic.pop('a')
k, v = dic.popitem()  # Changed in version 3.7: LIFO order is now guaranteed

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
    # When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list.
    dic[k].append(v)

if 'white' in dic:
    print("key in dict")

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
