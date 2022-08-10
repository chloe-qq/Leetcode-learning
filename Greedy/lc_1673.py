"""
We define that a subsequence a is more competitive than a subsequence b (of the same length) 
if in the first position where a and b differ,
subsequence a has a number less than the corresponding number in b. 
For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, 
and 4 is less than 5.


That is to find the smallest number sequence given the 
"""
from typing import List
import heapq
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        N = len(nums)
        for i in range(N):
            while (stack and nums[i] < stack[-1] and N-1-i >= k-len(stack) ):
                stack.pop()
            stack.append(nums[i])
        print(stack[:k])
            
        
                
    
    
lc_1673 = Solution()
nums = [2,4,3,3,5,4,9,6]
k = 4
print(lc_1673.mostCompetitive(nums,k))
            
                
                