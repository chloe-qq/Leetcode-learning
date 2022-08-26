"""
给定地图，起始点为[0,0]（左上角）
终止点为[m,n]右下角
要求 走路高度差不能超过h
问是否能从左上角走到右下角


BFS
"""

from collections import deque
def canReach(mountains, h):
    m = len(mountain)
    n = len(mountain[0])
    if ( m == 1 and n == 1):
        return True
    visited = [[False]*n for _ in range(m)]
    visited[0][0] = True
    queue = deque([(0,0)])
    
    step = 0
    
    while queue:
        step += 1
        qSize = len(queue)
        
        for _ in range(qSize):
            x,y = queue.popleft()
            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny = x+dx, y+dy
                if (nx >= 0 and nx < m and ny >= 0 and ny < n and (not visited[nx][ny]) and abs(mountains[nx][ny]-mountain[x][y]) <= h):
                    if (nx == m-1 and ny == n-1):
                        return step
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return -1

mountain = [[10,20,30,50,70],[160,140,120,100,80],[170,180,190,200,210]]
h = 20

print(canReach(mountain,h))