#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = x < 0
        x = abs(x)
        while x:
            n, x = x % 10, x / 10
            ret = ret * 10 + n
        ret = ret * (-1 if flag else 1)
        return ret if (-2 ** 31) <= ret <= (2 ** 31 -1) else 0
# @lc code=end

