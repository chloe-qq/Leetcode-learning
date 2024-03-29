"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

"""
from typing import List

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        l = 0
        max_length = 0
        dict = {}
        cur = []
        for r in range(N):
            # if s[r] not in the original list
            if (s[r] not in dict.keys() or dict[s[r]] < l):
                cur.append(s[r])
                dict[s[r]] = r
                while (len(cur) > 2 and l <= r):
                    if (dict[s[l]] == l):
                        cur.remove(s[l])
                    l += 1  # 这里只能一个个遍历，不像第三题可以直接取 l 和 map中次元素最大的index+1
            elif (dict[s[r]] >= l):  # if s[r] in the original list
                dict[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length

s = "ababcbcbaaabbdef"
lc_159 = Solution()
print(f'lc 159 solution: {lc_159.lengthOfLongestSubstringTwoDistinct(s)}')

            
