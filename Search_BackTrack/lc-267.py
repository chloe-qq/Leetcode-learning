from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        N = len(s)
        if (N == 1):
            return [s]

        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        
        odd = 0
        cur = ''
        for i in hashmap.keys():
            if (hashmap[i]%2 == 1):
                odd += 1
                # record the single odd appearance char
                cur += i
            if (odd >1):
                return []
        res = []
        # cur may be a single character or ''
        def backtrack(cur, hashmap):
            if (len(cur) == N):
                res.append(cur)
                return
            elif (all(v == 0 for v in hashmap.values())):
                return
            # generate Palidromes by adding two characters rather than just adding one char at a time
            for i in hashmap.keys():
                if (hashmap[i] > 1):
                    # directly form palidromes
                    cur = i + cur + i
                    hashmap[i] -= 2
                    backtrack(cur, hashmap)
                    hashmap[i] += 2
                    cur = cur[1:-1]
        backtrack(cur,hashmap)
        return res




class Solution_Brute:
    def generatePalindromes(self, s: str) -> List[str]:
        N = len(s)
        if (N == 1):
            return [s]
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        res  = []

        def checkPalidromes(s):
            l = 0
            r = N-1
            while (l <= r):
                if (s[l] == s[r]):
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(cur, hashmap):
            if (len(cur) == N):
                if (checkPalidromes(cur)):
                    res.append(cur)
                return
            elif (all(v == 0 for v in hashmap.values())):# 这个条件必须在len(cur) == N 之后，否则直接return了
                return
            for c in hashmap.keys():
                if (hashmap[c] > 0):
                    cur += c
                    hashmap[c] -= 1
                    backtrack(cur, hashmap)
                    cur = cur[:-1]
                    hashmap[c] += 1
        backtrack("", hashmap)
        return res



lc_267 = Solution()
res = lc_267.generatePalindromes('aab')
print(f'lc 267 result: {res}')