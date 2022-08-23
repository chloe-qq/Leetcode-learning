"""
918. Maximum Sum Circular Subarray
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
"""
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # case 1
        # case 2: total_sum - min_subarray
        # can be optimized from O(n) to O(1)
        N = len(nums)
        
        curMax, TotalMax = nums[0], nums[0]
        curMin, TotalMin = nums[0],nums[0]
        allSum = nums[0]
        for i in range(1,N):
            curMax = max(nums[i], curMax + nums[i])
            TotalMax = max(curMax,TotalMax)
            curMin = min(nums[i],curMin + nums[i])
            TotalMin = max(curMin,TotalMin)
            allSum += nums[0]
            
        if (allSum == TotalMin):
            # meaning that every element is negative, we cannot use total-min, otherwise it will result in 0, meaning that 0 element is chosen
            return TotalMax
        else:
            return (TotalMax, allSum-TotalMin)
            
            
            
        