#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                ret += i
                dividend -= temp
                i += i
                temp += temp
        if not positive:
            ret = -ret
        return min(max(ret, -2 ** 31), 2** 31 - 1)
# @lc code=end

