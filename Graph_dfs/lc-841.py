"""
841. Keys and Rooms
    """
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        # initial position = 0
        stack = [0]
        while (stack):
            cur = stack.pop()
            visited.add(cur)
            for key in rooms[cur]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)
            
            


lc841 = Solution()
rooms = [[2],[],[1]]
print(f'Leetcode 841 Solution:{lc841.canVisitAllRooms(rooms)}')     

