# Letter Combinations of a Phone Number
from typing import List

class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        dictionary = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']            
        }
        N = len(str)
        result = []
        def dfs(d,cur):
            if (len(cur) == N):
                result.append(cur)
                return
            if (d >= N):
                return
            for c in dictionary[digits[d]]:
                # 注意这里是+，因为是string type，区分于list
                dfs(d+1,cur+c)
        dfs(0,"")
        return result

# 法2            
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        result = [""]
        dictionary = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']            
        }
        for d in digits:
            cur_length = len(result)
            for i in range(cur_length):
                temp = result.pop(0)
                for c in dictionary[d]:
                    result += [temp+c]
        return result

lc_17 = Solution2()
digits = '23'
print(f'Leetcode 17: {lc_17.letterCombinations(digits)}')