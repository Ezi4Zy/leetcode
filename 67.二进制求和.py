#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_ = b_ = 0
        for c in a:
            a_ = a_ * 2 + int(c)
        for c in b:
            b_ = b_ * 2 + int(c)
        sum_ = a_ + b_
        ret = ""
        while sum_:
            ret = str(sum_ % 2) + ret
            sum_ = sum_ / 2
        return ret if ret else "0"

# @lc code=end

