
"""
You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Hint: count how many numbers is smaller than the target, need NOT sort the array 
in above example, only 1 number <= target, and the target appear 2 times, so return 1,1+1
"""
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        cnt = 0
        cnt_equal = 0
        for i in nums:
            if (i < target):
                cnt += 1
            elif (i == target):
                cnt_equal += 1
        return [cnt for cnt in range(cnt,cnt+cnt_equal)] if (cnt_equal!=0) else []
        
        