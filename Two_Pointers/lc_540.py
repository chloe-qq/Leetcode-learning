"""
You are given a SORTED array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.
Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
(log n) --> binary search

if use hash, time complexity and space complexity is O(n)

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Solution: 那个单独出现的数的index肯定在偶数位，
either出现在一对数后面，比如例子中，出现在一对2后，则index为2，或出现在第一个元素，则index为0
the total array length must be odd number

if the mid index is odd, cannot be that number
if the mid index is even, could be that single
"""
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = N-1
        while (l <= r):
            mid = l + (r-l)//2
            if (mid % 2 == 0):
                if (mid + 1 < N and nums[mid] == nums[mid+1]):
                    l = mid + 2
                elif (mid - 1 >=0 and nums[mid] == nums[mid-1]):
                    r = mid -2
                else:
                    return nums[mid]
            else:
                if (mid + 1 < N and nums[mid] == nums[mid+1]):
                    r = mid - 1
                elif (mid - 1 >=0 and nums[mid] == nums[mid-1]):
                    l = mid + 1
            print(f'updated l = {l}, r = {r}')
        return nums[mid]
    
lc_540 = Solution()
nums  = [3,3,7,7,10,11,11]
print(lc_540.singleNonDuplicate(nums))

