from typing import List
class Solution():
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        result = []
        def dfs(i, cur, total):
            if (total == target):
                result.append(cur.copy())
                return
            if (i >= N or total > target):
                return
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            # !! 去重的关键!!
            while (i+1 < N and candidates[i+1] == candidates[i]):
                i += 1
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return result
        
lc40 = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
result = lc40.combinationSum2(candidates,target)
print(f'leetcode 40: result = {result}')