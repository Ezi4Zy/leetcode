#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            ret = 0
            while num:
                ret += num % 10
                num /= 10
            return self.addDigits(ret)
# @lc code=end

