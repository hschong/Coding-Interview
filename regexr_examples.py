import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# replace none word with blank.
print(re.sub(r'[^\w]', ' ', paragraph))
# '^' -> not, '\w' -> word
# 'r' means raw string which keeps original string. do not not interpret '\'.
