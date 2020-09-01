# 819. Most Common Word
# https: // leetcode.com/problems/most-common-word/


import re
import collections
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. replace none-word with blank in paragraph.
        # 2. str.lower()
        # 3. str.split()
        # 4. Counter()
        string = re.sub(r'[^\w]', ' ', paragraph)
        lower_str_lst = string.lower().split()
        words = [word for word in lower_str_lst if word not in banned]
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]
