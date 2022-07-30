"""

238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [2,3,4]
Output: [24,12,8,6]

prefix + postfix
"""
from typing import List

from requests import post
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1 for _ in range(N+1)]
        postfix = [1 for _ in range(N+1)]
        result = [1 for _ in range(N)]
        for i in range(1, N+1):
            prefix[i] = prefix[i-1]*nums[i-1]
            postfix[N-i] = postfix[N+1-i]*nums[N-i]
        
        for i in range(1,N+1):
            result[i-1] = prefix[i-1]*postfix[i]
        return result
    
lc_238 = Solution()
nums = [2,3,4]
print(lc_238.productExceptSelf(nums))
            
        
            
        