integers = [1, 2, 5, 4, 7, 3]
characters = ['u', 'a', 'e', 'c', 'k', 'i']
duplicates = ['a', 'b', 'a', 'c', 'c']
languages = ['Korean']
languages_tuple = ('English', 'German')


# Reverse list.
def reverse_list(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
        return list(lst[0]) + reverse_list(lst[1:-1]) + list(lst[-1])
    else:
        return lst


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
if 'a' not in characters:
    print("'a' is not in character")
else:
    index = characters.index('a')

# Remove all items from list.
characters.clear()
del characters[:]
characters = []
characters[:] = []
characters *= 0

# characters == characters[:1] + characters[1:]
characters[1:] = []

occurrences = characters.count('a')
languages.extend(languages_tuple)
