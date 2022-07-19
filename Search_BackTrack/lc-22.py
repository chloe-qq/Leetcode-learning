"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(cur,left, right):

            if (left > n or right > n):
                return
            if (left == n and right ==n):
                result.append(cur)
                return
            # can only add right ) if left( num is greater than right num()
            if (left > right):
                dfs(cur+'(', left +1,right)
                dfs(cur + ')', left, right + 1)
            else:
                # case of left == right, as left cannot be smaller than right
                dfs(cur+'(', left +1,right)
        dfs('',0,0)
        return result
    
lc_22 = Solution()
print(lc_22.generateParenthesis(1))

                
            
            
            