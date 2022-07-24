"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Solution:
Flip the sign (since the range in [1,n]) of the number at index i, if seen already flipped, menns that number has appearred
We do not need to flip twoice

Input: nums = [4,3,2,7,8,2,3,1]
i = 4, nums = [4,3,2,-7,8,2,3,1];
i = 3, nums = [4,3,-2,-7,8,2,3,1];
i = -3, nums = [4,3,-2,-7,8,2,3,1];
Output: [2,3]
"""
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            # since i within range of [1,n], the i-1 must within the range of length of nums
            i = -i if i < 0 else i
            if (nums[i-1] < 0):
                result.append(i)
            else:
                nums[i-1] *= -1
        return result
lc_442= Solution()
nums = [4,3,2,7,8,2,3,1]
print(lc_442.findDuplicates(nums))
        
        