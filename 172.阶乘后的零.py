#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#

# @lc code=start
import math
class Solution(object):
    def five_count(self, n):
        ret = 0
        while True:
            if n % 5 == 0:
                ret += 1
            else:
                return ret
            n /= 5

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 5
        count = 1
        ret = 0
        while base * count <= n:
            ret += self.five_count(base * count)
            count += 1
        return ret 
# @lc code=end

