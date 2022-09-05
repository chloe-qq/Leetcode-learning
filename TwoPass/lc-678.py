# 也在greedy里写过这道题

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for c in s:
            if (c == '('):
                left_max += 1
                left_min += 1
            elif (c == '*'):
                left_max += 1
                left_min -= 1
                
            elif (c == ')'):
                left_max -= 1
                left_min -= 1
            left_min = max(0, left_min)    
            if (left_max < 0):
                return False
            
                
        return True if (left_min ==0 ) else False