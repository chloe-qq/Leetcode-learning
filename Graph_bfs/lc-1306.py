class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        N = len(arr)        
        queue = deque([start])
        visited = [False] * N
        
        while (queue):            
            cur = queue.popleft()
            visited[cur] = True
            if (arr[cur] == 0):
                return True
            for next_cur in [cur - arr[cur],cur + arr[cur]]:
                if (0 <= next_cur < N and visited[next_cur] == False):
                    queue.append(next_cur)
    
        return False
