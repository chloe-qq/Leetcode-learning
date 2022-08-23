"""

1150. Check If a Number Is Majority Element in a Sorted Array
"""
from typing import List
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # use binary search
        left = 0
        N = len(nums)
        right = N-1
        
        
        while (left <= right):
            mid = left + (right-left)//2
            
            #print(f'mid = {mid}, nums[mid] = {nums[mid] }')
            if (nums[mid]== target):
                break
            elif (nums[mid] > target):
                right = mid-1
            else:
                left = mid + 1
        cnt = 0
        #print(f'mid = {mid}')
        for i in range(mid, N):
            if (nums[i] == target):
                cnt += 1
            else:
                break
        for i in range(mid-1,-1,-1):
            if (nums[i] == target):
                cnt += 1
            else:
                break
        #print(cnt)
        return True if (cnt > N//2) else False
    
lc_1150 = Solution()
nums = [ 10,100,101,101]
target = 101
print(lc_1150.isMajorityElement(nums,target))