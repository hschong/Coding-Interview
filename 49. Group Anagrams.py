# 49. Group Anagrams
# https: // leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.


from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. put sorted word and org word into a dictionary
        # 2. count
        anagrams_dic = collections.defaultdict(list)
        for word in strs:
            # defaultdict[key].append(value) -> append value into list of values of key
            anagrams_dic[''.join(sorted(word))].append(word)

        return anagrams_dic.values()


sol = Solution()
values = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(values)
