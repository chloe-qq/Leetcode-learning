"""
Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1 

"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        L = len(grid)
        W = len(grid[0])
        def helper(x,y):
            if (x < 0 or x >= L or y < 0 or y >= W or grid[x][y] == '*' or grid[x][y] == '0'):
                return
            grid[x][y] = '*'
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                helper(x+dx,y+dy)
            return
        ans = 0
        for i in range(L):
            for j in range(W):
                if (grid[i][j] == '1'):
                    ans += 1
                    helper(i,j)
        return ans