class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split('/'):
            if (portion == '..'):
                # back to the parent directory
                if (stack):
                    stack.pop()
            elif (portion == '.' or portion == ''):
                continue
            else:
                stack.append(portion)

        # join method 是在list中element以这个 ‘/’ 链接
        return '/' + "/".join(stack)
                    
            