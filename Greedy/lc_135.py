"""
牛客  BM95 分糖果问题
一群孩子做游戏，现在请你根据游戏得分来发糖果，要求如下：

1. 每个孩子不管得分多少，起码分到一个糖果。
2. 任意两个相邻的孩子之间，得分较多的孩子必须拿多一些糖果。(若相同则无此限制)
Input: ratings = [1,0,2]
Output: 5
Explanation: 
You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        N = len(ratings)
        candyList = [1] * N
        #total = N
        for i in range(1,N):
            if (ratings[i] > ratings[i-1]):
                candyList[i] = candyList[i-1] + 1
        #反向扫描的时候要注意 update  candyList[j] 要取max 
        #正向扫描的时候不需要 因为 先 正向扫描 的时候不存在不是1 的情况    
        for j in range(N-2,-1,-1):
            if (ratings[j] > ratings[j+1]):
                candyList[j] = max(candyList[j+1] + 1, candyList[j])
        return sum(candyList)
            
lc_135 = Solution()
ratings = [1,0,2,3,4,4,1,1]
print(lc_135.candy(ratings))
            