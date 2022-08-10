
"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num


Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""
from numpy import int0


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        N = len(num)
        if (N == 1 and k > 0):
            return '0'
        for i in range(N):
            while (stack and k > 0 and num[i] < stack[-1]):
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        result = 0
        stack = stack[:-k] if k else stack 
        while (stack):
            result = result *10 + int(stack.pop(0))
        return str(result)
    
    
lc_402 = Solution()
num = "1432219"
k = 3
print(lc_402.removeKdigits(num,k))