
"""
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

Input: n = 43325 --> 43299
Output: 39999
"""
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if (n < 10):
            return n
        integer = []
        N = 0
        while (n > 0):
            integer = [n % 10] + integer
            n = n//10
            N += 1
        max_int_index = N-1

        for i in range(N-1,0,-1):
            if (integer[i] >= integer[i-1]):
                continue
            else:
                for j in range(i, min(N,max_int_index+1)):
                    integer[j] = 9
                max_int_index = j
                integer[i-1] -= 1
        result = 0
        for i in integer:
            result = result*10+i
        return result   
lc_738 = Solution()
n = 1027
print(lc_738.monotoneIncreasingDigits(n))
            
            