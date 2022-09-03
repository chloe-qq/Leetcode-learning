

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
from typing import Optional, List

# Average of Levels in Binary Tree
# traverse the given tree on a level-by-level basis

# start by pushing the root node into a queuequeue. 
# Then, we remove an element(node) from the front of the queuequeue. 
# For every node removed from the queuequeue, we add all its children to the back of the same queuequeue. 
# We keep on continuing this process till the queuequeue becomes empty

from collections import deque
from typing import Optional
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        ans = []
        if (root):
            queue.append(root)
            
        while (queue):
            N = len(queue)
            curSum = 0
            count = 0
            tempQueue = deque()
            while (queue):
                cur = queue.popleft()
                curSum += cur.val
                count += 1
                if (cur.left):
                    tempQueue.append(cur.left)
                if (cur.right):
                    tempQueue.append(cur.right)
            queue = tempQueue
            ans.append(curSum/count)
        return ans