"""
【lc-2024】进阶版
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dict = {}
        dict[s[l]] = 1
        N = len(s)
        max_length = 1
        max_frequency = 1
        for r in range(1,N):
            # update the frequency
            dict[s[r]] = dict.get(s[r],0) + 1
            max_frequency = max(max_frequency,dict[s[r]])
            while (r-l+1 - max_frequency > k):
                dict[s[l]] -= 1
                l += 1
                #max_frequency = max(dict.values())
                # no need to update max_frequency if max_freqency gets smaller, the max length will not be the final output
                # this point is important!
            max_length = max(r-l+1, max_length)

        return max_length

s = "ABBB"
k = 2
lc_424 = Solution()
print(f'lc 424 solution: {lc_424.characterReplacement(s,k)}')
                               
        