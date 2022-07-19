
"""

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

"""

from curses.ascii import SO
from typing import List
class Solution:
    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0 for _ in range(n)]
        reservation = []
        for begin,end,seat in bookings:
            reservation.append([begin, seat])
            reservation.append([end+1, -seat])
        reservation.sort()
        for t, seat in reservation:
            for t1 in range(t,n):
                answer[t1-1] += seat
        return answer

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0 for _ in range(n+1)]

        for begin,end,seat in bookings:
            answer[begin-1] += seat
            answer[end] -= seat
        print(answer)
        for i in range(1,n+1):
            answer[i] += answer[i-1]
        return answer[:-1]
    
lc_1109 = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(lc_1109.corpFlightBookings(bookings, n))