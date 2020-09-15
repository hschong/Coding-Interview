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


# Lambda
def add(a, b): return a+b  # add = lambda a, b: a + b


def calculate(a, b, func):
    return func(a, b)


calculate(3, 4, add)


# judge = lambda score: 'pass' if score>=80 else 'fail'
def judge(score): return 'pass' if score >= 80 else 'fail'


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


# Storage class
# https://www.geeksforgeeks.org/storage-classes-in-c-with-examples/
def manipulate_global_variable_in_func():
    global x
    x = 11


def func():
    x = 12
    print("local x = ", x)

    def func_in_func():
        nonlocal x
        x = 13

    func_in_func()
    print("after func_in_func() = ", x)


x = 10
print("golbal x = ", x)
manipulate_global_variable_in_func()
print("after manipulate_global_variable_in_func() = ", x)
func()


# Closure
def calc():
    a, b = 3, 5

    def mul_add(x):
        return a * x + b

    return mul_add


def calc_total():
    a, b, total = 3, 5, 0

    def mul_add(x):
        nonlocal total
        total = a * x + b
        print(total, end=' ')

    return mul_add


def calc_using_lambda():
    a, b = 3, 5
    return lambda x: a * x + b


c = calc()
print("closure:", end=' ')
for i in range(1, 11):
    print(c(i), end=' ')
print()

c_t = calc_total()
print("closure total:", end=' ')
for i in range(1, 11):
    c_t(i)
print()

c_l = calc_using_lambda()
print("closure lambda:", end=' ')
for i in range(1, 11):
    print(c_l(i), end=' ')
print()
