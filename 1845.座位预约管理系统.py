#
# @lc app=leetcode.cn id=1845 lang=python
#
# [1845] 座位预约管理系统
#

# @lc code=start
from heapq import heapify, heappop, heappush
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = range(1, n+1)
        
        


    def reserve(self):
        """
        :rtype: int
        """
        return heappop(self.seats)


    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heappush(self.seats, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

