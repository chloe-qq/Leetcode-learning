"""
Note: This question is the same as 1296:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].


min heap 遍历最小的元素回快一些 从O(n) --> O (log n)
hashmap
"""
from typing import List
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        N = len(hand)
        if ( N % groupSize > 0):
            return False
        
        for i in hand:
            hashmap[i] = hashmap.get(i, 0) + 1
        min_heap = [i for i in hashmap.keys()]
        heapq.heapify(min_heap)
        
        for round in range(N // groupSize):
            smallest = min_heap[0]

            for i in range(smallest, smallest + groupSize):
                if ( i not in min_heap):
                    return False
                hashmap[i] -= 1
                if (hashmap[i] == 0):
                    # 说明出现了 1 3 4 剩余的情况，不可能发生这种情况
                    if (i!=min_heap[0]):
                        return False
                    else:
                        heapq.heappop(min_heap)

                    
                    
                    

hand = [3,4,7,4,6,3,6,5,2,8]
groupSize = 2    
lc_846 = Solution()
print(lc_846.isNStraightHand(hand,groupSize ))