"""

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

solution1: choose each char is the middle point and expand
solution2: 2d array - dp
"""

class Solution:
    # method 1 dynamic programming
    def longestPalindrome_1(self, s: str) -> str:
        N = len(s)
        # use True or False will be quicker
        # use 0/1 will exceed time limit
        dp = [[False]*N for _ in range(N)]
        for i in range(N):
            # fill the diagonial to be 1
            dp[i][i] = True
        max_length = 1
        left_index = 0
        # iterate from the bottom (range between left and right should be bigger than the previous one)
        # 右上三角形(bottom up) since left must be smaller than right
        for left in range(N-1, -1,-1):
            for right in range(N-1, left, -1):
                if (s[left] == s[right]):
                    if (left == right-1 or dp[left+1][right-1]):
                        dp[left][right] = True
                        if (right - left + 1 > max_length):
                            max_length = right - left + 1
                            left_index = left
        return s[left_index:left_index+max_length]
                            
                    
      # method 2: two pointer
    def longestPalindrome_2(self, s: str) -> str:
        # each single char or each two identical char can be the middle point of the Palindrome 
        N = len(s)
        max_length = 1
        left_begin = 0
        def helper(l,r):
            while (l >= 0 and r <N):
                if (s[l] == s[r]):
                    l-=1
                    r+=1
                else:
                    break
            return r-1 - (l+1) + 1
        for i in range(N-1):
            cur_max = max(helper(i,i), helper(i, i+1))
            if (max_length < cur_max):
                left_begin = i - (cur_max-1)//2
                max_length = cur_max
        return s[left_begin: left_begin + max_length]
          
                        
                    
                    
        
                
        
lc_5 = Solution()
s = 'babad'
result = lc_5.longestPalindrome_1(s)
result = lc_5.longestPalindrome_2(s)
print(result)