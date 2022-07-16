"""
max subarray

A subarray is a contiguous part of an array.

Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        for i in range(1,N):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] + nums[i] >= nums[i] else nums[i]
        return max(dp)
    

lc_53 = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(f'Leetcode 2266: {lc_53.maxSubArray(nums)}')