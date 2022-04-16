"""
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined
"""

from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        N = len(nums)

        output = 0
        r = l
        while (r < N):
            if (nums[r] == 1):
                output = max(output, r-l+1)
                r += 1
            elif (k > 0):
                output = max(output, r-l+1)
                r += 1
                k -= 1                
            else:
                while (l < r and nums[l]!=0):
                    l += 1
                l += 1
                output = max(output, r-l+1)
                r+=1
                # no need to update k here, l 减少的flip 和r 增加的flip正好offset each other


        return output

lc_1004 = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


print(f'lc 1004 solution: {lc_1004.longestOnes(nums,k)}')

        
                

            
            
            

