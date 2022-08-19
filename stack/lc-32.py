class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxLen = 0
        cur = 0
        N = len(s)
        position = [0]*(N)
        for i,c in enumerate(s):
            if (not stack):
                stack.append([i,c])
            elif (c == ')' and stack[-1][1] == '('):
                position[ stack[-1][0] ] = 1
                position[i] = 1
                stack.pop()              
            else:
                stack.append([i,c])
        for i in position:
            if (i == 1):
                cur += 1
                maxLen = max(cur, maxLen)
            else:
                cur = 0
        #print(position)
        return maxLen
    
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0
        cur = 0
        N = len(s)

        for i in range(N):
            if (s[i] == '('):
                stack.append(i)
            else:
                stack.pop() 
                if (not stack):
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i-stack[-1])

        return maxLen