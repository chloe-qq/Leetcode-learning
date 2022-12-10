# 1026. Maximum Difference Between Node and Ancestor
from optional import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        if (not root):
            return self.ans
        # 找到一条路上的max与min value，返回max or min 减去node.val的最大值
        def helper(cur_node:TreeNode, cur_max:int,cur_min:int):
            if (not cur_node):
                return 
            self.ans = max(self.ans, abs(cur_max-cur_node.val),abs(cur_min-cur_node.val))
            cur_max = max(cur_max,cur_node.val)
            cur_min = min(cur_min,cur_node.val)
            helper(cur_node.left, cur_max, cur_min)
            helper(cur_node.right, cur_max, cur_min)
        helper(root, root.val, root.val)
        return self.ans