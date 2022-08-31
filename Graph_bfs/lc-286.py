
from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 -1
        #dijkstra algorithm
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()
        visited = {}

        for i in range(m):
            for j in range(n):
                if (rooms[i][j] == 0):
                    queue.append((i,j))       
        while queue:
            x,y = queue.popleft()
            cur_step = rooms[x][y]                  
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                next_x, next_y = x+dx, y+dy
                if (next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or rooms[next_x][next_y] == -1):
                    continue
                if (rooms[next_x][next_y] == INF):                    
                    rooms[next_x][next_y] = cur_step+1
                    queue.append((next_x,next_y))
                else:
                    rooms[next_x][next_y] = min(rooms[next_x][next_y],cur_step+1)
        for line in rooms:
            print(line)
            
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

lc_286 = Solution()
lc_286.wallsAndGates(rooms)