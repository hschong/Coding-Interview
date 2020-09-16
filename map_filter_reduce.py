import functools

integers = [1, 2, 5, 4, 7, 3]
float_nums = [1.2, 2.5, 3.1, 4.0, 5.00]
langs = ['Korean', 'Japanese', 'Chinese', 'Spanish']


# Using map() to convert float numbers to int numbers
int_nums = list(map(int, float_nums))
int_nums = list(map(lambda num: int(num), float_nums))
int_nums_1 = [int(num) for num in float_nums]


# filter()
def f(x: int):
    return True if x > 1 and x < 5 else False


list(filter(f, integers))  # [3, 4]
list(filter(lambda num: num > 1 and num < 5, integers))  # [3, 4]
[num for num in integers if num > 1 and num < 5]  # [3, 4]


# Using List/Dictionary comprehension instead of map() or filter().
lst = [num*2 for num in range(1, 11) if num % 2 == 1]
dic = {key: value for key, value in enumerate(lst)}


# functools.reduce()
# using reduce to compute sum of list
functools.reduce(lambda prev, cur: prev + cur, integers)
sum_from_1_to_10 = sum(range(1, 11))

# using reduce to compute maximum element from list
functools.reduce(lambda prev, cur: prev if prev > cur else cur, integers)

# append cur string to prev string
functools.reduce(lambda prev, cur: prev + cur, langs)
