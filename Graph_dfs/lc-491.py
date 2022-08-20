

from typing import List
#https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html#%E6%80%9D%E8%B7%AF
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def dfs(cur,startIndex):

            if (len(cur)>=2):
                ans.append(cur.copy())
            if ((not cur and startIndex == N-1) or startIndex >= N):
                return
            
            usedList = [False]*201 #-100 <= nums[i] <= 100
            for i in range(startIndex,N):
                if ((cur and cur[-1] > nums[i]) or usedList[nums[i]+100]):
                    continue
                else:
                    usedList[nums[i]+100] = True
                    cur.append(nums[i])
                    dfs(cur,i+1)
                    # 不用set to False 因为没进一次dfs 我们重新定义一次usedList
                    cur.pop()
        dfs([],0)

        # need to use a set to keep record whether an element is used or not
        # as we cannot sort array, while loop NOT work

        return ans
                
            
                