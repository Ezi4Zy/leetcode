#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        while end - start > 1:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end == x:
            return end
        return start
            
# @lc code=end

