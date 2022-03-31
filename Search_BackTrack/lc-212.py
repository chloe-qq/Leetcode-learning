# word search II https://www.youtube.com/watch?v=asbcE9mZz_U&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=9
# lc 提交超时了
# to optimize: remove if it is a leaf node when complete the search on that node??

from typing import List
# 定义一个class 叫Trie 即prefix tree 
# 每个node 储存其本身字符 以及 下一个字母 作为children + 本身是否为word结束
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            # first check whether this children exists! important
            if (c not in cur.children):
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


      
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        N = len(words)
        visited = set()
        res = set()

        root = TrieNode() # define the prefix tree
        for w in words:
            root.addWord(w)

        def dfs(x,y,node,word):
            if (x < 0 or y < 0 or x>=m or y >=n or (x,y) in visited or board[x][y] not in node.children):
                return
            visited.add((x,y))
            node = node.children[board[x][y]]
            word += board[x][y]
            if (node.isEnd):
                res.add(word)
            
            dfs(x+1,y,node, word)
            dfs(x-1,y,node, word)
            dfs(x,y+1,node, word)
            dfs(x,y-1,node, word)

            visited.remove((x,y))

        for i in range(m):
            for j in range(n):
                dfs(i,j,root, '')
        return list(res)

board =  [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]

word = ["oaa",'oa']
lc212 = Solution()
print(f'Leetcode 79 = {lc212.findWords(board,word)}')
       