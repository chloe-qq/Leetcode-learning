# solution 1: stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        symbolList = []
        N = len(s)
        for i in range(N):
            if (s[i] == '('):
                stack.append((s[i],i))
            elif (s[i] == ')'):
                if (stack and stack[-1][0] == '('):
                    stack.pop()
                else:
                    stack.append((s[i],i))
                    
        temp = 0
        for trash in stack:
            s = s[:trash[1]-temp] + s[trash[1]+1-temp::]
            temp += 1
        return s

# solution 2: two pass solution
def minRemoveToMakeValid(self, s: str) -> str:
        s = [i for i in s]
        def helper(s, leftSymbol,rightSymbol):
            balance = 0
            for i in range(len(s)):
                if (s[i] == leftSymbol):
                    balance += 1
                elif (s[i] == rightSymbol):
                    balance -= 1
                    if (balance < 0):
                        s[i] = ''
                        balance = 0
            return s
        s = helper(s, '(',')')
        s = helper(s[::-1], ')','(')
        s = s[::-1]
        return ''.join(s)