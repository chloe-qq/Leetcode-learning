# 和华为OA-1 非常相似，甚至更难一些

from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # very similar to huawei OA -1
        m = len(heights)
        n = len(heights[0])
        
        # 对于Pacific来说，初始在queue中的点为x = 0 or y = 0的点
        # 我们反向去check通过这些点能否到达别的点（即取反：走向高度大的地方）
        # 如果可以那么说明这些点也能到达这些点
        pacific_queue = deque([(0,0)])
        atlantic_queue = deque([(m-1,n-1)])
        # intialize queue
        for i in range(1,m):
            pacific_queue.append((i,0))
            atlantic_queue.append((m-1-i,n-1))
        for i in range(1,n):
            pacific_queue.append((0,i))
            atlantic_queue.append((m-1, n-1-i))

        def dfs(queue):
            canReach = set()
            while queue:
                x,y = queue.popleft()
                canReach.add((x,y))

                cur_h = heights[x][y]
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    cur_x,cur_y = x+dx, y+dy
                    if (cur_x < 0 or cur_x >= m or cur_y < 0 or cur_y >= n):
                        continue
                    if ((cur_x,cur_y) in canReach):
                        continue
                    # if new height smaller than the current
                    # meaning the new cell cannot be flowed to the current cell
                    if (heights[cur_x][cur_y]<cur_h):
                        continue
                    queue.append((cur_x,cur_y))
            return canReach
        canReach_pacific = dfs(pacific_queue)
        canReach_atlantic = dfs(atlantic_queue)
        
        return list(canReach_pacific.intersection(canReach_atlantic))
 