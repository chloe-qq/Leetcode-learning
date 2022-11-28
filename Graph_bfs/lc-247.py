# 类似 bfs 但不完全是bfs, 另一种方法是recursion
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidate = {    
            '0':'0',
            '1':'1',
            '8':'8',        
            '6':'9',
            '9':'6'
        }
        cur_length = n % 2
        queue = deque(['0','1','8']) if cur_length == 1 else deque([''])

        while (cur_length < n):
            cur_length += 2

            next_queue = deque([])
            while (queue):
                cur = queue.popleft()
                for pair in candidate.items():
                    if (cur_length==n and pair[0] == '0'):
                        continue
                    next_queue.append(pair[0]+cur+pair[1])
            queue = next_queue
        return queue
