# very similar to lc-907. Sum of Subarray Minimums
# 只需要找到subarray min和max即可, 但是不可以用补0操作了,因为每个数到取值范围不再是1-～
# check stack是否为空即可

from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        
        def findSubarrayMin(arr) -> List[int]:
            N = len(nums)
            ans = [0]*N
            stack = []


            for i in range(N):
                
                while (stack and arr[stack[-1]] > arr[i]):
                    stack.pop()
                
                if (stack):
                    j = stack[-1]
                    ans[i] = ans[j] + arr[i]*(i-j)
                else:
                    ans[i] = arr[i]*(i+1)
                stack.append(i)
            return ans
        ansForMin = findSubarrayMin(nums)
        ansForMax = list(map(neg,findSubarrayMin( list(map(neg, nums)) )))
        
        total = 0
        for i,j in zip(ansForMin,ansForMax):
            total += j-i
        return total

from operator import neg
nums = [4,-2,-3,4,1]


lc_2104 = Solution()
ans = lc_2104.subArrayRanges(nums)
print(ans)
        








            
