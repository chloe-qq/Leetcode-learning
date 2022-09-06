
from collections import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        m = len(grid)
        n = len(grid[0])
        # When current board is 1 (right), ball will move to right only if the right neighbor of current position is also 1
        # When current board is -1 (left), ball will move to left only if the left neighbor of current position is also -1
        
        
        def dfs(row, col):
            if (row == m):
                return col
            if (grid[row][col] == 1 and col+1<n and grid[row][col+1] == 1):
                return dfs(row+1, col+1)
            elif (grid[row][col] == -1 and col-1>=0 and grid[row][col-1] == -1):
                return dfs(row+1, col-1)
            else:
                return -1
        return [dfs(0,i) for i in range(n)]
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
lc_1706 = Solution()
lc_1706.findBall(grid)