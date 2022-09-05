
# count the extra close count, extraClose = 0
# if open bracket, extraClose -= 1; else extraClose += 1
# [[] each swap, actually get rid of 2 closing bracket
# since swap get rid of one, and the swapped matched again get rid of one
# so total swap time = (extraClose+1)//2
# https://www.youtube.com/watch?v=3YDBT9ZrfaU&t=3s
class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose = 0
        MaxextraClose = 0
        for char in s:
            if (char == ']'):
                extraClose += 1
                MaxextraClose = max(extraClose,MaxextraClose)
            else:
                extraClose -= 1
        return ( MaxextraClose+1)//2