"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

from typing import List
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        map = {}
        l = 0
        max_length = 0
        for r in range(N):
            if (s[r] in map.keys()):
                l = max(map[s[r]]+1, l)
            max_length = max(max_length,r-l+1)
            map[s[r]] = r
        return max_length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        maxLen = 0
        left = 0
        for i,c in enumerate(s):
            if (c in hashmap.keys()):
                if (hashmap[c] >= left):
                    left = hashmap[c] + 1
            hashmap[c] = i

            maxLen = max(maxLen, i-left+1)
        return maxLen

s = "abcabcbb"
lc_3 = Solution()
print(f'lc 3 solution: {lc_3.lengthOfLongestSubstring(s)}')
                




