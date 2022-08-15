"""
1727. Largest Submatrix With Rearrangements

"""


from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        height = [0] * cols
        ans = 0
        for i in range(rows):
            
            for j in range(cols):
                height[j] = 0 if (matrix[i][j] == 0) else height[j] + 1
            height_copy = height.copy()
            height_copy.sort()

            #必须在循环里面以便每层高度计算一遍
            for j in range(cols):
                ans = max(ans, height_copy[j] * (cols-j))

        return ans  
        