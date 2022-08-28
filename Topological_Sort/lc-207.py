"""
Course Schedule

可以用拓扑排序来做，也可以用dfs来做，见Graph_dfs lc-207
"""
from collections import defaultdict,deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # loop over number of course in case the graph are not connected each other !!! important!!
        """
    Course Schedule

detect whether graph forms a circle
use data structure hashmap preMap to keep record of each class
"""



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # loop over number of course in case the graph are not connected each other !!! important!!
        preList = [0]*numCourses
        hashmap = defaultdict(list)
        queue = deque()
        for cur, pre in prerequisites:
            preList[cur] += 1
            hashmap[pre].append(cur)
        for i, count in enumerate(preList):
            if (count == 0):
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            numCourses -= 1

            for i in hashmap[cur]:
                preList[i] -= 1
                if (preList[i] == 0):
                    queue.append(i)
        
        return True if (numCourses == 0 ) else False
            
lc_207 = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
lc_207.canFinish(numCourses,prerequisites)