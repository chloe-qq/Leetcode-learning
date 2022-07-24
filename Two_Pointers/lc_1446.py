"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
"""



class Solution:
    def maxPower(self, s: str) -> int:
        N = len(s)
        cur = 1
        max_length = 1
        for i in range(1,N):
            if (s[i] == s[i-1]):
                cur += 1
            else:
                max_length = max(max_length,cur)
                cur = 1
        max_length = max(max_length,cur)
        return max_length
    def maxPower1(self, s: str) -> int:
        left = 0
        right = 0
        N = len(s)
        max_length = 0
        while (left <= right and right < N):
            while (right < N and s[left] == s[right]):
                
                right += 1
            max_length = max(max_length, right-1-left+1)
            left = right
        return max_length
    
s = "abbcccddddeeeeedcba"
max_length = Solution().maxPower(s)
print(max_length)