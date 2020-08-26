integers = [1, 2, 5, 4, 7, 3]
characters = ['u', 'a', 'e', 'c', 'k', 'i']
string = 'apple#banana#cherry#orange'


# Sort the items of the list in place.
integers.sort()
integers.sort(reverse=True)

# Return a new sorted list from the items in iterable.
sorted_characters = sorted(characters)
sorted_characters = sorted(characters, reverse=True)

# Split a string into lists
# Setting the maxsplit parameter to 3, will return a list with 4
lists = string.split('#', 3)

# Convert a string to a list
new_list = list(string)
new_list = [character for character in string]

# Convert a list to a string
new_string = ''.join(new_list)
