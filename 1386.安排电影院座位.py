#
# @lc app=leetcode.cn id=1386 lang=python
#
# [1386] 安排电影院座位
#

# @lc code=start
import collections
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved_seats = collections.Counter()
        left = 0b11110000
        middle = 0b11000011
        right = 0b00001111
        for reserved_seat in reservedSeats:
            row = reserved_seat[0] - 1
            seat = reserved_seat[1]
            if 2 <= seat <= 9:
                reserved_seats[row] += 2 ** (seat-2)
        ret = 2 * (n - len(reserved_seats))
        for reserved_seat in reserved_seats.values():
            if reserved_seat:
                if (reserved_seat | left == left) or (reserved_seat | middle == middle) or (reserved_seat | right == right):
                    ret += 1
            else:
                ret += 2
            row += 1
        return ret

# @lc code=end

