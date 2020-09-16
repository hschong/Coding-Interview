# Lambda
def judge(score):
    return 'pass' if score >= 80 else 'fail'
#judge = lambda score: 'pass' if score>=80 else 'fail'


def add(a, b): return a+b
# add = lambda a, b: a + b


def calculate(a, b, func):
    return func(a, b)


calculate(3, 4, add)


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

    print('local total = ', total)
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
