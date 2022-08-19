"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


use DIVIDE AND CONQUER
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def LCP(s1,s2):
            N1 = len(s1)
            N2 = len(s2)
            N = min(N1,N2)
            res = 0
            while (res < N and s1[res] == s2[res]):
                res += 1
            return s1[:res]
        
        def div_conquer(left,right):
            if (left == right):
                return strs[left]
            else:
                mid = left + (right-left)//2
                s1 = div_conquer(left,mid)
                s2 = div_conquer(mid+1,right)
                ans = LCP(s1,s2)
                return ans
        
        ans = div_conquer(0, len(strs)-1)
        return ans
            
                    
                