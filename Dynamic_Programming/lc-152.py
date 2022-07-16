"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp_max = [1 for _ in range(N)]
        dp_min = [1 for _ in range(N)]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1,N):
            if (nums[i] > 0):
                dp_max[i] = max(dp_max[i-1]*nums[i],nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i],nums[i])
            elif (nums[i] < 0):
                dp_max[i] = dp_min[i-1]*nums[i]
                dp_min[i] = min(dp_max[i-1]*nums[i],nums[i])
            else:
                dp_max[i] = 0
                dp_min[i] = 0
        print('dp_max:',dp_max)
        print('dp_min:',dp_min)
        return max(dp_max)
            
lc_152 = Solution()
nums = [2,3,-2,4,5,6,-3]
print(f'Leetcode 152: {lc_152.maxProduct(nums)}')