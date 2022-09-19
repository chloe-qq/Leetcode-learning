# three sum
from typing import List

"""
nums = [-1,0,1,2,-1,-4]
[[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        N = len(nums)
        def twoSumTarget(target, left, right):
            nonlocal ans
            while (left < right):
                if (nums[left] + nums[right] == target):
                    ans.append([-target,nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (right > left and nums[left] == nums[left-1]):
                        left += 1
                    while (right > left and nums[right] == nums[right+1]):
                        right -= 1 
                elif (nums[left] + nums[right] < target):
                    left += 1
                    while (right > left and nums[left] == nums[left-1]):
                        left += 1
                else:
                    right -= 1
                    while (right > left and nums[right] == nums[right+1]):
                        right -= 1

        
        for i in range(N):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            twoSumTarget(-nums[i], i+1, N-1)

        return ans
    
            