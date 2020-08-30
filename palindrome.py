# 125. Valid palindrome
# https://leetcode.com/problems/valid-palindrome/#

from typing import List

palindrome = 'A man, a plan, a canal: Panama'
palindrome_1 = 'aba'
palindrome_2 = 'abba'
non_palindrome_1 = 'abdcba'
non_palindrome_2 = 'bbbba'
test_sample = palindrome


def remove_non_alphanumeric_characters(S: str) -> str:
    return ''.join([char.lower() for char in S if char.isalnum()])


def is_palindrome(S: str) -> bool:
    return True if S == S[::-1] else False
    # Do not use recursive call using list slicing because
    # copycopy overhead occurred like list.copy(), list() and [:]


class Solution:
    def isPalindrome(self, S: str) -> bool:
        alphanumeric_characters = [char.lower()
                                   for char in S if char.isalnum()]

        while len(alphanumeric_characters) > 1:
            if alphanumeric_characters.pop(0) != alphanumeric_characters.pop():
                return False

        return True
