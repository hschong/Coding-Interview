# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Easy


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def get_two_sum(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        for idx, num in enumerate(nums):
            complement = target - num

            # 'if in' is over 5 times faster than 'for in range'.
            if complement in nums[idx+1:]:
                return [idx, idx+1+nums[idx+1:].index(complement)]

    def get_two_sum_using_dict(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        reverse_nums_dic = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in reverse_nums_dic:
                return [reverse_nums_dic[complement], i]

            reverse_nums_dic[num] = i


sol = Solution()
print(sol.get_two_sum_using_dict([3, 2, 4], 6))
