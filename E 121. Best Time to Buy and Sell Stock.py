# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j] - price)

        return max_profit


def max_profit(prices: List[int]) -> int:
    # buy -> sell
    # 1. update low price from left to right
    # 2. update max_profit from left to right
    if len(prices) < 2:
        return 0

    max_profit, low_price = 0, sys.maxsize
    for price in prices:
        low_price = min(low_price, price)
        max_profit = max(max_profit, price - low_price)

    return max_profit
