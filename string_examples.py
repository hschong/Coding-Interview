string = 'apple#banana#cherry#orange'
name = 'heeseok'


# Split a string into lists.
# Setting the maxsplit parameter to 3, will return a list with 4.
new_list = string.split('#', 3)

# Convert a string to a list.
new_list = list(string)

# Convert a list to a string.
new_string = ''.join(new_list)

# String object is immutable.
# name[0] = 'H' wrong! using str.replace() instead of assignment.
new_name = name.replace('h', 'H')

# Reverse string
reversed_string = string[-1::-1]
reversed_string = string[::-1]
reversed_string = ''.join(list(reversed(list(string))))
