# Use deque: list-like container with fast appends and pops on either end. popleft() -> O(1)

from collections import deque
from typing import Deque
import itertools

lst = [i for i in range(10)]
mid = len(lst) // 2

# deque(lst[0:mid]):    wrong
# deque(lst[1:]):       correct
# can't use 'slice', only integer is allowed in deque()
# use itertools.islice() as follows:
first_half = deque(itertools.islice(lst, 0, mid))
second_half = deque(itertools.islice(lst, mid, len(lst)))

print(first_half)
print(second_half)
print(list(first_half))
print(list(second_half))
