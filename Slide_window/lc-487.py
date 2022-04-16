
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        N = len(nums)
        output = 0
        flipped = False
        for r in range(N):
            if (nums[r] == 1):
                output = max(output, r-l+1)

            elif (not flipped):
                output = max(output, -l+r+1)
                flipped = True

            else:
                while(l < r and nums[l] == 1):
                    l += 1
                l += 1
                output = max(output, -l+r+1)

        return output
        
lc_487 = Solution()
nums = [1,0,1,1,0,1]

print(f'lc 487 solution: {lc_487.findMaxConsecutiveOnes(nums)}')