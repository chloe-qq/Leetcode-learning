from collections import deque
from typing import List
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # get start location
        ans = []
        m = len(grid)
        n = len(grid[0])
        visited = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '*'):
                    queue.append((i,j))
                    visited[i][j] = 0
                    break
        
        while queue:
            cur_x,cur_y = queue.popleft()
            cur_step = visited[cur_x][cur_y]

            if (grid[cur_x][cur_y] == '#'):
                ans.append(cur_step)

            for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if (next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or visited[next_x][next_y]!=-1 or grid[next_x][next_y] == 'X'):
                    continue
                visited[next_x][next_y] = cur_step + 1
                queue.append((next_x,next_y))
        return min(ans) if ans else -1
    
    
lc_1730 = Solution()
grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print(lc_1730.getFood(grid))