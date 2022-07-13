
from heapq import heapify, heapreplace

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        heapify(nums)
        while (k > 0 and nums[0] < 0):
            # Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. 
            heapreplace(nums,-nums[0])
            k -= 1
        if (k%2 == 1):
            heapreplace(nums, -nums[0])
        return sum(nums)            
                    
                    
                    
                
        