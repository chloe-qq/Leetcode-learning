from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        def dfs(cur,i):
            if (i == N):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(cur,i+1)
            cur.pop()
            dfs(cur,i+1)
        dfs([],0)
        return res


lc_78 = Solution()
nums = [1,2,3]
print(f'Leetcode 78: {lc_78.subsets(nums)}')