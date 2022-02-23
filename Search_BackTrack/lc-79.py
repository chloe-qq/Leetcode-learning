# word search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        L = len(word)
        visited = set()
        def dfs(x,y,cur):
            if (cur == L):
                return True
            if (x < 0 or x >= m or y < 0 or y >= n or cur >= L or (x,y) in visited or board[x][y] != word[cur]):
                return False
            else:
                # mark as visited
                visited.add((x,y))
                result = (dfs(x+1,y,cur+1) or dfs(x-1,y,cur+1) or dfs(x,y+1,cur+1) or dfs(x,y-1,cur+1))
                # 重要！在这里需要把mark visited 去掉，见以下例子
                # 因为每在一个新的点开始第一轮 (cur = 0)的dfs search的时候，之前visited过的点是需要再次visit的
                # 故要把它们remove出来
                visited.remove((x,y))
                return result
        for i in range(m):
            for j in range(n):
                if (dfs(i,j,0)):
                    return True
        return False

board =  [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
lc79 = Solution()
print(f'Leetcode 79 = {lc79.exist(board,word)}')
       

        



        

            
        