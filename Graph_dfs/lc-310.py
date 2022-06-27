"""
minimun height tree
node with degree 1 can not be the node
recursively remove nodes with degree 1
"""
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        prev_leaves = leaves
        while leaves:
            new_leaves = []
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            prev_leaves, leaves = leaves, new_leaves

        return prev_leaves  
            
                
lc310 = Solution()
numCourses = 4
prerequisites = [[1,0],[1,2],[1,3]]
print(f'Leetcode 310 Solution:{lc310.findMinHeightTrees(numCourses,prerequisites)}')             
            