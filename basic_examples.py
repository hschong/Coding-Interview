import math
import pprint
import collections
import random

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

for _ in range(10):
    print('hi')

_, b = range(2)


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


# random
random.randrange(1, 100, 2)  # start, stop[, step]
random.random()  # random floating point number in the range [0.0, 1.0].

# a <= N <= b is equivalent to range(a, b+1)
random.randint(1, 100)
random.uniform(1.0, 100.0)
random.randrange(1, 101)
