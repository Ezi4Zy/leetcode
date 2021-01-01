#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        while True:
            if x % 2 != y % 2:
                ret += 1
            x /= 2
            y /= 2
            if not (x or y):
                return ret

# @lc code=end

