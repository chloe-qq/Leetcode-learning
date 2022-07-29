
"""
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
"""

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        N = len(number)
        right_most = -1
        for i in range(N-1):
            if (number[i] == digit):
                if ( int(number[i+1]) > int(digit) ):
                    return number[:i]+number[i+1:]
                else:
                    right_most = max(right_most, i)
        if (number[-1] == digit ):
            right_most = N-1

        return number[:right_most]+number[right_most+1:]
