# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/#


# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # log.split()[1:] : The letter-logs are ordered lexicographically ignoring identifier.
        # log.split()[0]) : with the identifier used in case of ties.
        letter_logs.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        return letter_logs + digit_logs
