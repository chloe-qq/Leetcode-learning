# 695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        M = len(grid)
        N = len(grid[0])
        def dfs(x,y):
            if (x < 0 or x >= M or y < 0 or y >=N or (x,y) in visited or grid[x][y] == 0) :
                return 0
            visited.add((x,y))
            if (grid[x][y] == 1):
                return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
        maxArea = 0
        for i in range(M):
            for j in range(N):
                maxArea = max(dfs(i,j),maxArea)
        return maxArea