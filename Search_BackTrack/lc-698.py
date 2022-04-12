from typing import List

"""
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""
# leetcode 提交还是超时了，虽然标准答案也超时了

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if (sum(nums)%k != 0):
            return False
        target = sum(nums)/k
        N = len(nums)
        used = [False]*N
        nums.sort(reverse=True)
        # 对于每一个数字 只有选/不选 2种选择，最多重新找k次(line21), 故time complexity = O(k * 2^n)
        def dfs(i,cur,k):
            if (k == 0):
                return True
            if (cur == target):
                # 找到一个 从投再来重新找
                return dfs(0,0,k-1)

            for j in range(i,N):
                if (not used[j]):
                    if (cur+nums[j] > target):
                        continue
                    used[j] = True
                    # important! 这个dfs是有return value的 所以在中间也要check一边
                    if(dfs(j+1,cur+nums[j],k)):
                        return True
                    used[j] = False
            return False

            
        return dfs(0,0,k)



lc_698 = Solution()

nums = [2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4]
k = 7
print(f'Leetcode 698: {lc_698.canPartitionKSubsets(nums,k)}')