"""

518. Coin Change 2

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

见 https://leetcode.cn/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/

总结，二维dp的组合数问题和排列数问题 都可以交换嵌套的循环，因为子问题不会变化；
一维的dp组合数问题和排列数问题 不可以交换嵌套的循环，因为会改变子问题； 
一维的dp组合数问题，交换嵌套的循环，子问题会变成排列数问题； 
一维的dp排列数问题，交换嵌套的循环，子问题会变成组合数问题； 


# 组合问题 v.s. 排列问题
# 组合问题 coin interation index 必须在外层
# 排列问题无所谓


"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0]*(amount+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 1
        # 状态转移：在必须使用第k个coin的时候，当前金额的 组合 数
        # 而不是排列问题，如果内外循环交换，则表示 组成当前金额 可有coin的排列数
        for i in range(1,N+1):
            for m in range(amount+1):
                if (coins[i-1] <= m):
                    # 即前k个硬币凑齐金额i的组合数
                    # 等于前k-1个硬币凑齐金额i的组合数
                    # 加上在原来i-k的基础上使用硬币的组合数。
                    dp[i][m] = dp[i][m-coins[i-1]] + dp[i-1][m]
                else:

                    dp[i][m] = dp[i-1][m]
        return dp[-1][amount]
    
    
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        # 内外层循环顺序不能变 否则会有重复的 例如 1 + 2 + 2 和 2 + 2+ 1 ? 不太理解 再需要看看
        for c in coins:
            for i in range(1, amount+1):            
                if (i-c >= 0):
                    dp[i] += dp[i-c]

        return dp[amount]
    
    