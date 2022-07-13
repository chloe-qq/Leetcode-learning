
"""
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.

dictionary = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']            
        }
"""

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        N = len(pressedKeys)
        dp = [0 for _ in range(N+1)]
        dp[0] = 1
        for i, digit in enumerate(pressedKeys):
            dp[i+1] = dp[i]
            # check if the cur push digits is the same as previous
            if (i >= 1 and pressedKeys[i-1]==digit):
                dp[i+1] += dp[i-1]
                if (i >= 2 and pressedKeys[i-2]==digit):
                    dp[i+1] += dp[i-2]
                    if (i >= 3 and  pressedKeys[i-2]==digit and (digit == '7' or digit == '9')):
                        dp[i+1] += dp[i-3]
        
        return dp[-1]
        


lc_2266 = Solution()
pressedKeys = '223'
print(f'Leetcode 2266: {lc_2266.countTexts(pressedKeys)}')