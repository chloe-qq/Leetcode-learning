"""
Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Since there are EXACT n integers, 
so if all appear, we can rearrange each number in to itself as index +1
eg. 1 appear at index 1-0 = 0 

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

[4,3,2,7,8,2,3,1]
[7,3,2,4,8,2,3,1]
[3,3,2,4,8,2,7,1]
[2,3,3,4,8,2,7,1]
[3,2,3,4,8,2,7,1]
[3,2,3,4,8,2,7,1]

[3,2,3,4,1,2,7,8]
[1,2,3,4,3,2,7,8]

can be seen that index 4 and index 5 (number = 5 and 6) is disappeared



"""
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            while (i+1 != nums[i] and nums[nums[i]-1] != nums[i]):
                t = nums[i]
                nums[i] = nums[t-1]
                nums[t-1] = t
                print(f'i = {i}')
                print(nums)
        result = []
        for i in range(N):
            if (i+1 != nums[i]):
                result.append(i+1)
        return result
nums = [4,3,2,7,8,2,3,1]
lc_448 = Solution()
print(lc_448.findDisappearedNumbers(nums))

                