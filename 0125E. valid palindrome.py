# 125. Valid palindrome
# https://leetcode.com/problems/valid-palindrome/#

from collections import deque
from typing import Deque


class Solution:
    # Use List: pop([i]) -> O(n), 280ms
    def isPalindrome(self, S: str) -> bool:
        alphanum_chars = [char.lower() for char in S if char.isalnum()]

        while len(alphanum_chars) > 1:
            if alphanum_chars.pop(0) != alphanum_chars.pop():
                return False

        return True

    # Use deque: list-like container with fast appends and pops on either end. popleft() -> O(1), 52ms
    def is_palindrome(self, S: str) -> bool:
        alphanum_chars: Deque = deque()

        for char in S:
            if char.isalnum():
                alphanum_chars.append(char.lower())

        while len(alphanum_chars) > 1:
            if alphanum_chars.popleft() != alphanum_chars.pop():
                return False

        return True


palindrome = 'A man, a plan, a canal: Panama'


def is_palindrome(S: str) -> bool:  # 36ms
    alpha_only = ''.join([char.lower() for char in S if char.isalnum()])
    return True if alpha_only == alpha_only[::-1] else False
    # Do not use recursive call using list slicing because
    # copy overhead occurred like list.copy(), list() and [:]


def is_palindrome_1(S: str) -> bool:
    # stack overflow occurred due to limited recursion depth(1000)
    # use generator instead of recursion
    if len(S) == 0:
        return True

    alpha_only = ''.join([char.lower() for char in S if char.isalnum()])

    return is_palindrome_1(alpha_only[1:-1]) if alpha_only[0] == alpha_only[-1] else False
