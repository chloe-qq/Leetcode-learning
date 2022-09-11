# 1996. The Number of Weak Characters in the Game
from typing import List 
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties,key = lambda x:(x[0],-x[1]))

        N = len(properties)
        maxDefense = 0
        ans = 0
        # 一定要从后向前遍历, 因为一个attack 和 defense 都大的元素只能被count一次
        for i in range(N-1,-1,-1):
            if (properties[i][1] < maxDefense):
                ans += 1
            maxDefense = max(maxDefense, properties[i][1])
        return ans