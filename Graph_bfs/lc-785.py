#  Is Graph Bipartite?
# 可以用unionFind来做 也可以用bfs dfs来做

# 此为BFS做法 --> queue, deque
from typing import List
from collections import deque
class Solution:
    # 转化成二分涂色问题，由边相连的相邻2个顶点不能被涂成同一个颜色
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0]*n # initial color = 0, set to 1 or -1 later
        
        for i in range(n):
            if (visited[i] != 0):
                continue
            
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while (queue):
                cur = queue.pop()
                cur_color = visited[cur]
                
                neighbour_col = 1 if (visited[cur] == -1) else -1
                for neighbour in graph[i]:
                    if (visited[neighbour]==cur_color):
                        return False
                    elif (visited[neighbour] == 0):
                        visited[neighbour] = neighbour_col
                        queue.append(neighbour)
        return True
                    
                
                
    