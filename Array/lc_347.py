
from typing import List
from collections import Counter
class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        CountFreq = Counter(nums).most_common(k)
        return [i[0] for i in CountFreq]
        