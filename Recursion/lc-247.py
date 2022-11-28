from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        candidate = {    
            '0':'0',
            '1':'1',
            '8':'8',        
            '6':'9',
            '9':'6'
        }

        def recursion(curLen,FullLen):
            if (curLen == 0):
                return [""]
            if (curLen == 1):
                return ['0','1','8']
            prev_nums = recursion(curLen-2,FullLen)
            cur_nums = []
            for prev in prev_nums:
                for pair in candidate.items():
                    if (pair[0]!='0' or curLen!=FullLen):
                        cur_nums.append(pair[0] + prev + pair[1])
            return cur_nums
        return recursion(n,n)