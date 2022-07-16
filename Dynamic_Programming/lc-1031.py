
"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.


since there is no rules that firstLen should ahead of secondLen 
so there're 2 cases in
[firstLen], xxx, [secondLen]
vice & versa
"""
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:        
        N = len(nums)
        prefix_sum = [0 for _ in range(N+1)]
        # since prefix sum, the first index should be 0 before before index 0 there is no num
        for i in range(1,N+1):
            prefix_sum[i] = nums[i-1] + prefix_sum[i-1]
        print(prefix_sum)
        max_first = 0
        max_second = 0
        result = 0
        for i in range(firstLen+secondLen, N+1):
            sub_sum_first = prefix_sum[i] - prefix_sum[i-firstLen]
            sub_sum_second = prefix_sum[i-firstLen] - prefix_sum[i-firstLen-secondLen]

            # always set the first appear array to be max and fix that one
            # here subarray with secondLen appear first
            max_second = max(max_second, sub_sum_second)
            result = max(result, max_second + sub_sum_first)

        for i in range(firstLen+secondLen, N+1):
            sub_sum_second = prefix_sum[i] - prefix_sum[i-secondLen]
            sub_sum_first = prefix_sum[i-secondLen] - prefix_sum[i-firstLen-secondLen]
            # always set the first appear array to be max and fix that one
            # here subarray with firstLen appear first

            max_first = max(sub_sum_first, max_first)
            result = max(result, max_first + sub_sum_second)
        return result
    
lc_1031 = Solution()
nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2
print(f'lc 1031:{lc_1031.maxSumTwoNoOverlap(nums, firstLen, secondLen)}')