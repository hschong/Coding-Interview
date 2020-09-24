# Generator-based Coroutines
# Note Support for generator-based coroutines is deprecated and is scheduled for removal in Python 3.10.

# send data to a coroutine
def continue_number():
    while True:
        x = (yield)
        print("continue_number(): ", x)


co = continue_number()
next(co)  # is equivalent to co.send(None)
co.send(1)
co.send(2)
co.send(3)


# send data to a coroutine and receive the data from the coroutine
def get_total():
    total = 0

    while True:
        outer = (yield total)
        total += outer


co = get_total()
print(co.send(None))
print(co.send(1))
print(co.send(2))
print(co.send(3))
