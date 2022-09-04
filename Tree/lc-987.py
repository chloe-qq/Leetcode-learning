# 987. Vertical Order Traversal of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
"""
queue 中放三个元素，(col, row, val)，因为sort的顺序是col, row, val 依次
用dfs进行search
走左儿子， col -1, row -1； 走右儿子 col -1, row -1
"""

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeEntries = []
        ans = []
        def dfs(cur, col, row):
            if (not cur):
                return
            heapq.heappush(nodeEntries,(col,row, cur.val))
            dfs(cur.left, col-1, row+1)
            dfs(cur.right, col+1, row+1)
            
        dfs(root,0,0)


        if (not nodeEntries):
            return []
        pre_col, pre_row, pre_val = heapq.heappop(nodeEntries)

        preGroup = [pre_val]
        while (nodeEntries):
            col, row, val = heapq.heappop(nodeEntries)
            if (col != pre_col):
                ans.append(preGroup)
                preGroup = [val]
            else:
                preGroup.append(val)
            pre_col, pre_row, pre_val = col, row, val
        # we did not append the last preGroup due to the previous structure, as for the last preGroup, we did not encouter a node with different col than that node
        if (preGroup):
            ans.append(preGroup)
        return ans
                
                
                
            
                
