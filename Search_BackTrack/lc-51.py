from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        p_diag_set = set()
        n_diag_set = set()
        col_set = set()

        list1 = ['.' for i in range(n)]
        temp = ''.join(list1)
        cur = []
        def dfs(cur,r,col_set,p_diag_set,n_diag_set):
            if (len(cur) == n or r >= n):
                res.append(cur.copy())
                return
            if (r >= n or r < 0):
                return
            for c in range(n):
                if (c in col_set or r+c in p_diag_set or r-c in n_diag_set):
                    c += 1
                    continue
                else:
                    col_set.add(c)
                    p_diag_set.add(c+r)
                    n_diag_set.add(r-c)
                    temp1 = temp[:c] + 'Q' + temp[c+1:]
                    cur.append(temp1)
                    dfs(cur,r+1,col_set,p_diag_set,n_diag_set)
                    cur.pop()
                    col_set.remove(c)
                    p_diag_set.remove(c+r)
                    n_diag_set.remove(r-c)
        dfs(cur,0,col_set,p_diag_set,n_diag_set)
        return res

lc_51 = Solution()
print(f'Leetcode 51: {lc_51.solveNQueens(4)}')


