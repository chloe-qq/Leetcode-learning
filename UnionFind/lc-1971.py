
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # unionFind
        def find(x):
            if (parent[x]!=x):
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            
            if (p1==p2):
                return
            if (degree[p1] > degree[p2]):
                parent[p2] = p1
                degree[p1] += degree[p2]
            else:
                parent[p1] = p2
                degree[p2] += degree[p1]
            return
        parent = [i for i in range(n)]
        degree = [1 for i in range(n)]
        for v1, v2 in edges:
            union(v1,v2)
        return True if find(destination) == find(source) else False
            
            
                