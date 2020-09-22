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
        it = generate_nums(3)
        for num in it:
            print(num)

        # x = next(it)

    except Exception as e:
        raise RuntimeError("exception occurred in test_divide(): ", e)


test_generator()
