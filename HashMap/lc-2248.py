class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)
        ans = []
        m = len(nums)

        for i in range(m):
            for j in nums[i]:
                hashmap[j] += 1

        for k,v in hashmap.items():
            if (v == m):
                ans.append(k)
        return sorted(ans)