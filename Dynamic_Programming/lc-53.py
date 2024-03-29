"""
max subarray

A subarray is a contiguous part of an array.

Input: nums = [5,4,-1,7,8]
Output: 23

kadane算法
我们将子问题定义为求以i为终止下标的子数组之和的最大值

递推基为dp[0]=array[0]。
递推关系:
对dp[i-1]和array[i]分正负讨论
若dp[i-1]<0, array[i]>0，dp[i]=array[i]
若dp[i-1]<0, array[i]<0, dp[i]=array[i]
若dp[i-1]>0, array[i]<0, dp[i]=dp[i-1]+array[i]
若dp[i-1]>0, array[i]>0, dp[i]=dp[i-1]+array[i]。
最后, 原始问题的解即max(dp)
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        for i in range(1,N):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]
        return max(dp)
    

lc_53 = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(f'Leetcode 2266: {lc_53.maxSubArray(nums)}')