#  lowest common ancestor (LCA) of two given nodes in the BINARY tree
# Approach 1: Recursive Approach
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            if (not cur):
                return False
            left = dfs(cur.left)
            
            

            mid = (cur == p) or (cur == q)

            right = dfs(cur.right)
            # # If any two of the three flags left, right or mid become True.
            if (left + mid + right >= 2):
                self.ans = cur
            # Return True if either of the three bool values is True.
            return mid or left or right

        dfs(root)
        return self.ans
# Approach 2: Iterative using parent pointers

