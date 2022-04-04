from typing import List


"""
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
"""

class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        N = len(s)
        candidates = []
        temp = []
        inbrackets = False
        for i in range(N):
            if (s[i] == '{'):
                inbrackets = True
                temp = []
            elif (s[i] == ','):
                continue
            elif (s[i] == '}'):
                inbrackets = False
                candidates.append(temp)
                temp = []
                continue
            elif (s[i].isalpha()):
                if (inbrackets):
                    temp.append(s[i])
                else:
                    candidates.append([s[i]])

        N = len(candidates)
        print('candidates: {candidates} ')
        def dfs(cur,i):
            if (i == N):
                res.append(cur)
                return
            if (len(candidates[i]) > 1):
                for c in candidates[i]:
                    cur += c
                    dfs(cur,i+1)
                    cur = cur[:-1]
            else:
                cur += candidates[i][0]
                dfs(cur,i+1)
        dfs('',0)

        return sorted(res)

lc_1087 = Solution()
s = "{a,b}{z,x,y}"
res = lc_1087.expand(s)

            

                
            
                
                







