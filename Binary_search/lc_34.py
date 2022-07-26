"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

log n --> binary search

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        left = 0
        right = N-1
        
        while (left <= right):
            mid = left + (right-left)//2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else: #  nums[mid] == target
                while (left < mid and nums[left]!=target):
                    left += 1
                while (right > mid and nums[right]!=target):
                    right -= 1
                return [left,right]
        return [-1,-1]
nums = [5,7,7,8,8,10]
print(Solution().searchRange(nums,7))
                
            