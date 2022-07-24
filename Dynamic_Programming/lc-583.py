"""
583. Delete Operation for Two Strings

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

# very similiar to LCS
find the command lcs if LCS_LENGTH = M, opertaion time = (N1-M) + (N2-M)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        
        # initialize one more row & col for default 0
        dp = [[0]*(N2+1) for _ in range(N1+1)]
        # we do not go through the last col/row since it is 0
        
        for i in range (N1-1,-1,-1):
            for j in range(N2-1, -1, -1):
                if (word1[i] == word2[j]):
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        LCS = dp[0][0]
        
        return N1+N2-2*LCS
    
word1 = "leetcode"
word2 = "etco"
operation = Solution().minDistance(word1, word2)
print(operation)