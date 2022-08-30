class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        bits = 0
        for i in range(32):
            if ((n & mask)!=0):
                # 如果此位为1，则bit += 1
                bits += 1
            mask <<= 1 # mask = mask*2， 依次升高1的位数
        return bits