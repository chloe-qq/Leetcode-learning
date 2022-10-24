from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 其实我们只需要知道重新排序后，符合条件递增的有几个即可
        # 非常类似lc334
        # 一定要按照第二个index排序
        cur,ans = -float('inf'),0
        pairs = sorted(pairs, key = lambda x:x[1])
        for begin, end in pairs:
            if (cur < begin):
                ans += 1
                cur = end
        return ans
pairs = [[-6,9],[-9,8],[-5,3],[0,3]]
lc646 = Solution()
lc646.findLongestChain(pairs)