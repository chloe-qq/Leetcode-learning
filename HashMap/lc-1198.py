from collections import Counter
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        m = len(mat)
        n = len(mat[0])
        

        # 因为strictly increasing, 所以每行的元素最多出现1次
        # 然后找出最小的 出现了m次的元素 （m为行数）
        # 先遍历列会快一些，因为smaller item 在每一行的最前 出现 （as sorted)
        for i in range(n):
            for j in range(m):
                hashmap[ mat[j][i] ] += 1
                if (hashmap[ mat[j][i] ] == m):
                    return mat[j][i]
 

        #优化 binary search

        return -1