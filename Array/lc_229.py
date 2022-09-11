# 229. Majority Element II
# Boyer-Moore Algorithm
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # the number must be <2
        vote1, vote2 = 0,0
        n1,n2 = None, None
        result = []
        for n in nums:
            if (n==n1):
                vote1 += 1
            elif (n==n2):
                vote2 += 1
            elif (vote1 <= 0):
                n1 = n
                vote1 = 1
            elif (vote2 <= 0):
                n2 = n
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        if (nums.count(n1)>len(nums)//3  ):
            result += [n1]
        if (nums.count(n2)>len(nums)//3  ):
            result += [n2]
        return result
            
        