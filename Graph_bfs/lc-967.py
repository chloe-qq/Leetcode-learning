

# 967. Numbers With Same Consecutive Differences
"""
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""


from collections import deque
from typing import List
# dfs
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def dfs(cur,i):
            if (i == n):
                ans.append(int(''.join(cur.copy())))
                return
            if (i == 0):
                for j in range(1,10):
                    cur.append(str(j))
                    dfs(cur, i+1)
                    cur.pop()
            else:
                last_digit = int(cur[-1])
                for j in range(0,10,1):
                    if (j-last_digit == k or j-last_digit == -k):
                        cur.append(str(j))
                        dfs(cur, i+1)
                        cur.pop()
        dfs([],0)
        return ans
# bfs

from collections import deque 
def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        # initialize when n == 1, the candidates are [1,2,...,9]
        
        queue = deque([i for i in range(1,10)])
        n -= 1        
        while (n>0):           
            next_queue = deque()
            while (queue):
                cur = queue.popleft()
                tail_digit = cur%10
                next_digit = set([tail_digit + k, tail_digit-k ])
                for i in next_digit:
                    if (i >= 0 and i < 10):
                        next_int = cur*10 + i
                        next_queue.append(next_int)
            queue = next_queue
            #print(f'queue: {queue}')
            n -= 1

        return list(next_queue)
    
                


            
            
        