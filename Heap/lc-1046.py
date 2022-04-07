"""
python 中只有最小堆

"""
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            temp1 = heapq.heappop(stones)
            temp2 = heapq.heappop(stones)
            heapq.heappush(stones,temp1-temp2)
        
        return stones[0]*-1
            

lc_1046 = Solution()
stones = [2,7,4,1,8,1]
stones1 = [1,23]
print(f'lc_1046:{lc_1046.lastStoneWeight(stones1)}')
