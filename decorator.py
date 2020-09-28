import time


# not using decorator
def print_timestamps(func):
    def wrapper():
        start = time.perf_counter()
        print(f"start: {start}, {func.__name__}")
        func()
        end = time.perf_counter()
        print(f"end: {end}, {func.__name__}")

    return wrapper


def say_hello():
    print('hello')


def say_world():
    print('world')


print_hello = print_timestamps(say_hello)
print_world = print_timestamps(say_world)
print_hello()
print_world()


# using decorator
def print_timestamps_using_decorator(func):
    def wrapper():
        start = time.perf_counter()
        print(f"start: {start}, {func.__name__}")
        func()
        end = time.perf_counter()
        print(f"end: {end}, {func.__name__}")

    return wrapper


@print_timestamps_using_decorator
def say_hello_using_decorator():
    print('hello1')


@print_timestamps_using_decorator
def say_world_using_decorator():
    print('world1')


say_hello_using_decorator()
say_world_using_decorator()


# passing arguments and returning return value in decorator
def print_add(func):
    def wrapper(a, b):
        result = func(a, b)
        print(f'func = {func.__name__}, a = {a}, b = {b}, result = {result}')
        return result
    return wrapper


@print_add
def add(a, b):
    return a+b


print(add(3, 4))


# variadic arguments
def print_arguments(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'func = {func.__name__}, *args: {args}, **kwargs: {kwargs}')
        return result
    return wrapper


@print_arguments
def get_max(*args):
    return max(args)


@print_arguments
def get_min(**kwargs):
    return min(kwargs.values())


print(get_max(10, 20))
print(get_min(x=10, y=20, z=5))
