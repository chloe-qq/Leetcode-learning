"""

course schedule II
dfs O(E+V)

each course has 3 states:
    visited -> if one course is completed done, remove it from visiting_set, add it to visited_set
    visiting -> if one course in already in the visiting set, but we encounter it again, must be a loop, return []
    unvisited ->
"""
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        result = []
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
            
        visited_set = set()
        visiting_set = set()
        valid = True
        def dfs(cur):
            if (cur in visiting_set):
                return 
            visiting_set.add(cur)
            if (preMap[cur] == []):
                result.append(cur)
                visited_set.add(cur)
                visiting_set.remove(cur)
                return
            for i in preMap[cur]:
                if (i in visiting_set):
                    return 
                elif (i in visited_set):
                    continue
                else:
                    dfs(i)
            result.append(cur)
            visited_set.add(cur)
            visiting_set.remove(cur)
        for i in range(numCourses):
            if (i in visiting_set):
                return []
            if (not(i in visited_set)):
                dfs(i)
            
        return result 
                
lc210 = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(f'Leetcode 210 Solution:{lc210.findOrder(numCourses,prerequisites)}')          
            
            
        