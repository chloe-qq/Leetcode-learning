# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
from typing import Optional
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        frequency = defaultdict(lambda: 0)
        def dfs(cur, frequency):
            # important usage of nonlocal, if ans is a list, non need to use 
            nonlocal ans
            if (not cur):
                return
            frequency[cur.val] += 1
            # if BOTH left and right is None, then it can reach the bottom
            # either one is NOT None, it DOES NOT REACH the bottom
            if (cur.left is None and cur.right is None):
                occurance = list(frequency.values())
                if (len([i for i in occurance if i%2 == 1]) <= 1):
                    ans += 1

            dfs(cur.left,frequency)
            dfs(cur.right,frequency)
            # important to backpop this value
            frequency[cur.val] -=1
        dfs(root,frequency)
        return ans
            