from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        result = []
        def dfs(i, cur, total):
            if (total > target or i >= N):
                return
            if (total == target):
                # since we only maintain a single variable list called cur, we do not want to append cur itself, 
                # we need to continue to use the cur variable recursively so we need to make a copy of it (因为之后还会修改这个cur所以要make a copy of it!!)
                # important!
                result.append(cur.copy())
                return
            cur.append(candidates[i])
            dfs(i,cur, total + candidates[i])
            cur.pop()
            # restore cur by poping out the last value 
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return result


candidates = [2,3,6,7]
target = 7
lc39 = Solution()
result = lc39.combinationSum(candidates,target)
print(f'result: {result}')