"""
 Longest Common Subsequence 
 
Subsequence v.s. substring

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.


bottom-up dp: find the sub-problem
if abcde, ace  -> bcde, ce
if the currnent text[i]==text[j], we move diagonally from the dp
or we go right, also go down and take the max of (going right, going down)

the below cell represents the subproblem 
比如 text1 长度为4, text2 长度为6，构建dp[4+1][6+1]
dp[3][5]表示text1[3:] 和text2[5:]中的common subsequence个数
所以最终返回dp[0][0]
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)
        # initialize one more column and row to be zero, since bottom up
        # we do not go over the last column and the last row, since it should be 0
        dp = [[0]*(N2+1) for _ in range(N1+1)]
        for i in range(N1-1,-1,-1):
            for j in range(N2-1,-1,-1):
                # since we initialize one more column and rows, so i+1, j+1 should not out of boundary
                if (text1[i] == text2[j]):
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
                
text1 = "abcde"
text2 = "ace"     
result = Solution().longestCommonSubsequence(text1, text2)
print(result)     
        
        
        
        