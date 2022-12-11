
"""
124. Binary Tree Maximum Path Sum
 It would make sense to consider a path sum contributed by a subtree only if it is positive. 
 只考虑node为正的path，不然没必要考虑
 In other words, the path goes down the left or the right subtree only if we see a gain in the path sum.

  first determine the gain in the path sum contributed by the left and the right subtree
  先考虑children 如果贡献gain为正，则加上这些children --〉 postorder traversal
  
  
  recursion function: The function returns the path sum gain contributed by the subtree.
  注意：一次只能考虑来自left or right subtree的贡献，否则可能不再是valid path
"""
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -float('inf')
        def gain_from_subtree(node):
            nonlocal max_path_sum
            if (not node):
                return 0
            
            gain_from_left = max(gain_from_subtree(node.left),0)
            gain_from_right = max(gain_from_subtree(node.right),0)
            max_path_sum = max(max_path_sum, gain_from_left+gain_from_right+node.val)
            return max(node.val + gain_from_left, node.val + gain_from_right)
        gain_from_subtree(root)
        return max_path_sum
