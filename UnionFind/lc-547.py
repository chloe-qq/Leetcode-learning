"""
547. Number of Provinces

"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1]*n
        
        def find(x):
            par = x
            while(par != parent[par]):
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par
        
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if (p1 == p2):
                return 0
            
            if (size[p1] > size[p2]):
                size[p1] += size[p2]
                parent[p2] = p1
            else:
                size[p2] += size[p1]
                parent[p1] = p2
            return 1
        
        for begin,end in edges:
            n -= union(begin,end)
            
        return n
