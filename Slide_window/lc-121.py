"""
Best Time to Buy and Sell Stock

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
from typing import List
class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0.0
        if (N < 2):
            return max_profit        
        buy = 0
        sell = 1
        while (buy <= sell and sell < N):
            profit = prices[sell] - prices[buy]
            if (profit > 0):
                max_profit = max(profit, max_profit)
            else:
                # becasue current sell is smaller than buy, so update buy to the cur sell (which is the minimum)
                buy = sell
            sell += 1
        return max_profit

lc_121 = Solution()
prices = prices = [7,1,5,3,6,4,0,9]
print(f'Leetcode 121: {lc_121.maxProfit1(prices)}')
            
            
