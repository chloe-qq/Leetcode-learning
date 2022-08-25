from typing import List
class UnionFind():
    def __init__(self,n):
        self.group = [i for i in range(n+1)]
        self.degree = [1 for _ in range(n+1)]
        
    def find(self, x):
        if (x!=self.group[x]):
            self.group[x] = self.find(self.group[x])
        return self.group[x]
    
    def union(self, x,y):
        p1 = self.find(x)
        p2 = self.find(y)
        
        if (p1 == p2):
            return False
        
        if (self.degree[p1] > self.degree[p2]):
            self.group[p2] = p1
            self.degree[p1] += self.degree[p2]
        else:
            self.group[p1] = p2
            self.degree[p2] += self.degree[p1]
        return True
    

class Solution:    
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # By Union-Find
        edges = []
        for i, cost in enumerate(wells):
            edges.append((cost,0,i+1))
        
        for house1, house2, cost in pipes:
            edges.append((cost,house1,house2))
        # sort edges by cost
        edges.sort(key = lambda x:x[0])    
        uf = UnionFind(n)
        total_cost = 0
        for cost, house1, house2 in edges:
            if (uf.union(house1, house2)):
                total_cost += cost
        return total_cost
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        