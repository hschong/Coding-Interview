# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Medium

import collections
from typing import DefaultDict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        longest_palindrome = ''
        for i in range(len(s)-1):
            longest_palindrome = max(
                longest_palindrome, expand(i, i+1), expand(i, i+2), key=len)

        return longest_palindrome


def longest_palindrome(s: str) -> list:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

    def get_max_key(dic: DefaultDict) -> int:
        max_key = 0
        for item in dic.items():
            max_key = max(max_key, item[0])

        return max_key

    if len(s) < 2 or s == s[::-1]:
        return s

    result = collections.defaultdict(list)
    for left in range(len(s)-1):
        # expand(left, left+1) for even case
        # expand(left, left+2) for odd case
        value = max(expand(left, left+1), expand(left, left+2), key=len)
        result[len(value)].append(value)

    return result[get_max_key(result)]
