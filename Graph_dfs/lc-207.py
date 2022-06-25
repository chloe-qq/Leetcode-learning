"""
    Course Schedule

detect whether graph forms a circle
use data structure hashmap preMap to keep record of each class
"""
from re import L
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # loop over number of course in case the graph are not connected each other !!! important!!
        preMap = {i:[]for i in range(numCourses)}
        
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
            
        visited_set = set() # set used to detect whether a loop exists
        

        def dfs(cur):
            # base case
            if (cur in visited_set):
                return False
            if (preMap[cur] == []):
                return True
            
            visited_set.add(cur)
            
            for pre in preMap[cur]:
                if (dfs(pre) == False):
                    return False
            # remove that course from visited list since this course can be completed in case meet it next time
            visited_set.remove(cur)
            # set the cur course pre to be empty list, as is verfied can be taken
            preMap[cur] = []
            return True
           
        
        # loop over number of course in case the graph are not connected each other !!! important!!
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
            
            

    
        
        


lc207 = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(f'Leetcode 207 Solution:{lc207.canFinish(numCourses,prerequisites)}')