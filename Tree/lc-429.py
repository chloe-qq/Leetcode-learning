class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque()
        ans = []
        if (root):
            queue.append(root)

        while queue:  
            curList = []
            next_queue = deque()
            while (queue):
                cur = queue.popleft()
                curList.append(cur.val)
                
                for child in cur.children:
                    next_queue.append(child)

            queue = next_queue
            ans.append(curList)
        return ans