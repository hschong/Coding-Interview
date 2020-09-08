# 1. Two Sum
# https://leetcode.com/problems/two-sum/

import time
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        start = time.perf_counter()  # 3.7 > time.clock()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    end = time.perf_counter()
                    print(end-start)
                    return [i, j]

    def get_two_sum(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        start = time.perf_counter()  # 3.7 > time.clock()

        for idx, num in enumerate(nums):
            complement = target - num

            # 'if in' is over 5 times faster than 'for in range'.
            if complement in nums[idx+1:]:
                end = time.perf_counter()
                print(end-start)
                return [idx, idx+1+nums[idx+1:].index(complement)]

    def get_two_sum_using_dict(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        start = time.perf_counter()  # 3.7 > time.clock()
        reverse_nums_dic = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in reverse_nums_dic:
                end = time.perf_counter()
                print(end-start)
                return [reverse_nums_dic[complement], i]

            reverse_nums_dic[num] = i


sol = Solution()
print("twoSum = ", sol.twoSum([3, 2, 4], 6))
print("get_two_sum = ", sol.get_two_sum([3, 2, 4], 6))
print("get_two_sum_using_dict = ", sol.get_two_sum_using_dict([3, 2, 4], 6))
