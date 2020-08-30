# 125. Valid palindrome
# https://leetcode.com/problems/valid-palindrome/#

import collections

palindrome = 'A man, a plan, a canal: Panama'


def remove_non_alphanumeric_characters(S: str) -> str:
    return ''.join([char.lower() for char in S if char.isalnum()])


def is_palindrome(S: str) -> bool:
    return True if S == S[::-1] else False
    # Do not use recursive call using list slicing because
    # copy overhead occurred like list.copy(), list() and [:]


class Solution:
    # Use List: pop([i]) -> O(n)
    def isPalindrome(self, S: str) -> bool:
        alphanumeric_characters = [char.lower()
                                   for char in S if char.isalnum()]

        while len(alphanumeric_characters) > 1:
            if alphanumeric_characters.pop(0) != alphanumeric_characters.pop():
                return False

        return True

    # Use deque: list-like container with fast appends and pops on either end. popleft() -> O(1)
    def is_palindrome_1(self, S: str) -> bool:
        alphanumeric_characters: Deque = collections.deque()

        for char in S:
            if char.isalnum():
                alphanumeric_characters.append(char.lower())

        while len(alphanumeric_characters) > 1:
            if alphanumeric_characters.popleft() != alphanumeric_characters.pop():
                return False

        return True
