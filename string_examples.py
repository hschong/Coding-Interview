string = 'apple#banana#cherry#orange'
name = 'heeseok'
text = 'a fine day'


# Split a string into lists.
# Setting the maxsplit parameter to 3, will return a list with 4.
new_list = string.split('#', 3)
# the default means split according to any white space, and discard empty strings from the result.
new_list = string.split()


# Convert a string to a list.
new_list = list(string)

# Convert a list to a string.
new_string = ''.join(new_list)

# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found.
integers = "123456789012345"
index = integers.find('1')  # return the first index of 'pl'.
index = integers.find('11')  # returns -1.
index = integers.rfind('5')  # returns 14.

# str.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.
index = integers.index('1')
# index = integers.index('11')  # ValueError

# String object is immutable.
# name[0] = 'H' wrong! using str.replace() instead of assignment.
new_name = name.replace('h', 'H')


# Reverse string
reverse_string = string[-1::-1]
reverse_string = string[::-1]
reverse_string = ''.join(list(reversed(list(string))))

# Capital
new_text = text.capitalize()
new_text = text.title()
new_text = new_text.swapcase()
new_text = text.upper()
new_text = text.lower()

# Strip
strip_sample = "    ,[strip sample],    "
strip_sample.lstrip()
strip_sample.rstrip()
strip_sample.strip()

strip_sample_1 = ",[strip sample],"
strip_sample_1.lstrip(',')
strip_sample_1.rstrip(',')
strip_sample_1.strip(',')
