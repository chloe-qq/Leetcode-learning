"""
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

    """

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        N = len(nums)
        right = 0
        max_length = 0
        while (left <= right and right < N):
            print(f'left = {left}, right = {right}')
            if (nums[right] == 1):
                
                max_length = max(max_length, right - left + 1)
                print(f'update maxlength = {max_length}')
                right += 1
            else:
                left = right
                while (left < N and nums[left] == 0):
                    left += 1
                right = left
        return max_length
                
lc_485 = Solution()
nums = [1,1,0,1,1,1]
max_length = lc_485.findMaxConsecutiveOnes(nums)
print(max_length)                
                