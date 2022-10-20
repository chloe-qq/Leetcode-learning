
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            print(key)
            hashmap[key].append(word)
        return list(hashmap.values())
    
strs = ["ddddddddddg","dgggggggggg"]
lc_49 = Solution()
print(lc_49.groupAnagrams(strs))