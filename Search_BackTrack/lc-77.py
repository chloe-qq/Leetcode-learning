from typing import List
# 有点类似amazon DE面试考的那道电话号码组合 lc17 其实还是有点不一样

"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [i for i in range(1,n+1)]
        result = []
        def dfs(i,cur):
            if (len(cur) == k):
                result.append(cur.copy())
                return
            if (i > n or len(cur) > k):
                return
            else:
                cur.append(i)
                dfs(i+1,cur)
                cur.pop()
                dfs(i+1,cur)
        dfs(1,[])
        return result
# time complexity: o(n^k), k is the height of the tree
lc77 = Solution()
result = lc77.combine(4,2)
print(result)