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
                if (len(cur) > 2):
                    if (dict[s[l]] <  dict[cur[1]]):
                        l = dict[s[l]] + 1
                        cur.pop(0)
                    else:
                        l = dict[cur[1]] + 1
                        cur = [cur[0]] + [cur[-1]]
            elif (dict[s[r]] >= l):  # if s[r] in the original list
                dict[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length

s = "ababcbcbaaabbdef"
lc_159 = Solution()
print(f'lc 159 solution: {lc_159.lengthOfLongestSubstringTwoDistinct(s)}')

            
