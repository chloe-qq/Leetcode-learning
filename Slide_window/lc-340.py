"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

"""
from typing import List

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        N = len(s)
        l = 0
        max_length = 0
        dict = {}
        cur = set() # 也可以用[]，list 也可以指定元素抛出， list 效率越高于set, 区别就是一个是add 一个是append
        for r in range(N):
            # if s[r] not in the original list
            if (s[r] not in dict.keys() or dict[s[r]] < l):
                cur.add(s[r])
                dict[s[r]] = r
                while (len(cur) > k and l <= r):
                    if (dict[s[l]] == l):
                        cur.remove(s[l])
                    l += 1       
            elif (dict[s[r]] >= l):  # if s[r] in the original list
                dict[s[r]] = r
            max_length = max(max_length, r-l+1)

        return max_length


s = "a@b$5!a8alskj234jasdf*()@$&%&#FJAvjjdaurNNMa8ASDF-0321jf?>{}L:fh"

k = 10



lc_340 = Solution()
print(f'lc 340 solution: {lc_340.lengthOfLongestSubstringKDistinct(s,k)}')

            
