
from typing import List
from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = defaultdict(lambda: 0)
        for word in words:
            hashmap[word] += 1
        #print(hashmap)
        ans = 0
        distinctword = list(hashmap.keys())
        addedMiddle = False
        for word in distinctword:
            if (word == word[::-1]):
                occ = hashmap[word]//2
                ans += occ*2*2
                #print(f'update ans = {ans}')
                if (addedMiddle == False and (hashmap[word]-2*occ == 1)):
                    ans += 2
                    #print(f'update ans = {ans}')
                    addedMiddle = True
                    
                continue
            if (hashmap[word] > 0):
                if (hashmap[word[::-1]] > 0):
                    min_freq = min(hashmap[word], hashmap[word[::-1]])
                    ans += 2*2*min_freq
                    #print(f'update ans = {ans}')
                    hashmap[word] -= min_freq
                    hashmap[word[::-1]] -= min_freq
        return ans
                    
            
            