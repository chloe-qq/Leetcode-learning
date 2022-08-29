
"""
Remove All Adjacent Duplicates In String
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        char = ''

        for i in s:
            if (not stack):
                stack.append(i)
                continue
            if (stack and stack[-1] == i):
                stack.pop()
                if (len(stack) > 1 and stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)