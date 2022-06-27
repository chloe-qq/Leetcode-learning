"""
is to detect whether forms a circle
if no circle and all notes are connected to each other -> valid tree
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges_dict = {i:[] for i in range(n)}
        for u,v in edges:
            edges_dict[u].append(v)
            edges_dict[v].append(u)
        
        
        print(edges_dict)
        visiting = set()

        # cur, pre ensure correctly detect the loop
        def dfs(cur,pre):
            print(f'current node: {cur}, pre node {pre}')
            if (cur in visiting ):
                return False

            if (edges_dict[cur] == []):
                return False
            visiting.add(cur)
            for i in edges_dict[cur]:
                if (i == pre):
                    continue
                if (not(dfs(i, cur))):
                    return False
            return True
                
        a = dfs(n-1,n-1)
        print(a)
        print(len(visiting))
        if (len(visiting) == n and a==True):
            return True
        
 
        return False
    
lc261 = Solution()
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(f'Leetcode 310 Solution:{lc261.validTree(n,edges)}')      