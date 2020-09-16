import math
import pprint
import collections

# Using infinity
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf


# For loop
string = "abcdef"
chars = ['u', 'a', 'e', 'c', 'k', 'i']
dic = collections.defaultdict(int)
dic['A'] = 90
dic['B'] = 80
dic['C'] = 1

for char in string:  # str
    print(char)

for idx, val in enumerate(chars):  # list
    print(idx, val)

for key, val in dic.items():  # dict
    print(key, val)

for countdown in 5, 4, 3, 2, 1, 'hey!':
    print(countdown)


sum_from_1_to_10 = sum(range(1, 11))


# print() usages.
idx = 0
fruit = 'apple'
print('a', 'b', sep=', ')
print('aa', end=' ')
print('bb')
print('{0}: {1}'.format(idx, fruit))
print('{}: {}'.format(idx, fruit))
print(f'{idx}: {fruit}')  # 3.6+


# Return a dictionary containing the current scope's local variables.
# import pprint
pprint.pprint(locals())


# Differences between 'is' and  '=='
# Return a shallow copy of the list.
lst_a = [1, 2, 3]
lst_b = lst_a[:]  # lst_a.copy(), list([1, 2, 3])

if lst_a is lst_b:  # 'is' compares id(lst_a) with id(lst_b).
    print('same id')

if lst_a == lst_b:  # '==' compares value of 'lst_a' with value of 'lst_b'.
    print('same value')
