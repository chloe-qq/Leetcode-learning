# 1101. The Earliest Moment When Everyone Become Friends

from typing import List
class UnionFind:
    def __init__(self, n):
        self.group = [i for i in range(n)]
        self.degree = [1 for _ in range(n)]
        
    def find(self,x):
        if (x!=self.group[x]):
            self.group[x] = self.find(self.group[x])
        return self.group[x]
    
    def union(self, x,y):
        p1 = self.find(x)
        p2 = self.find(y)
        if (p1 == p2):
            return False
        if (self.degree[p1] > self.degree[p2]):
            self.degree[p1] += self.degree[p2]
            self.group[p2] = p1
        else:
            self.group[p1] = p2
            self.degree[p2] += self.degree[p1]
        return True
            
from collections import deque

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x:x[0] )
        res = n
        uf = UnionFind(n)
        maxdegree = 0
        i = 0
        while (maxdegree < n and i < len(logs)):
            date, x, y = logs[i][0],logs[i][1],logs[i][2]
            if (uf.union(x,y)):
                maxdegree = max(uf.degree)
                print(f'union! i = {i}, degree ={uf.degree}')
            i += 1
        return date if maxdegree == n else -1
        
        
        
lc_1101 = Solution()
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
print(lc_1101.earliestAcq(logs, n))    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        