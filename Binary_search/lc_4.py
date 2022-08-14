"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). --> binary search

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        if (len2 < len1):
            return self.findMedianSortedArrays(nums2,nums1)
        
        if (len1 == 0):
            mid = len2//2
            return nums2[mid] if len2%2==1 else (nums2[mid]+nums2[mid-1])/2
        
        totalLen = len1 + len2
        left = 0
        right = len1-1

        
        while True:
            cut1 = (left+right)//2 
            cut2 = (totalLen-1)//2 - (cut1+1)
            
            Val1_left = nums1[cut1] if cut1 >= 0 else float('-inf')
            Val1_right = nums1[cut1+1] if cut1+1 < len1 else float('inf')
            Val2_left = nums2[cut2] if cut2 >= 0 else float('-inf')
            Val2_right = nums2[cut2+1] if cut2+1 < len2 else float('inf')
            
            if (Val1_left <= Val2_right and Val2_left <= Val1_right):
                # find the medium
                if (totalLen % 2 == 1):
                    return max(Val1_left,Val2_left)
                else:
                    return (max(Val1_left, Val2_left) + min(Val2_right,Val1_right))/2
            elif (Val1_left > Val2_right):
                right = cut1 - 1
            else:
                left = cut1 +1
                
            
        