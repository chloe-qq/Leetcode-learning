# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
中间节点的顺序就是所谓的遍历方式

前序遍历：中左右
中序遍历：左中右
后序遍历：左右中

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
#  Binary Tree Preorder Traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(root):
            if (not root):
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return result
            