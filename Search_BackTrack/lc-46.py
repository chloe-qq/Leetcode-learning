# permutation 排列问题
# backtrack 三要素 : choice, constrain, goal
# choice 为nums中任意int，constrain 为每个int只能选一次， goal 为res = nums 的length

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        if (N == 1):
            return [nums[:]]
        used = [False] * N
        def backtrack(cur, used):
            if (len(cur) == N):
                # 注意这里必须是cur.copy(), 如果只是cur会出现空
                res.append(cur.copy())
            for i in range(len(nums)):
                if (not used[i]):
                    # make a choice
                    cur.append(nums[i])
                    # 因为每个数字只能使用一次，故要用一个array来记录这个数字是否被使用
                    used[i] = True
                    backtrack(cur, used)
                    # undo the choice
                    cur.pop()
                    used[i] = False
        backtrack([],used)
        return res

lc_46 = Solution()
nums = [1,2,3]
print(f'Leetcode 46: {lc_46.permute(nums)}')
        


