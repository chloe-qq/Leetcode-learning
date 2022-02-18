from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def dfs(i, cur, total):
            # 必须是先执行这个判断，不然如果先执行下一个if,遇到i=9才符合条件的话会直接return不会把结果加到result
            if (len(cur) == k and total == n):
                result.append(cur.copy())
                return
            if (i > 9 or total > n or len(cur) > k):
                return            
            cur.append(i)
            dfs(i+1, cur, total+i)
            cur.pop()
            dfs(i+1,cur,total)
        dfs(1,[],0)
        return result
            
lc216 = Solution()
k = 5
n = 35
result = lc216.combinationSum3(k,n)
print(f'leetcode 216: result = {result}')