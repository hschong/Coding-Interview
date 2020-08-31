integers = [1, 2, 5, 4, 7, 3]
chars = ['u', 'a', 'e', 'c', 'k', 'i']
duplicates = ['a', 'b', 'a', 'c', 'c']
lang = ['Korean']
lang_tuple = ('English', 'German')

# Sort the items of the list in place.
integers.sort()
integers.sort(reverse=True)

# Return a new sorted list from the items in iterable.
sorted_chars = sorted(chars)
sorted_chars = sorted(chars, reverse=True)
sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# Reverse list.
integers.reverse()
reverse_integers = list(reversed(integers))  # returns reverse iterator.

# Remove duplicates from list.
non_duplicate = list(dict.fromkeys(duplicates))

# Append/Insert an object in a list.
integers.append(1)
integers.insert(0, 1)

# Remove and return item at index (default last).
last_item = integers.pop()
item_at_1 = integers.pop(1)
integers.remove(1)  # remove first occurrence of value.

# Return first index of value from list.
if 'a' not in chars:
    print("'a' is not in character")
else:
    index = chars.index('a')

# Remove all items from list.
chars.clear()
del chars[:]
chars = []
chars[:] = []
chars *= 0

# chars == chars[:1] + chars[1:]
chars[1:] = []

occurrences = chars.count('a')
lang.extend(lang_tuple)

# Using List/Dictionary comprehension instead of map() or filter().
lst = [number*2 for number in range(1, 10 + 1) if number % 2 == 1]
dic = {key: value for key, value in enumerate(lst)}
