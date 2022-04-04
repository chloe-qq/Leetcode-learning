from typing import List


"""
类比permutation 和 permutation with duplicates
不一样!!! 用hashmap不行 需要loop把duplicate去掉
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)
        def dfs(cur,i):
            if (i == N):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(cur,i+1)
            t = cur.pop()
            i += 1
            # 确保tree的右侧不和左侧+一样的数字 和permutation 方法不同
            while(i < N and nums[i] == t):
                i += 1
            dfs(cur,i)
            
        dfs([],0)
        return res

lc_90 = Solution()
nums = [1,2,2]
print(f'Leetcode 90: {lc_90.subsetsWithDup(nums)}')

