
import collections
class Solution1:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        length = 0
        odd_cnt = 0
        for i in hashmap.values():
            if (i%2 == 0):
                length += i
            else:
                length += i//2 * 2
                odd_cnt += 1
        return length + 1 if odd_cnt > 0 else length
    
class Solution:
    def longestPalindrome(self, s):
        ans = 0

        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans