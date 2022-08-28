
# 643. Maximum Average Subarray I
# prefix Sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSum = [0]*n
        preSum[0] = nums[0]
        for i in range(1,n):
            preSum[i] = preSum[i-1] + nums[i]

        maxValue = preSum[k-1]

        for i in range(k,n):
            maxValue = max(preSum[i] - preSum[i-k], maxValue)
        return maxValue/k
        
                
        