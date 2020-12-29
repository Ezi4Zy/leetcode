#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        begin = 0
        end = num + 1
        while begin < end:
            if end == begin + 1:
                return False
            mid = (begin + end) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid
            else:
                begin = mid

# @lc code=end

