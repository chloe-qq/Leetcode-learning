from typing import List
"""
Restore IP Addresses
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


如果s长度>12,则不可能form valid answer, 可直接return []
time complexity 是常数 O(3^12) (每个点最多看3位是否可以put dot on)
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        N = len(s)
        if (N > 12): # corner case 如果s长度大于12,则至少有一个数字是四位数，不可能会符合条件
            return res
        def dfs(cur, i, dot):
            if (dot == 4 and i == N):
                res.append(cur[:-1]) # need to exclude the '.'
                return
            elif (dot == 4 and i < N):
                return
            
            for j in range(i+1,min(i+4,N+1)):# j at most = N, index N will not be included at s[i:j]
                if (j != i+1 and s[i] == '0'):
                    continue
                elif (int(s[i:j]) < 256):
                    dot += 1
                    cur += s[i:j] + '.'
                    dfs(cur, j, dot)
                    dot -= 1
                    cur = cur[:-(j-i+1)]
        dfs('', 0, 0)
        return res

lc_93 = Solution()
s = "101023"
print(f'Leetcode 93: {lc_93.restoreIpAddresses(s)}')