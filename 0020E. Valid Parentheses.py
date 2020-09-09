# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        # 1. if char is equal to '(', '{' or '[' then push the char into stack.
        # 2. if char is equal to ')', '}' or ']' then compare the char to stack.pop()
        # 3. looping

        my_stack = []
        table = {')': '(',
                 '}': '{',
                 ']': '['}

        for char in s:
            if char not in table:
                # '(', '{', '['
                my_stack.append(char)
            elif not my_stack or table[char] != my_stack.pop():
                return False

        if not my_stack:  # len(my_stack) == 0
            return False


sol = Solution()
print(sol.isValid("(){()}"))
print(sol.isValid("((){()})"))
