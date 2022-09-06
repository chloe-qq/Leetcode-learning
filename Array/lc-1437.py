
#1437. Check If All 1's Are at Least Length K Places Away
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = -1
        cur = pre
        for i,digit in enumerate(nums):
            if (digit):
                cur = i
                if (pre == -1):
                    pre = cur
                    continue
                if (cur - pre <= k):
                    return False
                pre = cur
                
        return True