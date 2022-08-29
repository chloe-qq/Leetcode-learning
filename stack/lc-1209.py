
"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        
        
        for i in range(n):
            if (not stack):
                stack.append([s[i], 1])
                continue
            if (stack and s[i] == stack[-1][0]):
                stack[-1][1] += 1
                if (stack[-1][1] == k):
                    stack.pop()
                    if (len(stack)>1 and stack[-1][0] == stack[-2][0]):
                        stack[-1][1] += stack[-2][1]
                        stack.pop()
                        if (stack[-1][1] == k):
                            stack.pop()
            else:
                stack.append([s[i], 1])
        #print(stack)
        return ''.join([i[0]*i[1] for i in stack])

                    
                
        