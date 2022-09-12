class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        N = len(s)
        visited = [False]*N
        mx = 0
        while (queue):
            cur = queue.popleft()
            visited[cur] = True
            
            for j in range(max(cur + minJump, mx+1), min(cur + maxJump + 1, N)):
                if (s[j] == '0' and visited[j] == False):
                    if (j == N-1):
                        return True
                    queue.append(j)
            # prevent to start from repeated positions when performing BFS
            # as index before i + maxJump has been put into the queue
            mx = max(mx, cur + maxJump)
        return False
                
        