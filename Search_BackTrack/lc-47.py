from typing import List

# lc46 用的是一个array used 来indicate是否用过某个数字
# lc47 因为可能存在重复元素，所以用一个hashmap来indicate存在的可选的元素，被选择掉了就将数字-1
# 使用了hashmap，一开始选择的时候就不会有重复元素，而且每次选择保证不会重复，因为loop over的是hashmap的key

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if (N == 1):
            return [nums[:]]
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        res = []
        def backtrack(cur, hashmap):
            if (len(cur) == N):
                res.append(cur.copy())
                return
            elif (all(v == 0 for v in hashmap.values())): # 这个条件必须在len(cur) == N 之后，否则直接return了
                return
            for i in hashmap.keys():
                if (hashmap[i] > 0):
                    cur.append(i)
                    hashmap[i] -= 1
                    backtrack(cur, hashmap)
                    hashmap[i] += 1
                    cur.pop()
        backtrack([],hashmap)
        return res

lc_47 = Solution()
nums = [1,2,1]
print(f'Leetcode 47: {lc_47.permuteUnique(nums)}')
        

                

            