import math
import pprint
import copy

# Using infinity
# import math
INFINITY = math.inf
NEGATIVE_INFINITY = -math.inf

integers = [1, 2, 5, 4, 7, 3]
characters = ['u', 'a', 'e', 'c', 'k', 'i']
dictionary = {'a': 90, 'b': 80, 'c': 70, 'd': 60, 'f': 59}


# Sort the items of the list in place.
integers.sort()
integers.sort(reverse=True)

# Return a new sorted list from the items in iterable.
sorted_characters = sorted(characters)
sorted_characters = sorted(characters, reverse=True)


# For loop
for idx, val in enumerate(characters):
    print(idx, val)

for key, val in dictionary.items():
    print(key, val)

for countdown in 5, 4, 3, 2, 1, 'hey!':
    print(countdown)


sum_from_1_to_10 = 0
sum_from_1_to_10 = sum(range(1, 11))
for number in range(1, 10+1, 1):
    sum_from_1_to_10 += number


# Lambda
def add(a, b): return a+b  # add = lambda a, b: a + b


def calculate(a, b, func):
    return func(a, b)


calculate(3, 4, add)


# judge = lambda score: 'pass' if score>=80 else 'fail'
def judge(score): return 'pass' if score >= 80 else 'fail'


# print usages.
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
lst_b = lst_a[:]  # lst_a.copy(), list(lst_a)

if lst_a is lst_b:  # 'is' compares id(lst_a) with id(lst_b).
    print('same id')

if lst_a == lst_b:  # '==' compares value of 'lst_a' with value of 'lst_b'.
    print('same value')

# mutalbe object(list) in mutable object(list)
lst_c = [[1, 2, 3], 'a', 'b', 'c']
lst_d = lst_c[:]
lst_e = copy.deepcopy(lst_c)
lst_c[0].append(4)

# lst_d == [[1, 2, 3, 4], 'a', 'b', 'c']
# lst_e == [[1, 2, 3], 'a', 'b', 'c']
