"""
JUMP GAME

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
---------------------------
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i] >= goal):
                goal = i
                
        return True if goal == 0 else False
nums = [3,2,1,0,4]
lc_55 = Solution()
print(f'{lc_55.canJump(nums)}')