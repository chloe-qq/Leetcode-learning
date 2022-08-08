"""
from 牛客
BM46 最小的K个数
heap or binary search
要求：空间复杂度 O(n)，时间复杂度 O(nlogn)

python只有最小堆 所以要改成负数 把负数最小的（正数最大的）删掉
"""

import heapq
class Solution:
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        # write code here
        stack = []
        for i in input:
            if (len(stack) < k):
                heapq.heappush(stack,-i)
            elif (stack and -i > stack[0]):
                heapq.heappushpop(stack, -i)

                
                
        return [-i for i in stack]