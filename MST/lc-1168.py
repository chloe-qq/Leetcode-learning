"""
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.


Prim's Algorithm
"""
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        # set virtual node 0 and add inital value to be the edge from every virtual node to that node
        for i,cost in enumerate(wells):
            graph[0].append((cost,i+1))
        for house1, house2, cost in pipes:
            graph[house1].append((cost, house2))
            graph[house2].append((cost, house1))
            
        MST_nodes = set()
        TotalCost = 0
        
        
        # set intital start point as the virtual point
        
        heapq.heapify(graph[0])
        candidates = graph[0]
        
        while (len(MST_nodes) < n):
            cost, next_house = heapq.heappop(candidates)
            if (next_house not in MST_nodes):
                MST_nodes.add(next_house)
                TotalCost += cost
                
                for new_cost, neighbour_house in graph[next_house]:
                    if (neighbour_house not in MST_nodes):
                        heapq.heappush(candidates,(new_cost,neighbour_house))

        return TotalCost
                        
            
            
        