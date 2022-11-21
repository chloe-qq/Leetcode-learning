from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        def isExit(x,y):
            if ([x,y] == entrance):
                return False
            if (x == 0 or x == m-1 or y == 0 or y == n-1):
                return True
            return False
        
        queue = deque([(entrance[0],entrance[1])])
        maze[entrance[0]][entrance[1]] = 0
        ans = None
        while queue:
            cur_x, cur_y = queue.popleft()
            cur_step =  maze[cur_x][cur_y]
            if (isExit(cur_x,cur_y)):
                ans = ans = min(ans,cur_step) if ans is not None else cur_step
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                next_x = cur_x + dx
                next_y = cur_y + dy
                if (next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or maze[next_x][next_y] != '.'):
                    continue
                else:
                    maze[next_x][next_y] = cur_step+1
                    queue.append((next_x, next_y))


        return ans if ans is not None else -1
lc_1926 = Solution()
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
ans = lc_1926.nearestExit(maze, entrance)