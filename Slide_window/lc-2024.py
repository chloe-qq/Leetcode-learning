from typing import List
"""
【类比leetcode 424】
Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.

"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        output = 1
        l = 0
        
        N = len(answerKey)
        cnt_T = 1 if answerKey[l] == 'T' else 0
        for r in range(1,N):
            if (answerKey[r] == 'T'):
                cnt_T += 1
            if (k>= min(cnt_T, r-l+1 - cnt_T)):
                output = max(output,r-l+1)

            else:
                while (k < min(cnt_T, r-l+1 - cnt_T)):
                    cnt_T = cnt_T - 1 if answerKey[l] == 'T' else cnt_T
                    l += 1
        return output

answerKey = "TTFTTFTT"
k = 1
lc_2024 = Solution()
print(f'lc 2024 solution: {lc_2024.maxConsecutiveAnswers(answerKey,k)}')
                     




        



