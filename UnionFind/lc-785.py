# 785. Is Graph Bipartite?
#  could we separate the nodes in two separate disjoint sets which stand for two colors? Then Union Find is there for you!

from multiprocessing import parent_process
from typing import List
from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]
        def find(x):
            if (x!=parent[x]):
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x,y):
            px, py= find(x), find(y)
            
            if (px!=py):
                parent[py] = px
        
        for i in range(n):
            par = find(i)
            for j in graph[i]:
                if (find(j) == par):
                    return False
                # 需要把与i连着的涂成同一个颜色（即 与i不同的颜色才可以）所以他们得union
                union(graph[i][0], j)
        return True
            
                

lc_785 = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
lc_785.isBipartite(graph)