"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Input: s = "()[]{}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'{':'}',
                   '[':']',
                   '(':')'}
        
        for c in s:
            if (not stack):
                stack.append(c)
            else:
                if(stack[-1] in hashmap.keys() and hashmap[stack[-1]] == c):
                    stack.pop()
                else:
                    stack.append(c)
        return False if (stack) else True
                
                
lc_20 = Solution()
s = "([)]"
print(lc_20.isValid(s))