"""
 https://www.youtube.com/watch?v=dw2nMCxG0ik
 根据decision tree, 我们发现我们在其中做了很多重复calculation
 此时，
 1. bottom up dynamic programming
    dp[target]?
    from:
        dp[0] = 1
        dp[x] = dp[x-1]+dp[x-2]+dp[x-3] (1,2,3,... 为nums的数字)
 2. top down cache
 O(target*N)
"""
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = 0
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for j in nums:
                if (i - j >= 0):
                    dp[i] += dp[i-j]
        return dp[target]

lc377 = Solution()
nums = [1,2,3]
target = 4
print(f'Leetcode 377 Solution:{lc377.combinationSum4(nums,target)}')
            

