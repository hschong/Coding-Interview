from typing import List
import random

# iter(object[, sentinel])
for num in iter(lambda: random.randrange(0, 100), 7):
    print("random number is ", num)


# simple generator
def generate_nums(stop):
    num = 0

    while num < stop:
        yield num
        num += 1


def test_generator():
    try:
        yield from generate_nums(3)
        # x = next(it)

    except Exception as e:
        raise RuntimeError("exception occurred in test_divide(): ", e)


def upper_generator(lst: List):
    for item in lst:
        yield item.upper()


fruits = ['apple', 'pear', 'orange']
for item in upper_generator(fruits):
    print(item)

for item in test_generator():
    print(item)


def is_prime_number(number):
    try:
        if not isinstance(number, int):
            raise Exception("not number")

    except Exception as e:
        raise RuntimeError(e)

    else:
        if number < 2:
            return False
        elif number == 2 or number == 3:
            return True

        # remove even numbers and multiplication of 3
        if number % 2 == 0 or number % 3 == 0:
            return False

        for i in range(5, number, 2):
            if i % 3 == 0:
                continue

            if number % i == 0:
                return False

        return True


# a < b, 10 <= a <= 1000, 100 <= b <= 1000
def generate_prime_numbers(a, b):
    try:
        if a >= b:
            raise Exception('a is must less than b.')
        if a < 10 or a > 1000:
            raise Exception('10 <= a <= 1000')
        if b < 100 or b > 1000:
            raise Exception('100 <= b <= 1000')

    except Exception as e:
        raise RuntimeError(e)

    else:
        for i in range(a, b+1):
            if is_prime_number(i) == True:
                yield i


a, b = map(int, input("type 2 numbers: ").split())
g = generate_prime_numbers(a, b)
for i in g:
    print(i, end=' ')
