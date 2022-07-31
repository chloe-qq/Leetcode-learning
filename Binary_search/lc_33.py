"""

33. Search in Rotated Sorted Array
Input: nums = [4,5,6,7,1,2,3], target = 0
Output: 4

nums = [14,16,18,0,1,2,3,4,5,6,7], target = 14
You must write an algorithm with O(log n) runtime complexity.
"""


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while (left < right):
            mid = left + (right-left)//2
            if (nums[left] < nums[mid]):
                if (target == nums[mid]):
                    return mid
                elif (target == nums[left]):
                    return left
                elif ( target < nums[left] or target > nums[mid]):
                    left = mid + 1
                else:
                    right = mid-1
            elif (nums[mid] < nums[right]):
                if (target == nums[mid]):
                    return mid
                elif (target == nums[right]):
                    return right
                elif (target < nums[mid] or target > nums[right]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
lc_33 = Solution()

nums = [6,8,10,0,2,4]
target = 2
index = lc_33.search(nums,target)
print(index)                    
                    
            
           