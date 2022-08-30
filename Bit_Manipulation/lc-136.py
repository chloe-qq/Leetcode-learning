class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        # if we take XOR of two same bits, it will return 0
        for i in nums:
            x = x^ i
        return x