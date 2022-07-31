"""
背包问题
Coin Change
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

cannot use greedy, can use dfs (brute force)
bottom-up dynamic solution, solve in reverse order
状态转移方程
F(i,C) = max{F(i-1, C), v(i) + F(i-1, C-w(i))}
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount+1)]
        if (amount == 0):
            return amount
        for c in coins:
            if (c <= amount):
                dp[c] = 1
        for i in range(1, amount+1):
            if (dp[i] == 1):
                continue
            else:
                for c in coins:
                    # need to make sure i-c > 0
                    cur = 1 + dp[i-c] if i-c > 0 and dp[i-c]>0 else 0
                    if (cur!=0 and dp[i]!=0):
                        dp[i] = min(dp[i], cur)
                    elif (cur!=0 and dp[i] == 0):
                        dp[i] = cur
        return dp[amount] if dp[amount] > 0 else -1
    
lc_322 = Solution()
coins = [1,2,5]
amount = 11
result = lc_322.coinChange(coins, amount)
print(result)
            
        