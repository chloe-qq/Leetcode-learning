
"""
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
"""
from typing import List
import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        result = []
        def dfs(cur, i,product):
            print(f'cur = {cur}, i = {i}, product = {product}')
            for j in range(i, product//i+1):
                if (product%j == 0):
                    cur.append(j)
                    cur.append(product//j)
                    if (product//j >=j):
                        result.append(cur.copy())
                    cur.pop()
                    dfs(cur,j,product//j)
                    cur.pop()
        dfs([],2,n)
        return result
                    
result = Solution().getFactors(12)
print(result)
            