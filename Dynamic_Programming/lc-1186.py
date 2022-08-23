"""
1186. Maximum Subarray Sum with One Deletion
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. 
choose a subarray and optionally delete one element from it 
so that there is still at least one element left and the sum of the remaining elements is maximum possible.

the subarray needs to be non-empty after deleting one element.

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
"""
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [arr[0]]*N
        dp_deleted_one =  [arr[0]]*N
        
        for i in range(1, N):
            dp[i] = max(arr[i],dp[i-1]+arr[i])
            dp_deleted_one[i] = max(arr[i],dp_deleted_one[i-1]+arr[i])
            
            if (i >=2):
                dp_deleted_one[i] = max( dp_deleted_one[i], dp[i-2]+arr[i])
        return max(dp_deleted_one)
        