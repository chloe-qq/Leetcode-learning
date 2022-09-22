from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        prefixSum = 0
        hashmap = {0:0}
        
        for i in range(N):
            prefixSum += nums[i]
            rest = prefixSum%k
            if (rest in hashmap.keys() and hashmap[rest] < i ):
                return True
            if (rest not in hashmap.keys()):
                hashmap[rest] = i+1
        return False
        