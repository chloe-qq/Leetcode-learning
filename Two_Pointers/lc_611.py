
"""

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
"""
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        if (N < 3):
            return False
        nums.sort(reverse = True)
        ans = 0
        
        for i in range(N-2):
            first = i
            second = first + 1
            third = N-1
            while (second < third):
                if (nums[second]+nums[third] > nums[first]):
                    ans += third-second
                    second += 1
                else:
                    third -= 1
        return ans
                    
                    
                
            
        
        