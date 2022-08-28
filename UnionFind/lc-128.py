"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
an algorithm that runs in O(n) time.
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (not nums):
            return 0
        
        # Two nodes are connected if they are consecutive
        
        def find(x):
            if (x != parent[x]):
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            # instead of adding 1, we add degree[p1]
            # so that in later loop, we only need to call union(digit, digit+1)
            if (p1 + degree[p1] == p2):
                parent[p2] = p1
                degree[p1] += degree[p2]

        
        parent = {i:i for i in nums}
        degree = {i: 1 for i in nums}
        set_nums = set(nums)
        # We always set the smaller one to be the parent
        for digit in set_nums:
            if (digit + 1 in set_nums):
                union(digit, digit+1)

        return max(degree.values())
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best