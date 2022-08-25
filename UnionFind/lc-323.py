"""

323. Number of Connected Components in an Undirected Graph
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS: BRUTE FORCE
        # BETTER METHOD: UNION FIND
        # https://www.youtube.com/watch?v=8f1XPm4WOUc
        # the value in node denotes the parent of the node, at first, each node's parent is itself
        parent = [i for i in range(n)]
        # rank denote the parent has how much child + itself, the minimum is 1
        rank = [1 for i in range(n)]
        def find_parent(x):
            res = x
            while (res != parent[res]):
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        def union(n1,n2):
            p1 = find_parent(n1)
            p2 = find_parent(n2)
            if (p1 == p2):
                return 0
            if (rank[p1] >= rank[p2]):
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        result = n
        for n1,n2 in edges:
            result -= union(n1,n2)
        #print(parent)
        #print(rank)
        return result
                
                
            
        