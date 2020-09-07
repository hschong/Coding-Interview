# 561. Array Partition I

# https://leetcode.com/problems/array-partition-i/

# Easy

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        # minimize the difference between two numbers is adjacent elements pair.
        nums.sort()

        for num in nums:
            pair.append(num)

            if len(pair) == 2:
                sum += min(pair)
                pair.clear()

        return sum

    def array_pair_sum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for num in enumerate(nums):
            if num % 2 == 0:
                sum += num

        return sum


def array_pair_sum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
