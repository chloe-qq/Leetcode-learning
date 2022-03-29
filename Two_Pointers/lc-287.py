# find duplicate number in the list

# hashmap
# flip number
# Floyd's Cycle Algorithm (快慢指针问题)


from typing import List

class Solution:
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
lc_287 = Solution()
nums = [2,3,4,4,1,5]
print(f'Leetcode 287: {lc_287.findDuplicate(nums)}')
