palindrome_1 = 'aba'
palindrome_2 = 'abba'
non_palindrome_1 = 'abdcba'
non_palindrome_2 = 'bbbba'


def is_palindrome(S: str) -> bool:
    return True if S == S[::-1] else False


def is_palindrome_using_recursive(S) -> bool:
    if len(S) <= 1:
        return True

    if S[0] == S[-1]:
        return is_palindrome_using_recursive(S[1:-1])
    else:
        return False


print(is_palindrome(palindrome_2))
print(is_palindrome(non_palindrome_1))
print(is_palindrome_using_recursive(palindrome_2))
print(is_palindrome_using_recursive(non_palindrome_1))
