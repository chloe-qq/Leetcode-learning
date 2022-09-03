
"""
car pooling
The vehicle only drives east (i.e., it cannot turn around and drive west).

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
"""

from typing import List
import heapq
class Solution:
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: (x[1], x[2]))
        road = []
        heapq.heappush(road,[trips[0][2], trips[0][0]])
        capacity -= trips[0][0]
        if (capacity < 0):
            return False
        
        for i in trips[1:]:
            while (road and i[1] >= road[0][0]):
                capacity += road[0][1]
                print(f'update capacity:{capacity}')
                heapq.heappop(road)
            capacity -= i[0]
            
            if (capacity < 0):
                return False
            heapq.heappush(road,[i[2],i[0]])

        return True
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        # concept of bucket sort
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        print(lst)
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
    

trips = [[3,2,8],[4,4,6],[10,8,9]]

capacity = 11


lc_1094 = Solution()
print(f'lc_1094:{lc_1094.carPooling(trips,capacity)}')
                
