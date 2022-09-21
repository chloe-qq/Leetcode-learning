# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def dfs(cur, pre, length):
            nonlocal maxLength
            
            if (not cur):
                return

            if (pre == None):
                length = 1
            elif (cur.val == pre + 1):
                length += 1
            else:
                length = 1
            maxLength = max(maxLength, length)
            if (cur.left is None and cur.right is None):
                return
            dfs(cur.left, cur.val, length)
            dfs(cur.right, cur.val, length)
            length -= 1

        dfs(root, None, 0)
        return maxLength
        
            
                
        