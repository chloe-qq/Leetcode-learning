
from typing import List 
# arry + HashMap

# 也可以用trie做 待补
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        hashmap = {w: i for i, w in enumerate(words)}

        ans = []
        for i, w in enumerate(words):
            # no divide
            # 2 cases: 
            # case 1: '' with a self-palidrome
            # case 2: 2 word are palidrome of one another
            if (w[::-1] in hashmap.keys() and hashmap[w[::-1]] != i):
                ans.append([i,hashmap[w[::-1]]])
            if (w[::-1] == w and w!='' and ('' in hashmap.keys()) ):
                ans.append([i,hashmap['']])
                ans.append([hashmap[''],i])
            
            # has divide
            for k in range(1,len(w)):
                s1,s2 = w[:k],w[k:]

                # case 1 (s2 - s1 - s2)
                if (s1 == s1[::-1] and s2[::-1] in hashmap.keys()):
                    ans.append( [hashmap[s2[::-1]], i]  )
                
                if (s2 == s2[::-1] and s1[::-1] in hashmap.keys()):
                    ans.append([i,hashmap[s1[::-1] ]])
        return ans
            
        