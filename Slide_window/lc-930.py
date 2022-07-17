"""
930. Binary Subarrays With Sum

Example1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

"""
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)

        # find the subarray number which sum is smaller than goal and smaller than goal-1
        # substract those 2 number is the number which is exactly = goal
        def isSet(goal):
            left = 0
            res = 0
            for right in range(N):
                goal -= nums[right]
                # if goal < 0, update left and than add to res
                while (goal < 0):    
                    goal += nums[left]
                    left += 1
                # if l = 1, r = 3, we have [x,y,z] (max length subarray with sum <= goal), so we should have [x], [x,y],[x,y,z] -> 3 subarrays

                
                res += right - left + 1
                
            return res
        # should have condition of goal in case goal = 0 and -1 is difinitely impossible to appear for binary array
        return isSet(goal) - isSet(goal-1) if goal > 1 else isSet(goal)
                   
        
            
            
lc_930 = Solution()
nums = [0,0,0,0,0]
goal = 0
print(f'lc-930 solution: {lc_930.numSubarraysWithSum(nums,goal)}')