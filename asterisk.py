# There are 4 cases for using the asterisk in Python.
from functools import reduce

# 1. multiplication and power operations.
mul = 2 * 3  # 6
power = 2 ** 3  # 8

# 2. repeatedly extending the list-type containers.
zeros_list = [0] * 5
zeros_tuple = (0,) * 5
print(zeros_list)
print(zeros_tuple)
vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):
    print([(i + 1) * e for e in vector])


# 3. using the variadic arguments. (so-called “packing”)
# *args(positional arguments): tuple
# **kwargs(keyword arguments): dict
def save_ranking(*args, **kwargs):
    print(args)
    print(kwargs)


# 4. unpacking the containers.
def product(*numbers):
    return reduce(lambda x, y: x * y, numbers)


primes = [2, 3, 5, 7, 11, 13]
print(product(*primes))  # 30030
print(product(primes))  # an only argument [2, 3, 5, 7, 11, 13]


def pre_process(**headers):
    content_length = headers['Content-Length']
    print('content length: ', content_length)

    host = headers['Host']
    if 'https' not in host:
        raise ValueError('You must use SSL for http communication')


headers = {
    'Accept': 'text/plain',
    'Content-Length': 348,
    'Host': 'http://mingrammer.com'
}
pre_process(**headers)


numbers = [1, 2, 3, 4, 5, 6]
# left side should be a tuple or a list.
*a, = numbers  # a = [1, 2, 3, 4, 5, 6]
*a, b = numbers  # a = [1, 2, 3, 4, 5],  b = 6
a, *b, = numbers  # a = 1, b = [2, 3, 4, 5, 6]
a, *b, c = numbers  # a = 1, b = [2, 3, 4, 5], c = 6
