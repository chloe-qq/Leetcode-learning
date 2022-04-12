"""
[binary search] + [sliding window]
[heap]

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""


from typing import List
import heapq

class Solution_heap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if (k == len(arr)):
            return arr

        max_heap = []
        min_heap = []

        for i in arr:
            if(i - x <= 0):
                heapq.heappush(max_heap, -i + x)
            else:
                heapq.heappush(min_heap,i - x)
        result = []

        while (k > 0 and len(max_heap) > 0 and len(min_heap) > 0):
            #print(f'max heap[0]:{max_heap[0]}; min heap [0]: {min_heap[0]}')
            if (max_heap[0] <= min_heap[0]):               
                result.append(-heapq.heappop(max_heap)+x)
                k -= 1

            else:
                result.append(heapq.heappop(min_heap)+x)
                k -= 1

        
        if (k == 0):
            return sorted(result)
        elif (len(max_heap) > 0):
            while (k > 0):
                result.append(-heapq.heappop(max_heap)+x)
                k-=1
        else:
            while (k > 0):
                result.append(heapq.heappop(min_heap)+x)
                k-=1
        
        return sorted(result)



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        l = 0
        r = N-k
        m = l + (r-l)//2
        while (l<r):
            print(f'l = {l}, r = {r}, m = {m}')
            # 不能用绝对值 这样才能确保x在这个range内
            if (x-arr[m] <= arr[m+k]-x): # shift towards left
                r = m
            else: #shift toward right
                l = m+1
            m = l + (r-l)//2
        return arr[m:m+k]

arr = [1,1,2,2,2,2,2,3,3]

k=3
x=3
lc658 = Solution()
result = lc658.findClosestElements(arr,k,x)
print(f'result: {result}')