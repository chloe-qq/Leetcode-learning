
# 921. Minimum Add to Make Parentheses Valid
# using balance
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_bracket = 0
        right_bracket = 0
        for char in s:
            if (char == '('):
                left_bracket += 1
            else:
                if (left_bracket > 0):
                    left_bracket -= 1
                else:
                    right_bracket += 1
        return left_bracket + right_bracket