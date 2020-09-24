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


def three_generator():
    yield from generate_nums(3)


for item in generate_nums(3):  # simple
    print(item)

for item in three_generator():
    print(item)


def upper_generator(lst: List):
    for item in lst:
        yield item.upper()


fruits = ['apple', 'pear', 'orange']
for item in upper_generator(fruits):
    print(item)


def is_prime_number(number: int, primes: List) -> bool:
    try:
        if not isinstance(number, int):
            raise Exception("not number")

    except Exception as e:
        raise RuntimeError(e)

    else:
        if number < 2:
            return False

        for prime in primes:
            if number % prime == 0:
                return False

        for i in range(11, number, 2):
            if number % i == 0:
                if i not in primes:
                    primes.append(i)
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
        prime_numbers = [2, 3, 5, 7]
        for i in range(a, b+1):
            if is_prime_number(i, prime_numbers) == True:
                prime_numbers.append(i)
                yield i


a, b = map(int, input("type 2 numbers: ").split())
g = generate_prime_numbers(a, b)
for i in g:
    print(i, end=' ')
