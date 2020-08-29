import math

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
