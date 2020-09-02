# 125. Valid palindrome
# https://leetcode.com/problems/valid-palindrome/#

# Easy

from collections import deque
from typing import Deque


palindrome = 'A man, a plan, a canal: Panama'


def remove_non_alphanum_chars(S: str) -> str:
    return ''.join([char.lower() for char in S if char.isalnum()])


def is_palindrome(S: str) -> bool:
    return True if S == S[::-1] else False
    # Do not use recursive call using list slicing because
    # copy overhead occurred like list.copy(), list() and [:]


class Solution:
    # Use List: pop([i]) -> O(n)
    def isPalindrome(self, S: str) -> bool:
        alphanum_chars = [char.lower() for char in S if char.isalnum()]

        while len(alphanum_chars) > 1:
            if alphanum_chars.pop(0) != alphanum_chars.pop():
                return False

        return True

    # Use deque: list-like container with fast appends and pops on either end. popleft() -> O(1)
    def is_palindrome_1(self, S: str) -> bool:
        alphanum_chars: Deque = deque()

        for char in S:
            if char.isalnum():
                alphanum_chars.append(char.lower())

        while len(alphanum_chars) > 1:
            if alphanum_chars.popleft() != alphanum_chars.pop():
                return False

        return True
