"""
210. Course Schedule II
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
返回一个可能的拓扑排序
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        preCount = [0]*numCourses
        for cur, pre in prerequisites:
            preCount[cur] += 1
            preMap[pre].append(cur)
        
        queue = deque()
        for i,count in enumerate(preCount):
            if (count == 0):
                queue.append(i)
                
        ans = []      
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for i in preMap[cur]:
                preCount[i] -= 1
                if (preCount[i] ==0):
                    queue.append(i)
        return ans if len(ans) == numCourses else []
                    
        
            