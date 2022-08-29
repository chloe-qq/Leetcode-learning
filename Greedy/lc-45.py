"""
simplified BFS
没走一步 会有一个range [cur + 0, cur + nums[cur]]可走
走哪一步呢？ 取决于[cur + 0, cur + nums[cur]]每一个点可走的步数
所以要取上述最大值farthest（遍历） 当走到cur + nums[cur]时候，更新最大值, 且 step + 1
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        cur_jump_end = 0
        farthest = 0
        N = len(nums)
        for i in range(N-1):
            farthest = max(farthest, i + nums[i])
            # next move will fall somewhere between [start : end] 
            # to find the minimum number of jumps to reach the end of the array, we must determine which place will take us the farthest in the next jump.
            if (i == cur_jump_end):
                steps += 1
                cur_jump_end  = farthest
        return steps
                
