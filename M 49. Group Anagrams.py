# 49. Group Anagrams
# https: // leetcode.com/problems/group-anagrams/

# Medium

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
