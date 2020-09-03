# 238. Product of Array Except Self

# https://leetcode.com/problems/product-of-array-except-self/


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left * (pivot) * right
        result = []
        left, right = 1, 1

        for i in range(len(nums)):
            result.append(left)
            left *= nums[i]

        for revers_i in range(len(nums)-1, -1, -1):
            result[revers_i] *= right
            right *= nums[revers_i]

        return result
