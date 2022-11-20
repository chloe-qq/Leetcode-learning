

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        N = len(s)
        left = 0
        right = 0
        minLength = N + 1
        left_index = None
        while (left <= right and right < N):
            if (s[right] in t):
                required[s[right]] -= 1
            # 这里必须是<=0 不能是==0
            while (all(v <= 0 for v in required.values()) and left <= right):
                print(required)
                if (right-left + 1 < minLength):
                    minLength = right-left + 1
                    left_index = left
                    print(f'updated left_index: {left_index}, minLength = {minLength}')
                
                
                if (left < N and s[left] in t):
                    required[s[left]] += 1
                    print(f'--- required dict: {required}')
                left += 1
                    
            
            right += 1

        return s[left_index:left_index + minLength] if left_index is not None else ""
    
lc_76 = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(lc_76.minWindow(s,t))
            
                
            
                
            

                