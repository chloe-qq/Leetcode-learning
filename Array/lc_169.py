class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = 0
        vote = 0
        for i in nums:
            if (i == winner):
                vote += 1
            else:
                vote -= 1
            if (vote < 0):
                winner = i
                vote = 0
        return winner