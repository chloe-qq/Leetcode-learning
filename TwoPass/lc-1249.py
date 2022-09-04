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