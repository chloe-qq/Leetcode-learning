"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
"""
import heapq
from typing import List
class Solution:
    
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        occupy = []
        intervals = sorted(intervals, key = lambda x:( x[0], x[1]))
        cnt = 0
        # create a heap, saving the last ended meeting time
        # iterate the intervals, when iteration end, the size of the heap is exactly the room we need
        heapq.heappush(occupy, intervals[0][1])
        intervals.pop(0)
        for i in intervals:
            if (i[0] >= occupy[0]):
                heapq.heappop(occupy)
            heapq.heappush(occupy,i[1])
        return len(occupy)
    
    
    # similar questions 1094, 1109
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        occupy = []
        for begin,end in intervals:
            occupy.append([begin,1])
            occupy.append([end, -1])
        occupy.sort()

        cnt = 0
        res = 0
        for t, i in occupy:
            cnt += i
            res = max(res, cnt)
        return res
        

        
       
intervals = [[0,30],[0,10],[5,10],[15,20]]
lc_253 = Solution()
print(f'lc_253: {lc_253.minMeetingRooms(intervals)}')
