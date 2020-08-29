# 125. Valid palindrome
# https://leetcode.com/problems/valid-palindrome/#

from typing import List

palindrome = 'A man, a plan, a canal: Panama'
palindrome_1 = 'aba'
palindrome_2 = 'abba'
non_palindrome_1 = 'abdcba'
non_palindrome_2 = 'bbbba'
test_sample = palindrome


class Solution:
    def remove_non_alphanumeric_characters(self, S: str) -> List:
        return [char.lower() for char in S if char.isalnum()]

    def is_palindrome(self, lst: List) -> bool:
        if len(lst) <= 1:
            return True
        elif lst[0] == lst[-1]:
            return self.is_palindrome(lst[1:-1])
        else:
            return False

    def isPalindrome(self, S: str) -> bool:
        return self.is_palindrome(self.remove_non_alphanumeric_characters(S))


sol = Solution()
print(sol.isPalindrome(palindrome))


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
