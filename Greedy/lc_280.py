class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

        N = len(nums)
        less = True
        for i in range(N-1):
            if (less):
                if (nums[i] > nums[i+1]):
                    swap(nums, i, i+1)
            else:
                if (nums[i] < nums[i+1]):
                    swap(nums, i, i+1)
            less = not less