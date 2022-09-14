# 使得两个数列相同的最小花费
"""

两个数列A和B,长度分别为n和m
使得两个数列变成一样，有2种操作:
1) 选定一个数列，将一个数a改为b,会花费|a-b|
2) 选择一个数列中的a,丢掉

求使得两个数列变相同的最小花费
"""
from typing import List
def minCost(A: List[int], B:  List[int])->int:
    n = len(A)
    m = len(B)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0] + abs(A[i])
    for j in range(m):
        dp[0][j+1] = dp[0][j+1] + abs(B[j])
        
        
    for i in range(1,1+n):
        for j in range(1,1+m):
            curMin = min(dp[i-1][j]+abs(A[i-1]), dp[i][j-1]+abs(B[j-1]))
            dp[i][j] = min(curMin, dp[i-1][j-1] + abs(A[i-1]-B[j-1]))
    return dp[n][m]

A = [2,3,4,5]
B = [2,4,3,5]

cost = minCost(A,B)
print(cost)