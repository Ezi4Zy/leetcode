#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        bits = 0
        while True:
            ret += (0 if num % 2 else 1) * (2 ** bits)
            num /= 2
            bits += 1
            if not num:
                return ret
# @lc code=end

