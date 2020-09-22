from typing import List
import copy


integers = [1, 2, 5, 4, 7, 3]
chars = ['u', 'a', 'e', 'c', 'k', 'i']
# duplicates = ['a', 'b', 'a', 'c', 'c']
duplicates = ['a', 'b', 'a', 'c', 'c', 'a', 'b', 'a', 'c', 'c', 'a',
              'b', 'a', 'c', 'c', 'a', 'b', 'a', 'c', 'c', 1, 2, 5, 4, 7, 3, 'u', 'a', 'e', 'c', 'k', 'i', 'Korean', 'Japanese', 'Chinese', 'Spanish', 'English', 'German', 'Korean', 'Japanese', 'Chinese', 'Spanish']
lang = ['Korean', 'Japanese', 'Chinese', 'Spanish']
lang_tuple = ('English', 'German')


# Sort the items of the list in place.
integers.sort()
integers.sort(reverse=True)
lang.sort(key=len)
lang.sort(key=lambda lang: (lang[0], lang[-1]))  # ordering: lang[0] -> lang[1]

# Return a new sorted list from the items in iterable.
sorted_chars = sorted(chars)
sorted_chars = sorted(chars, reverse=True)
sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


# Reverse list.
integers.reverse()
reverse_integers = list(reversed(integers))  # returns reverse iterator.


# list.append(obj)
chars.append('1')
# list.insert(idx, obj)
chars.insert(100, '2')
chars.insert(100, '1')
chars.insert(100, '2')


# Remove and return item at index (default last).
last_item = integers.pop()
item_at_1 = integers.pop(1)
integers.remove(1)  # remove first occurrence of value.


# Remove all items from list.
chars.clear()
del chars[:]
chars = []
chars[:] = []
chars *= 0

# chars == chars[:1] + chars[1:]
chars[1:] = []


# list.index(item[, start[, end]])
# Raises a ValueError if there is no such item.
# a function such as str.find() is not supported in list.
index = chars.index('2', 7, -1)
# index = chars.index('2', 8, -1) # ValueError occurred

# Return first index of value from list.
if 'a' not in chars:
    print("'a' is not in character")
else:
    index = chars.index('a')


# mutalbe object(list) in mutable object(list)
lst_c = [[1, 2, 3], 'a', 'b', 'c']
lst_d = lst_c[:]
lst_e = copy.deepcopy(lst_c)
lst_c[0].append(4)
# lst_d == [[1, 2, 3, 4], 'a', 'b', 'c']
# lst_e == [[1, 2, 3], 'a', 'b', 'c']


# Remove duplicates from list.
def remove_duplicates(lst: List) -> List:  # O(n²)
    non_duplicate_list = []

    for item in lst:  # O(n)
        if item not in non_duplicate_list:  # O(n)
            non_duplicate_list.append(item)

    return non_duplicate_list


# dict.fromkeys() is much faster than using for looping. O(n) x O(1)
non_duplicate_list = list(dict.fromkeys(duplicates))


occurrences = chars.count('a')
lang.extend(lang_tuple)
