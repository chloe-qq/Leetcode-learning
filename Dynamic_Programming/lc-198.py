
# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre2 = 0
        pre1 = nums[0]
        cur = pre1
        for i in range(1,len(nums)):
            cur = max(nums[i]+pre2, pre1)
            pre2 = pre1
            pre1 = cur
        return cur
    
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[n]