"""
Given a string s, 
return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.


Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        N = len(s)
        last_occur = {s[i]: i for i in range(N)}
        
        stack = []
        instack = set()            
        for i in range(N):
            if (s[i] not in instack):
                while (stack and s[i] < stack[-1] and last_occur[s[i]] > i):
                    instack.remove(stack[-1])
                    stack.pop()    
                stack.append(s[i])
                instack.add(s[i])
            print(stack)
        return "".join(stack)
                
lc_1081 = Solution()
s = "cbaacabcaaccaacababa"
print(lc_1081.smallestSubsequence(s))