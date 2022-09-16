# very much like lc_2007
import collections
from typing import List


# optimization
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        frequency = collections.Counter(arr)
        
        arr = sorted(arr, key = abs)

        for x in arr:
            if (frequency[x] == 0): 
                continue
            if (frequency[2*x] == 0):
                return False
            frequency[2*x] -= frequency[x]
            if (frequency[2*x]<0):
                return False
            frequency[x] = 0
        return True

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        frequency = collections.Counter(arr)
        
        arr = sorted(arr, key = abs)

        for x in arr:
            if (frequency[x] == 0): 
                continue
            if (frequency[2*x] == 0):
                return False
            frequency[x] -= 1
            frequency[2*x] -= 1
        return True