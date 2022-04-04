
from typing import List

"""
784. Letter Case Permutation
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
"""
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        N = len(s)
        def dfs(cur,i):
            if (len(cur) == N):
                res.append(cur)
                return
            if (s[i].isalpha()):
                cur += s[i].lower()
                dfs(cur,i+1)
                cur = cur[:-1]
                cur += s[i].upper()
                dfs(cur,i+1)
            else:
                cur += s[i]
                dfs(cur,i+1)
        dfs('',0)
        return res

lc_784 = Solution()
s = "a1b2"
print(f'Leetcode 784: {lc_784.letterCasePermutation(s)}')

        
                
