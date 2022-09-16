from typing import List
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        N = len(changed)
        
        if (N%2 == 1):
            return []
        

        ans = []
        changed.sort()
        hashmap = Counter(changed)
        for smallest in changed:
            if (hashmap[smallest] <= 0):
                continue
            hashmap[smallest] -= 1
            if (2*smallest in hashmap.keys() and hashmap[2*smallest] > 0):
                hashmap[2*smallest] -= 1
                ans.append(smallest)
            else:
                return []

        return ans
        
lc_2007 = Solution()

changed = [8,1,3,4,6,2]
lc_2007.findOriginalArray(changed)
        