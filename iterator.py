import random


# iterator
it = range(10).__iter__()
print(it.__next__())
print(it.__next__())


# iter(object[, sentinel])
for num in iter(lambda: random.randrange(0, 100), 7):
    print("random number is ", num)


# range()
class Counter():
    def __init__(self, stop):
        self.cur = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.stop:
            result = self.cur
            self.cur += 1

            return result
        else:
            raise StopIteration
