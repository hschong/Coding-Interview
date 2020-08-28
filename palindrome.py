palindrome_1 = 'aba'
palindrome_2 = 'abba'
non_palindrome_1 = 'abdcba'
non_palindrome_2 = 'bbbba'


def is_palindrome(string):
    return True if string == string[::-1] else False


def is_palindrome_using_recursive(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome_using_recursive(string[1:-1])
    else:
        return False


print(is_palindrome(palindrome_2))
print(is_palindrome(non_palindrome_1))
print(is_palindrome_using_recursive(palindrome_2))
print(is_palindrome_using_recursive(non_palindrome_1))
