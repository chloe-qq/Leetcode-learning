# very similiar as lc-1186: max subarry with one deletion by kanane algo
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]

        
        dp_operated = [0]*n
        dp_operated[0] =  nums[0]**2
        for i in range(1,n):            
            dp[i] = dp[i-1] + nums[i] if dp[i-1] >= 0 else nums[i]
            dp_operated[i] = max(max(dp[i-1]+nums[i]**2, nums[i]**2),dp_operated[i-1] + nums[i])
        return max(dp_operated)