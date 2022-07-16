from typing import List
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_ = sorted([[num,i] for i,num in enumerate(nums)], key = lambda x:x[0], reverse = False)
        
        result = []
        while (k > 0):
            result.append(nums_.pop())
            k -= 1
        result = sorted(result, key = lambda x:x[1], reverse = False )
        
        return [i[0] for i in result]
    
lc_2099 = Solution()
nums = [2,7,4,1,8,1]

print(f'lc_2099:{lc_2099.maxSubsequence(nums,2)}')
