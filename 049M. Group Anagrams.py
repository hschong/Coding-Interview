# 49. Group Anagrams
# https: // leetcode.com/problems/group-anagrams/

# Medium

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. put sorted word and org word into a dictionary
        # 2. count
        anagrams_dic = defaultdict(list)
        for word in strs:
            # defaultdict[key].append(value) -> append value into list of values of key
            anagrams_dic[''.join(sorted(word))].append(word)

        return list(anagrams_dic.values())
