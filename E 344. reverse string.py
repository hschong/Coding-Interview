# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

# Easy

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1

        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse_string(self, L: List(str)) -> None:
        L.reverse()
