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
