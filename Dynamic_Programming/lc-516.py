# 516. Longest Palindromic Subsequence
# 不需要多一列0，而lc-1143 longest common sequencnce 需要多一行&一列 进行补0操作
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp =[ [0]*N  for _ in range(N)]
        
        for left in range(N-1,-1,-1):
            dp[left][left] = 1
            for right in range(left+1,N,1):
                if (right == left + 1 and s[left] == s[right]):
                    dp[left][right] = 2
                    continue
                elif (s[left] == s[right]):
                    dp[left][right] = dp[left+1][right-1] + 2
                else:
                    dp[left][right] = max(dp[left+1][right],dp[left][right-1])
        return dp[0][N-1]
                    
            
        