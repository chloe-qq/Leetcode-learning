from typing import List
from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        maxValue = 0
        cur = 0
        hashmap = defaultdict(int)
        for i, digit in enumerate(nums):
            cur += digit
            if (digit in hashmap.keys()):
                if (hashmap[digit] >= left):                    
                    for k in range(left, hashmap[digit]+1):
                        cur -= nums[k]                    
                    left = hashmap[digit] + 1
            hashmap[digit] = i
            maxValue = max(maxValue, cur)

        return maxValue