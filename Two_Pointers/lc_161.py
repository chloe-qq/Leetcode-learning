"""
One Edit distance
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if ((not s and len_t == 1) or (not t and len_s == 1)):
            return True
        if (abs(len(s) - len(t)) > 1 or s == t):
            return False
        
        p_s = 0
        p_t = 0
        cnt = 0
        while (p_s < len_s and p_t < len_t and cnt < 2):
            if (s[p_s] == t[p_t]):
                p_s += 1
                p_t += 1
            elif (len_s == len_t and cnt == 0):
                # by modify a number
                cnt += 1
                p_s += 1
                p_t += 1
            elif (len_s < len_t):
                p_t += 1
                cnt += 1
            else:
                p_s += 1
                cnt += 1
            if (cnt > 1):
                return False
        
        return True

                
s = "ab"
t = "acc"
lc_161 = Solution()
print(lc_161.isOneEditDistance(s,t))