# find duplicate number in the list

# hashmap
# flip number
# Floyd's Cycle Algorithm (快慢指针问题)

"""
Input: nums = [1,3,4,2,2]
Output: 2
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
"""
from typing import List


# flip number method
class Solution_1:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            #print(nums)
            if (i > 0):
                if (nums[i] > 0):
                    nums[i] *= -1
                else:
                    return i
            else:
                if (nums[-i] > 0):
                    nums[-i]*=-1
                else:
                    return -i
        return 0
class Solution_2:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            slow = nums[slow] #slow前进一步 即走到index 为 nums[0] 的地方
            fast = nums[nums[fast]] # fast前进两步 即走到index 为 nums[0] 的地方再重复此操作
            if (fast == slow):
                break
        # another pointer
        slow2 = nums[0]
        # 这里不能用while True
        # 上面那段可以用while True 是因为一开始fast和slow就是在一起的，需要走一次
        # 而这里如果slow和slow2 已经在一起了就需要直接return 用while True则会走一次 就不对了
        while (slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2
    

lc_287 = Solution_1()
nums = [1,3,4,2,2]
print(f'Leetcode 287: {lc_287.findDuplicate(nums)}')
