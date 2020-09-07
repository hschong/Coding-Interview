# 15. 3SUM

# https://leetcode.com/problems/3sum/

# Medium

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            # if nums[i] == nums[i+1]: -> nums[i+1] is out of index
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif sum > 0:
                    right -= 1

                else:  # sum < 0
                    left += 1

        return result
