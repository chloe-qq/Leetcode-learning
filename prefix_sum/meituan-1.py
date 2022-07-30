"""

2. 给出一个元素无序的数组，求出使得其左边的数都小于它，右边的数都大于等于它的所有数字。
作者：井绳
链接 https://www.nowcoder.com/discuss/943400?type=0&order=undefined&pos=3&page=1&ncTraceId=5cec478a10a648e8a819331c0dc3da41.4588.16592069672964427&gio_id=D359F3B61DEBECB272742D96DCDAE63E-1659206966587
来源：牛客网

eg. a) 1,2,3,1,2,0,5,6  --> 输出5,6

eg. b)1,2,3,1,2,0,5,5  -->  输出5 (第一个5)

eg. 3)1,2,3,4,5,6,7 -->  输出1,2,3,4,5,6,7

思路：
使用一个数组nArrMin[i]来保存[i,nLen-1]区间内的最小值。
使用一个变量nMax保存区间[0,i-1]的最大值。
对于第i个数,如果它满足nArr[i]大于左边的最大数nMax 且 小于右边的最小数nArrMin[i]，则该数即为所求。
复杂度: 时间O(n), 空O(n),
"""
from typing import List
class Solution():
    def find(self, nums:List[int])->List[int]:
        N = len(nums)
        result = []
        premax = [0 for _ in range(N)]
        postmin = [0 for _ in range(N)]
        premax[0] = nums[0]
        postmin[N-1] = nums[-1]
        for i in range(1,N):
            if (nums[i] > premax[i-1]):
                premax[i] = nums[i]
            else:
                premax[i] = premax[i-1]
        for i in range(N-2,-1,-1):
            if (nums[i] < postmin[i+1]):
                postmin[i] = nums[i]
            else:
                postmin[i] = postmin[i+1]
        for i in range(N):
            if (i == 0 and nums[i] <= postmin[i+1]):
                result.append(nums[i])
            elif (i == N-1 and nums[i] > premax[i-1] ):
                result.append(nums[i])
            elif (nums[i] > premax[i-1] and nums[i] <= postmin[i+1]):
                result.append(nums[i])
                
        return result
                
nums = [1,2,3,1,2,0,5,6 ] 
nums =[1,2,3,4,5,6,7]    
nums = [1,2,3,1,2,0,5,5]   
result = Solution().find(nums)     
print(result)      