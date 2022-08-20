"""    
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).


eg. 
[1,2,4,9,8,3] --> [1,2,8,3,4,9]
"""
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            tmp = nums[i]
            nums[i] =  nums[j]
            nums[j] = tmp
            
        N = len(nums)
        if (N == 1):
            return nums
        
        left = N-1      
        while (left-1 >= 0 and nums[left-1] >= nums[left]):
            left -= 1

        if (left-1 < 0):

            return nums.reverse()
        else:
            left = left-1
            swap_i = N-1
            while (swap_i > left and nums[swap_i] <= nums[left]):
                swap_i -= 1
            swap(swap_i, left)
        while (left+1 < N-1):
            swap(left+1,N-1)
            N -= 1
            left += 1
        return nums
                
                    
        
            
        
