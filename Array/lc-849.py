class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        pre = -1

        maxInterval = 0
        firstOccopied = -1
        for i,occupy in enumerate(seats):
            if (occupy):
                if (pre == -1):
                    pre = i
                    firstOccopied = i
                else:
                    maxInterval = max(maxInterval, i-pre)
                    pre = i
        lastOccupied = len(seats)-1-pre
        return max(max(lastOccupied,firstOccopied),maxInterval//2)